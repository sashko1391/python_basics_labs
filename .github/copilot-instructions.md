# Python Basics Labs - AI Coding Guidelines

## Project Overview
This repository contains beginner-level Python scripts demonstrating core concepts: strings, lists, loops, dictionaries, and turtle graphics. Each file focuses on a single topic with practical examples.

## Key Patterns & Conventions

### Code Structure
- **Single-purpose scripts**: Each `.py` file demonstrates one concept (e.g., `lists.py` for list operations, `turtle_practice.py` for graphics)
- **Global functions**: Define shape-drawing functions at module level, call them directly
- **No classes or modules**: Keep code simple for learning purposes

### String Handling
- Use f-strings for formatting: `f"Hello, {name.title()}"` (see `f_string.py`, `name_cases.py`)
- Apply string methods like `.title()`, `.upper()`, `.lower()`, `.strip()`, `.removesuffix()` for name formatting
- Prefer `.title()` for proper names and titles

### Data Structures
- **Lists**: Use for ordered collections; demonstrate indexing, slicing, modification (see `lists.py`)
- **Dictionaries**: Simple key-value pairs for user profiles (see `practice_from_gpt.py`)
- Modify in-place: `append()`, `insert()`, `remove()`, `pop()`, `del`

### Loops & Iteration
- **For loops**: Iterate over lists directly: `for item in items:` (see `loops.py`)
- **While loops**: For user input until quit condition
- Use `range()` for fixed iterations in graphics (e.g., `for i in range(4):` in `square()`)

### Turtle Graphics
- **Setup**: `import turtle; screen = turtle.Screen(); t = turtle.Turtle(); t.speed(1); t.color('blue')`
- **Drawing functions**: Define functions like `def square(length):` with loops for repetition
- **Angles**: Calculate turn angles as `360 / sides` for polygons
- **Cleanup**: `t.clear()` between demos, `turtle.done()` to keep window open
- **Pen control**: Use `t.penup()`, `t.pendown()` for positioning without drawing
- **Math integration**: Import `math` for trigonometric calculations (e.g., in `trianglepie()`)

### Execution & Workflow
- Run scripts directly: `python3 filename.py`
- Turtle scripts open interactive windows; close manually or use `turtle.done()`
- No build process or tests; focus on immediate execution and visual output

### Dependencies
- Standard library only: `turtle`, `math`
- No external packages required

## Examples
- Shape drawing: `polygon(sides, length)` in `turtle_practice.py`
- List manipulation: `guests.insert(0, 'new_guest')` in `lists.py`
- Input loops: `while True: number = input(prompt)` in `loops.py`