#14. Write a python program to define a module to find Fibonacci Numbers


def fibo_ser(n):
  if n <= 0:
        return[]
  series= [0]
  if n == 1:
        return series
  series.append(1)
  a,b = 0,1
  for _ in range(2,n):
    c = a + b
    series.append(c)  
    a, b = b,c
  return series;
print(fibo_ser(10));



def my_function():
    print("Hello World!");