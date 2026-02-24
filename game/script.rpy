# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    #class for both the main and side romances, I don't think I need to differentiate here
    class Love_Interest:
        def __init__(self, character, name, love = 0, lust = 0, plat = 0):
            self.c = character
            self.name = name
            self.love = love
            self.lust = lust
            self.plat = plat

    #class for Micah, so everything is neat and tidy
    class Hero:
        def __init__(self, character, name, orientation, corruption = 0, redemption = 0, silver = 0):
            self.c = character
            self.name = name
            self.orientation = orientation
            self.corruption = corruption
            self.redemption = redemption
            self.silver = silver

    m = Hero(Character("Micah"), "Micah", "Open", 0, 0, 20)
    me = Love_Interest(Character("Mephi"), "Mephi", 0, 0, 0)
    c = Love_Interest(Character("Clover"), "Clover", 0, 0, 0)
    n = Love_Interest(Character("Nox"), "Nox", 0, 0, 0)
    l = Love_Interest(Character("Lux"), "Lux", 0, 0, 0)
    lu = Love_Interest(Character("Luminia"), "Luminia", 0, 0, 0)
    ca = Love_Interest(Character("Cal"), "Cal", 0, 0, 0)




screen debug_overlay():
    frame:
        align (0.98, 0.02)   # top-right corner
        background "#f00"
        padding (10, 10)

        vbox:
            text "Mephi Love: [me.love]"
            text "Mephi Platonic: [me.plat]"
            text "Mephi Lust: [me.lust]"
            text "Clover Love: [c.love]"
            text "Clover Platonic: [c.plat]"
            text "Clover Lust: [c.lust]"
            text "Micah's finances: [m.silver]"

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
    
    $ m = Hero(Character("Micah"), "Micah", "Open", 0, 0, 20)
    $ me = Love_Interest(Character("Mephi"), "Mephi", 0, 0, 0)
    $ c = Love_Interest(Character("Clover"), "Clover", 0, 0, 0)
    $ n = Love_Interest(Character("Nox"), "Nox", 0, 0, 0)
    $ l = Love_Interest(Character("Lux"), "Lux", 0, 0, 0)
    $ lu = Love_Interest(Character("Luminia"), "Luminia", 0, 0, 0)
    $ ca = Love_Interest(Character("Cal"), "Cal", 0, 0, 0)


    define narrator = Character(None, what_italic=True)
    default bribed_into_lust = False
    default Mephi_intimacy1 = False
    default Clover_marriage_awareness = False
    default Clover_optout = False

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
    $ m.silver += 20

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
        jump ch1_1a
    "Deny, a demon can’t be trusted with such a thing.":
        jump ch1_1b
    
label ch1_1a:
    "???""Ah, good, I didn’t ambush the poor guy."
    jump ch1_1done
    
label ch1_1b:
    "???""Come now, your spear perfectly matches the description."
    jump ch1_1done
    
label ch1_1done: 
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
        jump ch1_2a
    "“Thanks, but I’m not into guys. Now tell me about Nike.”":
        $ m.orientation = "straight"
        jump ch1_2b
    "“Cute, now shut up and tell me about Nike.”":
        jump ch1_2a
label ch1_2a:
    me.c "Snippy, aren’t you?"
    jump ch1_2done
label ch1_2b:
    show mephi disappointed
    me.c "Aww, what a shame. Never mind then."
    jump ch1_2done

label ch1_2done:
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

    if m.orientation == "Open":
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
        $ me.plat += 1
        jump ch1_3a
    "Cute… Wait, what?":
        $ me.love += 1
        jump ch1_3b

label gameover1:
    "Micah brings down the spear."
    #implement speedy credits here lol
    return
label ch1_3a:
    show micah normal
    "Micah stares at Mephi for a few moments, hesitating. Then he lowers his arm, turning away."
    "He can’t do it. He has no idea if that thought would be temporary, but for now. He’d let Mephi be." 
    "As he returns to preparing for slumber himself, he hears Mephi whisper in his sleep."
    me.c "Cute kitty..."
    "Maybe he wasn’t as dangerous as he seems."
    jump Ch1Scene3
label ch1_3b:
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
        jump ch1_4a
    "You put my soul inside an angel?":
        jump ch1_4b
    "Make it quick, my patience is already fading":
        jump ch1_4c
label ch1_4a:
    "???""Perhaps I put it lightly. He's certainly not living angelically."
    jump ch1_4done
label ch1_4b:
    "???""Don't panic, I shall explain."
    jump ch1_4done
label ch1_4c:
    "???""Patience is certainly not your virtue, I see."
    jump ch1_4done
label ch1_4done:
    "???""You’re currently awaiting the afterlife, but a decision has not been made for you yet. So you have been assigned one final mission. Micah has strayed off the path, you have been tasked with guiding him back."

menu:
    "How am I meant to do that?":
        jump ch1_5done
    "What happens if I guide him further away?":
        jump ch1_5a
    "I don't want to play this game.":
        jump ch1_5b
label ch1_5a:
    "???""Then you will ultimately join him in the same afterlife you lead him towards."
    jump ch1_5done
label ch1_5b:
    "???""This isn’t a game, it’s an assignment. If you don’t follow, you’ll be left in Purgatory forever."
menu:
    "Fine, I'll play.":
        jump ch1_5bdone
    "Then leave me in Purgatory, I’m not chaperoning a grown man.":
        jump gameover2
label ch1_5bdone:
    "???""Good, then back to the briefing."
    jump ch1_5done
label gameover2:
    "???""Alright then, have fun in limbo."
    "Everything fades to black. The next thing you see is a flash of fire. Then a strange heaviness takes you over. More than anything, your spirit wants to sleep. It’ll be the last rest you’ll ever have."
    return

label ch1_5done:
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
        jump Chapter2
    "I hate people who avoid questions...":
        jump Chapter2
    "... This is going to be so much fun.":
        jump Chapter2

label Chapter2:

    scene inn 
    with Dissolve(1.0)
    "It was the break of a new day."
    show Micah normal
    "Micah lights the fireplace, embracing its warmth as he prepares for… Whatever life will toss at him today, he supposes. The routine is never truly routine, not for a priest following his goddess’ whims."
    "He spares a glance at the sleeping fiend a few metres away. Fortunately, he had not been kept up by giggling all night. Not that it would have been the worst thing that ever happened to him staying with temporary companions."
    "A shiver creeps down his spine. He wasn’t sure which had been worse, the two in the other room being far too loud or the one {b}in{/b} the room trying to grope him after getting too intoxicated." 
    "Thank the goddess Mephi hadn’t tried the same. Yet."

    "Blank parchment is already set before him, just far enough away from the fireplace not to burst into flames while he thinks. How did he do this?"
    "His wife's letter to another is set out as though it'll give him inspiration, yet it's difficult to write a response to a letter he was never meant to get."
    "'Raze'. Their village was only small, yet he couldn't place a face to that name. Maybe it was a nickname, for some mystery man who had swept her off her feet. At least she could still feel that way for someone."
    m.c "I should be angry... Shouldn't I?"
    "He doesn't know why he spoke aloud, as though his roommate would chime in. No matter what he {b}should{/b} feel, he couldn't be protective of a love he hadn't felt in Goddess knows how long."
    "Micah knows he'll never get it done if he doesn't start, so he drafts the response. It's messy, rambling, yet there's only one part that matters anyway."
    "'I know about Raze. It's alright, move on. I'll see you and El soon.'"
    "He signs the scroll and furls it up before walking over to the window and opening it. With a whispered spell, a bird approaches, enchanted."
    m.c "Take this to Catarina of Herald, please."
    "It doesn't matter if the creature doesn't know its destination, the spell will guide it regardless. It clutches the scroll in its talons and takes flight."
    "As the bird disappears into the distance, something feels strange. Heavier. The shackles are off, yet without them he feels disoriented."
    "He needs another focus."
    "His mind wanders as he looks back at his inventory. His reserves were lower than desired, perhaps before they hit the road he could fix that. He was positive he had seen a pawnbroker shop yesterday…"
    "Micah pulls something out of his bag. A large silver ring. Maybe not a ring? It was big enough to fit around someone’s neck, ‘choker’ was probably more accurate." 
    "It was something he had found in a treasure chest that emitted evil, instantly identifiable as cursed with a quick spell."
    "Nothing too bad, he had tried it on a boar out of curiosity and all he had observed was a strange tendency to backflip. Impulses to try it on himself were not overpowered, but angelic heritage seemed to unfortunately make him immune to it."
    m.c "I wonder how much I could get for this..."
    "He retrieves a small knife and starts carving into the metal. At first glance, the symbols would look like runes. Hopefully whoever ran the shop would be dense enough to fall for it."
    "Last night’s dream hits you. It looked like Micah was planning to con some poor sucker. This {b}is{/b} the kind of thing that man wanted you to steer him away from, right?"
