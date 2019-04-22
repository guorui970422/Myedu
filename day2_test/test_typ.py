adict = {"username":"yansl","password":"123456"}
bdict = {'5':"yansl","password":[2,5]}

cdict_str = '{"username":"yansl","password":"123456"}'

def ren1():
    print(type(adict))
    print(type(bdict))
    print(type(cdict_str))

def zzfc():
    adict1 = json.dumps(adict)
    print(type(adict1))
    print(adict1)
def zzc():
    cdict = json.loads(cdict_str)
    print(type(cdict))
    print(cdict)
import json

if __name__ == '__main__':
    # banh()
    # ren1()
    # zzfc()
    zzc()