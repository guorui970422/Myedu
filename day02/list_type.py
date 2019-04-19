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
def alist_app():
    alist = [9,8,7,6,5,4,3,2,1]
    alist.append('诶嘿嘿')
    print(alist)
    alist.append('hihihi')
    print(alist)
def blist_sel():
    blist = [9,8,7,6,5,4]
    print(blist[0:2])
    blist.append('hahaha')
def clist_lit():
    apc = [1,2,3,4,5,6,'你好']
    bpc = apc[:6]
    cpc = apc[-1]
    print('%s%s'%(cpc,bpc))
if __name__ == '__main__':
    # list_del()
    # alist_app()
    # blist_sel()
    clist_lit()