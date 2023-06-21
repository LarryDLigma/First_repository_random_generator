import random

def get_random_word(words):
    return random.choice(words) #random.choice() returns a randomly selected element from the specified sequence.

# Places (the places are fictional!)
places = ['Atlantis', 'Elysium', 'Avalora', 'Zephyria', 'Celestia', 'Emeraldia', 'Stellara', 'Novaria', 'Mythos', 'Evermore']

# Verbs
verbs = ['run', 'jump', 'eat', 'sleep', 'play', 'sing', 'dance', 'write', 'swim', 'read']

# Nouns
nouns = ['dog', 'cat', 'book', 'chair', 'tree', 'car', 'flower', 'house', 'computer', 'phone']

# Adverbs
adverbs = ['quickly', 'slowly', 'happily', 'sadly', 'loudly', 'quietly', 'gently', 'bravely', 'carefully', 'eagerly']

# Geographic Details
geo_details = ['near the river', 'on the hill', 'by the sea', 'in the desert', 'in the forest', 'at the waterfall',
               'on the island', 'by the lake', 'in the valley', 'in the mountains']

# Names
names = ['Emma', 'Liam', 'Olivia', 'Noah', 'Ava', 'Isabella', 'Sophia', 'Mia', 'Charlotte', 'Amelia']

print("Greetings, fellow human, lets play, shall we?")

while True:
    random_name = get_random_word(names)
    random_place = get_random_word(places)
    random_noun = get_random_word(nouns)
    random_adverb = get_random_word(adverbs)
    random_geo_details = get_random_word(geo_details)
    random_verb = get_random_word(verbs)
    article = 'an' if random_noun[0].lower() in ['a', 'e', 'i', 'o', 'u'] else 'a'
    print(f"{random_name} from {random_place} {random_adverb} {random_verb} {random_noun}")
    input("Click [Enter] to generate a new one.")


