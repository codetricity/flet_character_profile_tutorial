---
marp: true
theme: default
paginate: true
---

# Python Concepts

## Object-Oriented Programming Fundamentals

---

## Object Creation from Class

Classes are blueprints for creating objects.

```python
class Character:
    def __init__(self, name: str, image_path: str = None):
        self.name = name
        self.image_path = image_path
```

To create an object (instance), call the class like a function:

```python
character = Character("matt", "matt.png")
```

This creates a new `Character` object with `name="matt"` and `image_path="matt.png"`.

---

## `__init__` Constructor/Initializer

The `__init__` method is called automatically when an object is created.

```python
class Character:
    def __init__(self, name: str, image_path: str = None):
        self.name = name
        self.image_path = image_path
```

- `self` refers to the instance being created
- Parameters define what data the object needs
- `self.name` and `self.image_path` are instance attributes
- Default parameters (like `image_path = None`) are optional

---

## List of Objects

You can store multiple objects in a list:

```python
CHARACTER_LIST = [
    Character("matt", "matt.png"),
    Character("susan", "susan.png"),
    Character("jerry", "jerry.png"),
    Character("cory", "cory.png"),
    Character("kristi", "kristi.png"),
]
```

Each element in the list is a `Character` object with its own attributes.

Access objects by index: `CHARACTER_LIST[0].name` returns `"matt"`.

---

## List Comprehension

A concise way to create lists from iterables.

**Syntax:** `[expression for item in iterable]`

**Example:**

```python
options = [
    ft.DropdownOption(text=charac.name)
    for charac in characters.values()
]
```

This is equivalent to:

```python
options = []
for charac in characters.values():
    options.append(ft.DropdownOption(text=charac.name))
```

---

## Dictionary Comprehension

A concise way to create dictionaries from iterables.

**Syntax:** `{key_expression: value_expression for item in iterable}`

**Example:**

```python
characters = {character.name: character for character in CHARACTER_LIST}
```

This creates a dictionary where:

- Keys are character names (strings)
- Values are `Character` objects

Access: `characters["matt"]` returns the `Character` object for "matt".

---

## Nested Functions

Functions can be defined inside other functions.

**Example:**

```python
@ft.component
def App():
    characters = {character.name: character for character in CHARACTER_LIST}

    def handle_selection(e):
        print(e.control.value)

    return ft.Column(...)
```

- `handle_selection` is defined inside `App`
- It has access to variables in the outer scope (closure)
- Useful for event handlers and helper functions

---

## Summary

- **Object Creation**: Instantiate classes to create objects
- **`__init__`**: Constructor that initializes object attributes
- **List of Objects**: Store multiple instances in a list
- **List Comprehension**: Concise list creation syntax
- **Dictionary Comprehension**: Concise dictionary creation syntax
- **Nested Functions**: Functions defined inside other functions

---
