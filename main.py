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