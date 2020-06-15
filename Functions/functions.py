from json import load
from random import randint
from time import sleep, ctime

def open_data(filename):
    with open(filename, 'r') as f:
        data = load(f)
    return data

def append_score(filename, score):
    with open(filename, 'a') as f:
        f.write(f"{ctime()}:    {score}\n")
def rng():
    return randint(1, 101)

def print1(text=''):
    sleep(0.75)
    print(text)

def print2(text=''):
    sleep(1)
    print(text)

def print3(text=''):
    sleep(2)
    print(text)

def print_s1(text):
    print(text)
    sleep(0.75)

def print_s2(text):
    print(text)
    sleep(1.5)

def prompt(context=''):
    while True:
        sleep(0.2)
        try:
            if context:
                print(f"\n{context}")
            action = int(input("> "))
            return action
        except ValueError:
            print_s1("Error: Invalid input")
            continue