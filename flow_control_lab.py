#Conditionals and Flow control lab

#A variable to store the movie name
movieName = "Interstellar"

#A variable to store the rating of the movie
movieRating:int = 3

#A variable to hold the popularity score of the movie
popularityScore:float = 72.65

#based on the movie rating and the popularity score, print a statement

#if the movie rating is 4 or greater, and popularity is greater than 80
if movieRating >= 4 and popularityScore > 80:
    print("Highly recomended")

#if the movie rating is 3 or greater, and popularity is greater than 70
elif movieRating >= 3 and popularityScore > 70:
    print("I recommended it. It is good.")

#if the movie rating is 2 or less, and popularity is greater than 60
elif movieRating <= 2 and popularityScore > 60:
    print("You should check it out!")

#if the movie rating is 2 or less, and popularity is less than than 50
elif movieRating <= 2 and popularityScore < 50:
    print("Don't watch it. It is waste of time.")

#additional condition for other combinations, like rating = 3 and popularity = 10
else:
    print("Maybe you should give it a try")