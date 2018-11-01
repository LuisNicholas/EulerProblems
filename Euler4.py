def Palindrome():
    for i in range(900,999):
        for j in range (900, 999):
            k = i * j
            l = str(k)
            if l[0] == l[5] and l[1] == l[4] and l[2] == l[3]:
                print(l)
                print(i, " * " , j, " = ", l)

Palindrome()
