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

    #list the high scores table
    elif choice == "1":
        print("High Scores")
        for score in scores:
            print(score)
    
    #adding a score
    elif choice == "2":
        score = int(input("What score did you get?: "))
        scores.append(score)

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