def can_segment_str(s, dictionary):
    for i in range(1, len(s) + 1):
        first_str = s[0:i]
        print('first_str', first_str)
        if first_str in dictionary:
            second_str = s[i:]
            print('second_str', second_str)
            if (
                    not second_str
                    or second_str in dictionary
                    or can_segment_str(second_str, dictionary)
            ):
                return True
    return False


s = "datacampp"
dictionary = ["data", "camp", "cam", "lack"]
print(can_segment_str(s, dictionary))
# True


# def can_segment_str(s, dictionary, memo=None):
#     if memo is None:
#         memo = {}
#     if s in memo:
#         return memo[s]
#     if not s:
#         return True
#     for i in range(1, len(s) + 1):
#         prefix = s[:i]
#         if prefix in dictionary and can_segment_str(s[i:], dictionary, memo):
#             memo[s] = True
#             return True
#     memo[s] = False
#     return False
#
#
# s = "datacamp"
# dictionary = {"data", "camp", "cam", "lack"}  # Use set for O(1) lookups
# print(can_segment_str(s, dictionary))
