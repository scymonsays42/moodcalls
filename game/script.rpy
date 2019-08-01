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

# CHAR IMAGES


# PLACE HOLDERS
image ocd = "oscar.png"

# DEV
image dep = "devin sketch.png"
# BEN
image bip = "ben2.png"
# adhd
image adhd = "ava2.png"

# ADAM
image an = "anxiety_sketch.png"
# MC

#KIMI PICS
image k_smile = "kimi smile.png"
image k_mad = "kimi mad.png"

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define no = Character("???")
define k = Character("Kimi", color="#fa0a4a")
define mc = Character("[mc_name]", color="#9014de")
define us = Character("[username]")
define an = Character("Adam", color="#4c65e6")
define bip = Character("Ben", color="#e6b74c")
define adhd = Character("Ava", color="#f2e200")
define dep = Character("Devin", color="#c79fd1")
define ocd = Character("Oscar", color="#84cf4e")

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
            jump choice_boy

        "girl!":
            jump choice_girl

    label choice_girl:
        python:
            mc_name = renpy.input("What is your name?")

    "Alright '[mc_name]' welcome to Mood Calls!"
    scene hall

    show k_smile at center
    with dissolve

    k "[mc_name], hey, I've noticed that you've been feeling down lately..."

    menu:
        "What are you talking about?! I feel fine, thank you very much.":
            jump choice_fine

        "How...how did you know I wasn't feeling okay?":
            jump choice_accept

    label choice_accept:
        show k_smile
        with dissolve
        k "Let's call it bestfriend intuition, and we'll leave it at that."
        jump continue
    label choice_fine:
        show k_smile
        with dissolve
        k "Hey now, don't be all defensive, I just wanted to help."
        jump continue

# continue choice 1
label continue:

    show k_smile
    with dissolve

    k "Anyways, I heard about this club that can help! The club room is in C-3"

    mc "Hmmm, I don't know Kimi, I think I can handle this myself..."

    k "I know it doesn't seem ideal, but I still think you should give it a try!"

    k "Remember that I'm still here for you though, so don't worry, but try it. If not for yourself, then do this for me."

    scene bed_night

    mc "*sigh* {i}Fine, I should at least give it a look at, Kimi's just trying to help!{i}"


    mc "{i}BetterMoodClub, here I come.{i}"
    mc "{i}BetterMoodClub, that sure sounds like a cheesy visual novel.{i}"


    scene black

    #mc " And then everything..."
    #mc "{b} changed {b}"
#  SCENE 2 DAY 1
    scene bed_morn

    mc "{i}Alright today's the day, I gotta check out that club, at least I could tell Kimi that I made an attempt. {i}"

    scene hallway
    mc "{i}Room 3-C...{i}"

    scene clubroom

    "There was a total of five people in this room, but it sounded like there was 200."
    "In the far side of the room, you could see a very deep rooted argument taking place."

    show adhd at left
    with dissolve
    adhd "I didn't mean to do that! I swear!"

    show an at right
    with dissolve
    an "Oh sure you didn't, and I didn't mean to utterly destroy you in our Pokemon tournament yesterday."

    show dep at center
    with dissolve
    dep "Can we please drop this? You two are acting like children."

    an "I can, but I don't know about adhd here."

    adhd "Hey! What's that supposed to mean?!"

    adhd "Oosccaarr, Adam's bullying me!"
    hide an
    show ocd at right
    with dissolve
    ocd "All this? Over a Pokemon game, really?"

    adhd "You guys just don't understand!"
    hide adhd
    show bip at left
    bip "You guys can get really annoying sometimes you know?"

    hide bip
    hide dep
    show ocd at center
    with move
    ocd "Agreed, and look at the mess you guys made."
    hide ocd
    hide bip

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

    show bip at center
    with dissolve
    bip "Oh hey! Sorry we didn't notice you earlier!"

    show bip at left
    with move
    show ocd at right
    ocd "Yeah Ben, how could you not notice her earlier?"

    hide ocd
    show an at right
    with dissolve
    an "I didn't think we would get any new members..."

    mc "{i}They're all staring at me like a wild animal, this is super uncomfortable.{i}"

    hide bip
    show dep at left
    with dissolve
    dep "Guys, don't be rude."

    dep "Don't mind them, we're always open to accepting new members!"

    mc "That's fine actually I was just thinking I should head out."

    "You bolted out of the room before they had a chance to react."

    scene hallway
    dep "{i}Good going guys, she could've needed help.{i}"

    adhd "{i}Yeah, you  scared her off! we could of had a new friend!{i}"

    ocd "{i}Us?! It was you and Adam's petty fight!{i}"

    an "{i}Maybe she might come back?{i}"

    dep "{i}Hopefully...{i}"

    scene bed_ev

    mc "{i}That was awful, super embarassing, and I never wanna do that again.{i}"
    mc "{i}This is so bad, I think one of them was even in my class.{i}"
    mc "{i}Thanks Kimi.{i}"
