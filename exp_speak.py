from math import *
from speech_drive import *


def process_eqn():
    question = gideon_asks('What is the expression: ')
    question = question.lower()
    question = question.replace(" ", "")
    if "power" in question:
        question = question.replace("power", "^")
    if "square" in question:
        question = question.replace("square", "^2")
    if "cube" in question:
        question = question.replace("cube", "^3")
    if "star" in question:
        question = question.replace("star", "*")
    if "into" in question:
        question = question.replace("into", "*")
    if "by" in question:
        question = question.replace("by", "/")
    if "plus" in question:
        question = question.replace("plus", "+")
    if "minus" in question:
        question = question.replace("minus", "-")
    if "openbrackets" in question:
        question = question.replace("openbrackets", "(")
    if "closebrackets" in question:
        question = question.replace("closebrackets", ")")

    question = question.replace(" ", "")
    return question


def get_values():
    pass
