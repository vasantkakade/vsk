#!/usr/bin/python3
def main():
    a = 10
    b = 20
    a = a^b
    b = a^b
    a = a^b
    print('a = '+str(a) )
    print('b = '+str(b) )
if __name__ == '__main__':
    main()
