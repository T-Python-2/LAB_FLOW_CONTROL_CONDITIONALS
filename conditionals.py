

movieName:str = "The Batman"
movieRating:int = 3
moviePopularity:float = 72.65


print(movieName ,"\nRating :",movieRating , "\nPopularity:",moviePopularity)

if movieRating >= 4 and moviePopularity > 80 :
    print("Highly Recommended")
elif movieRating >= 3 and moviePopularity > 70 :
    print("I recommended it . It is good")
elif movieRating <= 2 and moviePopularity > 60 :
    print("You should check it out!")
else:
    print("Don't watch it. It is a waste of time")
    


