from datetime import date, timedelta

def count_sundays():
    start_date = date(1901, 1, 1)
    end_date = date(2000, 12, 31)  # Replace with a specific end date if needed

    current_date = start_date
    sunday_count = 0

    while current_date <= end_date:
        if current_date.weekday() == 6:  # Sunday is represented by 6 in the weekday() function
            sunday_count += 1

        # Move to the first day of the next month
        current_date = date(current_date.year + (current_date.month // 12), (current_date.month % 12) + 1, 1)

    return sunday_count

total_sundays = count_sundays()
print(f'Total number of Sundays on the first day of the month from January 1, 2001: {total_sundays}')
