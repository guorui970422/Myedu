alist = ['哈啊','我的','风男','贼强']
def fro_list():
    a = len(alist)
    for i in range(a):
        print(alist[i])
def fro_list1():
    for i in alist:
        print(i)
if __name__ == '__main__':
    fro_list()
    fro_list1()