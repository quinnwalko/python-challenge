import pandas as pd

election_data = "election_data.csv"

election_data_df = pd.read_csv(election_data)
election_data_df.head()

#Number of total voters
Total_Votes = election_data_df["Voter ID"].value_counts().sum
Total_Votes

#Candidates receiving votes/number of votes for each candidate
vote_count_df = election_data_df["Candidate"].value_counts()
vote_count_df

#Percentage of the vote for each candidate
election_data_df.groupby(["Candidate"]).sum()/election_data_df["Voter ID"].sum() * 100

