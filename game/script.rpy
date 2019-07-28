# BACKGROUNDS

image black = "black.jpg"
image clubroom = "classroom v2.png"
image classroom = "classroom v1.png"
image bed_morn = "bedroom morning.png"
image bed_day = "bedroom day-afternoon.png"
image bed_ev = "bedroom evening.png"
image bed_night = "bedroom night.png"
image hall = "Hallway.png"
# EXTRAS

image cherry_blossoms = "original.gif"

# CHAR IMAGES

# ADAM
image an_normal = "anxiety_sketch.png"
# MC

#KIMI PICS
image kimi = "clapping_man.png"
image kimi_wink = "wink.png"
image kimi_concerned = "concerned.png"

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define no = Character("???")
define k = Character("Kimi")
define mc = Character("[mc_name]")
define us = Character("[username]")
define an = Character("Adam")
define bip = Character("Ben")
define adhd = Character("Ava")
define dep = Character("Devin")
define ocd = Character("Oscar")

# PHONE??????

# Picking up the phone

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


    # DAY 0
    scene black
    no "{i}I've always been different...{i}"
    no "{i}I guess I've never felt the emotions that I was supposed to feel, like happiness, or sadness. I've always just been {i}fine{i}.{i}"
    no "{i}Until once day, my friend had recommended me to an outreach club at school. {i}"
    no "{i}A club she said would {i}help{i}.{i}"
    no "{i}At first I thought it was weird.{i}"
    no "'How is this gonna help me?'"
    no "{i}But still...{i}"
    no "{i}I gave it a try...{i}"

    #  BOY OR GIRL
    scene opening
    "Are you a boy or a girl?"
    menu:
        "boy!":
            jump choice_girl

        "girl!":
            jump choice_girl

    label choice_girl:
        python:
            mc_name = renpy.input("What is your name?")

    "Alright '[mc_name]' welcome to Mood Calls!"
    scene hall

    show kimi:
        truecenter

    k "[mc_name], hey, I've noticed that you've been feeling down lately..."

    menu:
        "What are you talking about?! I feel fine, thank you very much.":
            jump choice_fine

        "How...how did you know I wasn't feeling okay?":
            jump choice_accept

    label choice_accept:
        hide kimi
        show kimi_wink
        k "Let's call it bestfriend intuition, and we'll leave it at that."
        jump continue
    label choice_fine:
        hide kimi
        show kimi_concered
        k "Hey now, don't be all defensive, I just wanted to help."
        jump continue

# continue choice 1
label continue:
    k "Anyways, I heard about this club that can help! The club room is in C-3"

    mc "Hmmm, I don't know Kimi, I think I can handle this myself..."

    k "I know it doesn't seem ideal, but I still think you should give it a try!"
    show kimi_smile
    k "Remember that I'm still here for you though, so don't worry, but try it. If not for yourself, then do this for me."

    scene bed_night

    mc "*sigh* {i}Fine, I should at least give it a look at, Kimi's just trying to help!{i}"

    mc "{i}BetterMoodClub, that sure sounds like a cheesy visual novel.{i}"

    scene black
    
    mc " And then everything..."
    mc "{b} changed {b}"
#  SCENE 2 DAY 1
    scene bed_morn

    mc "{i}Alright today's the day, I gotta check out that club, at least I could tell Kimi that I made an attempt. {i}"
    mc "{i}Room 3-C...{i}"

    scene clubroom

    "There was a total of five people in this room, but it sounded like there was 200."
    "In the far side of the room, you could see a very deep rooted argument taking place."

    adhd "I didn't mean to do that! I swear!"

    show an_normal

    an "Oh sure you didn't, and I didn't mean to utterly destroy you in our Pokemon tournament yesterday."

    dep "Can we please drop this? You two are acting like children."

    an "I can, but I don't know about Ava here."

    adhd "Hey! What's that supposed to mean?!"

    adhd "Oosccaarr, Adam's bullying me!"

    ocd "All this? Over a Pokemon game, really?"

    adhd "You guys just don't understand!"

    bip "You guys can get really annoying sometimes you know?"

    ocd "Agreed, and look at the mess you guys made."

menu:
    mc "They haven't noticed me yet with all this yelling... Should I say something?"

    "Uhm...Hello?":
        mc "Ahem, hello?"
        jump cont1

    "...":
        mc "{i}Maybe I should just go, I technically checked it out for Kimi if she asks.{i}"
        "You try to turn and leave but you end up bumping very loudly into the door you thought was open."
        jump cont1

label cont1:
    "All five heads immediatley turned to your direction."

    bip "Oh hey! Sorry we didn't notice you earlier!"

    ocd "Yeah Ben, how could you not notice her earlier?"

    an "I didn't think we would get any new members..."

    mc "{i}They're all staring at me like a wild animal, this is super uncomfortable.{i}"

    dep "Guys, don't be rude."

    dep "Don't mind them, we're always open to accepting new members!"

    mc "That's fine actually I was just thinking I should head out."

    "You bolted out of the room before they had a chance to react."

    dep "{i}Good going guys, she could've needed help.{i}"

    adhd "{i}Yeah, you  scared her off! we could of had a new friend!{i}"

    ocd "{i}Us?! It was you and Adam's petty fight!{i}"

    an "{i}Maybe she might come back?{i}"

    dep "{i}Hopefully...{i}"

    scene bed_ev

    mc "{i}That was awful, and super embarassing, and I never wanna do that again.{i}"
    mc "{i}This is so bad, I think one of them was even in my class.{i}"
    mc "{i}Thanks Kimi.{i}"
