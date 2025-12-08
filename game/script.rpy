# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    #class for both the main and side romances, I don't think I need to differentiate here
    class Love_Interest:
        def __init__(self, character, name, love = 0, lust = 0, platonic = 0):
            self.c = character
            self.name = name
            self.love = love
            self.lust = lust
            self.platonic = platonic

    #class for Micah, so everything is neat and tidy
    class Hero:
        def __init__(self, character, name, orientation, corruption = 0, redemption = 0):
            self.c = character
            self.name = name
            self.orientation = orientation
            self.corruption = corruption
            self.redemption = redemption



screen debug_overlay():
    frame:
        align (0.98, 0.02)   # top-right corner
        background "#f00"
        padding (10, 10)

        vbox:
            text "Mephi Love: [me.love]"
            text "Mephi Platonic: [me.platonic]"
            text "Micah Corruption: [m.corruption]"
            text "Micah Redemption: [m.redemption]"

transform left:
    xalign 0.0
    yalign 1.0
transform slightleft:
    xalign 0.25
    yalign 1.0
transform right:
    xalign 1.0
    yalign 1.0
transform slightright:
    xalign 0.75
    yalign 1.0

# The game starts here.

label start:
    
    $ m = Hero(Character("Micah"), "Micah", "Open", 0, 0)
    $ me = Love_Interest(Character("Mephi"), "Mephi", 0, 0, 0)
    $ c = Love_Interest(Character("Clover"), "Clover", 0, 0, 0)
    $ n = Love_Interest(Character("Nox"), "Nox", 0, 0, 0)
    $ l = Love_Interest(Character("Lux"), "Lux", 0, 0, 0)
    $ lu = Love_Interest(Character("Luminia"), "Luminia", 0, 0, 0)
    $ ca = Love_Interest(Character("Cal"), "Cal", 0, 0, 0)

    define narrator = Character(None, what_italic=True)

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # Chapter 1 - Scene 1
    
    scene bg tavern
    show screen debug_overlay

    "The drunkards stare. Perhaps the quest items weren’t the only thing Micah should have cleaned before arriving at the tavern."
    
    show micah bloody 

    m.c "I’ve completed your request."

    "He lays five pristine bull horns on the table of the bewildered job requester. \n The horns of a minotaur are famed for their usage in medicine, however such medicine would be quickly expended for the average pharmacist in the process of gathering."
    "The man counts the horns."

    "Man""Thank you… This is more than I asked for, but this is still quite the odd number."

    show micah sheepish # make sure there's a few bloody portraits I guess lol

    m.c "I’m afraid I discovered that bone is rather weak to holy fire."

    "Man""… Never mind, this is enough to make more potions."

    "The man hands Micah a small bag, he checks his spoils as he walks away."

    "{b}Obtained 3 health potions and 20 silver pieces!{/b}"

    show micah bloody

    m.c "Potions as a reward for potion ingredients is strange, but I won’t complain."

    "The drunkards continue to stare as he leaves the tavern."
    m.c "Maybe I should have cleaned myself up before heading out. At least it doesn’t smell like human blood…" 
    m.c "...Now I’m hungry."

    scene bg town
    hide micah bloody
    "The sun has long disappeared, leaving the streets bare. The only company he could have is in the form of beggars who seem to be avoiding him anyway. Everything around Micah is desaturated yet clearly visible, a line of closed, currently useless shops passing him by."
    "Perhaps he should have memorised the route to an inn before agreeing to any quests in a new town."
    "A quiet rustle is all he hears before something grabs him by the arm, the street swiftly replaced by a dark alley." 
    "The stench of cheap alcohol and bile floods his senses before the clang of his armour against the wall, followed by his spear against the floor as he scrambles then fails to equip it."
    "The shadow evades Micah’s holy fire attack."

    "???""Hey, fire-cracker, cool it!"
    show mephi serious at slightright

    "A strange… person… comes into view. The dark chill of their aura flags their heritage as the same time Micah clocks their features, curled horns, a long arrow-headed tail. A demon, his only match in the darkness."

    show micah angry at slightleft

    m.c "Give me one reason why I shouldn’t rip your throat out!"

    "He charges light that forms an unstable blade, a spell the demon clearly recognises as he reveals an axe and takes on a defensive stance."

    "???""Alright, dragging you into an alley was a bad idea, I get it. You’re the war priest Micah, right?"

    "A demon that knows his name, even worse."

