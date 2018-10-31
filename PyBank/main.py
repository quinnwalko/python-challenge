import pandas as pd

budget_data = "budget_data.csv"

budget_data_df = pd.read_csv(budget_data)
budget_data_df.head()

Number_of_Months = budget_data_df["Date"].unique
Number_of_Months

Net_Profit_Losses = budget_data_df["Profit/Losses"].sum()
Net_Profit_Losses

budget_data_df["Profit/Losses"] - budget_data_df["Profit/Losses"].shift(1)
budget_data_df["Difference"] = budget_data_df["Profit/Losses"] - budget_data_df["Profit/Losses"].shift(1)

