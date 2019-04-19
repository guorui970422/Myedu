adict = {"username":"yansl","password":"123456"}
bdict = {5:"yansl","password":[2,5]}


def dict_test():
    adict.pop('password')
    print(adict)

if __name__ == '__main__':
    dict_test()