# hashmap of sets
my_map = {
    "a": {1, 2, 3},
    "b": {4, 5},
    "c": set()  # empty set
}

# add to a set inside the hashmap
my_map["a"].add(10)

# create a new set if key doesn't exist
my_map.setdefault("d", set()).add(99)

print(my_map)
# {'a': {1, 2, 3, 10}, 'b': {4, 5}, 'c': set(), 'd': {99}}
