import math

def encryption(s):
    le = len(s)
    ro = le ** .5
    r = math.floor(ro)
    c = math.ceil(ro)
    if c*r < le:
        r +=1
    l = list()
    for i in range(r):
        try:
            l.append(s[i*c:(i+1)*c])
        except:
            l.append(s[i*c:])
    enc =""
    for i in range(c):
        for j in range(r):
            try :
                enc = enc + l[j][i]
            except:
                pass
        enc = enc + " "
    print(enc)



if __name__ == '__main__':
    str = input().strip()
    encryption(str)