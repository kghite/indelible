"""Sign up page layout"""
import reflex as rx
from ..components.auth import auth_layout
from ..state.auth import AuthState


@rx.page(title="Indelible Signup")
def signup():
    return auth_layout(
        rx.box(
            rx.input(placeholder="Username", on_blur=AuthState.set_username, mb=4),
            rx.input(
                type_="password",
                placeholder="Password",
                on_blur=AuthState.set_password,
                mb=4,
            ),
            rx.input(
                type_="password",
                placeholder="Confirm password",
                on_blur=AuthState.set_confirm_password,
                mb=4,
            ),
            rx.button(
                "Sign up",
                on_click=AuthState.signup,
            ),
        ),
        rx.hstack(
            rx.text("Already have an account? "),
            rx.button("Sign in here.", on_click=rx.redirect("/login")),
        ),
    )
