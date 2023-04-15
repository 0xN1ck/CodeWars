import itertools


def rolldice_sum_prob(sum_, dice_amount):
    if sum_ < dice_amount or sum_ > 6 * dice_amount:
        return 0

    right_rolls = []
    rolls_list = list(itertools.product(range(1, 7), repeat=dice_amount))
    for rolls in rolls_list:
        if sum(rolls) == sum_:
            right_rolls.append(rolls)

    prob = float(len(right_rolls)) / 6 ** dice_amount
    return prob


if __name__ == '__main__':
    rolldice_sum_prob(8, 2)
