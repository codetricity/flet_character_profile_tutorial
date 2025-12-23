---
marp: true
theme: default
paginate: true
---

# Python Dataclasses

## Simplifying Class Definitions

---

## Our Current Character Class

```python
class Character:
    def __init__(
        self,
        name: str,
        image_path: str = None,
        *,
        skill: int = 0,
        luck: int = 0,
        stamina: int = 0,
    ):
        self.name = name
        self.image_path = image_path
        self.skill = skill
        self.luck = luck
        self.stamina = stamina
```

This is a lot of boilerplate code just to store some data!

---

## What is a Dataclass?

A **dataclass** is a decorator that automatically generates common methods for you.

**Benefits:**

- Less boilerplate code
- Automatic `__init__` generation
- Automatic `__repr__` (string representation)
- Automatic `__eq__` (equality comparison)
- Type hints are required and enforced

**Perfect for:** Classes that primarily store data (like our `Character` class)

---

## Converting to a Dataclass

**Step 1:** Import `dataclass` from the `dataclasses` module

```python
from dataclasses import dataclass
```

**Step 2:** Add the `@dataclass` decorator

**Step 3:** Remove `__init__` and use field declarations instead

---

## The Dataclass Version

```python
from dataclasses import dataclass

@dataclass
class Character:
    name: str
    image_path: str = None
    skill: int = 0
    luck: int = 0
    stamina: int = 0
```

**That's it!** Much cleaner, right?

---

## Before and After Comparison

**Before (Regular Class):**

```python
class Character:
    def __init__(
        self,
        name: str,
        image_path: str = None,
        *,
        skill: int = 0,
        luck: int = 0,
        stamina: int = 0,
    ):
        self.name = name
        self.image_path = image_path
        self.skill = skill
        self.luck = luck
        self.stamina = stamina
```

---

**After (Dataclass):**

```python
@dataclass
class Character:
    name: str
    image_path: str = None
    skill: int = 0
    luck: int = 0
    stamina: int = 0
```

**Reduced from 18 lines to 7 lines!**

---

## How It Works

The `@dataclass` decorator automatically generates:

1. **`__init__` method** - Initializes all fields
2. **`__repr__` method** - Nice string representation
3. **`__eq__` method** - Compares all fields for equality

You get all of this functionality automatically!

---

## Usage Remains the Same

You create and use `Character` objects exactly the same way:

```python
character = Character("matt", "matt.png", skill=5, luck=2, stamina=3)
```

**Note:** With dataclasses, keyword-only arguments (the `*` separator) are not needed. All fields with defaults come after fields without defaults.

---

## Keyword-Only Arguments

In the original class, we used `*` to make `skill`, `luck`, and `stamina` keyword-only:

```python
def __init__(
    self,
    name: str,
    image_path: str = None,
    *,  # Everything after this must be keyword-only
    skill: int = 0,
    luck: int = 0,
    stamina: int = 0,
):
```

In dataclasses, this is handled automatically by field order.

---

## Field Order Matters

**Rule:** Fields without defaults must come before fields with defaults.

**Correct:**

```python
@dataclass
class Character:
    name: str                    # No default - required
    image_path: str = None       # Has default - optional
    skill: int = 0               # Has default - optional
    luck: int = 0                # Has default - optional
    stamina: int = 0             # Has default - optional
```

---

**Incorrect:**

```python
@dataclass
class Character:
    name: str = "unknown"        # Has default
    image_path: str              # No default - ERROR!
```

Python will raise a `TypeError` if you mix them up.

---

## Automatic `__repr__` Method

Dataclasses automatically generate a nice string representation:

```python
character = Character("matt", "matt.png", skill=5, luck=2, stamina=3)
print(character)
```

**Output:**

```text
Character(name='matt', image_path='matt.png', skill=5, luck=2, stamina=3)
```

Much more useful than the default `<__main__.Character object at 0x...>`!

---

## Automatic `__eq__` Method

Dataclasses automatically compare all fields:

```python
char1 = Character("matt", "matt.png", skill=5)
char2 = Character("matt", "matt.png", skill=5)
char3 = Character("matt", "matt.png", skill=3)

print(char1 == char2)  # True - all fields match
print(char1 == char3)  # False - skill differs
```

Without dataclasses, `char1 == char2` would be `False` (compares object identity).

---

## Creating Characters (Same as Before)

Your existing code works exactly the same:

```python
CHARACTER_LIST = [
    Character("matt", "matt.png", skill=5, luck=2, stamina=3),
    Character("susan", "susan.png", skill=7, luck=5, stamina=8),
    Character("jerry", "jerry.png", skill=4, luck=2, stamina=5),
    Character("cory", "cory.png", skill=3, luck=9, stamina=4),
    Character("kristi", "kristi.png", skill=6, luck=6, stamina=9),
]
```

No changes needed to your existing code!

---

## Additional Dataclass Features

You can customize dataclasses further:

**Frozen dataclasses (immutable):**

```python
@dataclass(frozen=True)
class Character:
    name: str
    # Fields cannot be changed after creation
```

---

**Field defaults with `field()`:**

```python
from dataclasses import dataclass, field

@dataclass
class Character:
    name: str
    tags: list = field(default_factory=list)
    # Creates a new empty list for each instance
```

---

## When to Use Dataclasses

**Use dataclasses when:**

- Your class primarily stores data
- You want less boilerplate code
- You need automatic `__init__`, `__repr__`, and `__eq__`
- Type hints are important to you

---

**Don't use dataclasses when:**

- Your class has complex initialization logic
- You need custom `__init__` behavior
- Your class is primarily for behavior, not data storage

---

## Summary

**Dataclasses:**

- Reduce boilerplate code significantly
- Automatically generate `__init__`, `__repr__`, and `__eq__`
- Require type hints (good practice!)
- Work seamlessly with existing code
- Perfect for data-holding classes like `Character`

**Key Takeaway:** If your class is mostly about storing data, use `@dataclass`!
