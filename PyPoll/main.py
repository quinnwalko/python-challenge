import pandas as pd

election_data = "election_data.csv"

election_data_df = pd.read_csv(election_data)
election_data_df.head()

Total_Votes = election_data_df["Voter ID"].value_counts().sum
Total_Votes

