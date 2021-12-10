import random
import requests

print(r"""
               __                                    __                    __                                     
______   ____ |  | __ ____   _____   ____   ____   _/  |_  ____ ______   _/  |________ __ __  _____ ______  ______
\____ \ /  _ \|  |/ // __ \ /     \ /  _ \ /    \  \   __\/  _ \\____ \  \   __\_  __ \  |  \/     \\____ \/  ___/
|  |_> >  <_> )    <\  ___/|  Y Y  (  <_> )   |  \  |  | (  <_> )  |_> >  |  |  |  | \/  |  /  Y Y  \  |_> >___ \ 
|   __/ \____/|__|_ \\___  >__|_|  /\____/|___|  /  |__|  \____/|   __/   |__|  |__|  |____/|__|_|  /   __/____  >
|__|               \/    \/      \/            \/               |__|                              \/|__|       \/ 

                            """)
def pikachu():
    print(r"""
                 ,___        .-;'
               `"-.`\_...._/`.`
            ,      \        /
         .-' ',    / ()   ()\
        `'._   \  /()    .  (|
            > .' ;,     -'-  /
           / <   |;,     __.;
           '-.'-.|  , \    , \
              `>.|;, \_)    \_)
               `-;     ,    /
                  \    /   <
                   '. <`'-,_)
                     '._)
                        """)

