from datetime import date
def is_leap_year(input_year):
    """function to find if year is a leap year"""
    return (input_year%4==0 and input_year%100!=0) or (input_year%400==0)

def solver(start: date, end: date):
    """function to find total sunday on first day of month"""
    start_year, end_year, end_month = start.year, end.year, end.month
    start_date, end_date = start.date, end.date
    start_month = start.month if start_date==1  else (start_month+1)%12
    year_dict = {1: 31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    day_on_first, total_sunday_on_first = 1, 0
    for current_year in range(start_year,end_year+1):
        if is_leap_year(current_year):
            year_dict[2] = 29
        else:
            year_dict[2] = 28
        start_month_counter = start_month if current_year==start_year else 1
        end_month_counter = end_month if current_year==end_year else 12
        for current_month in range(start_month_counter,end_month_counter+1):
            remaining_days = year_dict[current_month]%7
            day_on_first = (day_on_first+remaining_days) % 7
            if day_on_first == 0:
                total_sunday_on_first += 1
    print(day_on_first-1)

    return total_sunday_on_first

if __name__ == "__main__":
    print(solver(date(2001, 1, 1), date(2023, 12, 31)))
            
            
            
