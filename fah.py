"""comment"""


def fever():
    """comment"""
    num = float(input())
    if 36 <= num < 38:
        print("No Fever")
    elif 38 <= num < 39:
        print("Mild Fever")
    elif 39 <= num < 40:
        print("High Fever")
    elif num >= 40:
        print("Very High Fever")


fever()
