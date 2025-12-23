---
marp: true
theme: default
paginate: true
---

# Flet `ft.use_state`

## Managing Component State

---

## What is `ft.use_state`?

`ft.use_state` is a Flet hook that manages state in component functions.

It allows components to:

- Store data that persists across re-renders
- Update the UI when data changes
- Create interactive, reactive applications

**Key Point:** State changes trigger automatic component re-rendering.

---

## Basic Syntax

```python
@ft.component
def MyComponent():
    value, set_value = ft.use_state(initial_value)
    # ... rest of component
```

`ft.use_state` returns a tuple with two elements:

1. **Current value**: The current state value
2. **Setter function**: A function to update the state

---

## Example from Our App

```python
@ft.component
def App():
    characters: dict[str, Character] = {
        character.name: character for character in CHARACTER_LIST
    }

    character: Character
    character, set_character = ft.use_state(characters["matt"])
```

- Initial state: `characters["matt"]` (the "matt" character)
- `character` holds the current `Character` object
- `set_character` is used to update which character is selected

---

## Updating State

Call the setter function with the new value:

```python
def handle_selection(e):
    set_character(characters[e.control.value])
    print(e.control.value)
```

When `set_character` is called:

1. The state is updated
2. The component automatically re-renders
3. The UI reflects the new state

---

## State Persistence

State persists across re-renders:

```python
character, set_character = ft.use_state(characters["matt"])

# Even if the component re-renders,
# character will still hold its value
# until set_character() is called
```

This is different from regular variables, which would reset on each function call.

---

## Using State in the UI

The state value can be used directly in your UI:

```python
return ft.Column(
    controls=[
        ft.Dropdown(
            value=character.name,  # Uses current state
            on_select=handle_selection,
        ),
        ft.Image(src=character.image_path),  # Uses current state
        ft.Text(f"Skill: {character.skill}"),  # Uses current state
    ],
)
```

When state changes, these UI elements automatically update.

---

## Complete Flow Example

```python
@ft.component
def App():
    characters = {...}

    # 1. Initialize state
    character, set_character = ft.use_state(characters["matt"])

    # 2. Define handler that updates state
    def handle_selection(e):
        set_character(characters[e.control.value])

    # 3. Use state in UI
    return ft.Column(
        controls=[
            ft.Dropdown(
                value=character.name,
                on_select=handle_selection,
            ),
            # ... more UI using character ...
        ],
    )
```

---

## State Update Triggers Re-render

**Flow:**

1. User selects dropdown option
2. `handle_selection` is called
3. `set_character` updates the state
4. Component re-renders automatically
5. UI shows the new character's data

**Result:** The UI stays in sync with the state!

---

## Multiple State Variables

You can use `ft.use_state` multiple times:

```python
@ft.component
def MyComponent():
    count, set_count = ft.use_state(0)
    name, set_name = ft.use_state("")
    is_active, set_is_active = ft.use_state(False)

    # Each state is independent
```

Each call to `ft.use_state` creates a separate state variable.

---

## Important Rules

1. **Only use inside `@ft.component` functions**

   - `ft.use_state` only works in component functions

2. **Call at the top level**

   - Don't call `ft.use_state` inside loops, conditions, or nested functions

3. **State is component-scoped**
   - Each component instance has its own state

---

## Common Patterns

**Counter Example:**

```python
@ft.component
def Counter():
    count, set_count = ft.use_state(0)

    def increment(e):
        set_count(count + 1)

    return ft.Row([
        ft.Text(f"Count: {count}"),
        ft.ElevatedButton("+", on_click=increment),
    ])
```

---

## Comparison: Flet vs React

Flet's `ft.use_state` is inspired by React's `useState` hook.

**React:**

```javascript
import { useState } from "react";

function MyComponent() {
  const [value, setValue] = useState(initialValue);
  // ...
}
```

**Flet:**

```python
@ft.component
def MyComponent():
    value, set_value = ft.use_state(initial_value)
    # ...
```

Both use the same pattern: hook returns `[value, setter]` tuple/array.

---

## Key Similarities: Flet & React

- **Same Concept**: Both manage component-local state
- **Same Pattern**: Return value and setter function
- **Same Behavior**: State persists across re-renders
- **Same Trigger**: State updates cause automatic re-rendering
- **Same Rules**: Must be called at top level, only in components

**Difference:** React uses array destructuring `[value, setValue]`, Flet uses tuple unpacking `value, set_value`.

---

## Comparison: Client-Side vs Server-Side State

**Flet `use_state` (Client-Side):**

- State lives in the browser/client
- Changes happen instantly (no network)
- State is component-scoped
- Perfect for UI interactions

**FastAPI Backend (Server-Side):**

- State lives on the server
- Changes require HTTP requests
- State is request-scoped or session-scoped
- Perfect for data persistence

---

## FastAPI State Management Patterns

**1. Request-Scoped State:**

```python
@app.get("/items")
async def get_items(request: Request):
    # State exists only during this request
    user_id = request.state.user_id
    return {"items": get_user_items(user_id)}
```

**2. Session State:**

```python
@app.post("/login")
async def login(request: Request):
    request.session["user_id"] = user_id
    # State persists across requests via cookies
```

**3. Application State:**

```python
app.state.cache = {}
# Shared across all requests (use carefully!)
```

---

## When to Use Each Approach

**Use Flet `use_state` for:**

- UI component state (dropdowns, forms, counters)
- Client-side interactions
- Temporary UI state
- Real-time UI updates

**Use FastAPI state for:**

- User authentication/sessions
- Database connections
- Shared application data
- Persistent data storage

---

## Architecture Comparison

**Flet (Client-Side State):**

```text
User Action → Event Handler → set_state() → Re-render
     ↑                                              ↓
     └────────────── UI Update ────────────────────┘
```

**FastAPI (Server-Side State):**

```text
Client Request → FastAPI Handler → State Update → Response
     ↑                                                    ↓
     └────────────── HTTP Response ──────────────────────┘
```

**Key Difference:** Flet is synchronous and local; FastAPI is asynchronous and remote.

---

## Hybrid Approach: Flet + FastAPI

You can combine both:

```python
# Flet: Client-side UI state
@ft.component
def App():
    character, set_character = ft.use_state(characters["matt"])

    async def save_to_server():
        # FastAPI: Server-side persistence
        async with httpx.AsyncClient() as client:
            await client.post("/api/characters", json={
                "selected": character.name
            })
```

- **Flet `use_state`**: Manages UI state
- **FastAPI**: Persists data to server/database

---

## Summary

**Flet `ft.use_state`:**

- Hook for managing component state
- Returns `(current_value, setter_function)` tuple
- Similar to React's `useState`
- Client-side, component-scoped state

**FastAPI State:**

- Request, session, or application-scoped
- Server-side state management
- Requires HTTP requests for updates
- Better for persistent data

**Best Practice:** Use Flet for UI state, FastAPI for data persistence.

---