menu:
    "You try to sway him away from the crime.":
        jump ch2_1a
    "You egg him on.":
        jump ch2_1b
    "You wait to see what happens.":
        jump ch2_1done

label ch2_1a:
    "Your attempt does not work, prompting you to realise. This is a decision you have no say in, he is completely set on scamming whoever he met at the shop. What was the point of being his conscience?"
    "Then you understand. Your job is to cement the decisions he’s torn on. Not push him away from his true nature."
    jump ch2_1done
label ch2_1b:
    "He doesn’t need your encouragement, he is wholeheartedly set on his nature as an angelic conman."
    jump ch2_1done

label ch2_1done:
    "He places the cursed item back in his bag and straps it on before looking over at Mephi. His need for money outweighs his patience. Mephi would find him, he might as well have some fun with this."
    "Micah writes a note and puts it on the bedside table. Then he takes Mephi’s bag with him, leaving the inn."
    jump Ch2Scene2

label Ch2Scene2:
    scene shop
    with Dissolve(1.0)
    show Micah normal at slightleft
    show woman normal at slightright
    "The worker at the counter was a pretty woman around Micah’s age."
    "That fact was a little less important than the fact his scheme was not working so far."
    "Woman""Again sir, I don’t see why you think this item is so valuable."
    m.c"I've told you twice, this choker is blessed."
    "His act was clearly not enthusiastic enough, how tired she looked as she crossed her arms. He pushed some more authority into his voice as he continued to present the item."
    m.c "All one has to do is wear it and it’ll ward evil spirits away, don’t you understand how useful that is?"
    "Woman""It looks like a piece of scrap metal that a 5 year old drew on."
    "At the insult, he could feel heat flush his cheeks. Surely it was better than some kid his son’s age could do!" 
    "… Maybe he should have put some effort into blessing the item so it was actually worth something. But where was the fun in that?"
    m.c "Don’t insult the language of angels like that. These are runes of protection, don’t you know?"
    "The woman discerns it once more. Micah can sense she’s just a regular human, maybe she wouldn’t know the carving was just a little off."
    "Woman""Why would an angel place a protective spell on such a tacky piece of jewelry?"
    "He flinches. He had considered trying to subtly place such a thing if she continued being stubborn, but now his goodwill was fading."
    m.c "Don’t ask me, ask whoever put it in a cave full of monsters. … None of which were demons."
    "With that train of thought, he wonders initially if he imagined the hairs on the back of his neck standing up, or the strange chill until he sees the woman turning pale, peeking behind him." 
    "He clocks the aura before he does the same, as the bell on the door chimes."
    show Mephi menacing with moveinleft
    "Mephi’s acting was surely more convincing to her, the way she squealed as he barged in with his axe in hand. What on Earth was he thinking?"
    me.c "Give me all your money if you don’t want to get hurt!"
    show woman panicked
    "Woman""Eek, demon!"
    "Clearly this was some type of game, no demon would be stupid enough to seriously try to rob someone in front of an angel." 
    "The woman dives under the counter nonetheless, completely unaware as it clicks in Micah’s mind."
    "Was this his attempt at helping him?"
    "Shaking his head, Micah clasps the choker around his throat and casts a light spell."
    m.c "Begone, demon!"
    hide Mephi menacing with moveoutleft
    "Maybe it worked too well, Mephi yelping as he stumbled away, nearly bumping into the door frame in the process. Micah stares blankly at the axe on the floor. … Now he hoped Mephi didn’t try to kill him in his sleep tonight."
    m.c "Wow, it works even better than I thought. Are you alright, Miss?"
    "The woman’s head peeks out from the counter, her eyes teary as she gives a shaky nod."
    "Woman""Yeah, that was scary... I didn't even know demons could be purple."
    "Micah offers his hand and helps her to her feet. The hand that isn’t clasping his wipes her eyes."
    m.c "Well, now you know. Don't you know how to use a sword?"
    "Woman""No… Usually my coworker is here, but it was just me today. No one ever succeeds in robbing us because she stabs them to death."
    "Thank the goddess it was her here today then, or he would have to pay for the next inn stay himself."
    "Woman""I noticed what you did there, though. Your light spell repelled the demon, not your choker."
    "Micah is powerless but to bring his hand to his face as she giggles."
    "Woman""Hey, if you teach me how to use that spell, I’ll take the choker off your hands."
    m.c "I'll still get paid, right?"
    "Woman""I'll give you 15 silver pieces."
    show Micah smug 
    "Now he was back in the game. He feigns a frown, peeking back at the door then the windows in sight. No Mephi, he would have to deliver the axe himself."
    m.c "I did just save your life... 30 sounds fair."
    show woman playful
    "She snorts. It's like she never even shed a tear, her expression playful."
    "Woman""How about this, conman? 25 if you throw in a kiss too."
    "Bold woman. 10 extra silver pieces for a kiss..."

menu:
    "Alright, let's have some private time.":
        jump ch2_2a
    "... 15 is fine.":
        jump ch2_2b

label ch2_2a:
    $ bribed_into_lust = True
    "She giggles and pulls him in close. It had been a while since he indulged, seeing his relationship status but… If his wife wanted to move on, she wouldn’t mind if he did the same, right?"
    "It soon escalates beyond a kiss but with the rise in price, Micah doesn’t mind as she closes the shop early and leads him into the back for some ‘magic lessons’."
    "{b}Obtained 40 silver pieces!{/b}"
    $ m.silver += 40
    jump Ch2Scene3

label ch2_2b:
    "She takes the rejection well, eager to learn regardless. For the next half hour, he tutors her. Never before has he seen an adult woman so fascinated by a mere light spell."
    "{b}Obtained 20 silver pieces!{/b}"
    $ m.silver += 20
    jump Ch2Scene3