# CH1 DAY 2

    scene classroom


    show k_smile at center
    with dissolve

    k "So, did you go to the club yesterday?"

menu:
    "Yeah I checked it out.":
        jump honest

    "Nope, not yet.":
        jump yikes

label honest:
    mc "Yeah I checked it out, I don't this is for me though."

    show k_mad at center
    with dissolve
    k "Did you really? Knowing you, you probably just peeked your head in and called it a day."
    k "I'm sure if you gave it another try you might stay."

    jump cont2

label yikes:

    mc "No I didn't get the chance."
    mc "I think I'll just skip it, I have homework to catch up on, y'know?"

    show k_mad at center
    with dissolve
    k "Nonsense, we're in the same class, and we both know that you've already done the work for this week and next."
    hide k_mad
    show k_smile at center
    k "Plus, being in a club might be fun for you! Don't you want some more excitement in your life?"

    jump cont2

label cont2:

    mc "Why are you being so insistent about this? I really don't know how a club like that is gonna help me."

    show k_smile at center
    with dissolve
    k "Trust me okay? My friend Devin is the leader, I'm gonna let him know that you're going to be swinging by after school today."

    mc "Will you at least go with me today?"

    k "Sorry hon, you know I have stuff going on... Maybe another time, okay?"

    mc "Uh-huh okay."

    k "Just, trust me, this will be good for you."
    hide kimi

    show hall

    "And that's how you ended up back to where you started, the door to class 3-C."

    mc "{i}Second time's a charm I guess.{i}"

    show clubroom

    "You peeked your head in the door, luckily there was no yelling, only a group of friends hovering over a make-shift table out of desks."
    show an at center
    with dissolve
    an "That was so weird yesterday..."

    show an at left
    with move
    show bip at center
    with dissolve

    bip "Yeah your guy's obnoxious arguing scared a pretty girl off."

    bip "We definitely need more of those around this sausage fest."
    show bip at right
    with move
    show adhd at center
    with dissolve
    adhd "Okay, that was extremely out of line and rude."

    adhd "And plus, maybe she might come back? Dev, didn't you say your friend Kimi recommended her here?"

    hide bip
    with dissolve
    hide adhd
    with dissolve
    hide an
    with dissolve
    show dep at center
    with dissolve
    dep "Yeah, but she also said that she might bail so who knows."

    show ocd at right
    with dissolve
    ocd "You guys do realize she's at the door right now."
    hide bip
    hide ocd
    hide dep

    "A hush goes over the room, nobody dared to move a muscle."

    show adhd at center
    with dissolve
    adhd "{i}If we stay still she might not notice us{i}"

    show adhd at left
    with move
    show dep at center
    with dissolve
    dep "{i}Why wouldn't we want her to notice us?{i}"


    show dep at right
    with move
    show bip at center
    with dissolve
    bip "{i}Or how about this. We {i}talk{i} to her like a normal human being?{i}"

    "They all simultaniously turned to face you."

    mc "{i}Nevermind I should've just went home.{i}"

    hide adhd
    hide bip

    show dep at center
    with move
    dep "Welcome back?"

    show dep at right
    with move
    show adhd at center
    with dissolve
    adhd "Yeah, welcome!"

    show adhd at left
    with move
    show ocd at center
    with dissolve
    ocd "I'm so sorry about our behavior."

    hide ocd
    hide adhd
    show dep at center
    with move
    dep "You must be [mc_name], Kimi told me about you!"

    show bip at right
    with dissolve
    bip "Don't be scared, we don't bite."

    hide bip
    hide dep
menu:
    "Oh uhm, thanks.":
        mc "Yeah, thanks. I'm sorry, I guess I'm just not used to meeting so many new people."

        show an at center
        with dissolve
        an "Haha yeah, don't worry about it, I was nervous when I first joined too."
        hide an

        jump cont3

    "Yeah I'm here for Kimi.":
        mc "Yeah I'm Kimi's friend, I promised her that I would see how I liked it here."
        mc "But it's fine if you guys are full or something..."

        show dep at center
        with dissolve
        dep "No, no, please stay, we're always open to new members."
        hide dep
        jump cont3

label cont3:

    dep "Alright! So I think our newest member would want to know who she's spending her after school time with, yes?"

    show adhd at center
    with dissolve
    adhd "Oh right! My name's Ava! It's great to have another girl around here, I'm really happy that you're here."

    hide adhd
    show ocd at center
    with dissolve
    ocd "I'm Oscar, delighted to meet you, I hope you find yourself comfortable amoung these {i}children{i} here."

    hide ocd
    show an at center
    with dissolve
    an "I'm Adam, I'm glad that we didn't scare you away yesterday."

    hide an
    show bip at center
    with dissolve
    bip "The name's Ben, like the clock tower."

    hide bip
    show dep at center
    with dissolve
    dep "And I'm Devin, the leader of this club, so make yourself comfortable here."

    pause

    hide dep
    menu:
        "My name's [mc_name], it's nice to meet you guys.":

            jump name_reveal

        "Oh uhm, alright, you can call me [mc_name].":
            show an at center
            with dissolve
            an "Hey, don't be so shy, we're all friends here now."

            an "I hope that you can be comfortable here."
            hide an

            jump name_reveal

