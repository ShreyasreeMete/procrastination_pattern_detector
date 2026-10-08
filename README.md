# 🧠 FocusLens — Procrastination Pattern Detector

### An Interactive Python-Based Productivity Analysis & Exploratory Data Analysis Dashboard

FocusLens is a data analytics application designed to analyze daily activity patterns, evaluate productivity, and identify time periods and task categories associated with lower performance. Built using Python, Pandas, NumPy, Streamlit, and Plotly, the application transforms activity data into interactive visualizations and actionable insights.

The project demonstrates practical applications of **data cleaning, exploratory data analysis (EDA), productivity metrics, pattern detection, and interactive dashboard development**.

## 🎯 Problem Statement

People often struggle to understand when they are most productive, which tasks they find difficult to complete, and when their focus tends to decrease.

FocusLens addresses this problem by analyzing activity records to identify productivity trends across different hours, weekdays, and task categories. It provides data-driven recommendations to help users plan tasks more effectively and improve their time management.

## ✨ Key Features

* **📂 CSV Data Upload:** Upload personal activity records for analysis or use the included sample dataset.
* **🧹 Data Cleaning & Preprocessing:** Standardizes column names, removes duplicate records, handles invalid values, and prepares data for analysis.
* **📊 Interactive Productivity Dashboard:** Displays total sessions, completed tasks, completion rate, average focus time, and average productivity score.
* **⏰ Hourly Productivity Analysis:** Identifies the hours associated with the highest and lowest productivity scores.
* **📅 Weekday Performance Analysis:** Compares productivity across the days of the week.
* **📈 Exploratory Data Analysis:** Visualizes task completion rates, focus-time distribution, daily productivity trends, and category-level performance.
* **🔍 Procrastination Pattern Detection:** Highlights lower-performing time slots and task categories based on the available activity data.
* **💡 Actionable Recommendations:** Generates practical suggestions for scheduling demanding tasks and improving focus.
* **📥 Downloadable Analysis Report:** Exports processed activity data and hourly, weekday, and category-level analysis as a CSV download.

## 🛠️ Tech Stack

| Technology | Purpose                                                |
| ---------- | ------------------------------------------------------ |
| Python     | Core programming and analytical logic                  |
| Pandas     | Data manipulation, cleaning, grouping, and aggregation |
| NumPy      | Numerical operations and data processing               |
| Streamlit  | Interactive web application and dashboard              |
| Plotly     | Interactive charts and data visualization              |
| CSV        | Activity data input and analysis report export         |

## 📊 Dashboard Modules

### 1. Overview Dashboard

* Total activity sessions and completed tasks
* Overall task completion rate
* Average focus duration
* Average productivity score
* Best and lowest-performing hours and weekdays
* Suggested focus strategy

### 2. Exploratory Data Analysis (EDA)

* Productivity by hour
* Productivity by weekday
* Task completion rate by category
* Focus-time distribution
* Daily productivity trends
* Category-wise performance metrics

### 3. Procrastination Pattern Analysis

* Best and lowest-productivity time slots
* Comparison of productivity and focus duration
* Identification of task categories with lower average performance
* Data-driven recommendations for better task scheduling

### 4. Processed Data & Reporting

* View the cleaned activity dataset
* Review the cleaning operations performed
* Download the processed dataset and analysis tables in CSV format

## ⚙️ How Productivity Is Calculated

FocusLens generates a project-specific productivity score on a scale of 0–100 using three factors:

* **Task completion:** Whether the task was completed.
* **Focus ratio:** The proportion of task duration spent focusing.
* **Duration efficiency:** Focus time relative to the configured target focus duration.

The target focus duration can be adjusted in the dashboard. The score is an analytical metric developed for this project and is not a scientifically validated measure of productivity.

## 📁 Project Structure

