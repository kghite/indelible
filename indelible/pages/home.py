"""Home page layout"""
import reflex as rx

from ..components.habit_bar import habit_bar
from ..components.header import header
from ..example_data import ExampleHabits


@rx.page(route="/", title="Indelible")
def index() -> rx.Component:
    return rx.fragment(
        rx.box(
            header(),
            rx.vstack(
                rx.flex(
                    rx.box(
                        rx.heading("Indelible"),
                        rx.text("The permanent record habit tracker"),
                        padding="2%",
                        width="36%"
                    ),
                    rx.spacer(),
                    width="100%",
                ),
                font_size="2em",
            ),
            # border_bottom="4px solid #267E5C",
            margin_bottom="2%",
        ),

        rx.vstack(
            rx.foreach(
                ExampleHabits.habits,
                habit_bar,
            ),
            rx.box(
                rx.button(
                    rx.icon(
                        tag="add",
                    ),
                    size="lg",
                    variant="outline",
                    margin_top="2%",
                    margin_right="2%",
                    float="right",
                ),
                width="100%",
            ),
        ),
    )
