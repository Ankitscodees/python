import calendar

def generate_calendar(year, month, holidays=None):
    holidays = holidays or []
    cal = calendar.TextCalendar()
    output = cal.formatmonth(year, month)
    
    # Highlight holidays and weekends
    for day in range(1, calendar.monthrange(year, month)[1] + 1):
        weekday = calendar.weekday(year, month, day)
        if weekday in (5, 6) or day in holidays:
            output = output.replace(f"{day:2} ", f"**{day:2}**", 1)
    
    print(output)

# Example usage
year, month = 2024, 12
holidays = [25, 31]  # Christmas and New Year's Eve
generate_calendar(year, month, holidays)