label name_reveal:

    show bip at center
    with dissolve
    bip "Pretty name."

    show bip at right
    with move
    show adhd at center
    with dissolve
    adhd "Your gonna scare her off again loser."

    show adhd at left
    with move
    show ocd at center
    with dissolve
    ocd "It's your fighting that put her off in the first place."

    mc "{i}Well even if it didn't go well at first, I think I might give this a try. Who knows? It could be intresting.{i}"

    jump day3

# DAY 3

label day3:

    scene

    mc "{i}It's only been a month since I started attending the club. And as always, Kimi was right. This really did help me.{i}"
    mc "{i}Our usual club activities is usually just talking to each other, being able to have a save outlet for our problems. We talk about our day, sometimes our triggers, and how to cope with them.{i}"
    mc "{i}It's nice having a group of friends that I can really talk to about this, making me feel less alone in the world.{i}"
    mc "{i}I remember when I had my first panic attack, and luckily I was walking to my class the Adam appeared out of no where....{i}"

    jump flashback

label flashback:

    scene hallway
    with fade

    mc "{i}I couldn't see. I couldn't breath. I didn't know what to do. But then I heard a familiar voice breaking through to me. It was guiding me, reminding me how to breathe."

    show an at center
    with dissolve
    an "Hey, hey it's okay, just look at me and take deep breaths [mc_name]."

    an "In, and out with me hm?"

    mc "{i}Why is he helping me?{i}"
    mc "{i}Why is he doing this?{i}"

    mc "And with his help, my panic attack was soon over, and I was suddenly more than aware of where I was and who I was with."

    an "Feeling better now?"

    mc "Yeah, yeah, thank you Adam."

    hide an
    jump day3cont

label day3cont:
    scene clubroom

    show an at center
    with dissolve
    an "So how is everyone today?"

    menu:
        "Good.":
            mc "I'm feeling pretty good today."
            an "Ah, well that's good [mc_name]!"

            jump day3cont1

        "Eh.":
            mc "I could be better..."
            an "Hm, that's a shame, do you wanna talk about it?"

            jump day3cont1

label day3cont1:
    hide an
    show adhd at center
    with dissolve
    adhd "Hey do you lovebirds wanna include the whole class in this discussion or?"

    show adhd at left
    with move
    show bip at center
    with dissolve
    bip "No actually guys, I think that our Prince here has found his long lost princess."

    hide bip
    show ocd at center
    with dissolve
    ocd "Benjamin, leave them alone."
    ocd "Sometimes I wonder how we stand your nosiness sometimes."

    hide an
    hide ocd
    show dep at right
    with dissolve
    dep "Yeah Benji, don't you have a girl waiting for you as well?"
    dep "Oh right, you're still holding out for your Minecraft girlfriend."

    show bip at center
    with dissolve
    bip "She's not a Minecraft girlfriend! She's real!"

    adhd "Yeah in your dreams."

    hide adhd
    hide dep
    show bip at center
    with move
    bip "Whatever, let's just leave the {i}lovebirds{i} alone."

    show dep at right
    with dissolve
    dep "Seriously Ben, knock it off, that wasn't cool."

    show adhd at left
    with dissolve
    adhd "Yeah {i}Ben{i} knooockk itt ooofff."

    "You could see out of the corner of your eye, Adam's face contoring into a fake smile, a sort of anxious and angry aura began to surround him."
    an "Yeah {i}Ben{i}, I was just being nice, and that wasn't a very cool thing to say. {b}{i}Very uncool{i}{b}."

    "The clubroom air stilled. You silently looked around the room, adhd was fidgeting was her fingers, never looking at the same place twice, Ben looked slightly angry, but mostly confused. Oscar was instantly fizated on a point on the floor, seemingly unaware of the world around him."
    "Devin looked around the room as well, hugging himself, his leadership role seeming to fall apart. You finally looked back at Adam who looked even more anxious from the quiet then before."

    hide adhd
    hide ocd
    hide dep
    mc "{i}This isn't good.{i}"
    mc"{i}I gotta clear the air somehow.{i}"
########################
    #"Let's go on a trip!":
    mc "Hey guys, how about we go on a club field trip or something! I feel like that'll be fun."

    show ocd at center
    with dissolve
    ocd "Yeah that sounds like a good idea, plus I think it'll be fun."

    show ocd at right
    with move
    show adhd at left
    with dissolve
    adhd "Yeah! Let's go somewhere! That would be so cool. Ah then we can go to the mall! Or the zoo! Or anything we want!"

    "Ava was back to life, jumping in her seat, clearly excited."

    adhd "Wait what were we talking about again?"

    hide adhd
    hide ocd
    show dep at center
    with dissolve
    dep "Well where should we go?"
    hide dep

