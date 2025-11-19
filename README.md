# Google Apps Performance <br> Consultant Dashboard

## :black_circle: About Me

I am a Doctor of Neuroscience with strong experience in data analysis, statistical modelling and research design. I focus on translating complex data into actionable insights for business and policy.

**Skills & tools**: advanced R, intermediate Python (*pandas*, *NumPy*, *matplotlib*, *seaborn*, *scipy*), developing my skills in Power BI & PowerApps. I enjoy data wrangling, visualization, and project management. My experience was gained through academic research and industry projects.

&emsp; **Location**: Poland, Krakow <br> 
&emsp; **Contact**: dominika.a.drazyk@gmail.com <br> 
&emsp; **LinkedIn**: [in/dominika-drazyk-otw95](https://www.linkedin.com/in/dominika-drazyk-otw95/)


## :black_circle: Overview

Imagine you are a *Market Research Consultant* hired by a mobile app company. One of your tasks is to assist the *Product Manager* and evaluate their app ideas. 
Managers need **fast, objective insight** into how their concept fits the current mobile-app landscape.

This Consultant Dashboard provides exactly that.
It helps the Consultant to:
- present the **most competitive** app categories;
- showcase the specific category targeted by the creators;
- **compare their goals against market medians**.

With these inputs, the app creators can ground their decisions in data rather than assumptions and quickly understand where their app stands relative to the market.


### Data & Source Metadata

External data source (Kaggle): Google Play Store Apps dataset [<link>](https://www.kaggle.com/datasets/lava18/google-play-store-apps?resource=download) Authored by L. Gupta (2019) 


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

Data Preprocessing: Python {`pandas`, `matplotlib`, `seaborn`}

Data Analysis and Visualization: Dashboard – Microsoft PowerBI

Version control & sharing: Git & GitHub


## :black_circle: Objectives

- Prepare a clean, merged dataset from both Kaggle .csv files.
<br> Code: `preprocessing_code.py`

- Load the dataset into PowerBI and prepare a star schema model.
<br> File: `AppPerformance_dashboard.pbix`

- Design drill-down hierarchy for Category-Genre levels, calculated columns and aggregation measures.
<br> File: `AppPerformance_dashboard.pbix`

- Plan for multi-page thematic layouts with navigation and filtering panels.
<br> File: `AppPerformance_dashboard.pbix`

- Create data visualizations, KPI cards and slicers.
<br> File: `AppPerformance_dashboard.pbix`

- Make sure that dashboard design provides a functional market analysis flow useful to Product Managers.
<br> File: `AppPerformance_dashboard.pbix`


### What this project delivers:

- A reproducible, well-documented merged datasets ready for dashboards or further analyses.

- Re-usable preprocessing code that can refresh results when source datasets are updated.

- PowerBI Consultant Dashboard – ready to use.


### Limitations of data coverage

- The `Last Updated` field does not extend beyond 2018, indicating that the source dataset is no longer current and may not fully reflect today’s app-store landscape.

- Several `Genres` contain only a small number of Apps, which limits the reliability of some category-level comparisons or trend-based interpretation. 

:grey_exclamation: This dashboard was created as a portfolio project to demonstrate analytical and data-modelling skills, as well as the Power BI proficiency. While the dataset has clear limitations, it serves adequately for those purposes.


## :black_circle: Presented skills

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