greeting = input("Greeting: ").lower().lstrip()

if greeting.find("hello", 0, 5) != -1:
  print("$0")
elif greeting.find("h", 0, 1) != -1:
  print("$20")
else:
  print("$100")