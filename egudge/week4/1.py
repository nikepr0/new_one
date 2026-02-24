n=int(input())

def my_generator(n):
  for i in range(1 ,n+1):
      yield i*i

for value in my_generator(n):
  print(value) 
  
  