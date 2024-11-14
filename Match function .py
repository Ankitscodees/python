def process_day(day):
    match day:
        case "Monday":
            return "Start of the work week!"
        case "Tuesday":
            return "Second day of the work week!"
        case "Wednesday":
            return "Midweek already!"
        case "Thursday":
            return "Almost there!"
        case "Friday":
            return "End of the work week!"
        case "Saturday" | "Sunday":
            return "It's the weekend!"
        case _:
            return "Not a valid day."

# Example usage
day = "Wednesday"
print(process_day(day))