menu :
    "To the mall!":
        mc "How about the mall?"

    "To my house!":
        mc "We can always hang out at my place, I don't mind having company over."

        pause

        show bip at center
        with dissolve
        bip "Why are you looking at me?!"

        show bip at left
        with move
        show ocd at center
        with dissolve

        ocd "Yeah maybe it's best if we leave Ben behind."

        "There was a collective nod from the group."

        mc "You guys are funny, we're all goint to my house. It's a {i}group{i} trip everyone."

        dep "So it's decided, we'll go to [mc_name]'s house tomorrow."

        jump day4

# DAY 4
label day4:
    scene bedroom_morn
    with fade

    mc "{i}Today's the day of our makeshift '{i}Club Field Trip{i}' and I can already feel the regret settling in.{i}"
    mc "{i}But I guess it was worth it to get out of an awkward situation. I'm sure everything will be fine.{i}"

    "Everything did not go fine."

    scene bedroom_day
    with fade

    mc "Well I've got everything ready now... This is fine, I feel fine, everything's {i}fine{i}."

    "{b}BBBZZZZZZZZZZZ{B}"

    mc "Shoot they're already here."

    show adhd at center
    with dissolve
    adhd "Hey [mc_name]! I love your room!"

    show adhd at right
    with move
    show ocd at center
    with dissolve
    ocd "And it's suprisingly clean. Good."

    show ocd at left
    with move
    show bip at center
    with dissolve
    bip "Kinda disapointing if I'm honest."

    hide adhd
    show bip at right
    with move
    show an at center
    with dissolve
    an "Why are you disappointed?"

    bip "Hm, nevermind, doesn't matter."

    hide adhd
    hide an
    hide ocd
    hide bip
    show dep at center
    with dissolve

    dep "Alright, now that everyone's here, how about we get started with our club activities, then we can do whatever afterwards."

    mc "{i}So far, so good. Time to keep it like this.{i}"
    mc "Yeah, let's get to it!"

    hide dep
    show bip at center
    with dissolve
    bip "Actually I was hoping we wouldn't have to do any club activities."

    show bip at left
    with move
    show an at center
    an "You do realize this is a '{i}Club{i} Field Trip' right?"

    bip "Yeah I'm aware, but still."

    show an at right
    with move
    show dep at center
    with dissolve
    dep "Anyways, let's get started."

    scene bedroom_evening
    mc "{i}When we finished our club duties, everyone split up to do their own thing.{i}"

menu:
    "Let's talk to Ben!":
        mc "{i}Ben's all alone in the corner, playing on his phone...{i}"

        show bip at center
        with dissolve
        bip "Oh hey [mc_name], what's up?"

        mc "Nothing much, guess I'm just nervous."

        bip "Why's that? There's not much to be nervous about dude."

        mc "Yeah I guess, but I just don't want anything to happen like yesterday."

        bip "Oh, yeah that. I'm sorry you were there during that, I just got really angry all of a sudden and I let it get the best of me..."

        mc "Ben, don't worry about it."

        bip "If you say so. Thanks for talking to me [mc_name], everyone here can be a bit extreme sometime, so I'm glad you stayed around."

        mc "Of course."

        jump gobears2

    "Let's talk to Adam!":
        mc "{i}I should go check on Adam.{i}"
        mc "Hey Adam! How's it going?"

        show an at center
        with dissolve
        an "I'm doing better now. Thanks."

        mc "That's good, I'm just double checking."

        an "Haha, don't worry about me. Plus I think {i}I'm{i} the one who should be checking up on you."

        mc "Heh, I guess so."

        jump gobears2

label gobears2:
    mc "{i}Well I've made my rounds of the various club members, checking up on everyone. But as I did, I felt like someone was watching me the whole time. Something doesn't feel right.{i}"

    show an at center
    with dissolve
    mc "Oh hey Adam, what's up?"

    an "Can we talk... like in private?"

    mc "Sure, I'll tell everyone to go downstairs real quick."

    mc "Dev would you do me a huge favor and go make something for everyone to eat?"
    show an at right
    with move
    show dep at center
    with dissolve

    dep "Yeah of course."

    "Everyone slowly exited the room in single file."

    show an at center
    with move

    mc "So what did you want to talk about?"

    an "Nothing really... I was just thinking."

    mc "About what?"

    an "How you make me feel... You know you like, calm me down."

    mc "Oh, well that's what friends do right? I'm supposed to be here for you."

    an "I don't think you understand... You're {i}addicting{i}."

    mc "{i}What am I supposed to say to this.{i}"
    mc "Oh uhm, okay..."

    "He stepped closer to you, not giving you an easy out."
    "Adam had a dangerous look in his eye, like something's possessed him."

    mc "Wha...What are you doing?"

    an "You can't leave me."

    "He's cornered you in the corner now, you could feel his heavy breath on your face."

    show adam at center:
        zoom 2
    mc "Adam seriously you're scaring me."

    an "I am being serious, I {i}can't{i} lose you."

    mc "{i}Should I scream? Should I try to help? This definitley isn't healthy.{i}"

    an "{b}You can't leave me.{b}"


