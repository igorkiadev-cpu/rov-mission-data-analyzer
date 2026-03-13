# ROV Mission Data Analyzer

Python tool for analyzing ROV mission logs from subsea inspection operations.

This project demonstrates how operational data from ROV missions can be processed and analyzed using Python.

## Overview

ROV (Remotely Operated Vehicle) missions generate operational logs containing mission events, inspection activities and depth profiles.

This tool reads mission log data and extracts useful operational insights.

## Features

- Parse ROV mission log datasets
- Calculate mission metrics
- Identify inspection events
- Visualize depth profile
- Generate mission summaries

## Technologies

- Python
- Pandas
- Matplotlib

## Example Dataset

The repository includes a simulated ROV mission log dataset:

```
timestamp,depth,status,event
00:00,0,launch,ROV deployed
00:10,30,inspection,pipeline check
00:20,32,inspection,anode inspection
00:30,35,inspection,structure inspection
00:40,10,ascent,return to surface
00:50,0,recovery,ROV recovered
```

## Example Output

The script calculates mission metrics such as:

- Maximum depth
- Total events
- Inspection activity

It also generates a **depth profile visualization** of the mission.

## How to Run

Install dependencies:

```
pip install pandas matplotlib
```

Run the script:

```
python main.py
```

## Use Cases

- Offshore inspection operations
- Subsea pipeline inspection
- ROV mission data analysis
- Offshore operational reporting

## Author

Igor Carvalho  
Python Developer | Offshore Operations Background
