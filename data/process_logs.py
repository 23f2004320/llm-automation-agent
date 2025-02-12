import os
from pathlib import Path

# Define directories
log_dir = Path("C:/Users/visha/Music/TDS project-1/data/logs")
output_file = Path("C:/Users/visha/Music/TDS project-1/data/logs-recent.txt")

# Get a list of all .log files sorted by last modified time (newest first)
log_files = sorted(log_dir.glob("*.log"), key=lambda f: f.stat().st_mtime, reverse=True)[:10]

if not log_files:
    print("No log files found.")

# Write first lines of these logs to the output file
with open(output_file, "w") as out_f:
    for log_file in log_files:
        with open(log_file, "r") as f:
            first_line = f.readline().strip()
            if first_line:
                out_f.write(first_line + "\n")

print(f"âœ… First lines of the 10 most recent .log files written to {output_file}")

