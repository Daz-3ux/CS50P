count = 0

while count < 50:
  print("Amount Due:",50 - count)
  coin = int(input("Insert Coin: "))
  if coin in [5, 10, 25]:
    count += coin

print("Change Owed:",count-50)