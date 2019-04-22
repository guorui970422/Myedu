alist = [['admin', '123456', '成功', '登录成功'], ['admin1', '123456', '错误', '用户名错误'], ['admin', '123456a', '错误', '密码错误'], ['admin', '123456', '成功', '登录成功1'], ['admin1', '123456', '错误', '用户名错误1'], ['admin', '123456a', '错误', '密码错误1']]


if __name__ == '__main__':
    print(alist)
    blist = []
    len1 = len(alist)
    for i in range(len1):
        a = alist[i].pop()
        blist.append(a)
        # print(a)
    print(alist)
    print(blist)

