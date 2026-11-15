# Lab 7 - Objects, encapsulation, and abstraction (Coding Cafe)
# Final versions of the classes (the minimum-transfer rule from the extension is included).


class AccountRecord:
    pass


# ---- Section 3: records ----
alice = AccountRecord()
alice.owner = "Alice"
alice.balance = 1200
alice.history = []
bob = AccountRecord()
bob.owner = "Bob"
bob.balance = 300
bob.history = []
print(alice.owner, alice.balance)
print(bob.owner, bob.balance)
alice.balance += 100
print("After adding to Alice:", alice.balance, bob.balance)

charlie = AccountRecord()
charlie.owner = "Charlie"
charlie.balance = 100
charlie.history = []
print(charlie.owner, charlie.balance)
assert charlie.owner == "Charlie"
assert charlie.balance == 100
assert charlie.history == []
print("Charlie's account is ready.")


# ---- Section 4: inline transfers (done by hand) ----
alice = AccountRecord()
alice.owner, alice.balance, alice.history = "Alice", 1200, []
bob = AccountRecord()
bob.owner, bob.balance, bob.history = "Bob", 300, []

amount = 250
if amount <= 0:
    print("Transfer rejected: amount must be positive.")
elif alice is bob:
    print("Transfer rejected: choose another account.")
elif amount > alice.balance:
    print("Transfer rejected: insufficient balance.")
else:
    alice.balance -= amount
    bob.balance += amount
    alice.history.append(("sent", bob.owner, amount))
    bob.history.append(("received", alice.owner, amount))
    print("Transfer complete.")
print("Balances:", alice.balance, bob.balance)
print("Alice's history:", alice.history)

# Your turn: three complete transfers
alice = AccountRecord()
alice.owner, alice.balance, alice.history = "Alice", 1200, []
bob = AccountRecord()
bob.owner, bob.balance, bob.history = "Bob", 300, []
charlie = AccountRecord()
charlie.owner, charlie.balance, charlie.history = "Charlie", 100, []

# 1. Alice -> Bob: 250
amount = 250
sender, recipient = alice, bob
if amount <= 0:
    print("Transfer rejected: amount must be positive.")
elif sender is recipient:
    print("Transfer rejected: choose another account.")
elif amount > sender.balance:
    print("Transfer rejected: insufficient balance.")
else:
    sender.balance -= amount
    recipient.balance += amount
    sender.history.append(("sent", recipient.owner, amount))
    recipient.history.append(("received", sender.owner, amount))
    print("Transfer complete.")

# 2. Bob -> Charlie: 200
amount = 200
sender, recipient = bob, charlie
if amount <= 0:
    print("Transfer rejected: amount must be positive.")
elif sender is recipient:
    print("Transfer rejected: choose another account.")
elif amount > sender.balance:
    print("Transfer rejected: insufficient balance.")
else:
    sender.balance -= amount
    recipient.balance += amount
    sender.history.append(("sent", recipient.owner, amount))
    recipient.history.append(("received", sender.owner, amount))
    print("Transfer complete.")

# 3. Charlie -> Alice: 500 (rejected)
amount = 500
sender, recipient = charlie, alice
if amount <= 0:
    print("Transfer rejected: amount must be positive.")
elif sender is recipient:
    print("Transfer rejected: choose another account.")
elif amount > sender.balance:
    print("Transfer rejected: insufficient balance.")
else:
    sender.balance -= amount
    recipient.balance += amount
    sender.history.append(("sent", recipient.owner, amount))
    recipient.history.append(("received", sender.owner, amount))
    print("Transfer complete.")

for acct in (alice, bob, charlie):
    print(acct.owner, acct.balance, acct.history)
assert (alice.balance, bob.balance, charlie.balance) == (950, 350, 300)
assert alice.history == [("sent", "Bob", 250)]
assert bob.history == [("received", "Alice", 250), ("sent", "Charlie", 200)]
assert charlie.history == [("received", "Bob", 200)]
assert alice.balance + bob.balance + charlie.balance == 1600
print("All three inline transactions behave correctly.")


# ---- Section 5: __init__ and methods ----
class BankAccountBasic:
    def __init__(self, owner, opening_balance):
        self.owner = owner
        self.balance = opening_balance

    def get_balance(self):
        return self.balance


alice_b = BankAccountBasic("Alice", 1200)
bob_b = BankAccountBasic("Bob", 300)
print("Alice:", alice_b.get_balance())
print("Bob:", bob_b.get_balance())