label Ch2Scene3:
    scene town
    with Dissolve(1.0)
    "Micah leaves the shop with a victorious smile, axe in one hand and stuffed pouch in the other. Mephi greeted him with a frown that was no doubt annoyed, however was not very effective when he was covered by odd specks of mud."
    "Did he fall into a puddle during his escape?"
    show Mephi annoyed at slightright
    show Micah smug at slightleft
    me.c "You look like you had fun. How much did you get for that little show?"

    if bribed_into_lust:
        m.c "I got 40 silver pieces."
        show Mephi startled
        me.c "Wha- How did you go from 25 to 40?!"
        "Micah hasn’t felt such confidence in a while, as he responds with a smirk."
        m.c "She {i}really{/i} liked me, use your imagination."
        "Though Mephi seems to be trying to pull a poker face, his lilac cheeks are flushed. That was what broke his composure, huh?"
        me.c "So, morning after your wife asks for a divorce, you sleep around. Talk about audacity. You didn’t share your bed with anyone else this year, did you?"
        "Micah shakes his head. Even if the distance had grown… A vow like that…"
        m.c "Plenty have tried, never succeeded though. Light flirting is fine, but my goddess would frown upon adultery."
        show Mephi annoyed
        "Mephi seems irritated as he retrieves his bag and axe."
        me.c "You’re still legally married, I doubt she’d approve of what you just did. Even without the scamming and stealing."
        show Micah annoyed
        m.c "And why do you care? You’re a demon, I thought you would love a little mischief."
        me.c "Mischief, yes. Stealing my stuff? No. And next time, warn me before you try to blind me with another light spell!"
        "For a moment they glare at each other then Micah groans, grabbing Mephi by the arm and tugging him away from the shop."
        m.c "It was only borrowing but fine, I’ll leave it alone next time. And I’ll try to avoid burning your eyes out in future too."
        "This relationship seemed like it would be one of mutual annoyance after all."
        jump Chapter3
    else:
        m.c "I got 20, turns out I’m a pretty good tutor. Try not to go back in there, you might get flashbanged again."
        me.c "If you’re that good at magic, then why don’t you use your skills to offer services more rather than scamming people with junk?"
        m.c "It’s pretty fun, but it doesn’t have the same thrill, you know? Making profit from turning useless scrap. I thought you demons were all about that kinda trade."
        me.c "I have a bit more honor than that, but it is amusing to watch, I’ll give you that. What isn’t so amusing is getting my stuff stolen. I doubt your goddess asked you to do that."
        show Micah annoyed
        m.c "I didn’t steal your stuff, I borrowed it. Your stock is all in one place, don’t worry. I just didn’t want to waste time returning to the inn."
        me.c "And next time don't try to blind me!"
        "They glare at each other for a moment. Then Micah grabs Mephi by the arm and drags him away."
        m.c "Alright, next time. Come on, let's get out of here."
        "Who was annoying who in this relationship?"
        jump Chapter3
label Chapter3:
    scene town
    with Dissolve(1.0)

    "The walk through the town plaza was awkward."
    "Micah was acutely aware that Mephi was sneaking silent glances at him, expression still irritated as he clutched the strap of his bag tight. Perhaps the best thing to do would be to let the silence last for now."
    "He takes out a scroll for a request he had snatched off a public quest board. That board had been overflowing, ranging from little things like potion ingredients to slaying monsters just outside the town. What percentage of the town knew how to fight?"
    "This particular quest was about howling. A nearby cave making strange noises, a 50 silver piece reward for investigating. Along with a ‘surprise’ gift. That sounded ominous." 
    "Hopefully whatever would be awaiting them wouldn’t require that reward to be used as medical fees… That was assuming he couldn't heal them, of course..."
    show Micah normal at slightleft
    show Mephi tense at slightright
    m.c "Oi, Mephi."
    "Mephi turns rigid. How startled he looks, all of a sudden."
    me.c "Y-Yeah?"
    "They were going to be together for a while, he might as well see if Mephi could even carry his own weight."
    m.c "What are you, exactly? Trade-wise, I mean. You’re dressed quite lightly for an average adventurer."
    show Mephi smug
    "He composes himself, back to his usual smug self for a moment. His voice is a purr, remarkably tranquil for what he’s about to say."
    me.c "Oh, me? I'm a mage in the school of Necromancy."
    show Micah discomfort
    "Great, Micah has found himself travelling with an insane person."
    m.c "Ah. Of course. Of course a demon has the power to resurrect the dead."
    "Mephi laughs, his tail flicking playfully."
    me.c "Don’t look so worried, angel. I do more than that. If we ever come across any zombies, I’m able to send them back to the underworld. Now how about we talk about you?"
    m.c "What do you wish to know about me?"
    if bribed_into_lust and m.orientation == "Open":
        me.c "I want to talk about that little stunt you pulled with the pawnbroker. I’ve never seen an angel prostitute himself, after all. How much would I need?"
        "Micah stares at him, stupified for a moment. Did he just imagine it, or is this demon trying to {b}buy{/b} him?"
        menu: 
            "Considering I don't consort with demons, you'll need a hell of a lot":
                jump ch3_1a
            "How about you try me later?":
                jump ch3_1b
            "No amount of money is going to make me sleep with you.":
                jump ch3_1c
        label ch3_1a:
            $ Mephi_intimacy1 = True
            m.c "Also, that wasn't prostituting myself, that was simply using my body to get what I want."
            me.c "So, prostitution."
            jump ch3_1done
        label ch3_1b:
            $ Mephi_intimacy1 = True
            $ me.lust += 1
            show Mephi flustered
            "For a brief second, Mephi looks stunned, flustered. Then he composes himself, albeit that does not stop the blushing."
            show Mephi smug
            me.c "I might have to hold you to that~"
            m.c "As long as you don’t call it prostitution, alright? I simply used my body to get what I wanted."
            me.c "However you want to dress it, that's still prostitution."
            jump ch3_1done
        label ch3_1c:
            me.c "I'm really not your type, am I? Ah well."
            m.c "Besides that… I wasn’t ‘prostituting’ myself. I simply knew how to get what I wanted."
            me.c "You traded sex for money, that's prostitution."
            jump ch3_1done
    else:
        me.c "I want to know how an angel gets so distracted by a ‘holy mission’ that he neglects his family for a whole year."
        m.c "I thought you said you weren't interested in that."
        me.c "I wasn’t interested in your excuses when I was trying to do my job, now we’re travelling together I might as well learn more. Was it not a pleasant marriage?"
        "Thinking about it fills Micah with tense dread. Dread he surely should be free of now, but…"
        m.c "I’m not comfortable talking about this. Not with some guy I barely know."
        me.c "We'll be knowing each other more, what's the harm?"
        jump ch3_1done
label ch3_1done:
    "Micah was about to argue when they heard a man yell."
    "Man" "Get back here, you thieving bitch!"
    "Turning around, they see a middle-aged man chasing after someone dressed in a cloak, hood shielding their identity."
    show Mephi serious
    show Micah normal
    me.c "How suspicious."
    "Micah draws his spear, ready to strike. However, something seems to strike the man first, prompting him to collapse to the dirt."
    "Not even a twitch left him. Did the thief stab him?"
    "He sticks out his foot as the thief tries to dart past, a feminine squeal leaving them as they topple over."
    m.c "That was easy."
    "She tries to get to her feet again and he spears her cloak, tearing it away. The hood hangs on by a scrap, falling back to reveal her face. Her flustered, baffled face."
    show Clover angry
    "Girl" "What's the big deal?! Can't a girl steal some apples in peace?!"
    "No such things were in sight, something that clearly bemuses Mephi as Micah scans over the girl, pondering {b}where{/b} she would hide such a thing."
    "She doesn't seem to have any bulging pockets, nor does the cloak now muddied by the cold ground."
    me.c "I think you lost them along with your mind, little miss."
    "Where would a woman without pockets hide anything? It clicks in Micah’s mind, you feel a strange sense of hesitation as he lingers on the thought however it doesn’t last long."
    "Without any input from yourself, he fluidly sweeps the girl up and over his shoulder as she shrieks. Two apples fall out from her shirt."
    me.c "Oh, there they are."
    "Unaffected by the thief thrashing on his back, Micah cautiously approaches the man and crouches down. Snoring. Maybe it wasn’t a stab wound after all."
    m.c "Did you seriously go to all that trouble just for a couple apples?"
    "Girl" "Of course not, I stole a Twinkie too!"
    "Micah wracks his brain. Was that some kind of magic item? No, someone selling apples for a living probably wouldn’t dabble in that kind of trade… Some kind of fruit, perhaps?"
    m.c "What the hell is a twinkie?"
    me.c "I don't know, do I look like I speak 'crazy girl'?"
    "Micah cannot see the woman's face, but he assumes from her voice that she is pouting."
    "Girl" "What are you, some uncultured woman hater? What kind of moron doesn't know what a Twinkie is?"
    "Talking to someone dangling from his shoulder was no way to have a conversation. How did he treat a thief, however?"
menu:
    "Place the girl back down. “Explain.”":
        jump ch3_2a
    "Put her back down. “Alright, then how about you educate me?”":
        jump ch3_2b
    "Throw her to the ground and point his spear at her. “Explain yourself right now.”":
        jump ch3_2c
