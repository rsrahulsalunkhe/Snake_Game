# Slice() Function
# The slice() function returns a slice object that is used to slice any sequence (string, tuple, list, range, or bytes).
# The syntax of slice() is:
# slice(start, stop, step)

piano_key = ["a", "b", "c", "d", "e", "f", "g"]

print(piano_key[2:4])
print(piano_key[4:])
print(piano_key[:3])
print(piano_key[2:5:2])
print(piano_key[::2])
print(piano_key[::-1])