def categorize_expense(description):
    description = description.lower()
    if any(word in description for word in ["uber", "taxi", "bus", "train"]):
        return "Transport"
    elif any(word in description for word in ["kfc", "food", "restaurant", "pizza", "coffee"]):
        return "Food"
    elif any(word in description for word in ["movie", "netflix", "game", "entertainment"]):
        return "Entertainment"
    else:
        return "Other"
