import pandas as pd

df = pd.read_csv("Amazon.csv")

print("Original rows:", len(df))
print("Original columns:", len(df.columns))

df["OrderDate"] = pd.to_datetime(df["OrderDate"])

text_columns = df.select_dtypes(include="object").columns

for column in text_columns:
    df[column] = df[column].str.strip()

ConversionRate = 95.81

df["UnitPrice"] = (
    df["UnitPrice"] * ConversionRate
).round(2)

df["Tax"] = (
    df["Tax"] * ConversionRate
).round(2)

df["ShippingCost"] = (
    df["ShippingCost"] * ConversionRate
).round(2)

df["TotalAmount"] = (
    df["TotalAmount"] * ConversionRate
).round(2)

df["GrossAmount"] = (
    df["Quantity"] * df["UnitPrice"]
).round(2)

df["DiscountAmount"] = (
    df["GrossAmount"] * df["Discount"]
).round(2)

df["NetSalesAmount"] = (
    df["GrossAmount"] - df["DiscountAmount"]
).round(2)

df["OrderYear"] = df["OrderDate"].dt.year

df["OrderMonth"] = df["OrderDate"].dt.month

df["OrderMonthName"] = df["OrderDate"].dt.strftime("%B")

df["OrderQuarter"] = (
    "Q" + df["OrderDate"].dt.quarter.astype(str)
)

df["OrderDayOfWeek"] = (
    df["OrderDate"].dt.strftime("%A")
)

df["OrderDayNumber"] = (
    df["OrderDate"].dt.dayofweek + 1
)

df["OrderValueBand"] = pd.cut(
    df["TotalAmount"],
    bins=[0, 25000, 50000, 100000, 200000, float("inf")],
    labels=[
        "Under 25,000",
        "25,000-49,999",
        "50,000-99,999",
        "100,000-199,999",
        "200,000+"
    ]
)

print("Final rows:", len(df))
print("Final columns:", len(df.columns))

print(df.head())

df.to_csv(
    "Amazon_ETL_Processed.csv",
    index=False
)

print("ETL completed successfully")