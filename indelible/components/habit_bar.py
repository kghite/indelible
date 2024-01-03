"""Component for individual habit summary bar in home stack"""
import reflex as rx

from ..style import habit_bar_style


def habit_bar(props: dict) -> rx.Component:
    return rx.box(
        rx.button(
            rx.flex(
                rx.text(
                    props["text"],
                    width="36%",
                    border_right="1px solid #267E5C",
                ),
                rx.spacer(),
                width="100%",
            ),
            padding="2%",
            margin="0px auto",
            style=habit_bar_style
        ),
        width="100%",
    )