def play_game():
    # Results are stored here
    with open('result.txt', 'w+') as result_file:
        result = '0'
        result_file.write(result)


    def random_pokemon():
        pokemon_id = random.randint(1, 151)
        url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_id)
        response = requests.get(url)
        pokemon = response.json()
        return {
            'name': pokemon['name'],
            'id': pokemon['id'],
            'height': pokemon['height'],
            'weight': pokemon['weight'],
            'type': pokemon['types'][0]['type']['name'],
            'hp': pokemon["stats"][0]["base_stat"]
        }


    def compare_stat():
        print("You: {}    Opponent: {}".format(
            player_stats["{}_stat".format(stat_to_compare)],
            opponent_stats["op_{}_stat".format(stat_to_compare)]
        ))
        if player_stats["{}_stat".format(stat_to_compare)] > opponent_stats["op_{}_stat".format(stat_to_compare)]:
            print("You win!")
            results = '1'
        elif player_stats["{}_stat".format(stat_to_compare)] == opponent_stats["op_{}_stat".format(stat_to_compare)]:
            print("It's a draw!")
            results = '0'
        else:
            print("You lose.")
            results = '-1'

        return results


    def compare_type():
        print("You: {}    Opponent: {}".format(player_type["type_stat"].title(), opponent_type["op_type_stat"].title()))
    # list[0] = you lose    list[1] = you win   neither list = draw
        if player_type["type_stat"] == "normal":
            normal = [["rock", "ghost"], []]
            player_type["type_stat"] = normal
        elif player_type["type_stat"] == "fire":
            fire = [["water", "rock", "dragon"], ["grass", "ice"]]
            player_type["type_stat"] = fire
        elif player_type["type_stat"] == "water":
            water = [["grass", "dragon"], ["fire", "ground", "rock"]]
            player_type["type_stat"] = water
        elif player_type["type_stat"] == "electric":
            electric = [["grass", "ground", "dragon"], ["water", "flying"]]
            player_type["type_stat"] = electric
        elif player_type["type_stat"] == "grass":
            grass = [["fire", "poison", "flying", "bug", "dragon"], ["water", "ground", "rock"]]
            player_type["type_stat"] = grass
        elif player_type["type_stat"] == "ice":
            ice = [["water"], ["grass", "flying", "dragon"]]
            player_type["type_stat"] = ice
        elif player_type["type_stat"] == "fighting":
            fighting = [["poison", "flying", "psychic", "bug", "ghost"], ["normal", "ice", "rock"]]
            player_type["type_stat"] = fighting
        elif player_type["type_stat"] == "poison":
            poison = [["ground", "rock", "ghost"], ["grass", "bug"]]
            player_type["type_stat"] = poison
        elif player_type["type_stat"] == "ground":
            ground = [["grass", "flying", "bug"], ["fire", "electric", "poison", "rock"]]
            player_type["type_stat"] = ground
        elif player_type["type_stat"] == "flying":
            flying = [["electric", "rock"], ["grass", "fighting", "bug"]]
            player_type["type_stat"] = flying
        elif player_type["type_stat"] == "psychic":
            psychic = [[], ["fighting", "poison"]]
            player_type["type_stat"] = psychic
        elif player_type["type_stat"] == "bug":
            bug = [["fire", "fighting", "flying", "ghost"], ["grass", "poison", "psychic"]]
            player_type["type_stat"] = bug
        elif player_type["type_stat"] == "rock":
            rock = [["fighting", "ground"], ["fire", "ice", "flying", "bug"]]
            player_type["type_stat"] = rock
        elif player_type["type_stat"] == "ghost":
            ghost = [[], ["ghost"]]
            player_type["type_stat"] = ghost
        elif player_type["type_stat"] == "dragon":
            dragon = [[], ["dragon"]]
            player_type["type_stat"] = dragon

        if opponent_type["op_type_stat"] in player_type["type_stat"][0]:
            print("You lose.")
            results = '-1'
        elif opponent_type["op_type_stat"] in player_type["type_stat"][1]:
            print("You win!")
            results = '1'
        else:
            print("It's a draw")
            results = '0'

        return results


    def final_result():
        with open('result.txt', 'r') as result_file:
            contents = result_file.read()
            contents.split(",")
            total = sum([int(num) for num in contents.split(',')])
            print("Your overall points: " + str(total))

        if total >= 1:
            print("You are the winner!")
        elif total == 0:
            print("No one wins.")
        else:
            print("The opponent wins!")

        return total


    def leaderboard_score():
        with open('result.txt', 'r') as result_file:
            contents = result_file.read()
            contents.split(",")
            total = sum([int(num) for num in contents.split(',')])

            return total


    # while loop so python doesn't stop the programme when you don't enter a number
    while True:
        try:
            # Number of rounds to play
            rounds = int(input("How many rounds do you want to play? "))
            # Game starts and repeats for the number of times you want to play
            for round in range(rounds):
                # Both players' pokemon
                player_pokemon = random_pokemon()
                opponent_pokemon = random_pokemon()

                print("You have " + (player_pokemon["name"]).title())
                print("Height: " + str(player_pokemon["height"]))
                print("Weight: " + str(player_pokemon["weight"]))
                print("HP: " + str((player_pokemon["hp"])))
                print("Type: " + (player_pokemon["type"]).title())

                player_stats = {
                    "height_stat": player_pokemon["height"],
                    "weight_stat": player_pokemon["weight"],
                    "type_stat": [],
                    "hp_stat": player_pokemon["hp"]
                }
                player_type = {"type_stat": player_pokemon["type"]}

                print("Your opponent has " + (opponent_pokemon["name"]).title())
                opponent_stats = {
                    "op_height_stat": opponent_pokemon["height"],
                    "op_weight_stat": opponent_pokemon["weight"],
                    "type_stat": [],
                    "op_hp_stat": opponent_pokemon["hp"]
                }
                opponent_type = {"op_type_stat": opponent_pokemon["type"]}

                # This is the comparison of their stats and writing results to the file
                stat_to_compare = input("Which stat do you want to compare? height/weight/type/hp ")
                # If the user inputs an invalid stat this gets them to try again instead of outputting an error message
                while stat_to_compare != "height" and stat_to_compare != "weight" and stat_to_compare != "type" and stat_to_compare != "hp":
                    stat_to_compare = input("Error: wrong input. Please try again and enter height/weight/type/hp only. ")

                if stat_to_compare == "type" and stat_to_compare != "height" and stat_to_compare != "weight" and stat_to_compare != "hp":
                    new_type_result = compare_type()
                    with open('result.txt', 'r') as result_file:
                        contents = result_file.read()
                    contents = contents + ',' + new_type_result
                    with open('result.txt', 'w+') as result_file:
                        result_file.write(contents)

                elif stat_to_compare == "height" or stat_to_compare == "weight" or stat_to_compare == "hp" and stat_to_compare != "type":
                    new_stat_result = compare_stat()
                    with open('result.txt', 'r') as result_file:
                        contents = result_file.read()
                    contents = contents + ',' + new_stat_result
                    with open('result.txt', 'w+') as result_file:
                        result_file.write(contents)

            final_result()

            leaderboard = input("Would you like to save your score on the leaderboard? y/n ")
            while leaderboard != "y" and leaderboard != "n":
                leaderboard = input("Error: wrong input. Please try again and enter y/n only. ")

            if leaderboard == "y":
                player_name = input("What is your name? ")
                with open("leaderboard.txt", "r") as leaderboard_file:
                    scores = leaderboard_file.read()
                total = leaderboard_score()
                scores = scores + "\n" + player_name + " " + str(total)
                with open("leaderboard.txt", "w+") as leaderboard_file:
                    leaderboard_file.write(scores)
                print("Scoreboard:" + scores)
                play_again = input("Do you want to play again? y/n ")
                if play_again == "y":
                    play_game()
                elif play_again == "n":
                    pikachu()
                    print("End of game. Goodbye! :)")
                break
            elif leaderboard == "n":
                play_again = input("Do you want to play again? y/n ")
                if play_again == "y":
                    play_game()
                elif play_again == "n":
                    pikachu()
                    print("End of game. Goodbye! :)")

                break

        except ValueError:
            print("Error: wrong input. Please try again and enter a whole number only. ")


play_game()
