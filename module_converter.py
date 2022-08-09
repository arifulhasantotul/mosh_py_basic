from utils import find_max


def lbs_to_kg(weight):
    return weight * 0.45


def kg_to_lbs(weight):
    return weight / 0.45


max_num = find_max([0, 10, 5, 6])
print(max_num)