# Q1
# shirt

# Q2
i = 1
sum =0
while i<1001:
    if i%3==0:
        sum+=i
    i+=1
print(sum)

# Q3
i=1
while i<6:
    print(i*'*')
    i+=1

# Q4
for v in range(1,101):
    print(v)

# Q5
a = [70,60,55,75,95,90,80,80,85,100]
sum = 0
for v in a:
    sum+=v
print(sum/10)

# Q6
numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n%2 ==1]
print(result)
