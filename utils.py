def get_weight(level):
    level = level.lower()
    if level == "hard":
        return 3
    elif level == "medium":
        return 2
    else:
        return 1