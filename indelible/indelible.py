"""Indelible app assembly"""
from rxconfig import config

import reflex as rx

from .pages import home, login, signup
from .state.base import State
from .style import global_style

app = rx.App(style=global_style)
app.compile()
