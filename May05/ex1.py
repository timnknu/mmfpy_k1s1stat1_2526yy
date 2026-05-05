def g():
    a = 1/0
    print('after a')

def f():
    pass
    g()
    print('after g')
    pass

def main():
    pass
    f()
    print('after f')
    pass

try:
    main()
except:
    print('Error in main')
print('after main')