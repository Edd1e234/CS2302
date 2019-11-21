from Python.data_structures.hash_table.lru_cache import LRUCache


def main():
    cache = LRUCache(3)

    cache.insert(1, 4)
    cache.insert(2, 5)
    cache.insert(3, 6)
    cache.insert(4, 7)
    cache.insert(5, 8)
    cache.insert(6, 9)
    cache.insert(7, 10)
    cache.insert(6, 9)
    cache.print_most_recent()
    print("Works")


main()
