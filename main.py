import flet as ft
from dataclasses import dataclass


@dataclass
class Character:
    name: str
    image_path: str = None
    skill: int = 0
    luck: int = 0
    stamina: int = 0


CHARACTER_LIST = [
    Character("matt", "matt.png", skill=5, luck=2, stamina=3),
    Character("matt", "matt.png", skill=5, luck=2, stamina=3),
    Character("susan", "susan.png", skill=7, luck=5, stamina=8),
    Character("jerry", "jerry.png", skill=4, luck=2, stamina=5),
    Character("cory", "cory.png", skill=3, luck=9, stamina=4),
    Character("kristi", "kristi.png", skill=6, luck=6, stamina=9),
]

print(f"Character string representation: {CHARACTER_LIST[0]}")

print(f"Contents of index 0 and 1 the same? {CHARACTER_LIST[0] == CHARACTER_LIST[1]}")


@ft.component
def App():
    characters: dict[str, Character] = {
        character.name: character for character in CHARACTER_LIST
    }

    character: Character
    character, set_character = ft.use_state(characters["matt"])
    snackbar_key, set_snackbar_key = ft.use_key = ft.use_state(0)

    def handle_selection(e):
        set_character(characters[e.control.value])
        set_snackbar_key(snackbar_key + 1)
        print(e.control.value)

    def change_snackbar_message(character_name: str):
        message = f"The story of {character_name} begins!"

        match character_name:
            case "matt":
                message = (
                    "Matt plans to take over the office by getting "
                    + "everyone else fired"
                )
            case "susan":
                message = (
                    "Susan wants to save the company by adapting "
                    + "a new AI model she tuned for healthcare data "
                    + "to  product delivery logistics"
                )
            case "jerry":
                message = (
                    "Jerry is supporting Susan.  He is trying to "
                    + "tune her AI model.  He asked her out last year, "
                    + "but got turned down.  He still admires her as a "
                    + "person and leader"
                )
            case "cory":
                message = (
                    "Cory met a woman at a bar who manages logistics "
                    + "at a health product delivery.  His new friend "
                    + "agreed to use Susan's prototype in a limited trial"
                )
            case "kristi":
                message = (
                    "Kristi initially was supporting Matt after she "
                    + "slept with him following a company bar outing "
                    + "in San Francisco.  However, she is now supporting "
                    + "Susan's plan and has advanced the distribution algorithm."
                )

        return message

    return ft.Column(
        controls=[
            ft.Text(value="Dropdown Demo", size=30),
            ft.Dropdown(
                label="character",
                options=[
                    ft.DropdownOption(text=charac.name)
                    for charac in characters.values()
                ],
                value=character.name,
                on_select=handle_selection,
            ),
            ft.Row(
                [
                    ft.Image(src=character.image_path),
                    ft.Column(
                        controls=[
                            ft.Text(f"Skill: {character.skill}", size=22),
                            ft.Text(f"Luck: {character.luck}", size=22),
                            ft.Text(f"Stamina: {character.stamina}", size=22),
                        ],
                    ),
                ],
            ),
            ft.SnackBar(
                content=ft.Text(change_snackbar_message(character.name)),
                key=f"snackbar_{snackbar_key}",
                open=snackbar_key > 0,
                on_dismiss=lambda e: set_snackbar_key(0),
            ),
        ],
    )


ft.run(lambda page: page.render(App))
