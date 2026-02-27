def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value) 
  
#_-------------------------------
def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1

for num in count_up_to(5):
  print(num) 
  
  
#-----------------------------------
def large_sequence(n):
  for i in range(n):
    yield i


gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))


#-----------------------------------
def simple_gen():
  yield "Emil"
  yield "Tobias"
  yield "Linus"

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen)) 



#-----------------------------------
list_comp = [x * x for x in range(5)]
print(list_comp)

# Generator expression - creates a generator
gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp)) 

#-----------------------------------
total = sum(x * x for x in range(10))
print(total)


#-----------------------------------
def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b

# Get first 100 Fibonacci numbers
gen = fibonacci()
for _ in range(100):
  print(next(gen)) 
  
#-----------------------------------
def echo_generator():
  while True:
    received = yield # This will pause here and wait for a value to be sent
    print("Received:", received)

gen = echo_generator()
next(gen) # Prime the generator
gen.send("Hello")
gen.send("World")

#-----------------------------------
def my_gen():
  try:
    yield 1
    yield 2
    yield 3
  finally:
    print("Generator closed")

gen = my_gen()
print(next(gen))
gen.close() 