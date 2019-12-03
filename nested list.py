if __name__ == '__main__':
    l = []
    for _ in range( int( input() ) ):
        name = input()
        score = float( input() )
        l.append( [name, score] )
    l.sort( key=lambda x: x[1] )
    c = l[0][1]
    for i in l:
        if i[1] > c:
            c = i[1]
            break
    x = list()
    for i in l:
        if i[1] == c:
            x.append(i[0])
    x.sort()
    for i in x:
        print(i)