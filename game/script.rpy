# BACKGROUNDS

image black = "black.jpg"
image website = "website.png"
# EXTRAS

image cherry_blossoms = "original.gif"

# CHAR IMAGES
# MC

#KIMI PICS
image kimi = "clapping_man.png"
image kimi wink = "clapping_man_wink.png"
image kimi concerned = "clapping_man_con.png"

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define no = Character("???")
define k = Character("Kimi")
define mc = Character("[mc_name]")
define us = Character("[username]")
define an = Character("anxiety")
define bip = Character("bipolar")
define adhd = Character("adhd")
define dep = Character("depression")
define ocd = Character("ocd")

# PHONE??????
define e = Character('Eileen', color="#c8ffc8")




# Picking up the phone
transform phone_pickup:
    yalign 1.0 xalign 0.5
    yoffset 600
    easein 0.3 yoffset 200

    on hide:
        easeout 0.2 yoffset 600

transform phone_message_bubble_tip:
    xoffset 10
    yoffset 1

transform phone_message_bubble_tip2:
    xoffset 165
    yoffset 1

transform scrolling_out_message:
    easeout 0.1 yoffset -30 alpha 0

transform incoming_message:
    yoffset 100
    alpha 0
    parallel:
        easein 0.1 alpha 1
    parallel:
        easein 0.2 yoffset 0

    on hide:
        scrolling_out_message
# The game starts here.

label start:

    $ day = 0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg

    #WARNWARN

    "WARNING! THIS IS ABOUT CERTAIN TOPICS SUCH AS MENTAL ILLNESSES, SEXUALITY, ETC"
    "ANY REALTION OR SIMILAR APPEARANCE TO REAL LIFE PEOPLE IS PURELY COINCIDENCIDENTAL"
    "GOOD LUCK AND HAVE FUN! REMEMBER TO EDCUATE YOURSELF ABOUT THESE TOPICS TO BE BETTER AWARE OF ANY PROBLEMS SOMEONE
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
        $mc_name=renpy.call_screen("input_softkeyboard")
        #python:
            #mc_name = renpy.input("what is your name?")

    "Alright '[mc_name]' welcome to Mood Calls!"

    mc "I really don't know how I ended up like this, I guess it started freshman year, after testing."
    scene black

    show kimi:
        truecenter

    k "[mc_name], hey, I've noticed that you've been feeling down lately..."

    menu:
        "What are you talking about?! I feel fine, thank you very much.":
            jump choice_fine

        "How...how did you know I wasn't feeling okay?":
            jump choice_accept

    label choice_accept:
        show kimi wink
        k "Let's call it bestfriend intuition, and we'll leave it at that."
        jump continue
    label choice_fine:
        show kimi concered
        k "Hey now, don't be all defensive, I just wanted to help."
        jump continue

# continue choice 1
label continue:
    k "Anyways, I heard about this website that can help! Here I'll send you the link."



    mc "Hmmm, I don't know Kim, I think I can handle this myself..."

    k "I know it doesn't seem like the most trustworthy website but I still think you should give it a try!"
    show kimi smile
    k "Remember that I'm still here for you though, so don't worry, but try it. If not for yourself, then do this for me."

    scene room

    mc "*sigh* {i}Fine, I should at least give it a look at, Kimi's just trying to help!{i}"

    scene website

    mc "{i} BetterMood.com...{i}"
    mc "Huh."

    mc " And then everything..."
    mc "{b} changed {b}"
#  SCENE 2 DAY 1
    scene bedroom
    mc "Okay... So I just need a username now."

    #USERNAME
    "What do you want your username to be?"
    $username=renpy.call_screen("input_softkeyboard")

    show connection
    "Welcome to BetterMooc.com [username] ! Relax and enjoy your time here!"

    mc "{i}Hmmm, what should I do first?{i}"

label website_page:
    menu:
        mc "{i}Hmmm, what should I do?{i}"

        "Search the About Page!":
            mc "So this is like a chatting app...for sad people."
            mc "{i}Sounds like a blast, thanks Kimi{i}"
            jump website_page

        "Search the Music Page!":
            #play song lmao
            mc "Lofi hiphop, alrighty then."
            jump website_page

        "Search the Help Page!":
            mc "'Help?' like actual help?"
            "you scroll through the forum page"
            "CALL 1-800-273-8255"
            "'we're here for you!'"
            "'you're never alone in this!'"
            "'don't worry! there's always another way!'"
            mc "{i}maybe...maybe this will be good for me.{i}"
            jump website_page

        "Next Page!":
            jump chatting

label chatting:
    menu:
        "I think that's enough, I don't belong here.":
            mc "I'm fine. I don't need {i}help{i}, I'm not depressed, this is just a passing feeling."
            mc "Nothing to worry about..."
            mc "Right?"

            scene black
            with dissolve

            "{b}{u}Don't downplay your problems, if you don't feel like you used to anymore, talk to someone, they want to help, trust me :){b}{u}"
            return

        "Start Chatting!":
            mc "{i}Chatting?{i} I guess I'll give it a try."

            jump game

label game:
    "...Joining random chatroom!..."
    "This will take a few minutes..."

    show phone at phone_pickup

    $renpy.pause(0.2)
    show screen phone_message("kimi <3", "so did you check it out yet?")
    $renpy.pause(0.2)
    call screen phone_reply("yeah :)", "nope", "i don't know about this...")

label yeah:
    hide screen phone_message
    $renpy.pause(0.1)

    show screen phone_message2("[mc_name]", "yeah i did :), so far it seems cool.")
    $renpy.pause()

    hide screen phone_message2
    $renpy.pause(0.1)

    show screen phone_message("kimi <3", "this will be good for you!")
    $ renpy.pause()

    hide screen phone_message
    hide phone

    $renpy.pause(0.2)
    jump continue2

label continue2:
    mc "{i}Ugh, what am I doing here? This is kinda weird.{i}"
    mc "..."
    mc "{i}For Kimi{i}"
    "You've been connected! Be nice!"

    scene chatroom

    adhd "i really didn't mean to do that i swear."

    an "Sure you didn't, and I didn't mean to absolutely destroy you but here we are."

    dep "Can we all just calm down please?"

    an "I will when she does."

    adhd ";P"

    dep "All this? Over a Pokemon game? Really guys?"

    adhd "not a guyyyyy"

    dep "Fine, y'all"

    dep "Is that more to your tastes, m'lady??"

    adhd "4 now >:D"

    mc "{i}This is going so fast... they haven't even noticed me yet..."

    menu:
        "Should I say something?"

        "Uhm...hello everyone?":
            jump hello

        "{i}say nothing{i}":
            jump nothing


label hello:
    bip "oh hey! Sorry we didn't notice you earlier!"

    adhd "hey hey hey"

    ocd "welcome to our mess"

    an "that's weird, I thought we had a closed gc"

    "you have the strange sense that you weren't really supposed to be there."

    dep "the more the merrier ig"

    an "so..."

    "the sinking feeling of displacement burries deeper in your stomach."

    menu:
        "so...":
            jump so

        "haha sorry, maybe i should just go?":
            jump leaving


label so:
    "no one's typed for at least a minute now."
    "this is really awkward."
    adhd "so how are you today."

    "this is gonna be a long day."






#label jump = game over

    # This ends the game.

    return
