# Student Performance Data Analysis

## Week 2 – Data Acquisition and Preliminary Analysis

This repository contains the practical work for Week 2 of the Python-based data exploration project. The project uses the **Student Performance** dataset from the UCI Machine Learning Repository and focuses on data acquisition, validation, cleaning, descriptive statistics, visualization, and preliminary relationship analysis.

## Dataset

**Source:** UCI Machine Learning Repository  
**Dataset:** Student Performance  
**Official page:** https://archive.ics.uci.edu/dataset/320/student%2Bperformance  
**Dataset DOI:** 10.24432/C5TG7T

The Mathematics subset (`student-mat.csv`) is used for this project.

### Main outcome

- `G3` – final grade, on a 0–20 scale.

### Important variables

- `studytime` – weekly study-time category
- `absences` – number of school absences
- `failures` – number of past class failures
- `G1` – first-period grade
- `G2` – second-period grade
- `G3` – final grade

## Project Structure

```text
student-performance-data-analysis/
├── data/
│   ├── raw/
│   │   └── README.md
│   └── processed/
│       └── README.md
├── notebooks/
│   └── week2_preliminary_analysis.ipynb
├── src/
│   └── data_cleaning.py
├── reports/
│   └── Week_2_Data_Acquisition_Preliminary_Analysis_Tarang.docx
├── figures/
│   └── README.md
├── README.md
└── requirements.txt
```

## Analysis Workflow

1. Acquire the public dataset from UCI.
2. Preserve the original data in `data/raw/`.
3. Inspect dimensions, columns, data types, missing values, and duplicates.
4. Validate documented numerical ranges.
5. Standardize categorical text where required.
6. Perform descriptive statistics.
7. Explore relationships using visualizations and correlations.
8. Document preliminary findings and limitations.

## Python Tools

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- ucimlrepo

## Preliminary Findings

The initial analysis indicates that earlier academic grades (`G1` and `G2`) have strong positive associations with the final grade (`G3`). Study time has a weaker simple linear association with `G3`, while absences show a negative association. These observations are exploratory and should not be interpreted as proof of causation.

## Reproducibility

Install the required packages:

```bash
pip install -r requirements.txt
```

Then open the notebook:

```bash
jupyter notebook
```

Run the notebook cells from top to bottom.

## Academic Note

This repository is prepared as an internship learning/project submission. The analysis is intended for educational and exploratory purposes.
