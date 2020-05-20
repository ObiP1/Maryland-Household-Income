# Maryland-Household-Income
An interactive map that shows the median household income for all counties within the state of Maryland. Allows users to hover over various counties and obtain their respective income values along with the county name, state name, and FIPS code. 

The program was created using Jupyter with python code. Copy & paste the code and implement your own username and API key in order to utilize the full potential of the code.

Relevant Files:
1) DataTable.csv - Data Table created to hold information (FIPS, State name, county name, median income) in order to create our map.

2) Code.py - Python code used to create map.

3) Visualization of map.png - Screenshot of the Map.


**STEP 1)**

Set up your imports. There is a username and API parameter that must be filled in as well.

![ChloroImports](https://user-images.githubusercontent.com/60532479/82475375-68ac8800-9a9a-11ea-9c1a-9cbe0546d334.png)


**STEP 2)**

Set the scope and pull data from csv file which is attached as a file in this repository.

![ScopeChloro](https://user-images.githubusercontent.com/60532479/82477114-f7ba9f80-9a9c-11ea-9e92-37eefed67757.png)


**STEP 3)**

Create a new dataframe function while using Panda's "isin()" function to filter the dataframe. Add Median Income and the FIPS code to the list of what will be displayed for each county.

![Chloro2](https://user-images.githubusercontent.com/60532479/82478304-bc20d500-9a9e-11ea-919a-0b157666d592.png)


**STEP 4)**

Create, edit, and label the chloropleth map.









