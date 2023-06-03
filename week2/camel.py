str = input("camelCase: ").strip()

new_str = ""
for ch in str:
    if ch.isupper():
        new_str += "_"
        new_str += ch.lower()
    else:
        new_str += ch

print(new_str)