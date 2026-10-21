# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# MAGIC %md
# MAGIC ## 0. Import Libraries

# COMMAND ----------

import pandas as pd
import numpy as np

# COMMAND ----------

# MAGIC %md
# MAGIC ## DATA INGESTION

# COMMAND ----------

# calling our table using spark from databricks catalog
Stores=spark.table("workspace.default.stores")

# converting the spark table into pandas
Stores=Stores.toPandas()

#ingesting the data from our table

display(Stores)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. DATA EXPLORATION

# COMMAND ----------

# looking for the  size of the table
Stores.shape

# COMMAND ----------

#checking for data/coloumn types;objects,int64,datestamps
Stores.dtypes

# COMMAND ----------

#checking for number of nulls values in each given column
Stores.isnull().sum()

# COMMAND ----------

#checking for number of duplicated values in a column
Stores.duplicated().sum()

# COMMAND ----------

# OR USE THIS CODE
number_of_duplicates = Stores.duplicated().sum()
print(f"the number of duplicates is {number_of_duplicates}")

# COMMAND ----------

#returns different/unique values in a column without repeating thme
Stores["store_format"].unique()

# COMMAND ----------

#counting the number of unique values in a column
Stores["store_format"].value_counts()


# COMMAND ----------

#returning all unique store names
Stores["store_name"].unique()

# COMMAND ----------

#returning the number of stores in each province
Stores["province"].value_counts()

# COMMAND ----------

# Returning the statistics
# al records for physical size of each store in square meter
Stores["floor_area_sqm"].describe().T

# COMMAND ----------

# OR USE THIS CODE to check

Stores["floor_area_sqm"].min()
Stores["floor_area_sqm"].mean()
Stores["floor_area_sqm"].std()
Stores["floor_area_sqm"].max()

# COMMAND ----------

#checking for managers and how many stores they run
Stores["region_manager"].value_counts()

# COMMAND ----------

#checking when was the first store opened,and the last one oepned
(Stores["opened_year"]).min()
(Stores["opened_year"]).max()

# COMMAND ----------

#checking for nearby competitors,No competitors nearby,but 12 are far
print(Stores["has_nearby_competitor"].value_counts())

# COMMAND ----------

#checking the first date of opening and dropping missing values
print(Stores["competitor_open_date"].dropna().min())

#checking the last date of opening and dropping missing values
print(Stores["competitor_open_date"].dropna().max())

# COMMAND ----------

#changing the competitor_open_date from object to a time stamp
Stores["competitor_open_date"]=pd.to_datetime(Stores["competitor_open_date"])

# COMMAND ----------

display(Stores)

# COMMAND ----------

# Load transactions data (from TRANSACTIONS.EDA notebook)
transactions = spark.table("workspace.default.transactions").toPandas()

# Left join (keeps all transaction rows)
merged_df = pd.merge(transactions, Stores, on="store_id", how="left")

display(merged_df)

# COMMAND ----------

# DBTITLE 1,Convert basket_value_zar to float (2 decimal places)
# Convert basket_value_zar from string to float, rounded to 2 decimal places
merged_df["basket_value_zar"] = pd.to_numeric(merged_df["basket_value_zar"]).round(2)

display(merged_df[["transaction_id", "basket_value_zar"]].head(10))

# COMMAND ----------

Stores['competitor_open_date'] = Stores['competitor_open_date'].dt.date

# COMMAND ----------

display(merged_df.head(10))


# COMMAND ----------

display(merged_df)


# COMMAND ----------

#checking for raw and columns in the new table
merged_df.shape

# COMMAND ----------

#checking for null or missing values in the table
merged_df.isnull().sum()

# COMMAND ----------

# Drop rows with missing customer_id
merged_df = merged_df.dropna(subset=["customer_id"])


# COMMAND ----------


#Fill missing competitor_open_date with "No competitor" (means the store has no competitor)
merged_df["competitor_open_date"] = merged_df["competitor_open_date"].fillna("No competitor").astype(str)
display(merged_df.head(10))

# COMMAND ----------

# DBTITLE 1,STOCKOUTS
#importing Libraries for the new table
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# COMMAND ----------

# calling our table using spark from databricks catalog
stockouts=spark.table("workspace.default.stockouts")

# converting the spark table into pandas
stockouts=stockouts.toPandas()

#ingesting the data from our table

display(stockouts)

# COMMAND ----------

# DBTITLE 1,Exploratory Data Analysis
#checking for rows and columns in the table
stockouts.shape

# COMMAND ----------

#checking for null or missing values
stockouts.isnull().sum()

# COMMAND ----------

#checking for data types
stockouts.dtypes

# COMMAND ----------

#change the date from an object/string to datestamp
stockouts["date"] = pd.to_datetime(stockouts["date"])

# COMMAND ----------

#checking for duplicated rows
stockouts.duplicated().sum()

# COMMAND ----------

#checking for numerical distributions on the duration 
stockouts["duration_hours"].describe()

# COMMAND ----------

#checking for unique categories
stockouts["category"].value_counts()

# COMMAND ----------

# creating weekdays/weekends from the date column
stockouts["day_type"] = stockouts["date"].dt.dayofweek.apply(
    lambda d: "Weekend" if d >= 5 else "Weekday"
)

stockouts[["date", "day_type"]].head()

# COMMAND ----------

stockouts.groupby("date")["duration_hours"].sum().plot(kind="line", figsize=(10, 4))
plt.title("Total Stockout Duration Over Time")
plt.show()

# COMMAND ----------

# Count of gaps (from the note column) per day, split by day classification (Weekday/Weekend)
gaps = stockouts[stockouts["note"].str.contains("gap", case=False, na=False)]

# Count gaps per day, then separate the counts into Weekday vs Weekend columns
gaps_per_day = gaps.groupby([gaps["date"].dt.date, "day_type"]).size().unstack(fill_value=0)

display(gaps_per_day)

# Line graph showing how the gap counts change over time for each day classification
gaps_per_day.plot(kind="line", figsize=(10, 4), title="Number of Gaps per Day by Day Classification")
plt.xlabel("Date")
plt.ylabel("Number of Gaps")
plt.show()

# COMMAND ----------

#displaing the final stockouts
display(stockouts)

# COMMAND ----------

# DBTITLE 1,Cell 45
# Merge stockouts with merged_df, keeping all columns from both
freshmart = pd.merge(stockouts, merged_df, on="store_id", how="left", suffixes=("_stockout", "_merged"))
display(freshmart)

# COMMAND ----------

