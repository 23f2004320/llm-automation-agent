from datetime import datetime

# Read the file
with open("C:/data/dates.txt", "r") as file:
    dates = file.readlines()

wednesday_count = 0

for date in dates:
    date_str = date.strip()
    parsed_date = None

    # Try different date formats
    for fmt in ("%Y-%m-%d", "%Y/%m/%d %H:%M:%S", "%Y/%m/%d"):
        try:
            parsed_date = datetime.strptime(date_str, fmt)
            break  # Stop checking formats once one is successful
        except ValueError:
            continue

    if parsed_date and parsed_date.weekday() == 2:  # Wednesday is weekday 2
        wednesday_count += 1

# Write the count to file
with open("C:/data/dates-wednesdays.txt", "w") as output_file:
    output_file.write(str(wednesday_count) + "\n")

print(f"Number of Wednesdays: {wednesday_count}")

