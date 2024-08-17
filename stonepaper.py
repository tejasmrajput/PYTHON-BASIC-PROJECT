import random
list =["stone ","paper","scissor"]
c= random.choice(list)
ui=input("STONE PAPER SCISSOR :-")
if ui==c:
    print("tie")
elif (ui == "stone" and c == "paper"):
        print("Paper covers stone, you lose!")
elif (ui == "stone" and c == "scissor"):
        print("Stone crushes scissor, you win!")
elif (ui == "paper" and c == "scissor"):
        print("Scissor cuts paper, you lose!")
elif (ui == "paper" and c == "stone"):
        print("Paper covers stone, you win!")
elif (ui == "scissor" and c == "stone"):
        print("Stone crushes scissor, you lose!")
elif (ui == "scissor" and c == "paper"):
        print("Scissor cuts paper, you win!")


