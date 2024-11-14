

def weekend(day) -> str:
    match day:
        case "Saturday" | "Sunday":
            print("This is a weekend!")
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            print("This is a weekday")
        case _:
            print("This is not a day")

weekend("Monday")
weekend("Sunday")
weekend("Cheese")