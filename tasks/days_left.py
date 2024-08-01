from datetime import datetime, timedelta

public_holidays = ['2024-01-01', '2024-02-23', '2024-03-11', '2024-05-01', '2024-05-31', '2024-07-15', '2024-12-25']

def is_working_day(date):
    if date.weekday() >= 5:
        return False
    if date.strftime('%Y-%m-%d') in public_holidays:
        return False
    return True

def calculate_days(graduation_date_str):
    today = datetime.today()
    graduation_date = datetime.strptime(graduation_date_str, '%Y-%m-%d')
    total_days = (graduation_date - today).days
    total_days_excl_final = total_days - 1
    current_date = today
    working_days = 0
    while current_date < graduation_date:
        if is_working_day(current_date):
            working_days += 1
        current_date += timedelta(days=1)
    return total_days, total_days_excl_final, working_days
