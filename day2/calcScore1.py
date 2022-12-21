f = open('input.txt','r') 

score = 0
for x in f:
    if len(x)>= 2:
        rival = x[0]
        you = x[2]
        if you == "X":
            score += 1
        elif you == "Y":
            score +=2
        elif you == "Z":
            score +=3

        if rival == "A" and you == "X" or rival == "B" and you == "Y" or rival == "C" and you == "Z":
            score += 3
        elif you == "X" and rival == "C" or you == "Y" and rival == "A" or you == "Z" and rival == "B":
            score += 6


print("Final score..",score)
