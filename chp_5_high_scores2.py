#High Scores Program
#This program uses list methods to create and maintain a list of the users best scores for a computer game

scores = [] #This empty list will contain scores

choice = None #

#Display the menu
#while loop will continue until the user enters 0

while choice != "0":
    print(
        """
        High Scores

        0 - Exit
        1 - Show Scores
        2 - Add a Score
        3 - Delete a Score
        4 - Sort Scores
        """
    )
    choice = input("Choice: ")
    print()

    if choice == "0":
        print("Good-Bye. ")

    #list the high scores table by accessing nested tuples
    elif choice == "1":
        print("High Scores\n")
        print("NAME\tSCORE")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)
    
    #adding a score by appending a nested tuple
    elif choice == "2":
        name = input("What is the players name?: ")
        score = int(input("What score did the player get?: "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5] #keep only top 5 scores

    #removing a score if the score is in the list. If the score is not in the list then the user is informed. 
    elif choice == "3":
        score = int(input("Remove which score?: "))
        if score in scores:
            scores.remove(score)
        else:
            print(score, "isnt in the high scores list.")

    #sort the scores and sort by decending order to get the higher scores first
    elif choice == "4":
        scores.sort(reverse=True)

    #dealing with an invalid chioce
    else:
        print("Sorry, but", choice, "isn't a valid choice. ")