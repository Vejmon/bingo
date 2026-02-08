from random import shuffle

def get_random_facts():
    with open("../../input.txt") as input_txt:
        facts = []
        for i in range(1, 13):
            facts.append( input_txt.readline().strip())

    shuffle(facts)
    return {f"fact{i+1}": facts[i] for i in range(len(facts))}

