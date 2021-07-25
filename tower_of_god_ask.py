#AreYouIntoToG Program Build a terminal program using Python from Computer Science

class ToG_Expert:
    def __init__(self,favorite_character_response,consumtion_option_response):
        self.favorite_character = favorite_character_response
        self.consumtion_option = consumtion_option_response
        

print("welcome to the Tower of God (ToG) Ask Game")
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

print("Thanks for the info. Give me a second as we categorize you...")
print("processing...\n")
print("processing...\n")
print("processing...\n")