label ch3_2a:
    show Clover normal
    "She brushes herself off, pulling the rest of her torn hood away."
    "Girl" "A Twinkie is a type of cake filled with cream. Have you really never heard of one before? They’re very tasty."
    show Clover flirty
    show Micah flustered
    "She winks at Micah, an odd heat consumes him all of a sudden. It is strong, almost unnatural, and his spear suddenly feels too heavy to hold even lightly."
    "Girl" "You look pretty tasty too, angel."
    "Never mind that she knew what he was, he could sense she was the opposite. So why did that make her seem almost {b}alluring{/b}?"
    m.c "H-Hey, hold on!"
    jump ch3_2done
label ch3_2b:
    $ c.plat += 1
    show Clover happy
    "Engaging with her interests seems to make her cheer up a bit, a grin on her face as she happily does so."
    "Girl" "A Twinkie is a very tasty cake filled with cream, you should try one someday!"
    show Clover flirty
    show Micah flustered
    "That cheerfulness takes on a… Different… Tune. She winks at him and it seems to be all it takes for a strange heat to possess him. It’s dizzying, intense, yet somehow both addictive and comforting."
    "Girl" "And maybe you can try me too, angel."
    "She knew what he was. No, that wasn’t important. What seemed more important was the fact he could sense she was just the opposite and for a brief moment, it was captivating."
    m.c "W-Wha-"
    jump ch3_2done
label ch3_2c:
    show Clover discomfort
    "Despite the force of his action, she doesn’t seem truly upset, maybe only a bit disoriented as she stares up at him."
    "Girl" "A Twinkie is a tasty little cake filled with cream. Man, are you overreacting..."
    show Clover flirty
    show Micah flustered
    "She winks at him and he drops the spear, heat flooding his senses and zapping his strength. What the-"
    "Girl" "Not that I mind, angels are pretty hot when they're angry."
    "All Micah can do for a moment is stare at her as that fire continues to devour him. Never mind that she knew what he was, why was he sensing something evil from her and why did it make her seem {b}sexy{/b}?"
    m.c "S-Shut up!"
    jump ch3_2done

label ch3_2done:
    if bribed_into_lust:
        show Mephi irritated
        me.c "Can you please stop flirting with my travelling companion? I don’t think I can take seeing him with his tongue down a random girl’s throat again."
        jump Ch3Scene1Part2
    else:
        show Mephi irritated
        me.c "Can you please stop flirting with my travelling companion? We have places to go."
        jump Ch3Scene1Part2
label Ch3Scene1Part2:
    show Clover flirty
    "She winks at Mephi. Micah is too snared to tell but it seems to click for you at the same time Mephi realises. Her eyes are glowing ever so faintly. A charm spell."
    "Girl" "Lonely? Maybe we could make it a threeway."
    show Clover pained 
    "Mephi bashes her over the head with his axe’s handle, knocking her down as she cradles herself, whining. With the return swing he catches Micah’s shoulder, the armour absorbing the shock as he snaps out of his flustered state."
    show Micah normal
    me.c "Get a grip, Micah. You're getting all horny over a fucking succubus."
    "Micah stares at the sniffling, pained woman. No more heat, no confusing allure, just a hollow realisation of what he had fallen for."
    m.c "I thought I sensed something dark about her..."
    "Then he huffs, a more natural heat taking him over in the form of embarrassment."
    m.c "Hey, I wasn't getting 'horny' over her!"
    "Girl" "Could have fooled me!"
menu:
    "Glare at her":
        jump ch3_3a
    "Kick her":
        jump ch3_3b
label ch3_3a:
    "Girl" "Alright, sorry! I'll lay off the tricks!"
    jump ch3_3done
label ch3_3b:
    "She starts crying."
    "Girl" "Sorry, sorry, sorry! I won't do it again!"
    jump ch3_3done
label ch3_3done:
    "Micah and Mephi share a sigh of relief before both tensing as they sense something behind them. Nope, it wasn’t imaginary, the townspeople in the plaza were now glaring at them."
    me.c "Why are they looking at us like that?"
    "The succubus whines from where she's curled up, still holding her head."
    "Girl" "Because you're picking on a helpless girl?"
    m.c "Helpless? You weren’t so helpless when you were robbing that man, were you? You’re coming with us."
    "Girl" "C-Coming where?"
    "Micah daydreams about coins."
    m.c "I wonder how much the police will give us for hauling you in."
    "Girl" "Oh come on, it was two apples and a Twinkie! If you two buffoons knew how good they tasted, you’d be doing it too!"
    "She squeals as Micah lifts her over his shoulder once more."
    "Doing their best to ignore the continued glares from the observers, Micah and Mephi leave the plaza with their new hostage."
    jump Ch3Scene2

label Ch3Scene2:
    scene station
    with Dissolve(1.0)

    "The station was quiet. Micah noticed the few officers there looked half-asleep, giving them little more than confused tired glances as they watched them approach the counter before returning to doing nothing." 
    "Apparently the sight of a man hauling a woman over his shoulder wasn’t that alarming."
    show Micah exhausted at slightleft
    show Mephi normal at left
    show Clover angry at slightright
    show Marie normal at right
    "The officer at the counter looked up at them as they greeted her, blinking in an exhausted manner."
    "Woman" "Hello sirs, how can I help..."
    show Marie exhausted
    "Her voice trailed off into stunned silence as she clocked the flailing hostage then sighed. The succubus stopped thrashing and gave a nervous giggle with a mumbled greeting."
    "Woman" "Oh for God's sake Clover, what did you do this time?"
    me.c "She stole from a shopkeeper and tried to seduce my friend."
    "Micah wishes he could object, yet it doesn’t seem like an argument he can win. Instead he sighs and places Clover down."
    m.c "Is she a repeat offender?"
    "Woman" "She’s won the prize for most petty theft since she was a child, yes."
    "The officer glares at Clover. Clover shrinks, looking down at her tattered boots."
    "Woman" "You’re an adult, little miss, you can’t keep getting into trouble like this!"
    c.c "It was a Twinkie and two apples!"
    "The officer's voice turns monotone, her expression one of true apathy."
    "Woman" "Twinkies don't exist and a minor crime is still illegal."
    "What {b}are{/b} they watching?"
    "Clover puffs out her tiny chest as she crosses her arms."
    c.c "Sorry but they were practically begging to be taken, no one else was buying them! And Twinkies {b}do{/b} exist! I bribed you with one yesterday, Marie!"
    "Marie" "You mean you {i}failed{/i} to bribe me, Clover. That was a cream cake, no one besides you calls them Twinkies."
    c.c "Then they should start doing it!"
    "Marie shakes her head, giving Micah and Mephi a tired smile."
    "Marie" "I’m sorry about her, we’ve been trying to give her interventions for her kleptomania but as you see, it never works."
    "She pauses, looking Micah over. Her gaze feels like a knife, stabbing him with a strange dread. She seems awfully interested in the crosses on his armour."
    "Marie" "Wait, are you a priest?"
    show Micah discomfort
    "His stomach unsettles but he nods anyway. Being incognito would be impossible with this armour."
    m.c "Yeah, I work for Athena."
    show Marie cheerful
    "Mephi looks at him curiously. It is second to the way Marie’s grin freakishly widens, however."
    "Marie" "Marie” “I can’t say I follow her myself, but I know her teachings. She’s one of the most lawful gods, yes? So I assume you’re as well versed in justice as us officers, sir?"
    show Clover discomfort
    "He had a terrible feeling about this."
menu: 
    "Of course! I am one of her most loyal servants, after all!":
        jump ch3_4a
    "As well versed as the law itself? That's an exaggeration.":
        jump ch3_4b
    "It's kinda hard when I'm travelling with a demon, but sure.":
        jump ch3_4c
label ch3_4a:
    "Marie's expression is one of full confidence, Clover clocks it and goes pale."
    c.c "Oh hell no, please..."
    "Marie" "Great! With that in mind..."
    jump ch3_4done
