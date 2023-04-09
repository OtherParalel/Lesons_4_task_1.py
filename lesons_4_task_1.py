def mon_name(m):
    if 1 <= m <= 12:

        if m % 12 < 3:
            return "This winter"

        if m % 12 < 6:
            return "This spring"

        if m % 12 < 9:
            return "This summer"

        if m % 12 < 12:
            return "This autumn"

    return "In a year, twelve months is not a month."


result = mon_name(int(input("Enter your month number ")))
print(result)
