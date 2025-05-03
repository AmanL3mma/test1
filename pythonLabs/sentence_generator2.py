import random

s_nouns = ["A lion", "My friend", "The Emperor", "Some guy", "A squid with anger issues", "A bear", "Your homie", "This cool guy my gardener met yesterday", "Namor"]
p_nouns = ["These dudes", "Both of my friends", "All the Emperors of the world", "Some guys", "All of a aquariums squids", "The multitude of bears living under your bed", "Your homies", "Like, these, like, all these people", "Atlanteans"]
s_verbs = ["eats", "punches", "gives", "treats", "meets with", "creates", "attacks", "configures", "spies on", "retards", "roars on", "flees from", "tries to automate", "explodes"]
p_verbs = ["eat", "punch", "give", "treat", "meet with", "create", "attack", "configure", "spy on", "retard", "roar on", "flee from", "try to automate", "explode"]
infinitives = ["to make clam chowder.", "for no apparent reason.", "because the ocean is poluted.", "for a disease.", "to avenge the kingdom.", "to know more about the surface world."]

def sing_sen_maker():
    '''Makes a random senctence from the different parts of speech. Uses a SINGULAR subject'''
    if input("Would you like to add a new word?").lower() == "yes":
        new_word = input("Please enter a singular noun.")
        s_nouns.append(new_word)
    else:
        print(random.choice(s_nouns), random.choice(s_verbs), random.choice(s_nouns).lower() or random.choice(p_nouns).lower(), random.choice(infinitives))

sing_sen_maker()