label ch3_4b:
    "Marie" "Law enforcement, the church, we all share an important role in justice. So if you’re up to it…"
    "Clover spies Marie’s confident grin. It is enough for her to shiver and whisper under her breath."
    c.c "Oh hell no..."
    jump ch3_4done
label ch3_4c:
    show Mephi irritated
    "Marie giggles, such a statement was obviously redundant when Mephi’s appearance just {b}projected{/b} his demon heritage. Instead it’s a joke Micah gets a glare from him for. It seemed to be faux. … At least he hoped it was."
    "Marie" "You seem to have him tamed, I'm not worried."
    "Mephi's eye twitches."
    "Marie" "So, with that said..."
    "Clover catches the glint in Marie's eyes and pales."
    c.c "Oh please god, no."
    jump ch3_4done
label ch3_4done:
    "Marie smiles sweetly."
    "Marie" "So, could you please help Clover find the path of justice too?"
    show Micah startled
    show Mephi startled
    "If Micah’s jaw was any more slack, it would be on the floor. Clearly the sentiment is the same for Mephi. Clover just squeals."
    c.c "Marie, no! He's an angel, he'll smite me if I fall even an inch out of line!"
    "Marie" "That's why I know you'll behave."
    "Marie continues to look at Micah with that saccharine smile. What kind of naive woman entrusted two male strangers with a possibly even more naive woman?! A thought crosses his mind." 
    "Maybe Clover was just that unbearable that Marie was willing to risk it. Why should he agree to this?"
    "Marie" "I'll pay you 75 silver pieces for training her."
    show Micah normal
    m.c "Make it 85 and we have a deal."
    "Clover gawks at him, her voice cracking. The amount she’s been yelping, he’s rather surprised she still has it."
    c.c "You have got to be kidding!"
    show Mephi smug
    me.c "Oh wow, this angel is so easily bribed. Well, I won’t complain about another demon in the team. If you behave yourself, that is."
    "Marie clasps her hands victoriously."
    "Marie" "I'll up it to 100 if she returns a perfectly disciplined young lady, hm?"
    "Oh, this poor woman made such a bad decision. But perhaps Clover realised she made the worst one in getting herself into this mess as she squeals once more."
    c.c "Don't I get any say in this at all?!"
    jump Chapter4

label Chapter4:
    scene bathhouse
    "Clover had been rowdy until they had offered to take her to the bathhouse."
    "With the sheer extortion they had been struck with upon arrival, Micah quickly understood {b}why{/b} Clover hadn’t had a hot bath in months, but at the very least Mephi was paying."
    "Having this demon around may not be such a bad thing."
    show Micah neutral-bathing at left
    show Mephi amused-bathing at slightright
    me.c "I still can't believe you agreed to this. For an angel, you're so easily tempted."
    "Micah watches as Mephi submerges himself deeper into the steaming water until only his head is poking out. A thought crosses his mind of whether demons could breathe underwater, one he swiftly dismisses." 
    "They’re surrounded by other men, even if they’re keeping their distance. It would not stay that way if his curiosity got the better of him."
    m.c "Don’t act like you aren’t tempted to, 100 silver is a hell of a lot. I could buy new armour and upgrade my spear with that, and still have enough to afford an inn for a week."
    "A thought crosses his mind, whether he could flat up buy a new spear and dual wield. No, that sounds like a way to get himself killed… Maybe just a shorter spear for an easier time in close combat…"
    show Mephi curious-bathing
    "Micah feels staring as he idly rinses the rest of the dirt out of his hair. Mephi’s gaze is {b}creeping{/b} down his back."
    me.c "Speaking of armour... How do you still get scars like these?"
    show Micah discomfort-bathing
    "It isn’t just his gaze that trails down now but a curious claw that sends freezing cold running down as his muscles turn rigid. Before he can completely restrain himself, his wings manifest and swat Mephi away."
    m.c "Don't touch me!"
    "Others are staring. The freezing sensation is replaced by fire and he checks his wings over. They weren’t material, their only presence in the form of their magic disturbing the water. He hushes his voice."
    m.c "I didn't wear my armour all the time, alright? Some of those are years old."
    "Those disapproving glances vanish. It was only his voice that had disturbed the peace, apparently. Of course no one else would notice, only Mephi - the bastard devil - detects his holy magic before he reaches out." 
    "Micah feels his hand on his wing, biting back a breath and then releasing it slowly before his wing slaps him away and withdraws back into his body."
    m.c "If you don't want me to kill you in your sleep, don't touch me again."
    "Before either of them can make another scene, he pulls himself out of the water and wraps a towel around his waist. Mephi creates a splash as he too scrambles out of the water to follow him."
    me.c "H-Hey, wait for me!"
    jump Ch4Scene2

label Ch4Scene2:
    scene lobby
    show Micah irritated-unarmoured at left
    show Mephi discomfort at right
    show Clover cheerful
    "Clover is already waiting for them by the time they get dressed and return to the lobby. For a moment she seems completely in her own world, sitting on a bench eating an apple she had stolen from Goddess knows where." 
    "She looks far more cheerful than earlier, practically bouncing up as she greets them."
    c.c "That felt so good! How was it for you two?"
    show Clover confused
    "Her expression turns bemused as she cocks her head to the side, her gaze jumping the short distance between them a few times."
    c.c "Uh... I take it that it {i}wasn't{/i} great."
    me.c "I think I pissed him off. I didn't even mean it this time."
    "Micah blanks the words, they feel acted. What feels more authentic is Clover’s curiosity as he feels her scan him up. It doesn’t feel quite uncomfortable, but not completely welcoming either."
    c.c "I see... Hey angel boy, you're a lot less bulky under that armour than I thought you were!"
    m.c "My armour isn’t that bulky, is it? It was lighter than most of my options. I’m surprised you’re still here, actually."
    "Clover giggles and twirls her still damp hair."
    c.c "I was considering ditching, but this little road trip might be good for {i}something{/i}. I could never survive outside of town on my own, after all."
    show Clover wink
    "Plus it gets boring when everyone else my age leaves. Being around two cute guys can't be too horrible right?"
    show Micah neutral-unarmoured
    "Micah feels a strange warmth. But what is it?"
menu:
    "Being around this woman is making him flustered. “I-I'm going to get our gear.”":
        $ c.love += 1
        jump ch4_1done
    "Was she trying to charm him? No, this feels more like… Fondness… “I’m going to get our gear.”":
        $ c.plat += 1
        jump ch4_1done
    "This succubus is irritating. “I’ll be right back.”":
        jump ch4_1done

