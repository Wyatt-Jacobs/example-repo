# Shoe Inventory Management System

A simple command-line Python program for managing a shoe warehouse inventory. It uses Object-Oriented Programming to model each shoe as an object, reads/writes inventory data to a CSV-style text file, and offers a menu-driven interface for common warehouse operations.

## Overview

The program loads shoe records from `inventory.txt`, stores each record as a `Shoe` object in memory, and lets the user view, search, update, and analyse the stock through a looping text menu.

## The `Shoe` Class

Each shoe is represented as an object with five attributes:

| Attribute  | Description                          |
|------------|---------------------------------------|
| `country`  | Country the shoe is stocked in        |
| `code`     | Unique product code (e.g. `SKU44386`) |
| `product`  | Product name (e.g. `Air Max 90`)      |
| `cost`     | Cost per unit                         |
| `quantity` | Number of units in stock              |

**Methods:**
- `get_cost()` — returns the shoe's cost.
- `get_quantity()` — returns the shoe's quantity in stock.
- `__str__()` — returns a nicely formatted, human-readable block showing all the shoe's details, bordered by divider lines.

## Core Functions

| Function | What it does |
|---|---|
| `read_shoes_data()` | Reads `inventory.txt`, skips the header row, and creates a `Shoe` object for each remaining line, appending it to `shoe_list`. Handles a missing file gracefully with a try/except. |
| `capture_shoes()` | Prompts the user to manually enter details for a new shoe and adds it to `shoe_list`. |
| `view_all()` | Prints every shoe currently in `shoe_list`, using each object's `__str__` formatting. |
| `re_stock()` | Finds the shoe with the **lowest** quantity, displays it, and asks the user whether to top up its stock. If confirmed, updates the quantity in memory and **rewrites the entire `inventory.txt` file** with the updated data. |
| `search_shoe()` | Prompts for a shoe code and prints the matching shoe's details, if found. |
| `value_per_item()` | Calculates and prints the total stock value (`cost × quantity`) for every shoe. |
| `highest_qty()` | Finds the shoe with the **highest** quantity and displays it as the item "on sale." |

## Main Menu

The program runs inside an infinite loop (`while True`) that displays a numbered menu and routes the user's choice to the matching function:

1. Read shoe data from file
2. Capture a new shoe
3. View all shoes
4. Re-stock (lowest quantity shoe)
5. Search for a shoe by code
6. View value per item
7. View highest quantity shoe (on sale)
8. Exit

Invalid menu selections are caught and prompt the user to try again. Selecting **8** breaks the loop and ends the program.

## File Format

`inventory.txt` is expected to be a comma-separated file with a header row:

```
Country,Code,Product,Cost,Quantity
South Africa,SKU44386,Air Max 90,2300,20
...
```

## How to Run

1. Ensure `inventory.txt` is in the same directory as the script.
2. Run the script:
   ```
   python inventory.py
   ```
3. Select **option 1** first to load existing stock data before using the other menu options.

## Notes / Possible Improvements

- `capture_shoes()` currently stores `cost` and `quantity` as raw strings from `input()`, rather than converting them to `float`/`int` like `read_shoes_data()` does — this could cause inconsistent data types between manually captured shoes and file-loaded shoes.
- Only `re_stock()` currently saves changes back to `inventory.txt`; shoes added via `capture_shoes()` are not persisted to the file unless a similar write-back step is added.
- Sorting and display functions could optionally use the `tabulate` module for a cleaner table layout, as noted in the code's docstrings.
