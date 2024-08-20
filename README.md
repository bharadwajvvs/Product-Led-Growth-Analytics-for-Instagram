# Instagram Product-Led-Growth-Analytics-for-Instagram

## Project Overview
This project focuses on analyzing and optimizing Instagram's product-led growth strategy by leveraging key metrics such as Time to Value, Total Engagements, Customer Lifetime Value (CLTV), and Ad Revenue. Through comprehensive user segmentation, funnel analysis, A/B testing, and interactive data visualizations, the project aims to enhance user engagement, retention, and overall product adoption.

## Key Objectives
### 1. Define and Calculate Core PLG Metrics:
  Metrics: Time to Value, Total Engagements, CLTV, Ad Revenue
  
  Tools: Python, SQL
### 2. User Segmentation and Funnel Analysis:
  Segmentation based on engagement and value metrics
  
  Customer journey mapping to identify drop-off points
  
  Tools: Snowflake, SQL
### 3. A/B Testing for Product Optimization:
  Design and execution of A/B tests for onboarding flows and in-app experiences
  
  Statistical analysis to inform product decisions
  
  Tools: Python, Statistical Analysis
### 4. Data Visualization and Reporting:
  Creation of interactive dashboards to visualize key insights
  
  Tools: Tableau

## Getting Started
  ### Prerequisites

  Python 3.x

  SQL (Snowflake or equivalent)

  Tableau
  
  Required Python libraries: pandas, numpy, scipy, sqlalchemy, matplotlib, seaborn

  1. Clone the Repository
   
    git clone https://github.com/yourusername/instagram-plg-analytics.git
    cd instagram-plg-analytics

  2. Set up Virtual Environment

    python3 -m venv venv
    source venv/bin/activate

  3. Install Dependencies

    pip install -r requirements.txt

## Running the Project

#### Data Preprocessing:
  
  Run the respective lines of code under data processing to clean and prepare the data from the notebook.
  
#### Calculate PLG Metrics:

  Use the PLG_metrics calculations in the notebook to calculate core metrics such as Time to Value, Total Engagements, CLTV, and Ad Revenue.

#### User Segmentation and Funnel Analysis:

  Execute the user segmentation code in the notebook to segment users and analyze their journey through the product.

#### A/B Testing:

  Run the respective lines of code under A/B testing in the notebook to perform A/B testing and analyze the results.

#### Visualize Data in:

  Visualisation using various libriraies is presented in the notebook for better understanding of the Metrics.



## Key Results

  1. Customer Lifetime Value (CLTV) Calculation:

      Method: CLTV was calculated by combining ad revenue (derived from ads clicked) and in-app purchases.
  
      Results:
  
      The CLTV for users varied significantly, with values ranging from $21.11 to $425.21, highlighting different user segments with varying contributions to revenue.

  2. Total and Average Engagements Per User:

      Method: User engagements were calculated by summing up key interaction metrics such as content views, likes, comments, shares, and sponsored content engagements.

      Results:

      Engagement levels varied widely, with total engagements per user ranging from 944 to 3285, and average engagements aligning with individual user behavior.

  3. Retention and Churn Rates:

      Method: Retention rates were calculated based on the presence of returning users and those who churned.

      Results:
  
      Returning User Rate: 49.94%
  
      Churn Rate: 49.83%

      This indicates a nearly equal split between retained and churned users.

  4. Feature Usage Rates:

      Method: Usage rates were calculated for various Instagram features, including Explore, Shopping, IGTV, Reels, and Stories.

      Results:

      Feature usage rates hovered around 50%, with the highest being Stories at 50.27% and the lowest being IGTV at 49.65%.



## Conclusion

  This project successfully leveraged data analysis, user segmentation, A/B testing, and data visualization to optimize Instagram's product-led growth strategy. The insights gained from this analysis  can be used to drive user engagement, retention, and overall product success.


## Contributing
  
  Contributions are welcome! Please feel free to submit a pull request or open an issue if you have suggestions or improvements.