label ch4_1done:
    hide Clover
    hide Mephi
    "Micah excuses himself, contemplating their next move. Their equipment wasn’t the only thing on his mind. On the way to the bathhouse, he had shared the request he had swiped off the board." 
    "A curious howling with an easy reward seems like the best way to determine whether his new companions were going to be any good… Besides the financial boons, that is. The only question was why such a simple request was {b}still{/b} on the board."
    "He vaguely registers that Mephi is lecturing Clover about something already. Only parts of it are even reaching his ears, but Mephi didn’t seem too appreciative of Clover’s casual flirtation. No, others’ inclinations mean nothing to him. He has to focus."
    show Man at right
    m.c "Excuse me, can we please have our gear back?"
    "The man behind the counter returns their items swiftly but not hastily. Micah observes the silence and retrieves the scroll from his bag."
    m.c "Thank you. May I ask you a few questions about this quest, if you have the time?"
    "He squints and takes a moment to stare at the scroll. For a minute, Micah ponders whether the man is illiterate before he responds."
    "Man" "Ah, the howling. Yeah, I have the time. That bloody thing's been scaring away the night time customers, after all."
    m.c "How long has this been happening?"
    "Man" "About a week... Our law enforcement hasn’t had much luck investigating it, the cave’s full of lesser demons. All the officers sent there have been…"
    "He makes a cut-throat motion."
    m.c "That's promising. Has anything been leaving the cave?"
    "Man" "No, whatever's in there is quite content on staying there. Can't talk any sense into the cowards of this town, however..."
    hide Man
    show Micah neutral
    show Mephi amused at right
    show Clover annoyed
    "After a polite exchange of farewells, Micah straps his armour back on then returns to Clover and Mephi. His brow raises as he clocks Clover now seems irritated. What had Mephi been doing?"
    m.c "What were you two on about?"
    me.c "Nothing for you to worry your pretty head about. What about you? You seemed pretty chatty then."
    m.c "I asked the worker about our quest. Apparently that howling’s been going for a week and no one has been able to check it out because devils keep ripping them apart."
    show Clover scared
    "Mephi grimaces for a few seconds as Clover pales, wide-eyed."
    me.c "Lovely. Well, it'll be fun ripping them apart in turn."
    "Mephi takes his axe with a grin, absolutely brimming with confidence as Clover’s attention jumps between them. She’s shaking a little."
    c.c "H-Hey, isn't this kinda dangerous? Sounds like the police should be dealing with this, not people taking apples."
    m.c "They've died. They died. Besides seduction magic, what exactly can you do to defend yourself?"
    c.c "I’m not bad with a bow, but Marie took mine off me because I kept ‘abusing’ people with it. Can I just wait at an inn until you return?"
    me.c "I don’t know how strong Micah is, but I’ll get us through this in one piece. Besides, we’re both healers. So there’s not much to worry about."
    "Ah, so Mephi could do more than just cure the dead. That doesn’t seem very reassuring to Clover however. Micah ponders how to bribe her."
    m.c "Alright, how about this? If you help us through this quest, we'll give you anything within reason."
    "He knows as soon as those words leave his mouth that they’re a bad idea, Mephi’s sharp stare only cements it further, however Clover seems a lot more enthusiastic now as she nods eagerly."
    c.c "I'm holding you to that!"
    jump Ch4Scene3

