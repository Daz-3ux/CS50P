# 解包: 将一个列表或元组中的元素分别赋值给多个变量
# unpacking

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = [100, 50, 25]

print(total(*coins), "Knuts")

coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(**coins), "Knuts")
