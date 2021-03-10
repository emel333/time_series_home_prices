# time_series_home_prices

Completed by: Marvin L. Mills II

#  Context: What's the best zip code in Charlotte, NC & surrounding areas to invest in? 

A real estate investment and asset management firm specializing in Build-to-rent property development has requested analysis, forecasting and reporting on the best zip code(s) for Charlotte, NC and surrounding areas.


<ul>
    <li>What does the historical data tell us?</li>
    <li>Should they be looking more towards Charlotte proper, or just outside of Charlotte perhaps?</li>
</ul>


# Process (& Data Science Tools) Used:


<ul>
    <li>Used the <i>Zillow housing dataset</i> provided by Zillow, a publicly avaialable dataset, for cleaning, analyzing and modeling</li>
    <li>Transposed the data into a Time Series of 1996-2018 as well as 2010-2018</li>
    <li>Derived Historical ROI figure from the series data, and focused on the top zip code for initial analysis</li>
    <li>Completed a seasonal decomposition of the series to de-seasonalize and de-trend the data</li>
    <li>Determined the optimal non-seasonal and seasonal terms to enter for SARIMA modeling</li>
    <li>Sought the zip code / time period combination with the lowest AIC score</li>
    <li>Used Folium and Geocode to map the top 21 zip codes according to Historical ROI</li>
</ul>


# Findings:


### Three zip codes (28203, 28204, and 28205) have an historical ROI above 2.5

All three of these zip codes are located in Mecklenburg county and are head & shoulders above the majority of the other zip codes on the top 21 zip codes list.

![alt text](https://github.com/emel333/you-got-frisked/blob/main/graphics/call_type_and_time_of_day.JPG "Call-Type-Time-of-Day-Heatmap")
![alt text](https://github.com/emel333/you-got-frisked/blob/main/graphics/time_of_day_with_age_group.JPG "Age-Group-Time-of-Day")



### Achieving stationarity on the Series for 28204 (and other zip codes) proved challenging

Even with multiple attempts at differencing the Series, it was only a Seasonal Decomposition of the Series that enabled me to verify stationarity with the series residuals. A Dickey-Fuller test run on the series residuals output a p-value at an acceptable level (below 0.05). Because multiple zip codes revealed the same challenge with stationarity, I continued focusing on 28204.

![alt text](https://github.com/emel333/you-got-frisked/blob/main/graphics/initial_baseline_model.JPG "Baseline-Model")



### Consistently Lower AIC Scores For 2010-2018 Time Series vs. 1996-2018 Time Series

By testing different non-seasonal and seasonal order terms with the SARIMA model for 5 of the top 21 zip codes, it was proven that the shorter time series was significantly better for modeling. As an example, zip code 28203 AIC score for the 1996-2018 series was ~4093 while the score for the 2010-2018 series was ~1028. This perhaps proves the disadvantage to including time series data from the period consisting of the Great Recession. The SARIMA modeling for the two series, however, revealed the same terms optimal for both periods, although the 1996-2018 series consistently showed homoscedasticity, lack of normal distribution of residuals, etc.


![alt text](https://github.com/emel333/you-got-frisked/blob/main/graphics/log_reg_smote_analysis_recall_score.JPG "Logistic-Regression-SMOTE-Date-Results")
![alt text](https://github.com/emel333/you-got-frisked/blob/main/graphics/log_reg_smote_analysis_recall_score.JPG "Logistic-Regression-SMOTE-Date-Results")



# Recommendedation -- Belmont, NC / Zip code 28012

Dynamic forecast RMSE of ~1023 as well as a forecasted increase in mean home prices to nearly $250,000 USD by 2023 (current mean home price in Belmont, NC as of 03/2021 is $268,653). These metrics, coupled with the contextual elements of low housing supply, high-level of demand for housing in Charlotte, and more, it is advised to focus on Belmont, NC for build-to-rent real estate development, as the initial investment and potential ROI combination fares better than the rival zip code 28205

![alt text](https://github.com/emel333/you-got-frisked/blob/main/graphics/final_model_scores_and_confusion_matrix.JPG "Final-Model-Random-Forests")



#### The key adjustments made along the way:

<ul>
    <li>Changed focus from zip code 28204 to 28012 and 28205, based on AIC scores from two time series per zip code</li>
</ul>



# Summary + Further Research:


<ul>
    <li>Belmont, NC (28012) is advisable for build-to-rent investment over zip code 28205. </li>
    <li>The forecasted mean home price for 28012 by 2023 is just under $250,000 USD</li>
    <li>Recent housing price data, migration trends, land cost and rental price data should be exogenous variables considered next</li>
    <li>Time series housing data from 2010-2018 is a better series for modeling than 1996-2018</li>
</ul>