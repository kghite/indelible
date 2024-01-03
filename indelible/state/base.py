"""Base state and schema for the Indelible app"""
from typing import List, Optional

from sqlmodel import Field, Relationship
import reflex as rx


class Habit(rx.Model, table=True):
    title: str = Field()
    percentage: int = Field()
    log: str = Field()
    user_id: int = Field(foreign_key="user.id")

    user: Optional["User"] = Relationship(
        back_populates="habits"
    )


class User(rx.Model, table=True):
    username: str = Field()
    password: str = Field()

    habits: List[Habit] = Relationship(
        back_populates="user"
    )


class State(rx.State):
    user: Optional[User] = None

    def logout(self):
        """Log out a user."""
        self.reset()
        return rx.redirect("/")

    def check_login(self):
        if not self.logged_in:
            return rx.redirect("/login")

    @rx.var
    def logged_in(self):
        return self.user is not None
