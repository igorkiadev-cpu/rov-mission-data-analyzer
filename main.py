import pandas as pd
import matplotlib.pyplot as plt

# Load mission data
data = pd.read_csv("data/sample_mission_log.csv")

print("\nROV Mission Log:")
print(data)

# Calculate mission metrics
max_depth = data["depth"].max()
min_depth = data["depth"].min()
total_events = len(data)

inspection_events = data[data["status"] == "inspection"]

print("\nMission Summary")
print("----------------------")
print("Maximum Depth:", max_depth, "meters")
print("Minimum Depth:", min_depth, "meters")
print("Total Events:", total_events)
print("Inspection Events:", len(inspection_events))

# Plot depth profile
plt.plot(data["depth"])
plt.title("ROV Depth Profile")
plt.xlabel("Mission Step")
plt.ylabel("Depth (meters)")
plt.show()
