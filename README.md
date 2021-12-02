# AirBnB-Boston-Seattle
This code compares the Airbnb prices for Boston and Seattle using a one-year calendar Airbnb data set from the Kaggle website. Boston's data set spans September 2016 to September 2017, whereas Seattle's data covers January 2016 to January 2017. As a result, the data only overlaps for four months. Regardless, we will attempt to compare one-year prices, and respond to the following questions:

1-	Is Airbnb more costly in Boston or Seattle, on average?
2-	Is there pricing fluctuation over a year?
3-	What percentage of the location providers alters price over the course of a year?
You can find the data set as a zip file here or use the following links that will take you to the Kaggle website where you can get the data set:

https://www.kaggle.com/Airbnb/boston# 

https://www.kaggle.com/Airbnb/seattle/data# 

The code has been broken down into the six Sections.

## Section 1
Section 1 is for importing the libraries and red the data

## Section 2
This section gives information about the data set. It shows the size of the data, data type and some statistics about the columns

## Section 3
The data set is preprocessed in the second section of the code by dealing with null values, deleting useless columns, and providing proper formatting for the data at each column. There are 643037 rows for Boston’s data and 934542 rows for Seattle’s data, each with the "listing_id", "date" and "price" fields. For Boston, there are 2906 unique "listing id" while for Seattle, there are 3723 unique "listing id."

## Section 4
The data is groped by month over mean price in this section, and a bar plot depicts average price over a year for these two cities. It reveals that the average Airbnb pricing in Boston is higher than in Seattle. The average price in Boston varies between $180 and $230, while the average price in Seattle is around $150. Both cities have seasonal variations. September is the most costly month in Boston and August is the most expensive month in Seattle. As shown in the graph, the plot's standard deviation is quite high, suggesting that the average is not an acceptable representation for each month and that we should compare prices in better approach.

## Section 5
The data is grouped on month first and then over the listing id by averaging the price and counting the listing id, in the third Section. Each month's box plot illustrates the price distribution in each city. The first important finding is that there are a lot of outliers, and certain data are really distant from the average of the data set. By deleting 8 listing id from Boston data and one from Seattle data, all prices are less than $1000. Not only does comparing the box plots support our conclusion from the bar plot, but it also explains why that plot has such a significant standard deviation. Around the average, the data is completely imbalanced. While 50% of the data is less than the average value, which is in the range of $100 to $200, the other 50% of the data is in the range of $800. Actually, one can state that the availability of lower-than-average costs is higher in both cities at each month.

## Section 6
Pie plot in this Section indicates that around 62% of Airbnb locations in Boston change their price over a year and it is around 56% for Seattle. 

## Conclusion
Overall, the data demonstrates that Airbnb in Boston is more costly than Airbnb in Seattle on average, and that both cities' prices fluctuate over the year. The analyses also revealed that in Boston, the fraction of places that vary their prices is greater.
