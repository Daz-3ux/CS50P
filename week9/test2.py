class Cat:
    # 类常量
    MEOWS = 3

    def meow(self):
        for _ in range(self.MEOWS):
            print("meow")

cat = Cat()
cat.meow()