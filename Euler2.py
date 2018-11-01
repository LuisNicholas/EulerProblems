def fib():
    i = 1
    l = 0
    j = 1
    while i <= 4000000:
        k = j 
        j = i
        if i/2 == int(i/2):
            l = l + i
        i = k + j
    print(l)

fib()
