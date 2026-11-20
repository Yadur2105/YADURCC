# Coding Café

Lab work for the Coding Café programming course at Plaksha (FM102).

**Name:** Yadur Babbar

## What this repository contains

- `lab4/` — Git and GitHub notes (answers to the 14 questions)
- `lab5/` — functions, arguments, scope, modules and file handling
- `lab6/` — lists, sets, tuples, dictionaries and CSV files (includes `data/`)
- `lab7/` — classes, encapsulation and a bank and coffee-machine simulation
- `lab8/` — inheritance, method overriding and polymorphism (Royal Court)
- `lab9/` — NumPy, Pandas and Matplotlib (includes the generated chart images)

## How to run

Each lab is a standalone Python script. From the repository root:

```bash
pip install numpy pandas matplotlib
python3 lab9/solution.py
```

Lab 6 reads `data/menu.csv` and `data/monsoon_sales.csv` relative to the folder it is run from, so run it from inside `lab6/`:

```bash
cd lab6 && python3 solution.py
```
