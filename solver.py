from datetime import date

def total_sundays(input_year, input_month):
    current_day = 0
    total_sundays = 0
    for current_year in range(1, input_year+1):
        end_month_counter = input_month if current_year == input_year else 12
        for current_month in range(1,end_month_counter+1):
            if current_year >= 1 and current_year <= input_year:
                if current_day == 6:
                    total_sundays += 1
        
        if current_month == 2:
            if current_year % 4 == 0 and(current_year % 100 != 0 or current_year % 400 == 0):
                current_month_days = 29
            else:
                current_month_days = 28
        elif current_month in [4, 6, 9, 11]:
            current_month_days = 30
        else:
            current_month_days = 31
        
        current_day = (current_day + current_month_days) % 7
    return total_sundays

def solver(start: date, end: date):
    """function to find total sunday on first day of month"""
    start_year, end_year, end_month = start.year, end.year, end.month
    start_date= start.day
    start_month = start.month if start_date==1  else (start_month+1)%12
    start_total_sundays = total_sundays(start_year, start_month)
    end_total_sundays = total_sundays(end_year, end_month)
    
    return end_total_sundays - start_total_sundays
    
    

if __name__ == "__main__":
    print(solver(date(2001, 1, 1), date(2023, 12, 31)))
            
            
            
