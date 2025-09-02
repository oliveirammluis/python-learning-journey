import pandas as pd

# Load the Excel file
df = pd.read_excel("head_to_head.xlsx")

# Show the first few rows
print(df.head())

#Total wins, losses and draws
total_wins = df['Wins'].sum()
total_losses = df['Losses'].sum()
total_draws = df['Draws'].sum()

# Total games
total_games = total_wins + total_losses + total_draws

# Win percentage (overall)
win_percentage = (total_wins / total_games) * 100 if total_games > 0 else 0

print("\n--- Summary ---")
print(f"Total Wins: {total_wins}")
print(f"Total Losses: {total_losses}")
print(f"Total Draws: {total_draws}")
print(f"Win Percentage: {win_percentage:.2f}%")

# Convert Win % column to numeric
df["Win %"] = df["Win %"].str.replace("%", "").astype(float)

# Easy opponents: win % >= 70%
easy_opponents = df[df["Win %"] >= 70]

# Hard opponents: win % <= 30%
hard_opponents = df[df["Win %"] <= 30]

print("--- Easy Opponents ---")
print(easy_opponents[["Opponent", "Win %"]])

print("\n--- Hard Opponents ---")
print(hard_opponents[["Opponent", "Win %"]])

# Most wins
most_wins = df.loc[df["Wins"].idxmax()]
print("Most wins against:")
print(most_wins)

# Most losses
most_losses = df.loc[df["Losses"].idxmax()]
print("\nMost losses against:")
print(most_losses)

