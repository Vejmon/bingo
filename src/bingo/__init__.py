from random import shuffle

def get_random_facts_ensuring_coverage(no_bingo_cards: int = 20, size: int = 12):
    """
    Generate bingo cards ensuring all facts appear at least once in the first 10 cards.
    """
    with open("../../input.txt") as input_txt:
        all_facts = [line.strip() for line in input_txt]

    all_facts_set = set(all_facts)

    count = 0

    while True and count < 1000:
        first_10_cards = []
        used_facts = set()

        for _ in range(10):
            shuffled = all_facts.copy()
            shuffle(shuffled)
            card = {f"fact{i + 1}": shuffled[i] for i in range(size)}
            first_10_cards.append(card)

            used_facts.update(shuffled[:size])

        count += 1
        if used_facts >= all_facts_set:
            break

    # Generate remaining cards (11-20) - no coverage requirement
    remaining_cards = []
    for _ in range(10, no_bingo_cards):
        shuffled = all_facts.copy()
        shuffle(shuffled)
        remaining_cards.append({f"fact{i + 1}": shuffled[i] for i in range(size)})

    return first_10_cards + remaining_cards