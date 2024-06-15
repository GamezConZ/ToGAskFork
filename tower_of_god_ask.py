#AreYouIntoToG Program Build a terminal program using Python from Computer Science

class ToG_Profile:
    def __init__(self,favorite_character_response,consumtion_option_response):
        self.favorite_character = favorite_character_response
        self.consumtion_option = consumtion_option_response
    
    #Helper functions
    def isBam(self):
        return self.favorite_character == 'bam'
    def isWebtoon(self):
        return self.consumtion_option == 'w'
    def isAnime(self):
        return self.consumtion_option == 'a'
        

print("Welcome to the Tower of God (ToG), Ask Game and Profile Creator")
print("Lets start with an easy question")

#both answer1 and answer2 are set to .lower() so it will accept both upper and lowercase as input

answer1 = input("Who is your favorite character in ToG?: ").lower()
if answer1 == "bam":
    print("That is AWESOME! He is the best so it makes sense.")
else:
    print("well...")
    print("Some of us just have bad taste I guess....")
print("Next question for ya.\n")

#Loops until a valid input is entered.
while True:
    answer2 = input("Are you reading the Webtoon or did you watch the anime?\n (PLEASE ENTER EITHER: W (Webtoon) or A (Anime)): ").lower()
    if answer2 == "w":
        print("YES!!!! The current arc is something else right???")
        break
    if answer2 == 'a':
        print("Hey at least you watched the anime. Make sure to go read the Webtoon. IT ONLY GETS BETTER")
        break
    else:
        print('\nInvalid input. Try again!')


user = ToG_Profile(answer1,answer2)

print("Thanks for the info. Give me a second as we categorize you...")
print("processing...\n")
print("processing...\n")
print("processing...\n")

print("Thank you for waiting\n")
print("Based on the responses you have provided and our calculations.\n Your ToG_Profile has been created and you are: \n")


if user.isBam() and user.isWebtoon():
    print("Considered an ToG Expert! Your welcome pass and additional materials will come in the mail later today")

elif user.isBam() and user.isAnime():
    print("Considered an ToG Novice! Your weclome package will come in the mail. However, keep training!")

elif user.isWebtoon():
    print("Considered ToG Expert in training. Maybe think about who your favorite character is...")
else:
    print("No profile has been created for you yet. Keep on keeping on friend. You have only scratched the surface of what the joy the show can bring you")
 