label Ch4Scene3: 
    scene cave
    show Micah neutral at left
    "The entrance was free of monsters. An iron-like scent lingered in the air, no immediate source discernible. Instead he pulls a face at the plucked clean, decaying bones in the corner."
    m.c "It's safe to come in."
    show Mephi neutral at right
    show Clover discomfort
    "His companions trail in behind him, their footsteps echoing gently. Micah can pinpoint the moment they spot the bones, Clover growing pale as Mephi snorts."
    me.c "Well, they’ve been there a while."
    c.c "A-Are you sure it’s safe?!"
    m.c "It’s as safe as it’s gonna get. I don’t think we’ll be able to get the jump on these monsters, but at least they won’t be creeping up behind us."
    "Clover looks around again, shaking."
    c.c "What’s the reward again, anyway? Is it really worth endangering ourselves like this?"
    me.c "Hey, this is how others your age get by, hm? This is an ‘honest’ living."
    "Micah stares at Mephi for a moment. Well, Clover certainly wasn’t used to that… Huh, ‘your age’? He decides to save the question for later."
    m.c "Our reward is 50 silver, four healing potions and a ‘fire magic amplifier’."
    c.c "I’ve never seen one of those before… How are we going to split that, though? I don’t think 50 and four split into three."
    m.c "We can work that out when we’re done here. We might find more treasure to throw in the pot."
    "Micah spies an odd blue glow down the tunnel. He grips his spear tight. That could be dangerous to just barrel towards as the three of them."
    m.c "Mephi, what’s your white magic level?"
    me.c "I’m at level 4, why do you ask?"
    show Mephi surprise
    "Micah starts shoving Mephi towards the tunnel, immediately meeting futile resistance. Huh, he had never heard a grown man squeal before."
    m.c "I’m a level 5, I can patch you up if you get injured scouting for us."
    me.c "What- Do I look like a scapegoat to you?!"
    m.c "You do have goat horns."
    me.c "They’re ram horns!"
    "Clover watches them, looking a bit too confused to be truly judgemental."
    c.c "He’s not using you as a scapegoat, Mephi, he’s using you as bait."
    me.c "Not helping!"
    "Micah swiftly blocks the swing of his axe with his spear. Mephi’s purple skin is flushed a deeper violet."
    show Mephi angry
    me.c "Fine, I’ll do it, but I’m taking 50%% of the treasure we find!"
    "Micah bows, plastering on a smile he knows is sarcastic."
    m.c "Thank you for your sacrifice, Mephi."
    me.c "Oh fuck off!"
    hide Mephi
    "Mephi scrambles down the tunnel before he can lose any more dignity. Clover watches after him open mouthed then looks at Micah."
    c.c "Are you sure he’s going to be alright by himself?"
    "Micah shrugs, cranking his shoulder."
    m.c "He looks fragile, but I sense something powerful about him. Don’t you, Clover? You’re both demons."
    c.c "I sense something about him, but I don’t think I want to know…"
    "She lets out a shaky sigh, hugging herself."
    c.c "So… We’re just waiting for him to come back, then." 
    m.c "I guess we are."
    "A silence breaks out, various thoughts linger in Micah’s mind as he peers at Clover. Her eyes are set on the tunnel. With the speed Mephi had left, his scouting wouldn’t take that long." 
    "Maybe he should get to know Clover. There were a lot of questions."

    menu:
        "Why did you never leave the town?":
            jump ch4_2a
        "Did it feel lonely being by yourself all the time?":
            jump ch4_2b
        "Were you seriously flirting with me earlier?":
            jump ch4_2c
    
    label ch4_2a:
        $ c.plat += 1
        show Clover cheerful
        c.c "Oh, do you want to know more about me?"
        "She giggles, swaying on the spot. However, there’s something odd about that giggle."
        c.c "I did leave the town sometimes, but I never went very far. I always liked to play in the forest surrounding our area, but I guess I always thought it’d be a little too scary to go any further."
        m.c "You mean because of the monsters?"
        c.c "Not really, it’s because I don’t know what it’s like. I lived here all my life, not many people want to stick around but… It’s home. I know where everything is. I can guess what people are going to do, you know? New things are just kinda scary." 
        "Her eyes return to the ominous blue light. Her teeth dig into her bottom lip, somehow it feels like he can see what’s on her mind before she speaks it."
        c.c "What about you? Did it scare you to leave home?"
        "He shakes his head. It’s not something he talks about often but… He doesn’t mind." 
        m.c "Not really, I think I was always eager to get out of there. I never liked to stay in one place for long. It feels… Itchy if that makes sense?" 
        "She gazes at him then muffles another, more authentic laugh."
        c.c "I-I get it. You feel restless. Did you not want to settle down?" 
        "His palms start to feel clammy. Did he want to have this conversation with her already?"

        menu:
            "I already did. It didn't work out.":
                jump ch4_2a_1
            "I'm not comfortable talking about that.":
                jump ch4_2a_2
        label ch4_2a_1:
            $ Clover_marriage_awareness = True
            c.c "What do you mean by that?"
            m.c "I tried the whole marriage thing. I… I have a son too. That’s why I’m with Mephi. He’s escorting me back home." 
            c.c "O-Oh… Did you not get along with your…" 
            "She trails off, waiting for him to clarify."
            m.c "No, she was a wonderful woman. I just lost interest, I guess. We were pretty young when we got together. I suppose it was bound to happen."
            "He rubs his neck sheepishly." 
            m.c "We are still legally married until we both sign off. But we’ve both agreed to move on." 
            c.c "That’s good to know. I don’t feel good interfering." 
            "Micah isn’t oblivious to what she’s getting at, but he decides to leave that implication for later, listening out for Mephi’s return." 
            jump ch4_2done
        label ch4_2a_2:
            c.c "It’s alright, you don’t have to tell me if you don’t want to. … I wonder how long it’ll be until we hear screaming."
            jump ch4_2done
    label ch4_2b:
        c.c "Where did this come from?"
        m.c "I was just thinking. You come from a small town, everyone else your age is going on adventures. I don’t know if anyone else was hanging around with you."
        "Clover giggles, but it feels forced. The tapping of her boots echoes as she shuffles on the spot."
        c.c "You’re right about that. Either you become a boring shopkeeper, a career criminal or you leave with a sword and shield. I see Marie more than I do anyone else."
        "She sighs."
        c.c "And uh… I guess I won’t be seeing her for a while now either. Seeing as she sold me to you." 
        "Micah rubs his neck, there seems to be a lump in his throat." 
        m.c "L-Look, you’re not a slave. I just want a quick buck, you know? I can’t ‘train’ you like she asked me to."
        "Clover stares at him, tilting her head. Her cheeks are faintly flushed. Were her eyes red before?"
        c.c "You- You lied? Then what am I doing here?"
        m.c "Just pretend to be a ‘perfect lady’ when we bring you back until we leave. I don’t really give a shit about being a real role model."
        "Clover is quiet for a moment again. Then she starts laughing."
        m.c "... What’s so funny?"
        c.c "Y-You’re an angel, wh-why are you like this?" 
        m.c "I’m half-angel, I still have some humanity, you know? I don’t just play the harp and fight demons… A man has needs."
        c.c "And yours are ‘money’."
        "Clover’s gaze turns to the tunnel. There’s nothing coming from it yet. The monsters must not have gotten to Mephi yet. As Micah debates how to continue the conversation, Clover clears her throat." 
        c.c "Enough about… Whatever mess I’ve ended up in. We’re going to be together for a while, aren’t we? So can you tell me a bit about yourself?"
        "It isn’t that he dislikes talking about himself.. The question was where to start. Micah scans her over." 
        menu:
            "Maybe he was a little interested in her. “I’m going through a divorce right now.”":
                jump ch4_2b_1
            "He wasn’t sure what he was feeling. “I come from a small town like yours.”":
                jump ch4_2b_2
        label ch4_2b_1:
            $ c.love += 1
            $ Clover_marriage_awareness = True
            c.c "Eh? You’re married, Micah?"
            m.c "Not for much longer, but yes. I thought I should let you know where we’re going. Mephi’s escorting me back home to sort out the legal business."
            "Clover’s expression twists into confusion as she looks down the tunnel again."
            c.c "You two aren’t…"
            m.c "No, he’s just my guide." 
            "His fingers drum against the handle of his spear. How did he put this?"
            m.c "We married because we had a son. She- She was a wonderful woman. But I think I lost interest in her a long time ago. She’s moved on, too. We’re just going to make it official." 
            "Clover gazes at him for a few silent seconds then exhales. That smile of hers seems anxious, yet genuine." 
            c.c "Well, thanks for telling me. I guess I’m coming with you too, then." 
            "There’s a strange tightness in his chest. He guessed she might be right, Marie never gave them a deadline. … But what was he doing when they finally got home?" 
            "He doesn’t want to deal with the discomfort right now, instead listening out for Mephi."
            jump ch4_2done
        label ch4_2b_2:
            c.c "Oh, do you come from a boring town too? I guess you couldn’t wait to escape."
            m.c "You’d be right about that. It’s popular with visitors but well… Once you’ve seen everything once or twice, you want to see something new. I always wanted to get out and see outside my home. I guess now you’ll be seeing everything new for the first time too." 
            "Clover giggles, playing with her hair."
            c.c "Yeah, I never ventured far because… It was just all new and scary. But I’ll be safe with you two." 
            "He wasn’t sure yet if Mephi was safe to be with. He listens out to see if he’s proven right or wrong."
            jump ch4_2done
    label ch4_2c:
        "Clover giggles, it sounds a little breathless as she holds herself." 
        c.c "Maybe I was serious, maybe I wasn't. I'm not sure I'm even doing the right thing, we're going to be travelling together a while. It might make it… Awkward." 
        m.c "Awkward how?"
        "She holds his gaze then subtly looks down. Micah stares at her for a few seconds. Then his face starts to feel hot." 
        menu: 
            "Do you like what you see?":
                jump ch4_2c_1
            "Hey, at least take me to dinner first.":
                jump ch4_2c_2
            "... Please don't get any ideas, I'm not interested.":
                jump ch4_2c_3
        label ch4_2c_1:
            $ c.lust += 1
            show Clover wink
            c.c "I do, yeah. It's not often I'm alone with a cute guy like this." 
            m.c "You're a succubus, though." 
            c.c "Hey, that doesn't mean anything!" 
            "Despite her voice raising in volume, her laugh is playful, her smile coy." 
            c.c "I'm not a full blooded succubus, I don't need to flirt as a job. … Besides, nearly everyone my age has left the village, anyway. It's been months since I've seen a new face." 
            m.c "You must get pretty lonely then." 
            show Clover discomfort 
            "She sighs, playing with her hair."
            c.c "Yeah, you'd be right. I'm not happy with what got me here… but I think if I didn't leave home one day, I would have lost my mind. I don't think I would have survived out there on my own." 
            m.c "Well, you're not on your own now." 
            show Clover wink
            "She giggles once more." 
            c.c "That's right. And hopefully I won't be alone tonight either." 
            jump ch4_2done
        label ch4_2c_2:
            c.c "Am I going a bit fast?" 
            m.c "We did only meet a couple hours ago…" 
            "Despite that, he finds himself chuckling." 
            m.c "We have plenty of time to get to know each other, don't we? So let's start there." 
            "He peers down the tunnel. No, still just darkness. No ram horned demon in sight." 
            m.c "Have you ever been on a quest like this before?" 
            c.c "No, this is my first time. It's uh…"
            show Clover discomfort 
            "Her smile cracks as she averts her eyes, rubbing her forearm." 
            c.c "It's kinda scary, actually. I've never been part of a party."
            m.c "My first time scared me too. But we'll keep you safe, I promise." 
            "Clover lowers her voice." 
            c.c "Sure, if Mephi can keep himself safe…" 
            jump ch4_2done
        label ch4_2c_3:
            $ Clover_optout = True
            "Clover gives a nervous laugh."
            c.c "O-Oh, I'm sorry. I thought you were uh.." 
            "Micah waits for an expansion that doesn't come. He sighs." 
            m.c "You thought I was…?" 
            c.c "I thought you were into women." 
            "He stares at her for a moment then pinches the bridge of his nose. His brain takes a few seconds to cooperate again." 
            m.c "... I have a wife." 
            $ Clover_marriage_awareness = True
            "Clover gazes at him, her jaw falling slack. It seems stuck for a little while before her voice blurts out." 
            c.c "I'm so sorry! I didn't realise!" 
            m.c "It's fine, we're- We're not together anymore. But can you please stop hitting on me?" 
            "Clover groans, putting her head in her hands." 
            c.c "O-Okay. Message is loud and clear. I'm sorry, I won't do it again." 
            m.c "Thank you." 
            "Silence returns as they wait for Mephi." 
            jump ch4_2done
    label ch4_2done: 
        "They didn’t have to wait much longer before the cave was filled by the echo of what sounded like several bloodcurdling screams." 
        "The vibrations almost knocked Clover off her feet as Micah moved to steady her, awkwardly covering his ear with his free hand."
        show Clover scared
        c.c "What the-"
        m.c "... Well, I don’t think we had to worry about Mephi." 
        jump Ch4Scene4
    
    label Ch4Scene4:
        scene cave-branch
        show Micah disgusted at slightleft
        show Clover pained at left
        "There were a lot of decapitated orcs littering the latter half of the tunnel. The stench of iron and bile has Micah covering his nose, seeing Clover’s pale nauseous expression as they skirt around red puddles. At the half-way point they had heard what sounded like faint laughter, growing gradually louder than the screams as they died down."
        show Mephi manic-bloody at right
        "The clearing led to a fork in the path, ground stained as the source of that echoing laughter hacks down the last orc. There was both something terrifying and fitting about Mephi’s pretty face being sprayed by the same crimson, his expression akin to a gleeful child as his prey hits the ground." 
        me.c "Take that! Oh, hey guys!"
        c.c "... I’m going to be sick." 
        "Clover drags herself over to the only death-free corner to do so, Micah averting his eyes from the carnage as he stepped over a corpse." 
        m.c "... You could have saved a few for me." 
        me.c "Sorry, I got a bit carried away~"
        "The devil giggles, checking his reflection in his murder weapon." 
        me.c "Aww, I’m gonna need another bath!" 
        "Clover stumbles over to them, trembling and holding onto herself tight. The colour was still missing from her face."
        c.c "Y-You are scarier than any monster I’ve met." 
        show Mephi smug-bloody
        me.c "Then you know you’re safe with me, eh? So, what do we do about this?"
        "Mephi gestures to the split in the path, on closer inspection Micah notices each new tunnel has a door. Odd for a monster den. Did the orcs have a carpenter?"
        m.c "Hm…"
        "Micah swipes a severed arm off the ground."
        m.c "How about we use this? Wherever it points, we’ll go."
        "Clover shrinks away from them."
        c.c "Uh… Arms don’t tend to spin."
        "Mephi gives a little smirk, clearly on his wavelength."
        me.c "Sure, let’s give it a try!"
        "Micah places the arm closer to the doors and spins it. As it twirls, he spies the grimace on Clover’s face."
        c.c "... Men are so gross."
        show Clover startled
        "The hand points at her, sticking its middle finger up at her as she shrieks. Micah rolls his eyes and spins it again."
        m.c "Mephi, that’s creepy."
        me.c "Sorry Micah!"
        show Micah amused
        m.c "No you’re not." 
        "The hand points at the middle door."
        "Which immediately leads to a pit of lava so they try again." 
        show Clover discomfort
        "The right door does not open to another death trap, only a long tunnel Micah cannot spy the end of. They start walking, Mephi soon decides to break the silence." 

        if Mephi_intimacy1 == True: 
            me.c "Hey Micah?" 
            "Micah instantly knows he’s gonna regret engaging."
            m.c "What is it?" 
            me.c "Did you want to do something exciting tonight?"
            "Micah shoots a nervous glance at Clover. She seems distracted, deep in thought. He sighs."
            m.c "Exciting, how? … What are you up to?"
            show Mephi startled-bloody
            "Mephi feigns offense, dramatically grabbing at his own chest."
            me.c "I’m not up to anything, thank you!"
            show Mephi smug-bloody
            me.c "I was just wondering… Have you ever tried knifeplay?" 
            "Micah stares at him for a moment. What on Earth did he mean by… Oh. Where the Hell did that come from?!"
            "He composes himself, flattening his tone."
            m.c "No, Mephi. I don’t have a knife kink." 
            me.c "Have you tried it?"
            m.c "No, but having a sharp object anywhere near my privates sounds the opposite of arousing." 
            "Clover is staring at them both now. Either Mephi is oblivious or he just doesn’t care as he pipes up."
            me.c "Oh, I didn’t mean there! It could be on your back~"
            m.c "I don’t want to be stabbed during sex!"
            "Clover is now set on facing neither of them. She looks positively exhausted."
            jump ch4_3done


        else:
            me.c "Whatever’s been making the howling has been pretty quiet since we got here."
            c.c "You have been murdering everything, it’s probably too scared to make a noise…"
            m.c "Either that or we haven’t heard it because of all the orcs screaming bloody murder."
            "He listens out just in case. The sound of their footsteps seems to be amplified, the only other thing he can hear seems to be… Wind? In a cave?"
            m.c "I think we’re close to some kind of exit." 
            "Clover tilts her head and listens out. She seems to hear the muffled sound too, however her expression seems worried."
            c.c "I didn’t think there was another way out of the cave… I wonder what’s on the other side."
            me.c "Hopefully some treasure." 
            m.c "Did you find any on your way through here?" 
            "Mephi chuckles quietly, flashing a small object that makes their jaws drop open. The coin looked like a smaller version of a regular silver coin initially, with a slightly darker shine. However, the weight was apparent in how he tilted it, revealing a denser build." 
            m.c "I-Is that a platinum coin?! Those are worth 75 silver each!"
            me.c "It is! I found four of these. 50%% means two of these go to me, so that leaves you two with one each, hm?" 
            c.c "I’ve never seen one of these in person before… It looks exactly how Marie described it…" 
            $ m.silver += 75
            "Obtained 75 silver pieces!"
            jump ch4_3done

    label ch4_3done: 
        "Clover halts as a new sound joins the strange wind. No, they all realise it isn’t a distant gale. There’s a… Whimpering, breaking up the low tired howling. Clover takes off down the tunnel, Micah and Mephi quickly give chase."
        m.c "Clover?! Don’t go off on your own, there might be more orcs!"
        "The winding tunnel initially feels like it’s only growing longer, their companion’s silhouette shrinking further from Micah’s line of sight before freezing and dropping down. The mouth of the path finally opens up as they reach her."
        show Clover cheerful
        "It wasn’t a violent drop, Micah realises as they find her crouching, holding a tiny black husky puppy to her chest."
        c.c "So cute! Are you the one making all the noise, little guy?"
        "Clover giggles as the puppy licks her cheek, barking happily. The barking bounces off the cave walls, echoing."
        m.c "Of course, the howling must have been this dog crying."
        "Mephi crouches down to observe the dog. It whimpers and buries into the crook of Clover’s neck. His expression twists into confusion."
        me.c "How did it survive with all the orcs here?"
        show Orc at slightright
        "The cave walls shake, vibrations joined by snarling as they all look to see a party of orcs forcing themselves through the narrow opening."
        me.c "Oh shit."
        show Clover determined
        "Clover scowls, gently placing the puppy down before bouncing up, pulling out her bow."
        c.c "You won’t get past me!"
        "Arrows rain down on the approaching orcs, some staggering out of range screaming as their slower companions are nailed down. Micah is unable to do anything but stare at Clover for a moment." 
    menu: 
        "He is so proud of her.":
            $ c.plat += 1
            jump ch4_4done
        "He’s not letting her take all the glory.":
            jump ch4_4done
    label ch4_4done: 
        m.c "There goes the cowardice from before."
        "Mephi laughs, wielding his bloody axe as his knees bend." 
        me.c "Come on, let’s go-" 
        "Mephi’s battle cry is drowned out by the puppy’s growling as it hurls itself as one of the orcs."
        show Kitty with moveinleft
        hide Orc
        show Micah startled
        "Micah’s jaw drops as its fangs savagely rip the beast’s throat out before throwing itself at its trembling companion."
        m.c "What the-"
        show Mephi startled
        "Mephi looks down at the puppy as it starts feasting on the already still carcass. His eyes are wider than Micah has ever seen them and he imagines he’s the same."
        me.c "Well uh… That explains a lot. I think we’ve found a baby hellhound."
        "Clover’s arrows take down the rest of the orcs before Mephi regains his bearings, she swoops the puppy up with glee. It goes right back to licking her cheek."
        c.c "A hellhound, this little guy? She’s so cute! Can we keep her? Please?"
        "... Why was Mephi looking at him? Micah still feels a bit disoriented as he watches the puppy. At the very least, she would be easy to feed. That fact was rather terrifying."
        m.c "Well, if we don’t feed it, I think it’ll turn on us. So uh… It’s your job to take care of her properly." 
        "Clover grins, hugging the hellhound closer. She hugged as best as she could in return with her stubby front legs."
        c.c "Hellhounds will eat anything, I’m sure we can get plenty of meat from monsters for her. Now, what do I call you… How about Kitty?"
        "Micah feels better at not being the only one in a stupor, Mephi staring with him at Kitty as she continues to enthusiastically lick Clover. Now he hoped the pup didn’t already have a taste for demon blood."
        m.c "Why would you call a dog…"
        "He shakes his head and turns around."
        m.c "Never mind. Let’s claim our reward."
        return