#label jump = game over

    # This ends the game.

    return










#label jump = game over

    # This ends the game.

    return

label choice_boy:
    python:
        mc_name = renpy.input("What is your name?")


    "Alright '[mc_name]' welcome to Mood Calls!"
    scene hall

    show k_smile at center
    with dissolve

    k "[mc_name], hey, I've noticed that you've been feeling down lately..."

    menu:
        "What are you talking about?! I feel fine, thank you very much.":
            jump choice_fine2

        "How...how did you know I wasn't feeling okay?":
            jump choice_accept2

    label choice_accept2:
        show k_smile
        with dissolve
        k "Let's call it bestfriend intuition, and we'll leave it at that."

        jump continue2
    label choice_fine2:
        show k_smile
        with dissolve
        k "Hey now, don't be all defensive, I just wanted to help."

        jump continue2

# continue choice 1
label continue2:

    show k_smile
    with dissolve

    k "Anyways, I heard about this club that can help! The club room is in C-3"

    mc "Hmmm, I don't know Kimi, I think I can handle this myself..."

    k "I know it doesn't seem ideal, but I still think you should give it a try!"

    k "Remember that I'm still here for you though, so don't worry, but try it. If not for yourself, then do this for me."

    scene bed_night

    mc "*sigh* {i}Fine, I should at least give it a look at, Kimi's just trying to help!{i}"


    mc "{i}BetterMoodClub, here I come.{i}"
    mc "{i}BetterMoodClub, that sure sounds like a cheesy visual novel.{i}"


    scene black

    #mc " And then everything..."
    #mc "{b} changed {b}"
#  SCENE 2 DAY 1
    scene bed_morn

    mc "{i}Alright today's the day, I gotta check out that club, at least I could tell Kimi that I made an attempt. {i}"

    scene hallway
    mc "{i}Room 3-C...{i}"

    scene clubroom

    "There was a total of five people in this room, but it sounded like there was 200."
    "In the far side of the room, you could see a very deep rooted argument taking place."

    show adhd at left
    with dissolve
    adhd "I didn't mean to do that! I swear!"

    show an at right
    with dissolve
    an "Oh sure you didn't, and I didn't mean to utterly destroy you in our Pokemon tournament yesterday."

    show dep at center
    with dissolve
    dep "Can we please drop this? You two are acting like children."

    an "I can, but I don't know about adhd here."

    adhd "Hey! What's that supposed to mean?!"

    adhd "Oosccaarr, Adam's bullying me!"
    hide an
    show ocd at right
    with dissolve
    ocd "All this? Over a Pokemon game, really?"

    adhd "You guys just don't understand!"
    hide adhd
    show bip at left
    bip "You guys can get really annoying sometimes you know?"

    hide bip
    hide dep
    show ocd at center
    with move
    ocd "Agreed, and look at the mess you guys made."
    hide ocd
    hide bip

menu:
    mc "They haven't noticed me yet with all this yelling... Should I say something?"

    "Uhm...Hello?":
        mc "Ahem, hello?"
        jump cont12

    "...":
        mc "{i}Maybe I should just go, I technically checked it out for Kimi if she asks.{i}"
        "You try to turn and leave but you end up bumping very loudly into the door you thought was open."
        jump cont12

label cont12:
    "All five heads immediatley turned to your direction."

    show bip at center
    with dissolve
    bip "Oh hey! Sorry we didn't notice you earlier!"

    show bip at left
    with move
    show ocd at right
    ocd "Yeah Ben, how could you not notice him earlier?"

    hide ocd
    show an at right
    with dissolve
    an "I didn't think we would get any new members..."

    mc "{i}They're all staring at me like a wild animal, this is super uncomfortable.{i}"

    hide bip
    show dep at left
    with dissolve
    dep "Guys, don't be rude."

    dep "Don't mind them, we're always open to accepting new members!"

    mc "That's fine actually I was just thinking I should head out."

    "You bolted out of the room before they had a chance to react."

    scene hallway
    dep "{i}Good going guys, he could've needed help.{i}"

    adhd "{i}Yeah, you scared him off! We could of had a new friend!{i}"

    ocd "{i}Us?! It was you and Adam's petty fight!{i}"

    an "{i}Maybe he might come back?{i}"

    dep "{i}Hopefully...{i}"

    scene bed_ev

    mc "{i}That was awful, super embarassing, and I never wanna do that again.{i}"
    mc "{i}This is so bad, I think one of them was even in my class.{i}"
    mc "{i}Thanks Kimi.{i}"
# CH1 DAY 2

    scene classroom


    show k_smile at center
    with dissolve

    k "So, did you go to the club yesterday?"

menu:
    "Yeah I checked it out.":
        jump honest2

    "Nope, not yet.":
        jump yikes2

