# 18-08-2025 dsa practice

#Recursion

# fibonacci series

class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)


# factorial of number

def fact(n):
  if n==0:
    return 1
  return n*fact(n-1)
fact(3)


# print number

def printNum(i,n):
  if n>=i:
    print(i)
    printNum(i+1,n)
printNum(1,5)