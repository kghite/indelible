"""Component for page header with info and mode buttons"""
import reflex as rx

from ..state.base import State


def header() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.popover(
                rx.popover_trigger(
                    rx.button(
                        rx.icon(tag="question_outline"),
                        size="lg",
                        variant="outline",
                    ),
                ),
                rx.popover_content(
                    rx.popover_header("Welcome to Indelible"),
                    rx.popover_body("Update the status of your daily habits below until they lock in at the end of the day"),
                    rx.popover_body("Log in using the gear button to create and log your own habits"),
                    rx.popover_close_button(),
                ),
            ),
            rx.color_mode_button(
                rx.color_mode_icon(),
                size="lg",
                variant="outline",
            ),
            rx.cond(
                State.logged_in,
                rx.menu(
                    rx.menu_button(
                        rx.avatar(
                            name=State.user.username,
                            size="md",
                            bg=None,
                            color="#267E5C",
                            border="1px solid #267E5C",
                        ),
                    ),
                    rx.menu_list(
                        rx.menu_item(
                            "Log Out",
                            on_click=State.logout,
                            variant="outline",
                            bg=None,
                            text_align="center",
                        ),
                    ),
                    variant="outline"
                ),
                rx.button(
                    rx.icon(tag="settings"),
                    on_click=State.check_login,
                    size="lg",
                    variant="outline",
                ),
            ),
            padding="1%",
        ),
        float="right",
        font_size="1.5em",
        padding="1%",
    )