label honest2:
    mc "Yeah I checked it out, I don't this is for me though."

    show k_mad at center
    with dissolve
    k "Did you really? Knowing you, you probably just peeked your head in and called it a day."
    k "I'm sure if you gave it another try you might stay."
    hide k_mad

    jump cont22

label yikes2:

    mc "No I didn't get the chance."
    mc "I think I'll just skip it, I have homework to catch up on, y'know?"

    show k_mad at center
    with dissolve
    k "Nonsense, we're in the same class, and we both know that you've already done the work for this week and next."
    hide k_mad
    show k_smile at center
    k "Plus, being in a club might be fun for you! Don't you want some more excitement in your life?"

    jump cont22

label cont22:

    mc "Why are you being so insistent about this? I really don't know how a club like that is gonna help me."

    show k_smile at center
    with dissolve
    k "Trust me okay? My friend Devin is the leader, I'm gonna let him know that you're going to be swinging by after school today."

    mc "Will you at least go with me today?"

    k "Sorry hon, you know I have stuff going on... Maybe another time, okay?"

    mc "Uh-huh okay."

    k "Just, trust me, this will be good for you."
    hide k_smile

    show hall

    "And that's how you ended up back to where you started, the door to class 3-C."

    mc "{i}Second time's a charm I guess.{i}"

    show clubroom

    "You peeked your head in the door, luckily there was no yelling, only a group of friends hovering over a make-shift table out of desks."
    show an at center
    with dissolve
    an "That was so weird yesterday..."

    show an at left
    with move
    show bip at center
    with dissolve

    bip "Yeah your guy's obnoxious arguing scared a new memeber off."
    bip "They probably realized that they didn't want to deal with {i}children{i} in their free time."

    show bip at right
    with move
    show adhd at center
    with dissolve
    adhd "Okay, that was extremely out of line and rude."

    adhd "And plus, maybe he might come back? Dev, didn't you say your friend Kimi recommended him here?"

    hide bip
    hide adhd
    hide an
    show dep at center
    with dissolve
    dep "Yeah, but Kimi also said that he might bail so who knows."

    show ocd at right
    with dissolve
    ocd "You guys do realize he's at the door right now."
    hide bip
    hide ocd
    hide dep

    "A hush goes over the room, nobody dared to move a muscle."

    show adhd at center
    with dissolve
    adhd "{i}If we stay still he might not notice us{i}"

    show adhd at left
    with move
    show dep at center
    with dissolve
    dep "{i}Why wouldn't we want him to notice us?{i}"


    show dep at right
    with move
    show bip at center
    with dissolve
    bip "{i}Or how about this. We {i}talk{i} to him like a normal human being?{i}"

    "They all simultaniously turned to face you."

    mc "{i}Nevermind I should've just went home.{i}"

    hide adhd
    hide bip

    show dep at center
    with move
    dep "Welcome back?"

    show dep at right
    with move
    show adhd at center
    with dissolve
    adhd "Yeah, welcome!"

    show adhd at left
    with move
    show ocd at center
    with dissolve
    ocd "I'm so sorry about our behavior."

    hide ocd
    hide adhd
    show dep at center
    with move
    dep "You must be [mc_name], Kimi told me about you!"

    show bip at right
    with dissolve
    bip "Don't be scared, we don't bite."

    hide bip
    hide dep
menu:
    "Oh uhm, thanks.":
        mc "Yeah, thanks. I'm sorry, I guess I'm just not used to meeting so many new people."

        show an at center
        with dissolve
        an "Haha yeah, don't worry about it, I was nervous when I first joined too."
        hide an
        jump cont32

    "Yeah I'm here for Kimi.":
        mc "Yeah I'm Kimi's friend, I promised her that I would see how I liked it here."
        mc "But it's fine if you guys are full or something..."

        show dep at center
        with dissolve
        dep "No, no, please stay, we're always open to new members."
        hide dep
        jump cont32

label cont32:

    show dep at center
    dep "Alright! So I think our newest member would want to know who he's spending his after school time with, yes?"

    hide dep
    show adhd at center
    with dissolve
    adhd "Oh right! My name's Ava! It's great to have a new face around here, I'm really happy that you're here."

    hide adhd
    show ocd at center
    with dissolve
    ocd "I'm Oscar, delighted to meet you, I hope you find yourself comfortable amoung these {i}children{i} here."

    hide ocd
    show an at center
    with dissolve
    an "I'm Adam, I'm glad that we didn't scare you away yesterday."

    hide an
    show bip at center
    with dissolve
    bip "The name's Ben, like the clock tower."

    hide bip
    show dep at center
    with dissolve
    dep "And I'm Devin, the leader of this club, so make yourself comfortable here."

    pause

    hide dep
    menu:
        "My name's [mc_name], it's nice to meet you guys.":

            jump name_reveal2

        "Oh uhm, alright, you can call me [mc_name].":
            show an at center
            with dissolve
            an "Hey, don't be so shy, we're all friends here now."

            an "I hope that you can be comfortable here."
            hide an

            jump name_reveal2

