#!/usr/bin/env python3

"""
Getting Started with Python:
Variables and Data Structures
"""

from typing import List, Tuple, Dict

# Basic data types
# ----------------

# Implicit type declarations (preferred in most cases)
nation = "United States"
year = 2013
birth_rate = 12.4

# Explicit type annotations (optional, for clarity or static analysis)
nation_explicit: str = "United States"
year_explicit: int = 2013
birth_rate_explicit: float = 12.4

# Variables of different types can be concatenated if cast as strings
sentence = (
    f"The {nation} had a birth rate of {birth_rate} per thousand population in {year}."
)
print(sentence)


# Data structures
# -----------------

# Lists (are mutable)
# Implicit type declaration
car_list = ["Honda", "Ford", "Buick"]
# Explicit type annotation
car_list_explicit: List[str] = ["Honda", "Ford", "Buick"]

# Retrieve the first item:
print(car_list[0])

# Sort the list, then print
car_list.sort()
print(car_list)

# Retrieve the first two items (slicing)
print(car_list[:2])

# Add and remove items from the list
car_list.append("Kia")
if "Honda" in car_list:
    car_list.remove("Honda")
print(car_list)


# Tuples (are immutable)
# Implicit type declaration
cars_tuple = ("Honda", "Ford", "Buick")
# Explicit type annotation
cars_tuple_explicit: Tuple[str, ...] = ("Honda", "Ford", "Buick")

# Retrieve the third item (note zero index)
print(cars_tuple[2])


# Dictionaries
# Implicit type declaration
cars_dict = {"make": "Honda", "year": 2010, "color": "Silver"}
# Explicit type annotation
cars_dict_explicit: Dict[str, object] = {"make": "Honda", "year": 2010, "color": "Silver"}

# Retrieve the value for the key 'year'
print(cars_dict["year"])

# Set a new value for the key 'year'
cars_dict["year"] = 2013
print(cars_dict["year"])
