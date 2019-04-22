def jiujiu():
    for n in range(1,10):
        for m in range(1,n+1):
            if n>=m:
                print('%sx%s=%s'%(m,n,n*m),end=' ')
        print('')

def oushu_demo(a,b):
    sum = 0
    for i in range(a,b+1):
        if i%2==0:
            sum=sum + i
    print(sum)
def demo(a,b):
    sum=0
    if a<b:
        for i in range(a,b):
            if i%2==0:
                sum=sum+i
    elif b<a:
        for i in range(b,a):
            if i%2==0:
                sum=sum+i
    else:
        print('a,b相等')
    print(sum)






if __name__ == '__main__':
    demo(1,10)