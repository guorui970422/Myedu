import json
adict = {"username":"yansl","password":"123456"}
bdict = {'5':"yansl","password":[2,5]}
adict1 = '{"username":"yansl","password":"123456"}'
def dict_test():
    adict.pop('password')
    print(adict)
def dict_add():
    adict.update(bdict)
    print(adict)
    cdict = dict(adict,**bdict)
    print(cdict)
def dict_update():
    adict["username"] = '快乐风男'
    bdict['password'] = '战绩0-25'
    adict.update(bdict)
    print(adict)
def ste2dict():
    ster1 = json.dumps(adict)
    print(ster1)
    print(type(ster1))
def dict_2():
    print(type(adict1))
    adict2 = json.loads(adict1)
    print(adict2)
    print(type(adict2))

if __name__ == '__main__':
    # dict_test()
    # dict_add()
    # ste2dict()
    dict_2()

