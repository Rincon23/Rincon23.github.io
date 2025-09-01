s = 0
for i in range(1,101):
    if i%3==0 and i%2 != 0:
        s += i
print(s)