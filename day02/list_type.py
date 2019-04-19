def list_sel(a):
    # 取第三个值
    # print( a[3] )
    # 取最后一个值
    # print(a[-1])
    # 取从第一位到最后一位的值
    # print(a[0:])
    # 去中间的值  x-1:y+1 (x表示从哪个值开始，y表示要取到的值)
    print(a[1:9])



def list_del():
    alist = ['快乐', 4396, '魔力瞎', '明凯', 'edg_win', '666', '777', '666', '777', '666', '777', '666', '777']
    blist = ['c','b','d']
    alist.pop(9)
    blist.pop(1)
    print(alist)
    print(blist)



if __name__ == '__main__':
    list_del()
