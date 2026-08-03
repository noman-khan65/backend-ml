def classify_stage(month):

    if month <= 10:
        return "Introduction"

    elif month <= 25:
        return "Growth"

    elif month <= 38:
        return "Maturity"

    else:
        return "Decline"