```text
procrastination_pattern_detector/
│
├── app.py                      # Streamlit application
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
│
├── data/
│   └── sample_activity.csv     # Sample activity dataset
│
└── src/
    ├── __init__.py
    ├── data_processing.py      # Data loading, validation and cleaning
    ├── analysis.py             # Metrics and pattern detection
    ├── visualization.py        # Interactive Plotly charts
    └── report.py               # CSV report generation
```

## 🚀 Installation & Setup

Follow these steps to run FocusLens locally.

### Prerequisites

* Python 3.10 or later
* Git
* A code editor such as Visual Studio Code

### Step 1: Clone the Repository

Replace `YOUR_USERNAME` with your GitHub username after uploading the project.

```bash
git clone https://github.com/YOUR_USERNAME/procrastination-pattern-detector.git
```

### Step 2: Navigate to the Project Directory

```bash
cd procrastination-pattern-detector
```

### Step 3: Create a Virtual Environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 4: Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Step 5: Run the Application

```bash
streamlit run app.py
```

Streamlit will display a local URL in the terminal. Open that URL in your browser to access the FocusLens dashboard.

## 📄 Dataset Format

The application accepts CSV files containing the following required columns:

| Column             | Description              | Example        |
| ------------------ | ------------------------ | -------------- |
| `date`             | Date of the activity     | `2026-01-05`   |
| `start_time`       | Activity start time      | `09:00`        |
| `task`             | Name of the task         | `Study Python` |
| `category`         | Task category            | `Study`        |
| `duration_minutes` | Task duration in minutes | `60`           |
| `completed`        | Completion status        | `1` or `0`     |
| `focus_minutes`    | Minutes spent focusing   | `52`           |

### Sample CSV Data

```csv
date,start_time,task,category,duration_minutes,completed,focus_minutes
2026-01-05,09:00,Study Python,Study,60,1,52
2026-01-05,14:00,Debug project,Programming,90,0,35
2026-01-06,10:30,Build dashboard,Project,120,1,105
2026-01-06,16:00,Read documentation,Study,45,1,40
2026-01-07,11:00,Practice SQL,Learning,60,1,55
```

You can start with the included `data/sample_activity.csv` file or upload your own dataset using the sidebar.

## 🔄 Application Workflow

1. **Data Input:** Load the included sample data or upload an activity CSV file.
2. **Data Preprocessing:** Standardize column names, remove duplicates, and process invalid values.
3. **Data Analysis:** Calculate productivity metrics and aggregate results by hour, weekday, and category.
4. **Pattern Detection:** Identify the highest- and lowest-performing periods and task categories.
5. **Visualization:** Present insights through interactive charts and dashboard metrics.
6. **Report Export:** Download the processed data and analytical summaries for further analysis.

## 🌍 Real-World Applications

* Personal productivity and time-management analysis
* Student study-habit and task-completion tracking
* Employee activity and work-pattern analysis, where appropriate and with consent
* Identification of tasks that may require better planning
* Data-driven scheduling and productivity improvement

## 🎓 Skills Demonstrated

This project demonstrates practical skills relevant to entry-level Data Analyst roles:

* Python programming and data manipulation
* Data cleaning, validation, and preprocessing
* Exploratory Data Analysis (EDA)
* Data aggregation and statistical summaries
* KPI calculation and performance tracking
* Interactive dashboard development
* Data visualization and interpretation
* CSV data processing and report generation
* Analytical problem-solving and insight communication

## 🔮 Future Enhancements

* Historical productivity tracking with database integration
* User profiles and personalized dashboards
* Weekly and monthly productivity reports
* Calendar integration for task scheduling
* Machine learning-based activity pattern clustering
* Personalized recommendations based on historical activity
* Optional email delivery of productivity reports

## ⚠️ Disclaimer

FocusLens identifies patterns in the activity data provided by the user. It does not establish the causes of procrastination, measure psychological conditions, or provide medical or clinical diagnoses. The accuracy and usefulness of its findings depend on the quality and quantity of the supplied data.

## 👨‍💻 Author

**Shreyasree Mete**

---

⭐ If you find this project useful, consider giving the repository a star!
