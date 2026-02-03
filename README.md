This is a massive milestone! You’ve moved from raw data cleaning to a sophisticated **Financial ROI framework**. Your code now handles complex data mapping, statistical correlation, and an "Efficiency Ratio" that separates useful tools from budget-drainers.

Below is the updated `README.md` that reflects your actual code logic, including the **Cost of Void** and **Efficiency Ratio** metrics.

---

# AI Tool Utilization & Sentiment Analysis (CapEx 2026)

Over the last year, Paramount invested heavily in generative AI products. A year later, the list of active tools has ballooned alongside increased CapEx, creating a significant division in tool usage, satisfaction, and engagement.

This repository provides a **data-driven framework** to evaluate AI software adoption across creative and operations teams. We focus on gaining a granular understanding of **Value per Expenditure** by synthesizing survey data from BET Digital, CBS Marketing, Editorial Post Production, Paramount Plus, The Multiplatform Group, and Nickelodeon Digital.

**GitHub Repository:** [https://github.com/lawwrites/ai_utilization_2026](https://github.com/lawwrites/ai_utilization_2026)

## Key Business Questions

1. **Product Performance:** Which generative AI products deliver the highest perceived value based on the `value_index`?
2. **Strategic ROI:** Which tools provide the highest **Efficiency per Dollar** spent?

---

## Technical Methodology

### 1. Data Exploration & Cleaning

To ensure data integrity, we performed the following:

* **Standardization:** Merged datasets from 6 departments and standardized 15+ job titles (e.g., mapping "Avid Editor" to "Video Editor").
* **Sanitization:** Stripped whitespace and normalized column headers to `snake_case`.
* **Verification:** Checked for null values and duplicates before exporting the master `total_department_surveys.csv`.

### 2. The Baseline Metric: Value Index

We established a baseline "Realized Value" for every seat license:



This metric ensures that tools with high satisfaction but low usage (or vice versa) are accurately weighted.

### 3. Correlation Analysis

We utilized a **Pearson Correlation Coefficient ()** to determine the relationship between satisfaction and usage. A high  value indicates that satisfaction is a reliable predictor of organic adoption.

---

## Financial Framework for ROI

### Defining the Sample Space & Outcomes

Probability theory relies on a defined environment. For this analysis:

* **Sample Space ():** * Satisfaction: 
* Utilization: 


* **Expected Value ():** We calculate the average realized value per license by grouping the `value_index` by product.

### The "Cost of Void" (Sunk Cost Modeling)

A major challenge in software procurement is paying for "Ghost Seats." We modeled the **Cost of Void** to identify financial waste:

* If a `value_index` is 0, the **Cost of Void** is the full price of the license (100% Waste).
* If a `value_index` is , we calculate the **Cost per Unit of Value**.

```python
# Logic implemented in the analysis
ts['cost_of_void'] = np.where(
    ts['value_index'] == 0, 
    ts['cost_per_seat'], 
    ts['cost_per_seat'] / ts['value_index']
)

```

### The Efficiency Ratio

Finally, we calculate the **Efficiency Ratio** to rank products. This tells us which tool gives the company the most "bang for its buck."


---

## Visualizing Performance

We utilize Seaborn to identify "High Performance" tools. Any tool exceeding a satisfaction threshold of **3.0** is flagged for an **Extension Review**.

---

## Project Structure

```text
/portfolio
└── /data_analysis
    └── /utilization
        ├── /data
        │   ├── surveys/ (Raw Departmental CSVs)
        │   ├── total_department_surveys.csv (Cleaned Master)
        │   └── final_pivot_report.csv (Stakeholder Table)
        └── analysis_script.py

```
