import os

def dayOfProgrammer(year):
    if(year == 1918): return "26.09.1918"
    if (((year%4 == 0 and year%100 != 0) or year%400==0) and year>=1917) or (year<=1917 and year%4 == 0):
        return "12.09.%d" %(year)
    return "13.09.%d" %(year)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
