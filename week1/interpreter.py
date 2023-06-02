x, y, z = input("Expression: ").strip().split(" ")
match y:
    case "+":
        ans = float(x) + float(z)
        print(f"{ans:.1f}")
    case "-":
        ans = float(x) - float(z)
        print(f"{ans:.1f}")
    case "*":
        ans = float(x) * float(z)
        print(f"{ans:.1f}")
    case "/":
        ans = float(x) / float(z)
        print(f"{ans:.1f}")
