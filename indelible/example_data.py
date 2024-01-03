"""Example habits to seed the page when not logged in"""
import reflex as rx

from typing import List


class ExampleHabits(rx.State):
    # TODO: Convert to list of Habit Schema objects
    habits: List[dict] = [
        {"text": "Mt. Shasta Training Plan", "percentage": "21"},
        {"text": "Daily Piano Practice", "percentage": "89"},
        {"text": "Drink 2 of full water bottle", "percentage": "100%"},
        {"text": "1hr game dev session / day", "percentage": "100%"},
    ]
