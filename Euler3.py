def print_factors(x):

   print("The prime factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           for j in range(1, i + 1):
               if j % i == 0:
                     print(j)

num = 600851475143

print_factors(num)
