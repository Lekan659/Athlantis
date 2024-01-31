from datetime import datetime, timedelta

# Get the current date
today_date = datetime.now().date()

# Set the starting date to 2024-01-30
end_date = today_date - timedelta(days=29)

# Reverse count down from 2024-01-30 to 2024-01-01 and print the dates
for day in reversed(range((today_date - end_date).days + 1)):
    print(day)
    current_date = end_date + timedelta(days=day)
    formatted_date = current_date.strftime("%Y-%m-%d")
    print(formatted_date)