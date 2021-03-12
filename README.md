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
    <li>Used the <i>Zillow housing dataset</i> provided by Zillow, a publicly available dataset, for cleaning, analyzing and modeling</li>
    <li>Transposed the data into Time Series of two lengths: 1996-2018 as well as 2010-2018</li>
    <li>Derived Historical ROI figure from the series data, and focused on the top zip code for initial analysis</li>
    <li>Completed a seasonal decomposition of the series to de-seasonalize and de-trend the data</li>
    <li>Determined the optimal non-seasonal and seasonal terms to enter for SARIMA modeling</li>
    <li>Sought the zip code / time period combination with the lowest AIC score</li>
    <li>Used Folium and Geocode to map the top 21 zip codes according to Historical ROI</li>
    <li>Evaluated forecasts for top-performing zip codes using MSE and RMSE</li>
</ul>


# Findings:


### Three zip codes (28203, 28204, and 28205) have an historical ROI above 2.5

All three of these zip codes are located in Mecklenburg county and are head & shoulders above the majority of the other zip codes on the top 21 zip codes list.

![alt text](https://github.com/emel333/time_series_home_prices/blob/main/Graphics/charlotte-and-surrounding-hroi.JPG "Historical ROI Top 21 Zip Codes In Charlotte, NC and Surrounding Areas")
![alt text](https://github.com/emel333/time_series_home_prices/blob/main/Graphics/charlotte-zips-map.JPG "Top 21 Zip Codes Plotted On Map")



### Achieving stationarity on the Series for 28204 (and other zip codes) proved challenging

Even with multiple attempts at differencing the Series, it was only a Seasonal Decomposition of the Series that enabled me to verify stationarity with the series residuals. A Dickey-Fuller test run on the series residuals output a p-value at an acceptable level (below 0.05). Because multiple zip codes revealed the same challenge with stationarity, I continued focusing on 28204.

![alt text](https://github.com/emel333/time_series_home_prices/blob/main/Graphics/differencing-onelag-28204.JPG "Zip Code 28204: One Difference")
![alt text](https://github.com/emel333/time_series_home_prices/blob/main/Graphics/seasdecom-28204.JPG "Zip Code 28204: After Seasonal Decomposition")



### Consistently Lower AIC Scores For 2010-2018 Time Series vs. 1996-2018 Time Series

By testing different non-seasonal and seasonal order terms with the SARIMA model for 5 of the top 21 zip codes, it was proven that the shorter time series was significantly better for modeling. As an example, zip code 28203 AIC score for the 1996-2018 series was ~4093 while the score for the 2010-2018 series was ~1028. This perhaps proves the disadvantage to including time series data from the period consisting of the Great Recession. The SARIMA modeling for the two series, however, revealed the same terms optimal for both periods, although the 1996-2018 series consistently showed homoscedasticity, lack of normal distribution of residuals, etc.

This led to a change in focus, to zip codes 28205 and 28012, as they both showed the lowest AIC scores irrespective of time Series length.


![alt text](https://github.com/emel333/time_series_home_prices/blob/main/Graphics/shorter-series-modeling-sarimax-vis.JPG "SARIMA Model Verification Results: Residuals + Histogram For Series 2010-2018")
![alt text](https://github.com/emel333/time_series_home_prices/blob/main/Graphics/longer-series-modeling-sarimax-vis.JPG "SARIMA Model Verification Results: Residuals + Histogram For Series 1996-2018")



# Recommendation -- Belmont, NC / Zip code 28012

Dynamic forecast RMSE of ~1023 as well as a forecasted increase in mean home prices to nearly $250,000 USD by 2023 (current mean home price in Belmont, NC as of 03/2021 is $268,653). These metrics, coupled with the contextual elements of low housing supply, high-level of demand for housing in Charlotte, and more, it is advised to focus on Belmont, NC for build-to-rent real estate development, as the potential initial investment-ROI combination is likely to fare better than the rival zip code 28205.

![alt text](https://github.com/emel333/time_series_home_prices/blob/main/Graphics/dynamic-28012.JPG "Dynamic Forecast: 28012")
![alt text](https://github.com/emel333/time_series_home_prices/blob/main/Graphics/RMSE-28012-DYNAMIC.JPG "RMSE Score For Dynamic Forecast: 28012")
![alt text](https://github.com/emel333/time_series_home_prices/blob/main/Graphics/28012-final-forecast.JPG "Zip Code28012: Forecast (2018-2023)")


#### The key adjustments made along the way:

<ul>
    <li>Changed focus from zip code 28204 to 28012 and 28205, based on AIC scores from two time series per zip code</li>
</ul>



# Summary + Further Research:


<ul>
    <li>Belmont, NC (28012) is recommended for build-to-rent investment over zip code 28205. </li>
    <li>The forecasted mean home price for zip code 28012, by 2023, is just under $250,000 USD</li>
    <li>Recent housing price data, migration trends, land cost and rental price data should be exogenous variables considered next</li>
    <li>Time series housing data from 2010-2018 is a better series for modeling than 1996-2018</li>
</ul>