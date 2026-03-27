# Google Apps Performance <br> Consultant Dashboard

## :large_orange_diamond: About Me

I am a Doctor of Neuroscience with strong experience in data analysis, statistical modelling and research design. I focus on translating complex data into actionable insights for business and policy. I enjoy data wrangling, visualization, and project management.

**Skills & tools:** 
- advanced **R**, advanced **Python** (*pandas*, *NumPy*, *matplotlib*, *seaborn*, *scipy*) - see my [Python portfolio project](https://github.com/DominikaDrazyk/DataAnalysis_Efficiency_and_Diversity), 
- developing my skills in **Power BI** and **Power Apps**,
- developing my skills in **SQL** (**ETL**, **PostgreSQL**, **pgAdmin4**, **DBeaver**) - see my [SQL portfolio project](https://github.com/DominikaDrazyk/DataAnalysis_eCommerce_Audit),
- technical documentation in **Jupyter Notebook** (*Markdown* syntax), version control in **Git**.

&emsp; **Location**: Poland, Krakow <br> 
&emsp; **Contact**: dominika.a.drazyk@gmail.com <br> 
&emsp; **LinkedIn**: [in/dominika-drazyk-otw95](https://www.linkedin.com/in/dominika-drazyk-otw95/)

## :large_orange_diamond: Project Navigation
Select the path that best matches your interest:

**1. Executive & Business Insight** <br>
*For reviewers focused on storytelling, strategy, and end-results.*

- [PDF Presentation](./reports/Consultant_Dashboard_presentation.pdf): a step-by-step walkthrough of the project’s assumptions, technical execution highlights, and business insights;

- [Images](./images/): a repository of example dashboard screenshots.

**2. Technical Deep-Dive & Audit** <br>
*For reviewers interested in the full analytical process and data interpretation.*

- [PowerBI Dashboard](./Consultant_Dashboard.pbix): an operational interactive dashboard;

- [Data Preprocessing Code](./py_code/): production-ready, concise .py preprocessing code.

:eight_spoked_asterisk: **Dependency Management** <br>
A strictly defined environment manifest ensuring 100% reproducibility and security. Please, follow those steps in case you would like to run the code on your local machine: 

- **Step 1: Initialize the Virtual Environment**

*Linux / macOS Bash*
```
python3 -m venv .venv
source .venv/bin/activate
```
*Windows PowerShell*
```
python -m venv .venv
.venv\Scripts\activate
```
- **Step 2: Install Required Dependencies**
```
pip install --upgrade pip
pip install -r requirements.txt
```

## :large_orange_diamond: Overview

Imagine you are a *Market Research Consultant* hired by a mobile app company. One of your tasks is to assist the *Product Manager* and evaluate their app ideas. 
Managers need **fast, objective insight** into how their concept fits the current mobile-app landscape.

This Consultant Dashboard provides exactly that.
It helps the Consultant to:
- present the **most competitive** app categories;
- showcase the specific category targeted by the creators;
- **compare their goals against market medians**.

With these inputs, the app creators can ground their decisions in data rather than assumptions and quickly understand where their app stands relative to the market.

![Screenshot of the first dashboard page - EXPO.](/images/Consultant_Dashboard_EXPO.jpg)

![Screenshot of the second dashboard page - YOUR CHOICE.](/images/Consultant_Dashboard_YOUR_CHOICE.jpg)

![Screenshot of the third dashboard page - YOUR TRENDS.](/images/Consultant_Dashboard_YOUR_TRENDS_OFF.jpg)

![Screenshot of the third dashboard page - YOUR TRENDS with Filters Panel.](/images/Consultant_Dashboard_YOUR_TRENDS_ON.jpg)

### Data & Source Metadata

External data source (Kaggle): [Google Play Store Apps dataset](https://www.kaggle.com/datasets/lava18/google-play-store-apps?resource=download) Authored by L. Gupta (2019) and available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

### Key variables

- `App` – the name of the mobile application.

- `Category` – the high-level classification assigned to the app (e.g., Tools, Games).

- `Genre` – more granular thematic type nested within each category.

- `Star Rating` – average user star rating.

- `Count of Ratings` – number of ratings submitted.

- `Installs` – total download count.

- `Price in USD` – app price in US dollars.

- `Content Rating` – age suitability classification (e.g., Everyone, Teen).

- `Size in KB` – application file size in kilobytes.

- `Last Updated` – date of the most recent app update.

- `Count of Reviews` – number of text reviews submitted.

- `% of Positive Sentiment` – the percentage of positive sentiment detected in a given text review.

- `% of Neutral Sentiment` – the percentage of neutral sentiment detected in a given text review.

- `% of Negative Sentiment` – the percentage of negative sentiment detected in a given text review.

- `Sentiment Polarity` – how polarized (Positive-Negative) was the sentiment detected in a given text review.

- `Sentiment Subjectivity` – how subjective was the narration of a given text review.

### Tools & Methods

**Data Preprocessing**: Python {`pandas`, `matplotlib`, `seaborn`}

**Data Analysis and Visualization**: Dashboard – Microsoft PowerBI

**Version control & sharing**: Git & GitHub

## :large_orange_diamond: Objectives

- Prepare a clean, merged dataset from both Kaggle .csv files.
<br> Code: `preprocessing_code.py`

- Load the dataset into PowerBI and prepare a star schema model.
<br> File: `Consultant_Dashboard.pbix`

- Design drill-down hierarchy for Category-Genre levels, calculated columns and aggregation measures.
<br> File: `Consultant_Dashboard.pbix`

- Plan for multi-page thematic layouts with navigation and filtering panels.
<br> File: `Consultant_Dashboard.pbix`

- Create data visualizations, KPI cards and slicers.
<br> File: `Consultant_Dashboard.pbix`

- Make sure that dashboard design provides a functional market analysis flow useful to Product Managers.
<br> File: `Consultant_Dashboard.pbix`

### What this project delivers:

- A reproducible, well-documented merged datasets ready for dashboards or further analyses.

- Re-usable preprocessing code that can refresh results when source datasets are updated.

- PowerBI Consultant Dashboard – ready to use.

### Limitations & Challenges

- The `Last Updated` field does not extend beyond 2018, indicating that the source dataset is no longer current and may not fully reflect today’s app-store landscape.

- Several `Genres` contain only a small number of Apps, which limits the reliability of some category-level comparisons or trend-based interpretation. 

:grey_exclamation: This dashboard was created as a portfolio project to demonstrate analytical and data-modelling skills, as well as the Power BI proficiency. While the dataset has clear limitations, it serves adequately for those purposes.

## :large_orange_diamond: Presented skills

**Data modelling**
- Designing a *star-schema model* (fact table + dimension tables).
- Creating one-to-many and one-to-one *relationships*.
- Resolving ambiguity with *bridging tables* (App–Genre–Category).
- Creating *calculated columns* (for categorical ranges and ordering).
- Building *aggregation* measures (counts, medians, ratios).

**Data visualization**
- Designing charts with *drill-down hierarchies* (Category → Genre).
- Configuring scatterplots with *logarithmic scaling* for a clean data presentation.
- Creating *user inputs* and *KPI cards* with goal-vs-median logic.
- Creating multi-page *thematic layouts* with *page navigation* and *filter panels*.

**Storytelling**
- Translating a *consultant-focused narrative* into a functional dashboard.
- Highlighting *high-impact* apps visually.
- Organizing visuals into *purposeful pages* aligned with a consulting scenario.
- Preparing a PowerPoint to *communicate methodology*.