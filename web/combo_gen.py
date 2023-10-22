import random
import eel

moves = ["Jab", "Cross", "Hook", "Uppercut", "Body shot", "Slip", "Duck", "Kick", "Teep", "Elbow", "Knee"]
sides = ["Lead", "Rear"]

def get_random_move():
    move = random.choice(moves)
    side = random.choice(sides)
    return (side, move)

def generate_random_combo():
    num_moves = random.randint(1, 6)
    combo = [get_random_move() for i in range(num_moves)]
    return combo

eel.init('web')

@eel.expose
def generate_combo():
    combo = generate_random_combo()
    combo_text = "\n".join([f"{move[0]} {move[1]}" for move in combo])
    print(f"Generated combo: {combo_text}")
    return combo_text

@eel.expose
def start():
    eel.start('index.html', size=(500, 600))

start()