label name_reveal2:

    show bip at center
    with dissolve
    bip "Nice name."

    show bip at right
    with move
    show adhd at center
    with dissolve
    adhd "Your gonna scare him off again loser."

    show adhd at left
    with move
    show ocd at center
    with dissolve
    ocd "It's your fighting that put him off in the first place."

    mc "{i}Well even if it didn't go well at first, I think I might give this a try. Who knows? It could be intresting.{i}"

    jump day32

# DAY 3

label day32:

    scene black
    with fade

    mc "{i}It's only been a month since I started attending the club. And as always, Kimi was right. This really did help me.{i}"
    mc "{i}Our usual club activities is usually just talking to each other, being able to have a save outlet for our problems. We talk about our day, sometimes our triggers, and how to cope with them.{i}"
    mc "{i}It's nice having a group of friends that I can really talk to about this, making me feel less alone in the world.{i}"
    mc "{i}I remember when I had my first panic attack, and luckily I was walking to my class the Adam appeared out of no where....{i}"

    jump flashback2

label flashback2:

    scene hallway
    with fade

    mc "{i}I couldn't see. I couldn't breath. I didn't know what to do. But then I heard a familiar voice breaking through to me. It was guiding me, reminding me how to breathe."

    show an at center
    with dissolve
    an "Hey, hey it's okay, just look at me and take deep breaths [mc_name]."

    an "In, and out with me hm?"

    mc "{i}Why is he helping me?{i}"
    mc "{i}Why is he doing this?{i}"

    mc "And with his help, my panic attack was soon over, and I was suddenly more than aware of where I was and who I was with."

    an "Feeling better now?"

    mc "Yeah, yeah, thank you Adam."

    hide an
    jump day3cont2

label day3cont2:
    scene clubroom

    show an at center
    with dissolve
    an "So how is everyone today?"

    menu:
        "Good.":
            mc "I'm feeling pretty good today."
            an "Ah, well that's good [mc_name]!"

            jump day3cont12

        "Eh.":
            mc "I could be better..."
            an "Hm, that's a shame, do you wanna talk about it?"

            jump day3cont12

label day3cont12:
    show an at right
    with move

    show adhd at center
    with dissolve
    adhd "Hey do you two wanna include the whole class in this discussion or?"

    show adhd at left
    with move
    show bip at center
    with dissolve
    bip "No actually guys, I think that our Prince here has found his long lost prince."

    hide bip
    show ocd at center
    with dissolve
    ocd "Benjamin, leave them alone."
    ocd "Sometimes I wonder how we stand your nosiness sometimes."

    hide an
    hide ocd
    show dep at right
    with dissolve
    dep "Yeah Benji, don't you have a girl waiting for you as well?"
    dep "Oh right, you're still holding out for your Minecraft girlfriend."

    show bip at center
    with dissolve
    bip "She's not a Minecraft girlfriend! She's real!"

    adhd "Yeah in your dreams."

    hide adhd
    hide dep
    show bip at center
    with move
    bip "Whatever, let's just leave the {i}lovebirds{i} alone."

    show dep at right
    with dissolve
    dep "Seriously Dev, knock it off, that wasn't cool."

    show adhd at left
    with dissolve
    adhd "Yeah {i}Dev{i} knooockk itt ooofff."

    hide adhd
    hide dep
    hide bip

    "You could see out of the corner of your eye, Adam's face contoring into a fake smile, a sort of anxious and angry aura began to surround him."
    an "Yeah {i}Ben{i}, I was just being nice, and that wasn't a very cool thing to say. {b}{i}Very uncool{i}{b}."

    "The clubroom air stilled. You silently looked around the room, adhd was fidgeting was her fingers, never looking at the same place twice, Ben looked slightly angry, but mostly confused. Oscar was instantly fizated on a point on the floor, seemingly unaware of the world around him."
    "Devin looked around the room as well, hugging himself, his leadership role seeming to fall apart. You finally looked back at Adam who looked even more anxious from the quiet then before."

    mc "{i}This isn't good.{i}"
    mc"{i}I gotta clear the air somehow.{i}"

    #"Let's go on a trip!":
    mc "Hey guys, how about we go on a club field trip or something! I feel like that'll be fun."

    show ocd at center
    with dissolve
    ocd "Yeah that sounds like a good idea, plus I think it'll be fun."

    show ocd at right
    with move
    show adhd at left
    with dissolve
    adhd "Yeah! Let's go somewhere! That would be so cool. Ah then we can go to the mall! Or the zoo! Or anything we want!"

    "Ava was back to life, jumping in her seat, clearly excited."

    adhd "Wait what were we talking about again?"

    hide adhd
    hide ocd
    show dep at center
    with dissolve
    dep "Well where should we go?"
    hide dep

