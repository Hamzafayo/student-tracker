# Student Tracker Application
# Author: Hamza Fayo
# Course: IY499
# ID number: P484205

import csv
import tkinter as tk
from tkinter import messagebox

import matplotlib.pyplot as plt

STUDENTS_FILE = "students.txt"
NAME_PLACEHOLDER = "Name"
AGE_PLACEHOLDER = "Age"
GRADE_PLACEHOLDER = "Grade"

students = []


def validate_age(age_text):
    #Check age text is digits and above zero.
    # Checks that age input is a positive whole number only.
    # Ref: Tkinter messagebox for errors - https://docs.python.org/3/library/tkinter.messagebox.html
    if not age_text.isdigit():
        messagebox.showerror("Error", "Age must be a positive whole number!")
        return None
    age = int(age_text)
    if age <= 0:
        messagebox.showerror("Error", "Age must be a positive whole number!")
        return None
    return age


def validate_grade(grade_text):
    #Check grade text is digits between zero and one hundred.
    # Checks that grade input is within the 0-100 range.
    # Ref: Python str.isdigit for numeric check - https://docs.python.org/3/library/stdtypes.html#str.isdigit
    if not grade_text.isdigit():
        messagebox.showerror("Error", "Grade must be a number between 0 and 100!")
        return None
    grade = int(grade_text)
    if grade < 0 or grade > 100:
        messagebox.showerror("Error", "Grade must be between 0 and 100!")
        return None
    return grade