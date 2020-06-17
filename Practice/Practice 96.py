def calcAverage(score1,score2,score3,score4,score5):
    average=(score1+score2+score3+score4+score5)/5
    return average
def determinGrade(userScore):
    if userScore<60:
        return "F"
    if userScore<70:
        return "D"
    if userScore<80:
        return "C"
    if userScore<90:
        return "B"
    if userScore<101:
        return "A"
def askScore():
    score1=int(input("please enter score1: "))
    score2 = int(input("please enter score2: "))
    score3 = int(input("please enter score3: "))
    score4 = int(input("please enter score4: "))
    score5 = int(input("please enter score5: "))
    return score1,score2,score3,score4,score5
def printTableOfResult(score1,score2,score3,score4,score5):
    print("score\tLetter Grade")
    print(str(score1)+"\t"+determinGrade(score1),\
          str(score2)+"\t"+determinGrade(score2),\
          str(score3)+"\t"+determinGrade(score3),\
          str(score4)+"\t"+determinGrade(score4),\
          str(score5)+"\t"+determinGrade(score5),sep="\n")
def main():
    score1,score2,score3,score4,score5=askScore()
    printTableOfResult(score1,score2,score3,score4,score5)
main()


