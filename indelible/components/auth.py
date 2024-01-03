"""Component for the shared login and signup layouts"""
import reflex as rx

def auth_layout(*args):
    return rx.box(
            rx.heading(
                rx.span("Indelible Login"),
                display="flex",
                flex_direction="column",
                align_items="center",
                text_align="center",
            ),
            rx.text(
                rx.span("Sign in or sign up to save your habits."),
                display="flex",
                flex_direction="column",
                align_items="center",
                text_align="center",
            ),
            *args,
            border_top_radius="lg",
            display="flex",
            flex_direction="column",
            align_items="center",
            py=12,
            gap=4,
        h="100vh",
        pt=16,
    )
