# Lab 8 - The Royal Inheritance


class RoyalMember:
    def __init__(self, name, age, kingdom):
        self.name = name
        self.age = age
        self.kingdom = kingdom

    def introduce(self):
        print(f"I am {self.name} of {self.kingdom}.")

    def give_advice(self):
        print(f"{self.name} has no official recommendation for the kingdom.")


class Knight(RoyalMember):
    def __init__(self, name, age, kingdom, weapon, battles_won):
        super().__init__(name, age, kingdom)
        self.weapon = weapon
        self.battles_won = battles_won

    def display_details(self):
        print(f"Knight: {self.name}")
        print(f"Kingdom: {self.kingdom}")
        print(f"Weapon: {self.weapon}")
        print(f"Battles won: {self.battles_won}")

    def introduce(self):
        print(f"I am {self.name} of {self.kingdom}. I fight with {self.weapon} and have won {self.battles_won} battles.")

    def fight(self):
        print(f"Sir {self.name} enters the tournament with a {self.weapon}!")

    def give_advice(self):
        print(f"{self.name} recommends strengthening the kingdom's army.")


class Prince(RoyalMember):
    def __init__(self, name, age, kingdom, title):
        super().__init__(name, age, kingdom)
        self.title = title

    def introduce(self):
        print(f"I am {self.title} {self.name}, heir to the throne of {self.kingdom}.")

    def give_advice(self):
        print(f"{self.name} recommends expanding the kingdom's territory.")


class RoyalGuard(RoyalMember):
    def __init__(self, name, age, kingdom, post):
        super().__init__(name, age, kingdom)
        self.post = post

    def guard_duty(self):
        print(f"{self.name} is on duty at {self.post}.")

    def introduce(self):
        print(f"I am {self.name} of {self.kingdom}, a Royal Guard posted at {self.post}.")

    def give_advice(self):
        print(f"{self.name} recommends improving the security of the castle.")


# Part 1
arthur = RoyalMember("Arthur", 25, "Eldoria")
print("Name:", arthur.name, "| Age:", arthur.age, "| Kingdom:", arthur.kingdom)
arthur.introduce()

# Part 2
lancelot = Knight("Sir Lancelot", 30, "Eldoria", "Sword", 12)
cedric = Knight("Sir Cedric", 27, "Northvale", "Spear", 8)
for knight in (lancelot, cedric):
    knight.display_details()
    print("Kingdom:", knight.kingdom)
    knight.introduce()
# Answer: No. Knight inherits introduce() from RoyalMember, so it works without being redefined.
# (Knight overrides it later in Part 3, which is why introduce() shows the knight version here.)

# Part 3: Prince overrides introduce(); Knight overrides it for Task 3
gareth = Knight("Sir Gareth", 32, "Northvale", "axe", 15)
gareth.introduce()  # Expected: I am Sir Gareth of Northvale. I fight with axe and have won 15 battles.
# Answer: Knight and Prince both inherit from RoyalMember, but each overrides introduce(),
# so the object's own class decides which version runs.

# Part 4: polymorphism
william = RoyalMember("William", 45, "Eldoria")
edward = Prince("Edward", 21, "Eldoria", "Prince")
royal_court = [
    william,
    Knight("Lancelot", 30, "Eldoria", "Sword", 12),
    edward,
    Knight("Cedric", 27, "Northvale", "Spear", 8),
]
royal_court.append(Prince("Harold", 19, "Northvale", "Prince"))
royal_court.append(Knight("Gawain", 29, "Eldoria", "Mace", 5))
for member in royal_court:
    member.introduce()

# Part 5: tournament
tournament = [
    Knight("Lancelot", 30, "Eldoria", "Sword", 12),
    Knight("Cedric", 27, "Northvale", "Spear", 8),
    Knight("Gareth", 32, "Northvale", "Axe", 15),
    Knight("Gawain", 29, "Eldoria", "Mace", 5),
]
for knight in tournament:
    knight.introduce()
    knight.fight()
    print(f"Battles won: {knight.battles_won}")
best = max(tournament, key=lambda k: k.battles_won)
print(f"Most experienced knight: {best.name} with {best.battles_won} battles won.")

# Final challenge: RoyalGuard
guard1 = RoyalGuard("Tom", 35, "Eldoria", "Castle Gate")
guard2 = RoyalGuard("Ruth", 40, "Northvale", "Throne Room")
guard1.guard_duty()
guard2.guard_duty()
royal_court.extend([guard1, guard2])
for member in royal_court:
    member.introduce()

# Optional Part 6: Royal council
royal_council = [
    RoyalMember("William", 45, "Eldoria"),
    Knight("Lancelot", 30, "Eldoria", "Sword", 12),
    Knight("Cedric", 27, "Northvale", "Spear", 8),
    Prince("Edward", 21, "Eldoria", "Prince"),
    Prince("Harold", 19, "Northvale", "Prince"),
    RoyalGuard("Tom", 35, "Eldoria", "Castle Gate"),
    RoyalGuard("Ruth", 40, "Northvale", "Throne Room"),
]
for member in royal_council:
    member.introduce()
    member.give_advice()

counts = {"RoyalMember": 0, "Knight": 0, "Prince": 0, "RoyalGuard": 0}
for member in royal_council:
    if isinstance(member, Knight):
        counts["Knight"] += 1
    elif isinstance(member, Prince):
        counts["Prince"] += 1
    elif isinstance(member, RoyalGuard):
        counts["RoyalGuard"] += 1
    elif isinstance(member, RoyalMember):
        counts["RoyalMember"] += 1
for label, n in counts.items():
    print(f"Total {label}s: {n}")

security_recommendations = sum(
    1 for m in royal_council if isinstance(m, (Knight, RoyalGuard))
)
print("Council members recommending military or security improvements:", security_recommendations)
