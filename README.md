# Purpose of Project
This is an assignment to build test repository for DE. 

## Table of Contents

- [Week 4 Updates: polars](#week-4-update) 
- [Week 3 Updates: pandas](#week-3-update) 
- [Week 2 Updates: build draft repository](#week-2-update) 

---

## Week 4 update:
# Analysis of eGRID 2016 Data Using Polars

## Introduction

This project performs statistical analysis and visualization on the eGRID 2016 dataset using Polars, Matplotlib, and ydata_profiling. It calculates key statistics for the "CAPFAC" feature, creates a scatter plot between "CAPFAC" and "PLNGENAN", and generates a comprehensive data profiling report in both HTML and Markdown formats.

## Project Structure

Ensure that the eGRID 2016 CSV file (`egrid2016.csv`) is placed inside a folder named `data` in the same directory as the script.

```
project/
├── polars_wk3.py
├── egrid.png
├── egrid_summary.md
├── egrid_summary.html
├── data/
    └── egrid2016.csv
```

## Usage

Run the script using the command:

```bash
python polars_wk3.py
```

## Script Overview

The script performs the following steps:

### 1. Data Loading

Reads the eGRID 2016 dataset using Polars while ignoring any errors during parsing.

```python
import polars as pl

df = pl.read_csv("data/egrid2016.csv", ignore_errors=True)
```

### 2. Statistical Analysis

Calculates and prints the **mean**, **median**, and **standard deviation** for the "CAPFAC" feature. You can access detailed statistics [here](#summary-statistics)

```python
print("Mean for the feature CAPFAC is {}".format(df.select(pl.mean("CAPFAC"))))
print("Median for the feature CAPFAC is {}".format(df.select(pl.median("CAPFAC"))))
print("Std for the feature CAPFAC is {}".format(df.select(pl.std("CAPFAC"))))
```

### 3. Data Visualization

Creates a scatter plot of "CAPFAC" vs. "PLNGENAN", labels the axes and title, displays the plot, and saves it as `egrid.png`. You can reference pictures [here](#visualizations)


### 4. Data Profiling

Generates a comprehensive profiling report of the dataset using ydata_profiling and saves it as `egrid_summary.html`.

### 5. Report Conversion

Converts the HTML profiling report to Markdown format and saves it as `egrid_summary.md`.

## Output Files

- **Console Output:**
  - Mean, median, and standard deviation of the "CAPFAC" feature.
- **`egrid.png`:**
  - Scatter plot image of "CAPFAC" vs. "PLNGENAN".
- **`egrid_summary.html`:**
  - HTML file containing the comprehensive data profiling report.
- **`egrid_summary.md`:**
  - Markdown file of the data profiling report.

## Week3 update: 
I performed EDA on the egrid data in the file "pandas_test.py" and produced the EDA result to both html and md file in "egrid_summary.html" and "egrid_summary.md". 

## Week2 update: 
I created two py files to test the make file and CI actions: "hellp.py" and "test_hello.py". The "hello.py" contains a function to add two parameters provided, and the "test_hello.py" contains assert statements to check if the sum is correct.

# Preparation

Go through the make file.

# Egrid dataset

## Visualizations

The below visualization can be obtained by the pandas_test.py and it is saved as "descriptive_data.pdf". You can check more detailed EDA in the file "profile report.pdf" and "egrid_summary.md".
<img width="648" alt="image" src="https://github.com/user-attachments/assets/a10d0609-5d0b-4c3d-9fb1-011c728d2b59">


## Summary Statistics
<img width="334" alt="image" src="https://github.com/user-attachments/assets/05a341cc-5c45-4601-85e9-d856abf59a7b">


## License

This project is provided under the [MIT License](LICENSE).




