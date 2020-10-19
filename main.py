# Course: CS 30
# Period: 1
# Date Created: 20/10/15
# Date Last Modified: 20/10/19
# Name: Subanaya Thirunavukkarasu
# Description: Create a function for your menu and add a loop
# for continuous gameplay


# Player's inventory
inventory = {
    'dagger': {
        'description': 'An old but sharp dagger',
        'damage': '30',
        'healing': '0'
        },
    'rotten apple': {
        'description': 'A commonly found health item',
        'damage': '0',
        'healing': '5'
        },
    'red potion': {
        'description': 'A potion that damages enemies',
        'damage': '40',
        'healing': '0'
        }
  }


# list of locations player can visit
locations = [
            'sewer', 'shopping centre', 'scrap yard', 'north oxygen station',
            'south oxygen station'
            ]


# list of actions player can choose
actions = ['attack enemy', 'check inventory', 'explore', 'leave location']


# The prompt presented to the user
prompt_1 = "Go to the following locations:"
for location in locations:
    prompt_1 += f"\n{location}"
prompt_1 += "\n"
prompt_1 += "\n"
prompt_1 += "Or choose one of the following actions:"
for action in actions:
    prompt_1 += f"\n{action}"
prompt_1 += "\n\n"
prompt_1 += "(type 'quit' to exit)"

print(prompt_1)


# the prompt for the function
prompt_2 = "\n\nYour Action/Location: "


# The function that asks the user to choose an action
def user_action(locations, actions):
    """create continous gameplay for the user; will ask them to go to a location
    or choose an action"""
    movements = f"{locations}, {actions}"
    return movements.title()

while True:
    response = input(prompt_2)

# The code for choosing a location
    if response == "sewer":
        print(f"* You've entered the {response}\n")

    elif response == 'shopping centre':
        print(f"* You've entered the {response}\n")

    elif response == 'scrap yard':
        print(f"* You've entered the {response}\n")

    elif response == 'north oxygen station':
        print(f"* You've entered the {response}\n")

    elif response == 'south oxygen station':
        print(f"* You've entered the {response}\n")

# The code for choosing an action
    elif response == 'attack enemy':
        print("* You attacked the enemy\n")

    elif response == 'check inventory':
        print("\nInventory:")
        for item, stats in inventory.items():
            Description = stats['description']
            Damage = stats['damage']
            Healing = stats['healing']

            print(f"* {item.title()}")
            print(f"Description: {Description}")
            print(f"Damage: {Damage}")
            print(f"Healing: {Healing}\n")

    elif response == 'explore':
        print("* You decided to explore\n")

    elif response == 'leave location':
        print("* You left the location\n")

# Code for quit option
    elif response == 'quit':
        break
# Code for invalid output
    else:
        print("* Your response is not valid. Try again with a valid reponse\n")

user_action(location, action)
