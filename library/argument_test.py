



def myfunction(a,b,c,d=5,*args, **kwargs):
    print("a = " + str(a))
    print("b = " + str(b))
    print("c = " + str(c))
    print("d = " + str(d))

    print(type(args))
    print(args)

    print(type(kwargs))
    print(kwargs)



def main():
    myfunction(1,2,3,4,"a","b", m=5,n=10)


if __name__ == "__main__":
    main()