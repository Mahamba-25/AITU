import random

def create_bingo_card():
    return {letter: random.sample(range(start, start + 15), 5) for letter, start in zip('BINGO', range(1, 76, 15))}

def display_bingo_card(bingo_card):
    for letter, numbers in bingo_card.items():
        print(f'{letter}: {numbers}')

display_bingo_card(create_bingo_card())
