# This main will be use as workspace for quick tests and for review.
from data_structures.hash_table.lru_cache import LRUCache


def main():
    cache = LRUCache(3)
    cache.put(4, 6)
    cache.put(7, 9)
    cache.put(8, 0)
    cache.put(12, 4)

    cache.print_most_recent()

    print(cache.get(12))

    print("Works")


main()
