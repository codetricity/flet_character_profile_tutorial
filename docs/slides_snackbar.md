---
marp: true
theme: default
paginate: true
---

# Flet `ft.SnackBar`

## Temporary Notifications and Messages

---

## What is a Snackbar?

A **Snackbar** is a temporary notification that appears at the bottom of the screen.

**Common Uses:**

- Show success/error messages
- Display brief information
- Provide user feedback
- Confirm actions

**Key Characteristics:**

- Appears temporarily (auto-dismisses)
- Non-intrusive (doesn't block UI)
- Positioned at bottom of screen

---

## Basic Snackbar Syntax

```python
ft.SnackBar(
    content=ft.Text("Your message here"),
    open=True,  # Controls visibility
)
```

**Required Properties:**

- `content`: The widget to display (usually `ft.Text`)
- `open`: Boolean controlling if snackbar is visible

---

## Example from Our App

```python
ft.SnackBar(
    content=ft.Text(change_snackbar_message(character.name)),
    key=f"snackbar_{snackbar_key}",
    open=snackbar_key > 0,
    on_dismiss=lambda e: set_snackbar_key(0),
)
```

This snackbar shows a character story when a character is selected.

---

## Controlling Snackbar Visibility

**Using State to Control Display:**

```python
snackbar_key, set_snackbar_key = ft.use_state(0)

ft.SnackBar(
    open=snackbar_key > 0,  # Show when key > 0
    on_dismiss=lambda e: set_snackbar_key(0),  # Hide on dismiss
)
```

**To Show the Snackbar:**

```python
def handle_selection(e):
    set_snackbar_key(snackbar_key + 1)  # Increment to show
```

---

## Why Use a Key?

The `key` property forces Flet to recognize the snackbar as "new":

```python
ft.SnackBar(
    key=f"snackbar_{snackbar_key}",
    # ...
)
```

**Why This Matters:**

- Changing the key creates a new snackbar instance
- Ensures the snackbar shows even if already open
- Allows showing multiple snackbars in sequence

**Without a changing key:** The snackbar might not appear if it's already open.

---

## Dynamic Content

You can change the snackbar message based on state:

```python
def change_snackbar_message(character_name: str):
    message = f"The story of {character_name} begins!"

    match character_name:
        case "matt":
            message = "Matt plans to take over the office..."
        case "susan":
            message = "Susan wants to save the company..."
        # ... more cases

    return message

ft.SnackBar(
    content=ft.Text(change_snackbar_message(character.name)),
    # ...
)
```

---

## Complete Flow Example

```python
@ft.component
def App():
    # 1. State to control snackbar
    snackbar_key, set_snackbar_key = ft.use_state(0)

    # 2. Handler that triggers snackbar
    def handle_selection(e):
        set_character(characters[e.control.value])
        set_snackbar_key(snackbar_key + 1)  # Show snackbar

    # 3. Snackbar component
    return ft.Column(
        controls=[
            # ... other controls ...
            ft.SnackBar(
                content=ft.Text(change_snackbar_message(character.name)),
                key=f"snackbar_{snackbar_key}",
                open=snackbar_key > 0,
                on_dismiss=lambda e: set_snackbar_key(0),
            ),
        ],
    )
```

---

## Snackbar Lifecycle

**1. Initial State:**

```python
snackbar_key = 0  # Snackbar hidden
```

**2. Trigger Display:**

```python
set_snackbar_key(snackbar_key + 1)  # Key becomes 1
# open=snackbar_key > 0  # Now True, snackbar appears
```

**3. User Dismisses:**

```python
on_dismiss=lambda e: set_snackbar_key(0)  # Key becomes 0
# open=snackbar_key > 0  # Now False, snackbar hides
```

**4. Show Again:**

```python
set_snackbar_key(snackbar_key + 1)  # Key becomes 2 (new key!)
# New snackbar instance appears
```

---

## Key Properties

**`content`** (required):

- The widget to display inside the snackbar
- Usually `ft.Text`, but can be any widget

**`open`** (required):

- Boolean controlling visibility
- `True` = visible, `False` = hidden

**`key`** (optional but recommended):

- Unique identifier for the snackbar
- Changing key forces new instance

**`on_dismiss`** (optional):

- Callback when snackbar is dismissed
- Use to reset state

---

## Common Patterns

**Simple Message:**

```python
ft.SnackBar(
    content=ft.Text("Operation successful!"),
    open=True,
)
```

**With Dismiss Handler:**

```python
show_snackbar, set_show_snackbar = ft.use_state(False)

ft.SnackBar(
    content=ft.Text("Saved!"),
    open=show_snackbar,
    on_dismiss=lambda e: set_show_snackbar(False),
)
```

**Forcing Re-display:**

```python
snackbar_id, set_snackbar_id = ft.use_state(0)

ft.SnackBar(
    key=f"msg_{snackbar_id}",
    content=ft.Text("New message"),
    open=snackbar_id > 0,
    on_dismiss=lambda e: set_snackbar_id(0),
)
```

---

## Advanced: Custom Content

Snackbars can contain more than just text:

```python
ft.SnackBar(
    content=ft.Row(
        controls=[
            ft.Icon(ft.icons.CHECK_CIRCLE, color=ft.colors.GREEN),
            ft.Text("Successfully saved!"),
            ft.ElevatedButton("Undo", on_click=undo_action),
        ],
    ),
    open=True,
)
```

---

## Snackbar vs Other UI Elements

**Snackbar:**

- Temporary, auto-dismisses
- Bottom of screen
- Non-blocking
- For brief notifications

**Dialog:**

- Requires user interaction
- Blocks UI
- For important decisions

**Banner:**

- Persistent until dismissed
- Top of screen
- For important warnings

---

## Best Practices

1. **Keep messages short**

   - Snackbars are for brief notifications
   - Long text should use dialogs

2. **Use meaningful keys**

   - `key=f"snackbar_{snackbar_key}"` helps track instances

3. **Handle dismiss events**

   - Reset state in `on_dismiss` callback

4. **Don't overuse**

   - Too many snackbars can be annoying
   - Use sparingly for important feedback

---

## Integration with `use_state`

Snackbars work perfectly with `ft.use_state`:

```python
@ft.component
def MyComponent():
    # State for snackbar control
    snackbar_key, set_snackbar_key = ft.use_state(0)

    def show_message():
        set_snackbar_key(snackbar_key + 1)

    return ft.Column(
        controls=[
            ft.ElevatedButton("Show Message", on_click=lambda e: show_message()),
            ft.SnackBar(
                content=ft.Text("Hello from snackbar!"),
                key=f"snackbar_{snackbar_key}",
                open=snackbar_key > 0,
                on_dismiss=lambda e: set_snackbar_key(0),
            ),
        ],
    )
```

---

## Summary

- **`ft.SnackBar`**: Temporary notification widget
- **`content`**: Widget to display (usually `ft.Text`)
- **`open`**: Boolean controlling visibility
- **`key`**: Unique identifier (helps force re-display)
- **`on_dismiss`**: Callback when dismissed
- **Use with `use_state`**: Control visibility with state
- **Best for**: Brief, non-intrusive notifications

---
