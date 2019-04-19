def test1():
    print ('test1')
def test2():
    print ('test2')
def test3():
    print('test3')

def int_test():
    aint = 6
    print(aint)
    print(type(aint))

def str_test():
    astr = '5'
    print(astr)
    print(type(astr))

def float_test():
    float = 1.25
    print(float)
    print(type(float))

def add_test(a,b):
    print(a+b)
def zh_test():
    aint = 9
    print(type(aint))
    print(type( str(aint) ))
    print(type(int(aint)))
    print(type(str(aint)))

def jion():
    a = '我的'
    b ='快乐风男'
    c ='贼'
    d = '强！'
    print('%s%s%s%s'%(a,b,c,d))
def jianfa_test(a,b):
    return a-b

if __name__ == '__main__':
    # str_test()
    # float_test()
    # int = 123
    # add_test('你好',str(int))
    # zh_test()
    # jion()
    jianfa_test(4,3)
    d = add_test(4,6)
    print(jianfa_test(4,3))
    print(d)

