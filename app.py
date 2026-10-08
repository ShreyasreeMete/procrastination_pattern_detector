import streamlit as st
import pandas as pd
import numpy as np

from src.data_processing import (
    load_data,
    validate_columns,
    clean_data,
    generate_sample_data,
)
from src.analysis import (
    calculate_summary,
    calculate_productivity_by_hour,
    calculate_productivity_by_day,
    calculate_task_analysis,
    detect_patterns,
    build_productivity_score,
)
from src.visualization import (
    plot_productivity_by_hour,
    plot_productivity_by_day,
    plot_task_completion,
    plot_focus_distribution,
    plot_productivity_trend,
)
from src.report import create_csv_report

st.set_page_config(
    page_title="FocusLens - Procrastination Pattern Detector",
    page_icon="🧠",
    layout="wide",
)

st.markdown(
    """
    <style>
    .main-title {font-size: 2.5rem; font-weight: 800;}
    .subtitle {font-size: 1.05rem; color: #666;}
    .insight {padding: 1rem; border-radius: 0.7rem; border: 1px solid #ddd;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="main-title">🧠 FocusLens</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Procrastination Pattern Detector & Productivity EDA Dashboard</div>',
    unsafe_allow_html=True,
)

with st.sidebar:
    st.header("⚙️ Data Input")
    uploaded = st.file_uploader("Upload activity CSV", type=["csv"])

    use_sample = st.checkbox("Use included sample data", value=uploaded is None)

    if uploaded is not None and not use_sample:
        raw_df = load_data(uploaded)
        source_name = uploaded.name
    else:
        raw_df = generate_sample_data()
        source_name = "Generated sample data"

    st.divider()
    st.header("🎯 Analysis Settings")
    target_focus = st.slider(
        "Target focus duration (minutes)",
        min_value=15,
        max_value=180,
        value=60,
        step=5,
    )
    min_tasks = st.slider(
        "Minimum tasks for a reliable time-slot comparison",
        min_value=1,
        max_value=20,
        value=3,
    )

try:
    df, cleaning_log = clean_data(raw_df)
except Exception as exc:
    st.error(f"Could not process the dataset: {exc}")
    st.stop()

required = validate_columns(df)
if required:
    st.error("Missing required columns: " + ", ".join(required))
    st.info(
        "Required columns: date, start_time, task, category, "
        "duration_minutes, completed, focus_minutes"
    )
    st.stop()

# Derived productivity score
df = build_productivity_score(df, target_focus)

summary = calculate_summary(df)
hour_df = calculate_productivity_by_hour(df)
day_df = calculate_productivity_by_day(df)
task_df = calculate_task_analysis(df)
patterns = detect_patterns(df, hour_df, day_df, min_tasks)

tabs = st.tabs(
    ["📌 Overview", "📊 EDA", "🔎 Patterns", "📋 Data", "ℹ️ About"]
)

with tabs[0]:
    st.subheader("Your productivity at a glance")

    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Total Sessions", summary["sessions"])
    c2.metric("Completed", summary["completed"])
    c3.metric("Completion Rate", f'{summary["completion_rate"]:.1f}%')
    c4.metric("Avg Focus", f'{summary["avg_focus"]:.0f} min')
    c5.metric("Avg Productivity", f'{summary["avg_productivity"]:.1f}/100')

    st.divider()

    left, right = st.columns(2)
    with left:
        st.plotly_chart(
            plot_productivity_by_hour(hour_df),
            use_container_width=True,
        )
    with right:
        st.plotly_chart(
            plot_productivity_by_day(day_df),
            use_container_width=True,
        )

    st.subheader("💡 Key findings")
    findings = [
        f"**Best productivity hour:** {patterns['best_hour_label']}",
        f"**Highest procrastination hour:** {patterns['worst_hour_label']}",
        f"**Best weekday:** {patterns['best_day']}",
        f"**Lowest weekday:** {patterns['worst_day']}",
        f"**Most difficult category:** {patterns['hardest_category']}",
        f"**Average focus session:** {summary['avg_focus']:.0f} minutes",
    ]

    cols = st.columns(3)
    for i, finding in enumerate(findings):
        with cols[i % 3]:
            st.markdown(f'<div class="insight">{finding}</div>', unsafe_allow_html=True)

    st.subheader("🎯 Suggested focus strategy")
    st.success(patterns["recommendation"])

with tabs[1]:
    st.subheader("Exploratory Data Analysis")

    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(
            plot_task_completion(task_df),
            use_container_width=True,
        )
    with col2:
        st.plotly_chart(
            plot_focus_distribution(df),
            use_container_width=True,
        )

    st.subheader("📈 Productivity trend")
    st.plotly_chart(
        plot_productivity_trend(df),
        use_container_width=True,
    )

    st.subheader("Category performance")
    category_df = (
        df.groupby("category", as_index=False)
        .agg(
            sessions=("task", "count"),
            completion_rate=("completed", "mean"),
            avg_focus=("focus_minutes", "mean"),
            avg_productivity=("productivity_score", "mean"),
        )
        .sort_values("avg_productivity", ascending=False)
    )
    category_df["completion_rate"] *= 100
    st.dataframe(
        category_df.round(2),
        use_container_width=True,
        hide_index=True,
    )

with tabs[2]:
    st.subheader("🔎 Procrastination patterns")

    st.markdown(
        """
        FocusLens does not diagnose a medical or psychological condition.
        It identifies **behavioral patterns in the supplied activity data**.
        """
    )

    a, b = st.columns(2)
    with a:
        st.metric(
            "High-risk time slot",
            patterns["worst_hour_label"],
        )
        st.write(
            f"Average productivity during this hour: "
            f"**{patterns['worst_hour_score']:.1f}/100**"
        )
    with b:
        st.metric(
            "Best time slot",
            patterns["best_hour_label"],
        )
        st.write(
            f"Average productivity during this hour: "
            f"**{patterns['best_hour_score']:.1f}/100**"
        )

    st.subheader("What may be causing low productivity?")
    for item in patterns["causes"]:
        st.write(f"• {item}")

    st.subheader("Actionable recommendations")
    for item in patterns["actions"]:
        st.write(f"✅ {item}")

    st.subheader("Task difficulty")
    difficulty = task_df.copy()
    difficulty["completion_rate"] = difficulty["completion_rate"].round(1)
    difficulty["avg_focus"] = difficulty["avg_focus"].round(1)
    difficulty["avg_productivity"] = difficulty["avg_productivity"].round(1)
    st.dataframe(difficulty, use_container_width=True, hide_index=True)

with tabs[3]:
    st.subheader("📋 Processed dataset")
    st.caption(f"Source: {source_name}")

    if cleaning_log:
        with st.expander("Cleaning operations performed"):
            for item in cleaning_log:
                st.write(f"• {item}")

    st.dataframe(
        df.sort_values(["date", "start_time"], ascending=False),
        use_container_width=True,
        hide_index=True,
    )

    report = create_csv_report(df, hour_df, day_df, task_df)
    st.download_button(
        "⬇️ Download processed analysis CSV",
        data=report,
        file_name="focuslens_analysis.csv",
        mime="text/csv",
    )

with tabs[4]:
    st.subheader("About FocusLens")
    st.markdown(
        """
        **FocusLens** is an EDA-focused Streamlit project that studies
        work/activity patterns and highlights time periods associated with
        lower productivity.

        ### Required CSV columns

        - `date` — activity date, e.g. `2026-01-05`
        - `start_time` — start time, e.g. `09:30`
        - `task` — task name
        - `category` — task category
        - `duration_minutes` — planned/observed task duration
        - `completed` — 1/0 or True/False
        - `focus_minutes` — focused minutes spent on the task

        ### Productivity score

        The score combines completion, focus ratio, and duration efficiency.
        It is an analytical metric created for this project, not a clinical
        or scientific diagnosis.
        """
    )
    st.code(
        "streamlit run app.py",
        language="bash",
    )
