
def recursive_fibo(n):
   if n <= 1:
       return n
   else:
       return(recursive_fibo(n-1) + recursive_fibo(n-2))

ntime = 5

for i in range(ntime):
    print(recursive_fibo(i))







