age=18
#PRETESTED LOOP;TOP-DOWN TESTED LOOP;ENTRY  CHECKED LOOP;ENTRY CONTROLLED LOOP;WHILE LOOP
while age<30:
    print(f"arch is {age} yrs old")
    print("REady to vote")
    age+=1

#LIST LOOP;RANGE LOOP;FOR LOOP
fruits=["apple","orange","mango"]
for fruits in fruits:
    print(f"I like {len(fruits)}")
n=[1,2,3,4,5]
for i in n:
    if i%2==0:
        print(n)
    
#NESTED_LOOP
h=1
m=0
while h<3:
    while m<60:
        print(f"{h}:{m:02d}")
        m+=1
    h+=1
    m=0
#outerLoop&innerLoop
for hr in range(1,3): #o.l
    for min in range(60): #i.l
        print(f"{hr}:{min:02d}")