f = open('input','r') 
#f = open('input2','r') 
#print(f.read())
#print(f.readline())
official = 0
count = 0
top_three = [0,0,0]
level = 0
#fourth , third ,fifth
'''
def find_spot(x):
    i = 0
    while x < top_three[i] and i < 3:
        i + =1
    if i < 3:
        tmp = top_three[i]
        top_three[i] = x
        find_spot(tmp)
'''
def translate(index):
    for i in range(2,index,-1):
        top_three[i] = top_three[i-1]
for x in f:
    print(top_three)
    if x != '\n':
        count += int(x)
    else:
        if len(top_three) == 0:
            top_three.append(count)
    
        elif top_three[0] < count :
            translate(0)
            top_three[0] = count
        elif top_three[1] < count:
            translate(1)
            top_three[1] = count
        elif  top_three[2] < count:
            translate(2)
            top_three[2] = count
        count = 0

for y in top_three:
    official += y
    
print("max = ", official)

