
def middlescore(rival, you):
    score = 0
    if you == "X":
        score +=1
    if  you == "Y":
        score +=2
    if you == "Z":
        score +=3

    if rival == "A" and you == "X" or rival == "B" and you == "Y" or rival == "C" and you == "Z":
        score += 3
    if you == "X" and rival == "C" or you == "Y" and rival == "A" or you == "Z" and rival == "B":
        score += 6

    return score


def main():
    score = 0
    f = open('input.txt','r') 

    for x in f:
        if len(x)>= 2:
            rival = x[0]
            game = x[2]
            you = ""
            if game == "X":
                # lose
                if rival == "A":
                    you = "Z"
                elif rival == "B":
                    you = "X"
                elif rival == "C":
                    you = "Y"
            elif game == "Y":
                #draw game
                you = rival
            elif game == "Z":
                # you win
                if rival == "A":
                    you = "Y"
                elif rival == "B":
                    you = "Z"
                elif rival == "C":
                    you = "X"
            score += middlescore(rival, you)

    print("Final score..",score)
"""
X means you need to lose,
Y means you need to end the round in a draw,
and Z means you need to win.

"""
main()
