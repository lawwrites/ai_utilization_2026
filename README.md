

# AI Tool Utilization & Sentiment Analysis (CapEx 2026)

Over the last year, Paramount invested heavily in generative AI products. A year later, the list of active tools has ballooned alongside increased CapEx, creating a significant division in tool usage, satisfaction, and engagement.

This repository provides a **data-driven framework** to evaluate AI software adoption across creative and operations teams. I focused on gaining a granular understanding of **Value per Expenditure** by synthesizing survey data from Production Technologies, BET Digital, CBS Marketing, Editorial Post Production, Paramount Plus, The Multiplatform Group, and Nickelodeon Digital.

**GitHub Repository:** [https://github.com/lawwrites/ai_utilization_2026](https://github.com/lawwrites/ai_utilization_2026)
**Further Learnings:** The idea to use expected value to determine satisfaction and engagement comes from [Khan Academy's](https://www.khanacademy.org/math/statistics-probability/random-variables-stats-library) Unit 9 on Discrete Random Variable

## Key Business Questions

1. **Product Performance:** Which generative AI products deliver the highest perceived value based on the `value_index`?
2. **Strategic ROI:** Which tools provide the highest **Efficiency per Dollar** spent?

---

## Technical Methodology

### 1. Data Exploration & Cleaning

To ensure data integrity, I performed the following:

* **Standardization:** Merged datasets from 6 departments and standardized 15+ job titles (e.g., mapping "Avid Editor" to "Video Editor").
* **Sanitization:** Stripped whitespace and normalized column headers to `snake_case`.
* **Verification:** Checked for null values and duplicates before exporting the master `total_department_surveys.csv`.

### 2. The Baseline Metric: Value Index

I established a baseline "Realized Value" for every seat license:



This metric ensures that tools with high satisfaction but low usage (or vice versa) are accurately weighted.

### 3. Correlation Analysis

I utilized a **Pearson Correlation Coefficient ()** to determine the relationship between satisfaction and usage. A high  value indicates that satisfaction is a reliable predictor of organic adoption.

---

## Financial Framework for ROI

### Defining the Sample Space & Outcomes

Probability theory relies on a defined environment. For this analysis:

* **Sample Space ():** * Satisfaction: 
* Utilization: 


* **Expected Value ():** I calculated the average realized value per license by grouping the `value_index` by product.

### The "Cost of Void" (Sunk Cost Modeling)

A major challenge in software procurement is paying for "Ghost Seats." I modeled the **Cost of Void** to identify financial waste:

* If a `value_index` is 0, the **Cost of Void** is the full price of the license (100% Waste).
* If a `value_index` is not 0, I calculated the **Cost per Unit of Value**.

```python
# Logic implemented in the analysis
ts['cost_of_void'] = np.where(
    ts['value_index'] == 0, 
    ts['cost_per_seat'], 
    ts['cost_per_seat'] / ts['value_index']
)

```

### The Efficiency Ratio

Finally, I calculated the **Efficiency Ratio** to rank products. This tells us which tool gives the company the most "bang for its buck."


---

## Visualizing Performance

I utilized Seaborn to identify "High Performance" tools. Any tool exceeding a satisfaction threshold of **3.0** is flagged for an **Extension Review**.

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

## AI Usage

Google Gemini is used to create the synthetic survey data. It was also used to calculate the expected value scores.
