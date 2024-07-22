
age = int(input("Enter your age: "))
rating = input("Enter movie rating(G, PG, PG-13, R): ")

if rating == "G":
    print("you can watch this movie")
elif rating == "PG" and age >= 7:
    print("you can watch this movie")
elif rating == "pg-13" and age >= 13:
    print("you can watch this movie")
elif rating == "R" and age >=17:
    print("you can watch this movie")
else:
    print("you are not allowed to wacth this movie")