# Lab 5 - Potions, Libraries, and Ancient Scrolls
import math
import random
import time


# ---- Part 1: functions ----
def summon_ghost():
    print("A tiny ghost pops out of the mirror!")


def check_if_even(number):
    if number % 2 == 0:
        print(f"Yay! {number} is an even number! ")
    else:
        print(f"Oh no! {number} is odd! ")


def double_the_number(number):
    return number * 2


def cast_spell():
    print("Sparkles everywhere!")


if __name__ == "__main__":
    print("wait for the ghost..")
    summon_ghost()

    check_if_even(7)
    check_if_even(10)
    print("Doubled:", double_the_number(21))

    # Challenge one
    cast_spell()
    print("Spell complete!")

    # ---- Part 2: arguments ----
    # add_points(player_score, xp_boost=10)
    def add_points(player_score, xp_boost=10):
        total = player_score + xp_boost
        print("your total points are :", total)

    add_points(50)        # uses default bonus 10
    add_points(50, 25)    # replaces the default

    def calculate_score(score, level, bonus=2, multiplier=0.05):
        return score * level * bonus * multiplier

    print("Legal call 1:", calculate_score(score=3000, level=5))
    print("Legal call 2:", calculate_score(multiplier=0.12, score=5000, level=4))
    print("Legal call 3:", calculate_score(level=4, multiplier=0.12, score=5000))
    print("Legal call 4:", calculate_score(5000, 3, multiplier=0.05))
    # Illegal calls (left as comments; they would raise SyntaxError/TypeError):
    # calculate_score(multiplier=0.05, 5000, 3)
    # calculate_score(5000, score=300, level=2)
    # calculate_score(5000, points=300, level=2)
    # calculate_score(500, bonus=2, multiplier=0.05)

    # Challenge two (a)
    def calculate_chest_volume(length, width, height):
        return length * width * height

    print("The treasure chest can hold : ", calculate_chest_volume(3, 4, 5))

    # Challenge two (b)
    def upgrade_weapon(weapon_name, material="Iron", level=1):
        power = level * 10
        return f"Upgraded {weapon_name} with {material} to level {level}! Power is now {power}."

    print(upgrade_weapon("sword", level=5))

    # ---- Part 3: scope ----
    daily_steps = 9500

    def walk_to_the_village_1():
        global daily_steps
        daily_steps = daily_steps + 500
        print(f"Quest complete! Total steps: {daily_steps} ")

    walk_to_the_village_1()

    # Challenge 3: expected output 95, 15, 95
    tigers = 95

    def count_local_tigers():
        tigers = 15  # new local variable
        print(tigers)

    print(tigers)
    count_local_tigers()
    print(tigers)

    # ---- Part 4: modules ----
    print("Casting spell in 3...")
    time.sleep(0.1)
    print("RIBBIT! You are now a frog.")

    # Challenge 4: smoke bomb area
    radius = random.uniform(1, 20)
    area = math.pi * math.pow(radius, 2)
    print(f"Smoke bomb radius: {round(radius, 2)}")
    print(f"Smoke cloud area: {round(area, 2)}")

    # ---- Part 5: files ----
    ingredients = ["broccoli", "carrots", "garlic", "ginger"]
    with open("goodsoup.txt", "w") as scroll:
        for item in ingredients:
            scroll.write(f"Chop and add {item}\n")
    with open("goodsoup.txt", "r") as scroll:
        print("The ancient recipe says:\n")
        print(scroll.read())

    # Challenge five: stamina tracker
    def evaluate_stamina(steps, fluid_liters):
        if steps > 10000 and fluid_liters > 3:
            message = "Quest Ready for the Triund Trek!"
        else:
            message = "Rest and Hydrate at the Tavern."
        with open("ranger_stamina_log.txt", "a") as log:
            log.write(message + "\n")
        return message

    steps = int(input("Daily step count: "))
    fluid = float(input("Daily fluid intake (liters): "))
    print(evaluate_stamina(steps, fluid))

    # Grand challenge: Trial of Shadows
    def attempt_trial(hero_name):
        print(f"{hero_name} is entering the Trial of Shadows...")
        time.sleep(2)
        score = random.randint(1, 100)
        outcome = "survived" if score >= 50 else "failed"
        with open("hall_of_fame.txt", "a") as hall:
            hall.write(f"{hero_name} scored {score} and {outcome} the trial.\n")
        return score

    final_score = attempt_trial("Sir Aldric")
    print(f"Game over. Final score: {final_score}")
