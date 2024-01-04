"""Counting sundays"""
from datetime import date


def total_sundays(input_year, input_month):
    """function to find total sundays in first day of month"""
    current_day = 0
    sundays = 0
    for current_year in range(1, input_year + 1):
        end_month_iter = input_month if current_year == input_year else 12
        for month in range(1, end_month_iter + 1):
            if current_year >= 1 and current_year <= input_year:
                if current_day == 6:
                    sundays += 1
            if month == 2:
                if current_year % 4 == 0 and (
                    current_year % 100 != 0 or current_year % 400 == 0
                ):
                    days_in_month = 29
                else:
                    days_in_month = 28
            elif month in [4, 6, 9, 11]:
                days_in_month = 30
            else:
                days_in_month = 31
            current_day = (current_day + days_in_month) % 7

    return sundays


def solver(start: date, end: date):
    """function to find total sunday on first day of month"""
    start_year, end_year, start_month, end_month = (
        start.year,
        end.year,
        start.month,
        end.month,
    )
    start_date = start.day
    start_month = start.month if start_date == 1 else (start_month + 1) % 12
    start_total_sundays = total_sundays(start_year, start_month)
    end_total_sundays = total_sundays(end_year, end_month)

    return end_total_sundays - start_total_sundays


if __name__ == "__main__":
    print(solver(date(2001, 1, 13), date(2023, 12, 31)))