menu:
    "Nod, perhaps they aren’t as dangerous as they seem.":
        jump choice1_yes
    "Deny, a demon can’t be trusted with such a thing.":
        jump choice1_no
    
label choice1_yes:
    "???""Ah, good, I didn’t ambush the poor guy."
    jump choice1_done
    
label choice1_no:
    "???""Come now, your spear perfectly matches the description."
    jump choice1_done
    
label choice1_done: 
    "???""I didn’t come to cause you any harm. A man called Nike sent me to find you."

    show micah discomfort 

    "Cold floods through Micah, as he casts a detective spell. The demon is telling the truth, yet that only causes him to tense further. No, maybe, he {b}hoped{/b}, it was a different Nike."

    m.c "Who are you and what does ‘Nike’ want with me?"

    "???""Oh, right, introductions! How rude of me to forget. I’m Mephi."

    show mephi wink

    me.c "And if you need a cute boy toy tonight, I’m the perfect candidate."

    "Great, the demon was flirting with him. Heat floods through him. How was he meant to feel about this?"

menu: 
    "It doesn’t matter that he’s a guy, he’s still a demon. “Shut up and tell me about Nike!”":
        jump choice2_open
    "“Thanks, but I’m not into guys. Now tell me about Nike.”":
        $ m.orientation = "straight"
        jump choice2_close
    "“Cute, now shut up and tell me about Nike.”":
        jump choice2_open
label choice2_open:
    me.c "Snippy, aren’t you?"
    jump choice2_done
label choice2_close:
    show mephi disappointed
    me.c "Aww, what a shame. Never mind then."

label choice2_done:
    show mephi smug
    me.c "See, Nike told me to find the man who ditched his sister and her son back home."

    "The chill is almost suffocating. Maybe if he hid his spear, repressed his holy aura, this fiend wouldn’t be able to track him so easily." 
    "His stomach churns. Hunger seems to have completely subsided now."

    m.c "That’s all the way on the opposite side of the continent… You didn’t come all this way just to find me, did you?"

    me.c "Not exactly, he was out of town. I kinda owed him a favour after he saved me from some brutes and I just hate things being held over my head, you know? So I offered to find his missing brother-in-law for him."
    me.c "Ditching your wife and child isn’t very virtuous, is it angel?"

    "All he can seem to do as he tries to gather his thoughts and retort is roll his eyes. For a moment, it feels like his throat is closing up."

    m.c "My goddess sent me on a mission… I couldn’t deny her…"

    "Mephi crosses his arms. That smug expression destroys the creeping cold in exchange for barely restrained heat. It almost feels like he’s enjoying his pain."

    me.c "Doesn’t leaving a five year old on his own for a year not weigh on your conscience though, Micah? If you were that desperate to get away from your wife, there’s much less cruel methods than pretending to be all holy about it."

    show micah angry

    m.c "Shut it, you know nothing about what I’m doing! I was going to return eventually!"

    me.c "I don’t care what you were doing, all I need to know is that I’ll get rewarded for dragging you back. \n What’ll that be, I don’t know yet." 
    me.c "Maybe one of the village’s magic artifacts?"

    "Those holy artifacts the village elders hoarded, he dreaded to think what a fiend would do with such a thing. Why was Nike so desperate to get him back home?"

    m.c "He always hated me with his sister, I thought he’d be happy with me gone. Why did he bother sending a demon after me?"

    show mephi serious

    "Mephi doesn’t speak another word. Instead he pulls out a scroll from his cloak. The first thing Micah sees as he unfurls it is the name ‘Raze’. Why was he reading someone else’s mail?" 
    show micah discomfort
    "However, the handwriting is unmistakable. One line sticks out as though etched with gold."
    "‘I am sorry, but I cannot be with you while I am still married.’"
    "His eyes flit to the bottom, a gracefully scribed ‘Catarina’ signing off the message. The rest of the contents feel unimportant, just the little he’s seen is enough to disturb his stomach as it clicks."

    m.c "She wants a divorce, doesn’t she?"

    me.c "That’s right, and without you she can’t finalise it. … You don’t seem that bothered, I take it your relationship wasn’t that great."

    "Maybe that was natural after a month of careless bliss turned into five long years. Micah retrieves his spear. Out of the corner of his eye, Mephi reaches for his axe then relaxes as Micah straps the spear to his back."

    m.c "Alright, I’ll return. It’ll take a bloody long time to get back home, though."

    me.c "It couldn’t take you longer than the year you’ve already been gone. But I’ll accompany you. I need to get that reward, after all."

    if m.orientation == "Open":
        show mephi wink
        me.c "And maybe you’ll let me accompany you to bed?"
        "Mephi dodges the holy fire."
    jump Ch1Scene2