menu :
    #"To the mall!":
        #mc "How about the mall?"

    "To my house!":
        mc "We can always hang out at my place, I don't mind having company over."

        pause

        show bip at center
        with dissolve
        bip "Why are you looking at me?!"

        show bip at left
        with move
        show ocd at center
        with dissolve

        ocd "Yeah maybe it's best if we leave Ben behind."

        "There was a collective nod from the group."

        mc "You guys are funny, we're all goint to my house. It's a {i}group{i} trip everyone."

        hide ocd
        show dep at center
        dep "So it's decided, we'll go to [mc_name]'s house tomorrow."

        jump day42

# DAY 4
label day42:
    scene bedroom_morn
    with fade

    mc "{i}Today's the day of our makeshift '{i}Club Field Trip{i}' and I can already feel the regret settling in.{i}"
    mc "{i}But I guess it was worth it to get out of an awkward situation. I'm sure everything will be fine.{i}"

    "Everything did not go fine."

    scene bedroom_day
    with fade

    mc "Well I've got everything ready now... This is fine, I feel fine, everything's {i}fine{i}."

    "{b}BBBZZZZZZZZZZZ{B}"

    mc "Shoot they're already here."

    show adhd at center
    with dissolve
    adhd "Hey [mc_name]! I love your room!"

    show adhd at right
    with move
    show ocd at center
    with dissolve
    ocd "And it's suprisingly clean. Good."

    show ocd at left
    with move
    show bip at center
    with dissolve
    bip "Kinda disapointing if I'm honest."

    hide adhd
    show bip at right
    with move
    show an at center
    with dissolve
    an "Why are you disappointed?"

    bip "Hm, nevermind, doesn't matter."

    hide adhd
    hide an
    hide ocd
    hide bip
    show dep at center
    with dissolve

    dep "Alright, now that everyone's here, how about we get started with our club activities, then we can do whatever afterwards."

    mc "{i}So far, so good. Time to keep it like this.{i}"
    mc "Yeah, let's get to it!"

    hide dep
    show bip at center
    with dissolve
    bip "Actually I was hoping we wouldn't have to do any club activities."

    show bip at left
    with move
    show an at center
    an "You do realize this is a '{i}Club{i} Field Trip' right?"

    bip "Yeah I'm aware, but still."

    show an at right
    with move
    show dep at center
    with dissolve
    dep "Anyways, let's get started."

    scene bedroom_evening
    mc "{i}When we finished our club duties, everyone split up to do their own thing.{i}"

menu:
    "Let's talk to Ben!":
        mc "{i}Ben's all alone in the corner, playing on his phone...{i}"

        show bip at center
        with dissolve
        bip "Oh hey [mc_name], what's up?"

        mc "Nothing much, guess I'm just nervous."

        bip "Why's that? There's not much to be nervous about dude."

        mc "Yeah I guess, but I just don't want anything to happen like yesterday."

        bip "Oh, yeah that. I'm sorry you were there during that, I just got really angry all of a sudden and I let it get the best of me..."

        mc "Ben, don't worry about it."

        bip "If you say so. Thanks for talking to me [mc_name], everyone here can be a bit extreme sometime, so I'm glad you stayed around."

        mc "Of course."

        jump gobears

    "Let's talk to Adam!":
        mc "{i}I should go check on Adam.{i}"
        mc "Hey Adam! How's it going?"

        show an at center
        with dissolve
        an "I'm doing better now. Thanks."

        mc "That's good, I'm just double checking."

        an "Haha, don't worry about me. Plus I think {i}I'm{i} the one who should be checking up on you."

        mc "Heh, I guess so."

        jump gobears

label gobears:
    mc "{i}Well I've made my rounds of the various club members, checking up on everyone. But as I did, I felt like someone was watching me the whole time. Something doesn't feel right.{i}"

    show an at center
    with dissolve
    mc "Oh hey Adam, what's up?"

    an "Can we talk... like in private?"

    mc "Sure, I'll tell everyone to go downstairs real quick."

    mc "Dev would you do me a huge favor and go make something for everyone to eat?"
    show an at right
    with move
    show dep at center
    with dissolve

    dep "Yeah of course."

    "Everyone slowly exited the room in single file."

    show an at center
    with move

    mc "So what did you want to talk about?"

    an "Nothing really... I was just thinking."

    mc "About what?"

    an "How you make me feel... You know you like, calm me down."

    mc "Oh, well that's what friends do right? I'm supposed to be here for you."

    an "I don't think you understand... You're {i}addicting{i}."

    mc "{i}What am I supposed to say to this.{i}"
    mc "Oh uhm, okay..."

    "He stepped closer to you, not giving you an easy out."
    "Adam had a dangerous look in his eye, like something's possessed him."

    mc "Wha...What are you doing?"

    an "You can't leave me."

    "He's cornered you in the corner now, you could feel his heavy breath on your face."

    show an  at center:
        zoom 2
    mc "Adam seriously you're scaring me."

    an "I am being serious, I {i}can't{i} lose you."

    mc "{i}Should I scream? Should I try to help? This definitley isn't healthy.{i}"

    an "{b}You can't leave me.{b}"


#label jump = game over

    # This ends the game.

    return
