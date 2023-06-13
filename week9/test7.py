# args: 位置参数: 用相对位置指代参数
# kwargs: 命名参数: 用参数名指代参数

def f(*args, **kwargs):
    print("Named:", kwargs)


f(galleons=100, sickles=50, knuts=25)