label Ch1Scene2:
    
    # Scene 2

    scene bg inn
    with Dissolve(1.0)

    "Micah sits by the fireplace, polishing the blood off his armour. His new companion had offered to pay for a higher class inn than he was used to." 
    "One that the horrible state of his attire had nearly kicked them right out of until the staff clocked the unmistakable scent of beefburgers that minotaurs were famous for." 
    "It was one he was wary of until he realised Mephi had been practically ready to drop unconscious by the time they entered the inn’s lobby."

    "Mephi was currently curled up in one of the beds, so silent he couldn’t help but wonder for a moment if he was faking slumber. At least he had the {b}decency{/b} to be quiet after the barrage of intrusively curious questions on the way here."

    scene bg town
    with Dissolve(1.0)

    show mephi normal at slightright
    show micah annoyed at slightleft
    me.c "Wow, how does your hair look so feathery?"
    m.c "It’s angelic heritage."
    me.c "Where are your wings?"
    m.c "Hiding."
    me.c "Are they pretty? Can I see them?"
    m.c "..."

    if m.orientation == "open":
        me.c "Hey, can I see your spear? Oh wow, it’s so big! Wanna see mine?"
        "He had the feeling he didn’t mean a weapon."
    
    "Never before had he had a companion so irritating."

    scene bg inn
    with Dissolve(1.0)

    hide mephi normal
    "Now he was sleeping, Micah could finally hear himself think again. How innocent the fiend looked in this moment, resting in a fetal position with his gently swaying tail peeking out of the duvet." 
    "What an angelic looking demon, how devilishly {b}aggravating{/b} he was."
    "What an idiot he was to sleep unguarded in the same room as a stranger."

    "Micah set down the freshly polished armour, picking up his spear and approaching Mephi’s sleeping form. With a trembling hand, he pulled back the duvet to reveal his torso and aimed." 
    "A glance was enough to tell it was thicker than a human’s skin, if the lack of scars wasn’t due to avoiding fights altogether. Still, just a bit of force from a blessed weapon would be enough."

    m.c "God give me strength, let this pretty boy be slain just as easily as the rest…"

    "One strong blow and it would be instant, then he would be out of here before anyone found out."

    me.c "Hehe..."

    "Micah freezes up, hearing the demon’s barely audible yet melodic laugh. He was still sleeping, he could tell that by the lack of defense, the peaceful expression as he curled up tighter into his ball. What on Earth was this fiend dreaming?"

menu: 
    "Don’t hesitate, deliver the blow before he wakes up.":
        jump gameover1
    "Maybe this isn’t the best idea…":
        $ me.platonic += 1
        jump choice3A
    "Cute… Wait, what?":
        $ me.love += 1
        jump choice3B

label gameover1:
    "Micah brings down the spear."
    #implement speedy credits here lol
    return
label choice3A:
    show micah normal
    "Micah stares at Mephi for a few moments, hesitating. Then he lowers his arm, turning away."
    "He can’t do it. He has no idea if that thought would be temporary, but for now. He’d let Mephi be." 
    "As he returns to preparing for slumber himself, he hears Mephi whisper in his sleep."
    me.c "Cute kitty..."
    "Maybe he wasn’t as dangerous as he seems."
    jump Ch1Scene3
