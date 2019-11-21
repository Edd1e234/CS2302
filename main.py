# This main will be use as workspace for quick tests and for review.
from data_structures.hash_table.lru_cache import LRUCache


def amount_poured(poured, cups, query_row, query_glass):
    if query_row == 0:
        return cups[query_glass]


def champagne_tower(poured, query_row, query_glass):
    rows = [[] for i in range(query_row)]
    if poured >= 2:
        rows[0][0] = 1
        rows[1][0] = .5
        rows[1][1] = .5
        poured += -2

    ith_row = 2
    while poured > 0:
        poured += -1

        for i in rows[ith_row]:
            if i == rows[ith_row][0] or i == rows[ith_row][-1]:
                rows[ith_row][i] += 2.5


def main():
    print("Hello!")


main()
