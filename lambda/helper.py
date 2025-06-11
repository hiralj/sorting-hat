import random

houses = ["Hufflepuff", "Ravenclaw", "Slytherin", "Hufflepuff", "Ravenclaw", "Slytherin", "Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin", "Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin", "Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin", "Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin", "Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin", "Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin", "Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

launch_utterances = [
    "Who is the next wizard?",
    "Next wizard please..",
    "Who should be assigned a Hogwarts house?"
]

assign_thinking = [
    "Sure, working on it..",
    "hmm... let me think..",
    "of course... let me check..."
]

birthday_kid_thinking = "I am so excited to assign a Hogwarts house to our birthday girl!"

def hack_kid(kid_name):
    kid_name = kid_name.lower()
    return birthday_kid(kid_name) or kid_name == 'misha' or kid_name == 'misa' or kid_name == 'meesa' or kid_name == 'meesha' or kid_name == 'nisha' or kid_name == 'hermoine' or kid_name == 'ginny' or kid_name == 'harry'

def birthday_kid(kid_name):
    kid_name = kid_name.lower()
    return kid_name == 'panthi' or kid_name == 'panti' or kid_name == 'panthy' or kid_name == 'monthly' or kid_name == 'monthy' or kid_name == 'panthee'

def get_assign_thinking(kid_name):
    if birthday_kid(kid_name):
        return birthday_kid_thinking
    else:
        return random.choice(assign_thinking)

def assign_house_response(kid_name, house):
    return random.choice([
        f"{kid_name} goes to {house}.",
        f"It's {house} for {kid_name}.",
        f"{kid_name} is assigned to {house}."
    ])
