import random
import os
import art
import game_data

score = 0

def higher_and_lower_game(score):
    
    os.system('cls')
    print(art.logo)
    if score != 0:
        print(f"You're right! Current score: {score}")
    
    character_A = random.choice(game_data.data)
    character_B = random.choice(game_data.data)
    
    user_answer = input(f"""
Compare A: {character_A["name"]}, a {character_A["description"]}, from {character_A["country"]}

{art.vs}
Compare B: {character_B["name"]}, a {character_B["description"]}, from {character_B["country"]}
Who has more followers? Type 'A' or 'B': 
""")
    is_lost = False
    if user_answer == "A":
        if character_A["follower_count"] > character_B["follower_count"]:
            score += 1
        else:
            is_lost = True
    elif user_answer == "B":
        if character_B["follower_count"] > character_A["follower_count"]:
            score += 1
        else:
            is_lost = True
    
    if is_lost:
        os.system("cls")
        print(art.logo)
        print(f"Sorry, You lost, and your score: {score}")
        return
   
    return higher_and_lower_game(score)
    
    
higher_and_lower_game(score)