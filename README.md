# Editorial Post Production: AI Strategic Analysis & CapEx Planning

This repository contains a data-driven framework for evaluating AI software adoption across creative and operations teams. The primary goal is to provide the **Editorial Post Production Operations** team with quantitative benchmarks to guide the mid-year CapEx cycle, specifically evaluating whether to extend partnerships for the licenses of their clients. 

## The Organic Adoption Proxy: "Weekend Usage"

Weekly usage takes weekend days into account to capture employees' tendency to use AI tools they are passionate about outside of work. Traditional software metrics often fail to capture true user-centricity. This project introduces a **0–7 usage scale** to distinguish between standard business utilization and organic, personal adoption.

* **0–5 Range:** Represents standard business-week utilization and mandatory task completion.
* **6–7 Range:** Captures weekend usage for personal work, hobbies, or fulfilling side projects.

This serves as a proxy for **Cognitive Ease** and **Stickiness**. If a teammate uses a tool during their personal time, the "Learning Tax" is effectively zero, and the tool has transitioned from a corporate requirement to a natural extension of their creative workflow. Higher personal usage leads to a happier, more engaged employee base and reduced long-term operational friction.

## Mathematical Framework & Weighted ROI

To move beyond simple averages which can be skewed by outliers, this analysis employs **Expected Value ()** to determine the weighted performance of each tool.

### Expected Value Calculation

The Expected Value is calculated by taking the sum of each satisfaction rating () multiplied by its probability (), determined by the relative frequency of that rating within the team.

```python
# Python logic for Expected Value (E[X])
total_respondents = 65
ratings = [1, 2, 3, 4, 5]
frequencies = [12, 32, 11, 5, 5]

# Calculate weighted probability for each rating
weighted_probabilities = [r * (f / total_respondents) for r, f in zip(ratings, frequencies)]

# Expected Value is the sum of these probabilities
expected_value = sum(weighted_probabilities)
# Result: 2.69

```

### Value-per-Seat Metric

By calculating the cost per weighted value of satisfaction and utilization, we can determine the true ROI of a seat license. This allows for a direct "Value-per-Dollar" comparison across products with different price points.

```python
# Python logic for Value-per-Seat
monthly_cost_per_seat = 30.00
weighted_satisfaction = 2.69

value_per_seat = monthly_cost_per_seat / weighted_satisfaction

```

## Microsoft Copilot Performance Summary

The initial benchmark for the Editorial Post Production Operations team (N=65) shows an **Expected Value of 2.69** for User Satisfaction.

* **Primary Cluster:** 49% of the team reported a satisfaction rating of 2.
* **Interpretation:** While the tool has established a baseline, the low  suggests that the "Learning Tax" remains high, or the current feature set is not yet meeting the specific technical needs of the post-production workflow.

## File and Folder Structure

```text
/portfolio
└── /data_analysis
    └── /utilization
        ├── /data
        │   ├── bet_digital.csv
        │   ├── CBS_Marketing.csv
        │   ├── Editorial_Post_Production_Operations.csv
        │   ├── Nickelodeon_Digital.csv
        │   ├── Paramount_Plus_Brand_Creative.csv
        │   ├── The_Multiplatform_Group.csv
        │   └── total_department_surveys.csv
        └── analysis_script.py

```

## Technical Methodology

* **Standardization:** Automated cleaning of row and column data using Pandas `.str` accessors to ensure data integrity across multiple department CSVs.
* **Categorization:** Role mapping to consolidate disparate job titles into standardized professional cohorts (e.g., "Avid Editor" and "Multi-platform Editor" to "Video Editor").
* **Aggregation:** Using `groupby` and `pivot_table` to identify high-performing AI tools by specific business units.
