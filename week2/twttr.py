str = input("Input: ")

new_str = ""
for ch in str:
    if ch in ['a', 'e', 'i', 'o', 'u']:
        continue
    elif ch in ['A', 'E', 'I', 'O', 'U']:
        continue
    else:
        new_str += ch

print("Output:", new_str)