# CH1 DAY 2

    scene classroom

    k "So, did you go to the club yesterday?"

menu:
    "Yeah I checked it out.":
        jump honest

    "Nope, not yet.":
        jump yikes

label honest:
    mc "Yeah I checked it out, I don't this is for me though."

    k "Did you really? Knowing you, you probably just peeked your head in and called it a day."
    k "I'm sure if you gave it another try you might stay."

    jump cont2

label yikes:

    mc "No I didn't get the chance."
    mc "I think I'll just skip it, I have homework to catch up on, y'know?"

    k "Nonsense, we're in the same class, and we both know that you've already done the work for this week and next."
    k "Plus, being in a clul might be fun for you! Don't you want some more excitement in your life?"

    jump cont2

label cont2:

    mc "Why are you being so insistent about this? I really don't know how a club like that is gonna help me."

    k "Trust me okay? My friend Devin is the leader, I'm gonna let him know that you're going to be swinging by after school today."

    mc "Will you at least go with me today?"

    k "Sorry hon, you know I have stuff going on... Maybe another time, okay?"

    mc "Uh-huh okay."

    k "Just, trust me, this will be good for you."

    show hall

    "And that's how you ended up back to where you started, the door to class 3-C."

    mc "{i}Second time's a charm I guess.{i}"

    show clubroom

    "You peeked your head in the door, luckily there was no yelling, only a group of friends hovering over a make-shift table out of desks."

    an "That was so weird yesterday..."

    bip "Yeah your guy's obnoxious arguing scared a pretty girl off."

    bip "We definitely need more of those around this sausage fest."

    adhd "Okay, that was extremely out of line and rude."

    adhd "And plus, maybe she might come back? Dev, didn't you say your friend Kimi recommended her here?"

    dep "Yeah, but she also said that she might bail so who knows."

    ocd "You guys do realize she's at the door right now."

    "A hush goes over the room, no bosy dared to move a muscle."

    adhd "{i}If we stay still she might not notice us{i}"

    dep "{i}Why wouldn't we want her to notice us?{i}"

    bip "{i}Or how about this. We {i}talk{i} to her like a normal human being?{i}"

    "They all simultaniously turned to face you."

    mc "{i}Nevermind I should've just went home.{i}"

    dep "Welcome back?"

    adhd "Yeah, welcome!"

    ocd "I'm so sorry about our behavior."

    dep "You must be [mc_name], Kimi told me about you!"

    bip "Don't be scared, we don't bite."

menu:
    "Oh uhm, thanks.":
        mc "Yeah, thanks. I'm sorry, I guess I'm just not used to meeting so many new people."

        an "Haha yeah, don't worry about it, I was nervous when I first joined too."
        jump cont3

    "Yeah I'm here for Kimi.":
        mc "Yeah I'm Kimi's friend, I promised her that I would see how I liked it here."
        mc "But it's fine if you guys are full or something..."

        dep "No, no, please stay, we're always open to new members."
        jump cont3

label cont3:
    dep "Alright! So I think our newest member would want to know who she's spending her after school time with, yes?"

    adhd "Oh right! My name's Ava! It's great to have another girl around here, I'm really happy that you're here."

    ocd "I'm Oscar, delighted to meet you, I hope you find yourself comforatble amoung these {i}children{i} here."

    an "I'm Adam, I'm glad that we didn't scare you away yesterday."

    bip "The name's Ben, like the clock tower."

    dep "And I'm Devin, the leader of this club, so make yourself comfortable here."

    menu:
        "My name's [mc_name], it's nice to meet you guys.":

            jump name_reveal

        "Oh uhm, alright, you can call me [mc_name].":
            an "Hey, don't be so shy, we're all friends here now."

            an "I hope that you can be comfortable here."

            jump name_reveal

label name_reveal:

    bip "Pretty name."

    adhd "Your gonna scare her off again loser."

    ocd "It's your fighting that put her off in the first place."

    mc "{i}Well even if it didn't go well at first, I think I might give this a try. Who knows? It could be intresting.{i}"

    jump day3

# DAY 3

label day3:

    scene black

    mc "{i}It's only been a month since I started attending the club. And as always, Kimi was right. This really did help me.{i}"
    mc "{i}Our usual club activits is usually just talking to each other, being able to have a save outlet for our problems. We talk about our day, sometimes our triggers, and how to cope with them.{i}"
    mc "{i}It's nice having a group of friends that I can really talk to about this, making me feel less alone in the world.{i}"
    mc "{i}I remember when I had my first panic attack, and luckily I was walking to my class the Adam appeared out of no where....{i}"

    jump flashback

label flashback:

    scene black

    mc "{i}I couldn't see. I couldn't breath. I didn't know what to do. But then I heard a familiar voice breaking through to me. It was guiding me, reminding me how to breathe."






#label jump = game over

    # This ends the game.

    return
