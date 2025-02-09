"""
<Pseudocode:>

function get_score_result(score)
    if score < 0 or score > 100
        return "Invalid score"
    else if score >= 90
        return "Excellent"
    else if score >= 50
        return "Passable"
    else
        return "Bad"

function main()
    get score as float
    print get_score_result(score)

    random_score = random integer between 0 and 100
    print "Random score:", random_score, "->", get_score_result(random_score)

"""

import random


def get_score_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def main():
    score = float(input("Enter score: "))
    print(get_score_result(score))
    random_score = random.randint(0, 100)
    print(f"Random score: {random_score:.2f} -> {get_score_result(random_score)}")


if __name__ == "__main__":
    main()
