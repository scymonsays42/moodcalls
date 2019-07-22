# BACKGROUNDS

image black = "black.jpg"
image website = "website.png"
# EXTRAS

image cherry_blossoms = "original.gif"

# CHAR IMAGES
# MC

#RC
image dark rc = "clapping_man.png"

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define no = Character("???")
define k = Character("Kimi")
define mc = Character("[mc_name]")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg

    #WARNWARN

    "WARNING! THIS IS ABOUT CERTAIN TOPICS SUCH AS MENTAL ILLNESSES, SEXUALITY, ETC"
    "ANY REALTION OR SIMULAR APPEARANCE TO AND REAL LIFE PEOPLE IS PURELY COINCIDENCE"
    "GOOD LUCK AND HAVE FUN! REMEMBER TO EDCUATE YOURSELF ABOUT THESE TOPICS TO BE MORE WELL AWARE OF A PROBLEM SOMEONE
    CLOSE TO YOU MAY BE EXPERIENCING"

    # SCENE 1
    scene black
    no "{i}I've always been different...{i}"
    no "I guess I have tried to be a normal person, practicing my faces in the mirror."
    no "Until once day, my friend had recommended me to a website."
    no "A website they said would {i}help{i}."
    no "At first I thought it was weird."
    no "{i}'How is this gonna help me?'{i}"
    no "But still..."
    no "I gave it a try..."

    #  BOY OR GIRL
    scene website
    "are you a boy or a girl?"
    menu:
        "boy!":
            jump choice_girl

        "girl!":
            jump choice_girl

    label choice_girl:
        python:
            mc_name = renpy.input("what is your name?")

    "alright '[mc_name]' welcome to Mood Calls!"

    mc "I really don't know how I ended up like this, I guess it started freshman year, after testing."
    scene website 

    # This ends the game.

    return
