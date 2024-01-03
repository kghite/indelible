"""App and page level style definitions"""
import reflex as rx

global_style = {
    "color": "#267E5C",
    "font_family": "Sans",
    rx.Button: {
        "border": "1px solid #267E5C",
    }
}

habit_bar_style = {
    "border_top": "2px solid #267E5C",
    "border_bottom": "2px solid #267E5C",
    "border_radius": None,
    "bg": None,
    "width": "100%",
}