label choice3B:
    "Micah is lost in thought for a moment as he gazes at the fiend, his heart doing a strange flutter as Mephi quietly giggled in his sleep." 
    "Less than an hour ago, his mind had considered defenestrating itself because of this man’s voice, why was his laugh…"
    me.c "Cute kitty..."
    show micah angry
    "Micah throws his spear to the floor. Despite the clatter, Mephi does not stir. Damn horned bastard, only a master trickster could charm him while sleeping."
    "Right now, he can’t do it. Maybe later..?"
    "It was only so Mephi didn’t realise his failed attempt on his life that Micah tucked his duvet back into place. Not because it was cold."
    jump Ch1Scene3

label Ch1Scene3:

    scene dream
    with Dissolve(1.0)
    "...?"
    "You find yourself in a surreal world. The sky looks like nothing you’ve ever seen before, bleeding rose and scarlet." 
    "The earth has been replaced by clouds much more stable than those above you, or at least you can gather that with a glance. Your feet aren’t on them but hovering, bleached of colour like the rest of you."
    "You""Is this Heaven?"
    "???""Not quite."
    show silhouette
    "There’s a silhouette of a man before you, or at least it seems to be a man. Certainly not human, there’s rays of light protruding from his back. None of his features are discernible, however."
    "You""Who are you? What happened to me?"
    "???""You’re asking that now, hm? Were you not wondering that when you were making decisions for someone else?"
    "..."
    "???""Do not be afraid. You haven’t done anything wrong… Yet. I’m the one who placed your soul within that nephilim. You’ve seen what a mess Micah is, yes?"

menu:
    "Mess is an understatement.":
        jump Choice4A
    "You put my soul inside an angel?":
        jump Choice4B
    "Make it quick, my patience is already fading":
        jump Choice4C
label Choice4A:
    "???""Perhaps I put it lightly. He's certainly not living angelically."
    jump Choice4_done
label Choice4B:
    "???""Don't panic, I shall explain."
    jump Choice4_done
label Choice4C:
    "???""Patience is certainly not your virtue, I see."
    jump Choice4_done
label Choice4_done:
    "???""You’re currently awaiting the afterlife, but a decision has not been made for you yet. So you have been assigned one final mission. Micah has strayed off the path, you have been tasked with guiding him back."

menu:
    "How am I meant to do that?":
        jump Choice5_done
    "What happens if I guide him further away?":
        jump Choice5A
    "I don't want to play this game.":
        jump Choice5B
label Choice5A:
    "???""Then you will ultimately join him in the same afterlife you lead him towards."
    jump Choice5_done
label Choice5B:
    "???""This isn’t a game, it’s an assignment. If you don’t follow, you’ll be left in Purgatory forever."
menu:
    "Fine, I'll play.":
        jump Choice5B_close
    "Then leave me in Purgatory, I’m not chaperoning a grown man.":
        jump gameover2
label Choice5B_close:
    "???""Good, then back to the briefing."
    jump Choice5_done
label gameover2:
    "???""Alright then, have fun in limbo."
    "Everything fades to black. The next thing you see is a flash of fire. Then a strange heaviness takes you over. More than anything, your spirit wants to sleep. It’ll be the last rest you’ll ever have."
    return

label Choice5_done:
    "???""You’ll be guiding Micah through aiding him in making decisions. That is, you’ll be his conscience. You’ve seen how impatient he can be, consider yourself his impulse control."
    "???""Think through his choices before he barrels in and gets himself deeper into sin. If you succeed, you’ll be rewarded with eternal light."
    "You""Should someone really be trusted with the ability to control someone else’s life?"
    "???""You probably won’t be dooming him more than he has already doomed himself, that isn’t to say though that you should be careless. This isn’t possession, you aren’t pushing him towards territory he would never approach himself." 
    "???""You are pushing him towards or away from his impulses. Try not to get him killed, you’ll join him after all."
    "You""I understand... But again, who are you?"
    "???""My identity isn't important. Focus on Micah."
    "..."
    "???""... I'll check on you every so often. Don't be too irresponsible."
    hide silhouette
    "You are now alone in this strange world. Not Heaven, not Hell, not Purgatory… Is this a dream?"
menu:
    "This is a lot of pressure... But I'll do my best.":
        return
    "I hate people who avoid questions...":
        return
    "... This is going to be so much fun.":
        return

    

