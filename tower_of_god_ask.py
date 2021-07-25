#AreYouIntoToG Program Build a terminal program using Python from Computer Science

class ToG_Profile:
    def __init__(self,favorite_character_response,consumtion_option_response):
        self.favorite_character = favorite_character_response
        self.consumtion_option = consumtion_option_response
        

print("Welcome to the Tower of God (ToG) Ask Game and Profile Creator")
print("Lets start with an easy question")

answer1 = input("Who is your favorite character in ToG?")

if answer1 == "Bam":
    print("That is AWESOME! He is the best so it makes sense")
else:
    print("well...")
    print("Some of us just have bad taste I guess....")

print("Next question for ya.\n")
answer2 = input("Are you reading the Webtoon or did you watch the anime?\n (PLEASE ENTER EITHER: W (Webtoon) or A (Anime))")

if answer2 == "W":
    print("YES!!!! The current arc is something else right???")
else:
    print("Hey at least you watched the anime. Make sure to go read the Webtoon. IT ONLY GETS BETTER")


user = ToG_Profile(answer1,answer2)

print("Thanks for the info. Give me a second as we categorize you...")
print("processing...\n")
print("processing...\n")
print("processing...\n")

print("Thank you for waiting\n")
print("Based on the responses you have provided and our calculations.\n Your ToG_Profile has been created and you are: \n")


if user.favorite_character == "Bam" and user.consumtion_option == "W":
    print("Considered an ToG Expert! Your welcome pass and additional materials will come in the mail later today")

elif user.consumtion_option == "W":
    print("Considered ToG Expert in training. Maybe think about who your favorite character is...")

else:
    print("No profile has been created for you yet. Keep on keeping on friend. You have only scratched the surface of what the joy the show can bring you")
 


