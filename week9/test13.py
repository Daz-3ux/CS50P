# yield; 定义生成器函数，并控制生成器函数的执行流程

def main():
    n = int(input("Number: "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "🐑" * (i+1)

if __name__ == "__main__":
    main()