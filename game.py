# The High-Score Tracker Game
# Continuously asks the player for their score until they type "stop".

while True:
    score_input = input("Enter your game score (or type 'stop' to end): ")
    cleaned_input = score_input.strip().lower()

    if cleaned_input == "stop":
        print("Game session ended!")
        break
    else:
        score = int(score_input)
        if score > 100:
            print("Wow! That's a new high score!")
        else:
            print("Good try, keep playing!")