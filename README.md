# 🎓 Sri Lanka G.C.E. A/L (2020) Data Analysis & Profiling

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?logo=pandas)
![Sweetviz](https://img.shields.io/badge/Sweetviz-EDA-ff69b4)
![Status](https://img.shields.io/badge/Status-Completed-success)

A comprehensive Exploratory Data Analysis (EDA) and automated data profiling project based on the Sri Lankan G.C.E. Advanced Level (A/L) 2020 examination results dataset. This repository serves as a data exploration pipeline to uncover insights regarding student performance, subject distributions, and descriptive statistics.

---

## 📑 Table of Contents
- [Project Overview](#-project-overview)
- [Dataset Characteristics](#-dataset-characteristics)
- [Repository Structure](#-repository-structure)
- [Interactive Profiling Report](#-interactive-profiling-report)
- [Installation & Setup](#-installation--setup)
- [Usage](#-usage)
- [Author](#-author)

---

## 📌 Project Overview
The primary objective of this project is to process and analyze a large-scale educational dataset. Using **Pandas** for data wrangling and **Sweetviz** for automated profiling, the project generates an in-depth, interactive HTML report that details feature correlations, missing values, and statistical distributions.

## 📊 Dataset Characteristics
* **Total Records:** 337,553 students
* **Total Features:** 19 columns
* **Key Features Include:**
  - stream: Academic stream (e.g., Arts, Commerce, Science)
  - Zscore: Standardized Z-Score of the student
  - district_rank & island_rank: Geographical rankings
  - sub1_r, sub2_r, sub3_r: Subject specific grades (A, B, C, S, F)
  - gender: Demographics (Male/Female)

> **Preview of Data Snapshot:**
> 
> ![Data Summary](day%203/Screenshot%202026-08-24%20104822.png)

---

## 📁 Repository Structure

`	ext
📦 Sri-Lanka-AL-results-2020-analysis
 ┣ 📂 day 3
 ┃ ┣ 📜 al_data_analysis.ipynb      # Main Jupyter Notebook with data processing logic
 ┃ ┣ 📜 profiling_report.html       # Sweetviz generated interactive EDA report
 ┃ ┗ 🖼️ Screenshot 2026-08-24 104822.png # Snapshot of dataset tail/head
 ┗ 📜 README.md                     # Project documentation
`

---

## 🚀 Interactive Profiling Report
You do not need to download the repository or run the code to view the data insights. The automated EDA report can be viewed directly in your browser:

👉 **[View the Live Interactive Data Profiling Report Here](https://htmlpreview.github.io/?https://github.com/sahas-hasaranga/Sri-Lanka-AL-results-2020-analysis/blob/main/day%203/profiling_report.html)**

---

## ⚙️ Installation & Setup

To run this project locally, ensure you have Python 3.8+ installed.

1. **Clone the repository:**
   `ash
   git clone https://github.com/sahas-hasaranga/Sri-Lanka-AL-results-2020-analysis.git
   cd Sri-Lanka-AL-results-2020-analysis
   `

2. **Install dependencies:**
   `ash
   pip install pandas sweetviz jupyter
   `

3. **Launch the Notebook:**
   `ash
   jupyter notebook "day 3/al_data_analysis.ipynb"
   `
*(Note: You will need to download and place the raw .csv dataset in the appropriate directory as it is not included in this repository due to size constraints).*

---

## 💻 Usage
The notebook contains the foundational code to:
1. Ingest the large dataset efficiently.
2. Provide immediate row/column metrics and handle missing value checks.
3. Automatically generate the profiling_report.html via the Sweetviz engine.

Feel free to fork the repository and add your own specific analytical queries (e.g., visualizing Z-score distributions across different districts).

---

## 🎓 Author

* **Name:** S.H. SOORIYAARACHCHI
* **Student ID:** GAHDSE252F-028
* **GitHub:** [@sahas-hasaranga](https://github.com/sahas-hasaranga)

---
*If you found this analysis helpful, please consider giving this repository a ⭐!*

## 🛠️ Data Processing & Cleaning Steps
In this analysis, several data wrangling steps were performed to ensure data quality and prepare for deeper insights:
* **Distribution Analysis:** Analyzed the distribution of students across different academic streams, gender, and General Test (CGT) results.
* **Data Cleaning & Deduplication:** Removed missing records (null values in the gender column) and eliminated duplicate entries to ensure a clean dataset.
* **Rank Extraction:** Extracted pure numerical values from the `district_rank` column (which initially contained mixed text/number formats).
* **Top Performers Filtering:** Filtered the dataset to isolate and analyze top-performing students who secured a District Rank of less than 500.
* **Interactive Visualization:** Integrated interactive data tables for seamless scrolling and searching within the notebook environment.

## 🔍 Advanced Data Filtering Examples
The notebook can be expanded to uncover fascinating insights. Here are a few advanced filtering examples you can try:

1. **Top Performers (3 A's)**
   Identify students who achieved 'A' grades in all three main subjects:
   ``python
   top_students = df_cleaned[(df_cleaned['sub1_r'] == 'A') & 
                             (df_cleaned['sub2_r'] == 'A') & 
                             (df_cleaned['sub3_r'] == 'A')]
   ``

2. **District 1st Ranks**
   Isolate the students who secured the 1st rank in their respective districts:
   ``python
   district_first = df_cleaned[df_cleaned['district_rank_numeric'] == 1]
   ``

3. **High Achievers in Science**
   Find Science stream students with an exceptional Z-Score (above 2.0):
   ``python
   high_zscore_science = df_cleaned[(df_cleaned['stream'] == 'SCIENCE') & (df_cleaned['Zscore'] > 2.0)]
   ``

4. **Interesting Anomalies**
   Find students who excelled in General English ('A' grade) but failed all three main subjects (3 'F's):
   ``python
   english_pro_but_failed = df_cleaned[(df_cleaned['ge_r'] == 'A') & 
                                       (df_cleaned['sub1_r'] == 'F') & 
                                       (df_cleaned['sub2_r'] == 'F') & 
                                       (df_cleaned['sub3_r'] == 'F')]
   ``
