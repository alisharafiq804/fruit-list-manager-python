# Fruit List Manager

## Project Description
Fruit List Manager is a simple beginner-friendly Python console project. It allows a user to add items to a list, remove items from the list, and exit the program.

The original uploaded file was titled `To_do_list.py`, but its actual code works with a `Fruitlist` and provides add/remove functionality. The original version also displayed an exit message without implementing a real exit option. This repository contains a cleaned and runnable version of the same basic project idea.

## Features
- Add an item to the list
- Remove an item from the list
- Display the updated list after adding or removing an item
- Exit the program
- Handles invalid menu input

## Technology
- Python 3
- Console / terminal

## How to Run

1. Install Python 3.
2. Open a terminal in this project folder.
3. Run:

```bash
python fruit_list_manager.py
```

On some systems, use:

```bash
python3 fruit_list_manager.py
```

## Example

```text
--- Fruit List Manager ---
1. Add an item
2. Remove an item
3. Exit
Choose your option: 1
Add an item to the list: Apple
Item added: ['Apple']

--- Fruit List Manager ---
1. Add an item
2. Remove an item
3. Exit
Choose your option: 2
Remove an item from the list: Apple
Item removed: []

--- Fruit List Manager ---
1. Add an item
2. Remove an item
3. Exit
Choose your option: 3
Program closed. Goodbye!
```

## Project Structure

```text
fruit-list-manager-python/
├── fruit_list_manager.py
└── README.md
```

## Concepts Used
- Lists
- `append()`
- `remove()`
- `input()`
- `print()`
- `if / elif / else`
- `while` loop
- `try / except`
- Basic user input validation

## Repository Name
Recommended GitHub repository name:

`fruit-list-manager-python`
