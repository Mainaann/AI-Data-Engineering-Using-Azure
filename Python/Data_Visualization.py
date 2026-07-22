# IMPORT DATA AND READ FILE
#Import library pandas
import pandas as pd
#Reading the CSV file
df = pd.read_csv("C:/Users/maina/OneDrive/OneNote/AI Data Engineer Ann Maina/PYTHON SCRIPTS/Sales_Data.csv")
#Confirm file was found and read successfully
print(df.head())
#Understanding the dataset
print(df.info())
#Import Data Viz library
import matplotlib
#Import Package
import matplotlib.pyplot as plt
#impoort numpy for mathematical calculation
import numpy as np
#DATA VISUALIZATION USING PYTHON
##which region has the highest number of transactions - BAR CHARTS
'''
region_sales = df["Region"].value_counts()
#print (region_sales)
region_sales.plot(kind= "bar")
plt.title("Number of Transactions by Region")
plt.xlabel("Region")
plt.ylabel("Transaction")
plt.show()


#LINE CHART
#How do sales change over timeby calculating monthly sales.
df["OrderDate"]= pd.to_datetime(df["OrderDate"])#converting the date column data type
monthly_sales = df.groupby(df["OrderDate"].dt.month)(df["SalesAmount"].sum())
#print(monthly_sales)
monthly_sales.plot(kind="line", marker="o")
plt.title ("monthly_sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid
plt.show()


#which payment method are used often
payment = df["PaymentMethod"].value_counts()
payment.plot(kind="pie",autopct="%1.1f%%")
plt.title("Payment Method")
plt.ylabel("")
plt.show()

##HISTOGRAMS- How are sales amounts distributed- shows how often the values fall within different ranges 
plt.hist(df["SalesAmount"], bins=5)
plt.title("Distribution Of Amount")
plt.xlabel("Sales Amount")
plt.ylabel("Frequency")
plt.show()

##SCATTER PLOT - checking the relationship between quantity and sales amount
plt.scatter(df["Quantity"], df["SalesAmount"])
plt.title('Quantity vs SalesAmount')
plt.xlabel("Quantity")
plt.ylabel("SalesAmount")
plt.show()
'''
##Customizing a chart
plt.figure(figsize=(8,5))
region_sales = df["Region"].value_counts()
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Transactions")
plt.grid(True)
plt.show()


