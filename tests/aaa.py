# def find_common_prefix(strings):
#     if not strings:
#         return ""
#     # Take the shortest string as a reference for comparison
#     shortest = min(strings, key=len)
#     for i, char in enumerate(shortest):
#         for other in strings:
#             if other[i] != char:
#                 return shortest[:i]
#     return shortest  # All strings have the same prefix as the shortest string

def find_common_prefix(strings):
    common = ""
    if strings:
        for i, ch in enumerate(strings[0]):
            for j, s in enumerate(strings[1:]):
                if len(s) <= i or s[i] != ch:
                    return common
                elif j == len(strings) - 2:
                    common += ch
    return common


# Find common prefix
common_prefix = find_common_prefix(["maff", "maff", "mafffma"])
print(f"common: \"{common_prefix}\"")
common_prefix = find_common_prefix(["ffma", "bima", "bbma"])
print(f"common: \"{common_prefix}\"")


def find_missing_min(array):
    non_negative = [x for x in array if x > 0]
    my_set = set(non_negative)
    minimum = min(my_set)
    if not my_set or minimum > 1:
        return 1
    for i in range(len(my_set)):
        if minimum + i not in my_set:
            return minimum + i
    return max(my_set) + 1



print(find_missing_min([-5, 5, 1, 4, 2, 3]))
print(find_missing_min([-5, 0, 1, 8, 1]))
print(find_missing_min([-5, 0, 2, 8, 3]))
