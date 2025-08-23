# python
# Remove duplicates from a list
def remove_duplicates(collection):
    return list(set(collection))

# Example usage
data = [1, 2, 2, 3, 4, 4, 5]
deduplicated = remove_duplicates(data)
print(deduplicated)


def remove_duplicates(collection):
    result = []
    for item in collection:
        if item not in result:
            result.append(item)
    return result

# Example usage
data = [1, 2, 2, 3, 4, 4, 5]
deduplicated = remove_duplicates(data)
print(deduplicated)


# Remove duplicates from a list of dictionaries
def remove_duplicates_dicts(collection):
    seen = set()
    result = []
    for d in collection:
        # Convert dictionary to a frozenset of its items for hashing
        hashable = frozenset(d.items())
        if hashable not in seen:
            seen.add(hashable)
            result.append(d)
    return result

# Example usage
data = [
    {"a": 1, "b": 2},
    {"a": 1, "b": 2},
    {"a": 2, "b": 3}
]
deduplicated = remove_duplicates_dicts(data)
print(deduplicated)