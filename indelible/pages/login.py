"""Login page layout"""
import reflex as rx

from ..components.auth import auth_layout
from ..state.auth import AuthState


@rx.page(title="Indelible Login")
def login():
    """The login page."""
    return auth_layout(
        rx.box(
            rx.input(placeholder="Username", on_blur=AuthState.set_username, mb=4),
            rx.input(
                type_="password",
                placeholder="Password",
                on_blur=AuthState.set_password,
                mb=4,
            ),
            rx.button(
                "Log in",
                on_click=AuthState.login,
            ),
        ),
        rx.hstack(
            rx.text("Don't have an account yet? "),
            rx.button("Sign up here.", on_click=rx.redirect("/signup")),
        ),
    )