# Guided practice
meera = BankAccountBasic("Meera", 800)
kabir = BankAccountBasic("Kabir", 200)
combined = meera.get_balance() + kabir.get_balance()
print(combined)
assert meera.owner == "Meera" and kabir.owner == "Kabir"
assert meera.get_balance() == 800 and kabir.get_balance() == 200
assert combined == 1000


# ---- Section 6: encapsulated BankAccount ----
class BankAccount:
    def __init__(self, owner, opening_balance):
        if opening_balance < 0:
            raise ValueError("Opening balance cannot be negative.")
        self.owner = owner
        self._balance = opening_balance
        self._history = []

    def get_balance(self):
        return self._balance

    def get_history(self):
        return self._history.copy()

    def transfer_to(self, recipient, amount):
        if amount <= 0:
            return "Transfer rejected: amount must be positive."
        # Extension: minimum transfer rule (Rs 10), placed after the positive check
        if amount < 10:
            return "Transfer rejected: minimum amount is Rs 10."
        if recipient is self:
            return "Transfer rejected: choose another account."
        if amount > self._balance:
            return "Transfer rejected: insufficient balance."

        self._balance -= amount
        recipient._balance += amount
        self._history.append(("sent", recipient.owner, amount))
        recipient._history.append(("received", self.owner, amount))
        return f"Transferred Rs {amount} to {recipient.owner}."


# Method-based transfers (same starting balances as the inline section)
alice = BankAccount("Alice", 1200)
bob = BankAccount("Bob", 300)
charlie = BankAccount("Charlie", 100)
print(alice.transfer_to(bob, 250))
print(bob.transfer_to(charlie, 200))
print(charlie.transfer_to(alice, 500))
print("Balances:", alice.get_balance(), bob.get_balance(), charlie.get_balance())
print("Bob's history:", bob.get_history())
assert (alice.get_balance(), bob.get_balance(), charlie.get_balance()) == (950, 350, 300)

# Your turn: five requests
meera = BankAccount("Meera", 800)
kabir = BankAccount("Kabir", 200)
print(meera.transfer_to(kabir, 150))
print(meera.transfer_to(kabir, 0))
print(meera.transfer_to(meera, 50))
print(kabir.transfer_to(meera, 500))
print(kabir.transfer_to(meera, 100))
print("Balances:", meera.get_balance(), kabir.get_balance())
print("Histories:", meera.get_history(), kabir.get_history())
assert (meera.get_balance(), kabir.get_balance()) == (750, 250)
assert meera.get_history() == [("sent", "Kabir", 150), ("received", "Kabir", 100)]
assert kabir.get_history() == [("received", "Meera", 150), ("sent", "Meera", 100)]
print("Valid transfers work; rejected transfers leave no changes.")

# Minimum-transfer rule trial
meera = BankAccount("Meera", 800)
kabir = BankAccount("Kabir", 200)
print(meera.transfer_to(kabir, 5))
assert meera.get_balance() == 800 and kabir.get_balance() == 200
assert meera.get_history() == [] and kabir.get_history() == []
print(meera.transfer_to(kabir, 10))
assert meera.get_balance() == 790 and kabir.get_balance() == 210
assert meera.get_history() == [("sent", "Kabir", 10)]
assert kabir.get_history() == [("received", "Meera", 10)]


# ---- Section 8: CoffeeMachine ----
class CoffeeMachine:
    COFFEE_WATER_ML = 100

    def __init__(self, water_ml):
        if water_ml < 0:
            raise ValueError("Starting water cannot be negative.")
        self._water_ml = water_ml

    def get_water(self):
        return self._water_ml

    def refill_water(self, amount):
        if amount <= 0:
            return False
        self._water_ml += amount
        return True

    def make_coffee(self):
        if self._water_ml < self.COFFEE_WATER_ML:
            return "Not enough water."
        print("Heating water...")
        print("Brewing coffee...")
        print("Pouring coffee...")
        self._water_ml -= self.COFFEE_WATER_ML
        return "Coffee ready!"


machine = CoffeeMachine(150)
print(machine.make_coffee())
print("Water:", machine.get_water())
print(machine.make_coffee())
print("Refilled:", machine.refill_water(200))
print(machine.make_coffee())
print("Water:", machine.get_water())

test_machine = CoffeeMachine(100)
assert test_machine.refill_water(0) is False
assert test_machine.refill_water(-20) is False
assert test_machine.get_water() == 100
assert test_machine.make_coffee() == "Coffee ready!"
assert test_machine.get_water() == 0
assert test_machine.make_coffee() == "Not enough water."
assert test_machine.get_water() == 0
second_machine = CoffeeMachine(300)
assert second_machine.get_water() == 300
assert test_machine.get_water() == 0
print("Coffee-machine checks passed.")
