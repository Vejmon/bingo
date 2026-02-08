from random import shuffle

def get_random_facts():
    with open("../../input.txt") as input_txt:
        facts = [line.strip() for line in input_txt]

    shuffle(facts)
    return {f"fact{i+1}": facts[i] for i in range(len(facts))}

