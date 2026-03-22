for i in range(100):
    if i==50:
        break
    print(i)
#2
n=[2,3,4,5,6]
x=4
for i in n:
    if i==x:
        print("Found")
        break
else:
    print("Not found")