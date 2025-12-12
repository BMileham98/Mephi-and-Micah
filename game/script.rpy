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
        def __init__(self, character, name, orientation, corruption = 0, redemption = 0, silver = 0):
            self.c = character
            self.name = name
            self.orientation = orientation
            self.corruption = corruption
            self.redemption = redemption
            self.silver = silver



screen debug_overlay():
    frame:
        align (0.98, 0.02)   # top-right corner
        background "#f00"
        padding (10, 10)

        vbox:
            text "Mephi Love: [me.love]"
            text "Mephi Platonic: [me.platonic]"
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
        return
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
        return





    

