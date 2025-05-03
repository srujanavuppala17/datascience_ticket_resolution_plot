import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Step 1: Load the data
df = pd.read_csv("data/team_ticket_data_random.csv", parse_dates=["OpenTime", "CloseTime"])

# Step 2: (Re)calculate duration if needed
df["DurationHours"] = (df["CloseTime"] - df["OpenTime"]).dt.total_seconds() / 3600

# Step 3: Summary stats per team
summary = df.groupby('Team')['DurationHours'].agg(
    TicketCount='count',
    AvgDuration='mean',
    MedianDuration='median',
    P95Duration=lambda x: np.percentile(x, 95)
).reset_index()

# Step 4: Plot boxplot for resolution time per team
plt.figure(figsize=(14, 6))
sns.boxplot(data=df, x='Team', y='DurationHours', palette='Set3')
plt.title('Ticket Resolution Time by Team')
plt.ylabel('Resolution Time (Hours)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 5: Print or save summary table
print(summary)
