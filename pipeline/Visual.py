import matplotlib.pyplot as plt
from Analyse import top_scorers, most_assists, distance_covered

colors = ['#e63946','#f4a261','#2a9d8f','#457b9d','#e9c46a',
          '#264653','#8ecae6','#a8dadc','#f77f00','#6a4c93']

# --- Top 10 Scorers ---
fig, ax = plt.subplots(figsize=(10, 6))
data = top_scorers.head(10).reset_index()
bars = ax.bar(data['PLAYER'], data['GOALS'], color=colors)
for bar in bars:
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.1,
        str(int(bar.get_height())),
        ha='center', fontsize=10, fontweight='bold'
    )
ax.set_title('Top 10 UCL Scorers 2021-22')
ax.set_xlabel('Player')
ax.set_ylabel('Goals')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('../data/processed/ucl_scorers.png')
plt.close()

# --- Top 10 Assisters ---
fig, ax = plt.subplots(figsize=(10, 6))
data = most_assists.head(10).reset_index()
bars = ax.bar(data['PLAYER'], data['ASSISTS'], color=colors)
for bar in bars:
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.1,
        str(int(bar.get_height())),
        ha='center', fontsize=10, fontweight='bold'
    )
ax.set_title('Top 10 UCL Assisters 2021-22')
ax.set_xlabel('Players')
ax.set_ylabel('Assists')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('../data/processed/ucl_assists.png')
plt.close()

# --- Top 10 Distance Covered ---
fig, ax = plt.subplots(figsize=(10, 6))
data = distance_covered.head(10).reset_index()
bars = ax.bar(data['PLAYER'], data['DISTANCE(KM)'], color=colors)
for bar in bars:
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.1,
        str(round(bar.get_height(), 1)),
        ha='center', fontsize=10, fontweight='bold'
    )
ax.set_title('Top 10 UCL Distance Covered 2021-22')
ax.set_xlabel('Players')
ax.set_ylabel('Distance Covered (km)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('../data/processed/ucl_distance.png')
plt.close()

print("All 3 charts saved.")