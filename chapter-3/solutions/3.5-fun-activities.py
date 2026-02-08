weekday = "Wednesday"

match weekday:
    case "Monday":
        activity = "Go hiking"
    case "Tuesday":
        activity = "Take your dog to the park"
    case "Wednesday":
        activity = "Learn Python"
    case "Thursday":
        activity = "Knit a sweater"
    case "Friday":
        activity = "Go to the beach"
    case "Saturday":
        activity = "Go skate"
    case "Sunday":
        activity = "Watch a movie"
    case _:
        activity = "Go on an unknown adventure"

print("On " +  weekday + ", you should: " + activity)
