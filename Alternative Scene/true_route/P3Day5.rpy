label P3Day5:
#; The plane will burn before you can ride it, despite getting the key

window show dissolve
play music Morning
show bg MansionMorning with dissolve
show k flirt at pos50k with dissolve
k "What do you know, [name]! You actually made it to the last one-on-one date."
show k happy

menu:
    k "How are you feeling?"

    "Pretty good":
        jump p3d5_addChoice1
    "I've been better":
        jump p3d5_addChoice2

label p3d5_addChoice1:
m "Honestly, pretty good!"
m "I'm excited to see how a day with Allie will be."
show k sassy
k "...Oh, you've got a real surprise in store."
jump p3d5_addAfter

label p3d5_addChoice2:
m "I've been better, but I'll manage."
show k sassy
k "I'm sure a fun day with Allie will cheer you up!"

label p3d5_addAfter:

show k happy
k "She has all of us in the crew working extra hard to prepare a special date for you."
show k sassy
k "And by all of us in the crew, I mean the Brothers Five."
show k flirt
k "How about you go find her, spend some time together while we set things up for you?"
m "Sounds like a plan, Kat."
show k sassy
k "Let's see... oh, looks like she's by the beach."
m "Guess that's where I'm headed!"
show k laugh
k "Don't do anything we can't air!"
show k sassy
k "Murder is okay, but god forbid someone takes their top off."
hide k with dissolve
"I waved to Kat as I went on my way."
show bg BeachMorning with dissolve # time:2
show a neutral at pos50a with dissolve
stop music
play music JazzBrunch
"Just as Kat said, Allie was by the beach. She was looking out at the ocean."
m "Morning, Allie."
show a happy
a "[name]! It's always nice to see you."
"The difference between Allie's voice during the day and night was like day and night."
"I guess we do have to worry about the cameras, but... still, it takes some getting used to."
show a sassy
a "I know it's going to be tough to top your previous dates with all the other girls... but I think I have a good shot."
m "I'm looking forward to it, Allie."
show a laugh
a "You better be - we've been saving the best for last!"
show a neutral
"She reached for my hand."
show a happy
a "Walk with me?"
"I reached for her outstretched hand."
m "It'd be my pleasure."
"The two of us walked around the beach for a while, \"getting to know each other\"."
m "So what will you be doing when this show's over?"
show a happy
a "First thing I'm gonna do is say hey to my family again, and make them a nice dinner!"
show a laugh
a "I'm sure that they've gone sick with worry in the week since I've been gone."
a "...I wonder what they are thinking now. It's been at least two years since then."
"Kat was right. Sometimes not remembering is a blessing."
"Allie doesn't have that luxury."
show a happy
a "Anyway, I've got a surprise for you - come on!"
show bg LakeMorning with dissolve #time:2
"She pulled me along by the hand into the forest."
"I have to say, Allie's really impressed me."
"Of course, it was her deliberate plan to come into the forest and get to the hangar - but she made it seem so spontaneous."
show a happy


# BEGINNING of modifications
a "You're going to love it!"

hide a with dissolve #time:2
show bg HangarNoon with dissolve #time:2
show a happy at pos20a with dissolve #time:2
"We approached the hangar as I remember having done so many times before."
"The doors were all closed for now before we got the key to open  the hangar."
"Yet this time, it feels different..."
"Hope."
"It was the warmth of hope in my heart—hope that we will finally be free."
show a neutral
m "So how are we doing this?" 
show a sassy
a "Ever heard of womanly charm? "
show a laugh
a "Two is usually around the outside here and, like the gentleman he is, will offer his key when the little lady can't open the door."
show a annoyed
m "I've heard of \"womanly charm\", I just didn't realize you had any."
play sound Hit
show a angry
a "Hey!"
"Quickly changing the topic before she hit me again, I just avoided her glare that bore a heat into my neck."

m "So what's the surprise you've got then? It seems like Two isn't here yet."
show a neutral
"Oh, it's nothing big..."
show a laugh
a "...but we need on the plane first."
show a blush
a "On a completely unrelated note, did you know there's a private stash of booze in the passenger cabin?"
show a laugh
a "It'll be good for celebration, at the very least!"

"Opening my mouth to respond, there was a smile on my face."
show a surprised
stop music
play music DevastationAndRevenge
"It fell a second later as we froze, hearing something nearby."
play audio WalkingOnDirt
"Footsteps. Not outside but..."
"...inside the hangar."
"We were by the door as the footsteps approached."
"As the doorknob jumped and twisted, Allie and I just both stared at each other, anxiety dipping into our minds."
play audio DoorOpen
"It's just Two, right? I shouldn't feel this... presence..."

stop music
play music SmileEnding
show k surprised at pos75k with dissolve
k "...!"
show a angry
a "!"
show k bored
k "..."
show a annoyed
show k annoyed:
    linear 0.2 xpos 0.9
"Kat leaned away from Allie and I for a moment, her microphone glowing with a green ring around the edge for a second."
k "Hey Two, I'm seeing a potential fuel leak in the airplane. Mind explaining yourself?"
show k happy:
    linear 0.2 xpos 0.8
k "Hey there, lovebirds! I forgot you two would swing by around here."
show a worried
a "H-Hey, Kat! How's it uh... going?"
"Her voice is shaking... it isn't like Allie to be startled like this."
"I'm just as startled now that I think about it... my tongue feels like it's twice it's size right now."
"We're on the cusp of escape... all we need to do is get past the door that Kat is blocking, get on the plane, and regroup with the others."
"It feels as if there was a cold hand gripping the back of my neck as Kat stayed in the doorway."
show k  flirt
k "As good as usual!"
show k laugh
k "I hope you two aren't getting into any trouble out there." 

#make a choice here on whether to follow Kat or shove her out of the door and charge past
"Her eyes are closed..."
"Now's our chance. Allie is frozen in place but we have to do something."
"If we just push Kat out of the door, we can lock her outside the hangar. Then the plane is ours, we'll just need to pick up the others quickly."
"It's a risk... but I'm not seeing many options. It's either that or we follow whatever Kat does."

menu:
    "Do I..."

    "Follow Kat":
        jump FollowKat
    "Push Kat":
        jump PushKat

label PushKat:
m "...I'm sorry, Kat."
show a worried
show k worried
k "What?"
"Reaching forward, I pulled on Kat's shoulder. Moving beside her, I shoved her unceremoniously away from the hangar."
play audio Hit
show k surprised:
    linear 0.1 xpos 0.3
show a surprised:
    linear 0.2 xpos 0.6
with vpunch
k "W-Wait!"
m "Come on, Allie!"
show a worried:
    linear 0.1 xpos 0.7
show k worried
a "..."
a "Quickly!" 
"She caught up with what I was doing as we dove into the building."
with vpunch
play audio DoorClose
"Slamming the door shut behind us, she promptly locked it with an inner latch."
"Turning to the side, she saw a panel of hooks that held keys on them. There were two missing, but one plane key remained."
show a serious
a "I'll work on getting the plane started, you open the hangar!"
show a serious:
    linear 0.1 xpos 0.85
"The door we came in jostled as Kat grabbed the doorknob."
"It wouldn't open for her."
"Her head pushed up to look through the window of the door, staring at me."
"Kat's face was as white as a ghost."
show k surprised
with vpunch
k "You don't know what you're about to do! Open this door - right now!" 
"I couldn't meet her eyes, I didn't dare. "
m "Sorry, Kat, but I'm done following the script."
"Looking over to the panel of door controls, I saw a lever labelled for every door in the hangar. Each lever had a green LED flashing underneath it."
show k angry:
    linear 0.1 xpos 0.4
with vpunch
k "Listen to me!"
play audio Engine
"The airplane engine roared to life behind me."
show a worried
a "It's running! Come on!"
stop music
play music FutureGladiator
with vpunch
show k surprised:
    linear 0.1 xpos 0.4
k "Damian has the other key!" 
"This was enough for me to look at her, to tempt my gaze with that of a snake."
"Kat's face was white as a sheet, her eyes open with a sudden panic."
"Her hands fumbled with something before she pushed it against the window... a key for the airplane."
"One of three... we have one... she has one... so then...?"
play audio Intercom
show a surprised
show k surprised
d "Trying to escape? Don't you think a plane is a bit cliche?"

"The colour drained out of my face as the intercom rose to life, Damian speaking to us through it. "
show a angry
a "What's taking so long with the door?!"

"Panic rose in my body as I heard Allie and saw Kat."
"Within seconds, all I could sense was my own heartbeat."
"Reaching over to the door controls, I found the lever for the main hangar doors."
"Pulling on the lever, it simply refused to move."
"The light beneath it flickered to red. A moment later, the scarlet colour swarmed over the rest of the levers."
"Inside the hangar, the lights shut off before red emergency lights filled the space."
show k serious
k "Open this door! Don't you do it...!"
d "Sorry Kit Kat, but we both know the rules."
"A high frequency whistle began to rise from the intercom. It itched at my ears as it rose higher in both frequency and volume."
show a surprised 
a "W-What is...?"
show a angry 
a "[name], what are you doing?!"

"All I could do is turn back, staring at Allie as my heart sank. Hopelessness settled in as I realized all the doors were forcibly locked."

show k sad
k "You..."
with vpunch
show k angry
k "Idiot!" 
with vpunch
k "Why did you do that?!"
show k sad
k "Why did you have to...?"
show k angry:
    linear 0.1 xpos 0.3
k "Damian! Don't you dare! I'll..."
show k sad:
    linear 0.1 xpos 0.4
k "I'll do anything... everything... you say."

"..."
"I can see how genuine she's being. No longer are her emotions locked behind her facade or a thin smile."
"The tears that swarmed the edges of Kat's eyes were one of the realest things I've experienced from her all this time."

show a surprised:
    linear 0.1 xpos 0.8
a "[name]...?"
d "Too little too late, Kit Kat."
"The high-pitch frequency reached a crescendo. It grew so high that it moved outside the range we could hear - yet its presence still loomed."
show k surprised:
    linear 0.1 xpos 0.42
stop music
k "W-Wait!"

show bg black with dissolve
$ renpy.pause(delay = 0.5, hard = True) # wait

"There wasn't a single thing I could do as the plane that Allie sat inside ruptured in slow motion."
hide a with dissolve
"Liquid flame rolled out from it, hidden explosives inside detonating one after the other."
"The only thing I had time for was to look at Kat's face one last time."
"Her anguish would've spoken to me more if I had the time to process it-"
show k angry:
    linear 0.1 xpos 0.5
with vpunch
k "No!"


hide k
play audio Explosion

$ renpy.pause(delay = 2.0, hard = True) # wait
play music MasterDisorder

d "Right when I thought it was going to get interesting."
d "Could you look at the cameras, Kit Kat?"
with vpunch
d "I want to see the exact moment that spark in your eyes snuffs out."

play sound Glitch1
d "{glitch=30}{b} As for you... when you get to Hell, let me know what it's like.{/b}{/glitch}"
play sound Glitch2
d "{glitch=50}{b} We won't be far behind you.{/b}{/glitch}"

return





label FollowKat:

show a neutral
"Kat stepped out of the doorway... before closing and locking the door to the hangar behind her."
"She began walking away from the hangar, gesturing for us to follow calmly."
"We couldn't disobey so openly without risking everything... so we acquiescently followed."
show k happy
m "Not anymore than usual, Kat!"
show a happy
a "Yeah! I had this idea for our date..."
"Allie was nervous under that innocent facade, but we just needed to sprint this last hurdle."
show k serious
k "I'm afraid that's not possible, anymore. We've had a minor setback around here."
show a worried
a "A setback? What kind of...?"
show k bored 
"Kat just sighed."
show k bored:
    linear 0.1 xpos 0.75
"Reaching into her dress jacket, she pulled out a small object."
show a annoyed:
    linear 0.2 xpos 0.15
"Keys... the keys to the plane!"

show k sassy
k "Isn't it obvious? ..."
hide a with dissolve #time:0.5
hide k with dissolve #time:0.5
show bg Black with dissolve
show bg KatControl with dissolve
"Holding up the keys, she took off one of the side panels. Underneath was a hidden button she pressed down on."
"It began to emit... sound."
"The frequency rose to a high-pitched squeal before becoming a screeching inside my head."
"Clasping both hands overtop of my ears in surprise, I noticed Allie doing the same beside me."
"The sound suddenly died, the frequency reaching so high we couldn't hear it any longer - only its looming presence remained."
k "...I've got a flame to smother."
"Then... it happened."
play sound Explosion
"An explosion rippled through the air, the shattering of the wind knocking the air out of me for a moment."
"Heat is the only way I could describe it."
"As alarms began to blare out their roaring cry, the hangar doors opened..."
"...from them was as if the gates of hell itself had opened."
"Liquid flame poured out as we watched in horror."

show bg HangarNoonBurns with dissolve
show k sassy at pos80k with dissolve 
show a angry at pos15a with dissolve 
a "...No..."
with vpunch
show a angry:
    linear 0.2 xpos 0.1
"She staggered and almost fell."

"Kat... didn't even turn to look at it."
"She just stared at us... studying us..."

show k serious
k"I'm sure you can see it's uh..."
show k sassy:
    linear 0.1 xpos 0.75
k "An \"all-hands-on-deck\" kind of situation."
"Illuminated by the flames behind her, my gaze couldn't shift anywhere other than her eyes."
show k flirt
k "How about you two spend your day on the ground instead? Flying is... out of style."
"A blood vessel in my temple tensed from the strain on my body - the strain of having to hold myself back."
"I want to scream."
"I want to attack her with every bone in my body."

menu:
    "I..."

    "Attack her":
        jump p3d5_addChoice5
    "I can't do anything":
        jump p3d5_addChoice6

label p3d5_addChoice5:
"Between fight or flight... I choose fight in the face of this witch."
"As soon as I took one step towards her, I could feel a hand pulling me back."
show a serious:
    linear 0.2 xpos 0.20
"...It's Allie."
"One look from her says everything - you can't do this."
"And she's right. I can't afford to put everyone in danger."
jump p3d5_addAfter3


label p3d5_addChoice6:
"But I can't."
"I can't, or I'll be killed."
"And not just me, but everyone else."
"I can't react on instinct like that when so much hangs in the balance."


label p3d5_addAfter3:
"...To hold myself back from giving away what this plane meant to me took all the strength I had."
"I need to calm down - Kat might be able to read my face and see that -"
show a surprised:
    linear 0.1 xpos 0.15
a "Are you okay, Kat?! The hangar..."
show a worried
m "Quite a stunt to pull off, Kat."
show k laugh 
k "Say it louder, I'm the best producer you've ever had."
show k happy
k "Nothing boosts ratings like an explosion."
k "..."
show k neutral
"Kat just gave a thin smile, all three of us hiding behind a veil of formality."
"Somehow... she'd known. Something tipped our hand and now she's taking precautions."
"Maybe... she's doing this all pre-emptively. There's still a chance she doesn't know our full plan."
"But either way... to stand here in front of us and still pretend this was a \"fuel leak\" or a stunt..."
show k laugh 
k "Now, let's get back to your date! We can't really use this scene of us talking about the logistics of the fire for public footage."
show a neutral
a "Well... there's nothing to be done about that."
show a happy
a "How about we go somewhere else, [name]?"
"She reached for my hand and held it tight."
"How could she smile like this at me?"
show k neutral
k "..."
m "...Of course, Allie."

hide a with dissolve
show k serious
"..."

#END of modifications 

hide k with dissolve
show bg Black with dissolve
stop music
play music LeavingHome
"For the rest of the day, Allie and I put on the performance of a lifetime."
show bg KatControl with dissolve
"Though our faces were all smiles and laughter, we knew, now more than ever, that we were trapped in Kat's macabre puppet show."
"And Kat loved to make us dance."
"She must have known we were trying to escape - but how?"
"Did we make a mistake?"
"Did Four give us away?"
"Should we ever have trusted him in the first place?"
"...Who can I trust now?"
"Time is ticking, and the end of the show looms closer and closer."
show bg MansionNight with dissolve
"...It's time I'm supposed to meet with the group, but... what would we even do?"
"There's no way we can escape - our last chance died with the hangar."
"Should I just make a break for it?"
"No, I'd never make it. And the others would suffer for my mistake."
"What do I do...?"
show k flirt at pos50k with dissolve
k "You don't look so good, [name]."

menu:
    "What do you want?":
        jump p3d5_addChoice7
    "...I've been better":
        jump p3d5_addChoice8

label p3d5_addChoice7:
m "...What do you want, Kat?"
m "I'm not in a great mood right now. Can we talk later?"
show k laugh
k "You're not much for acting, are you, [name]?"
jump p3d5_addAfter4

label p3d5_addChoice8:
m "...I've been better, Kat."
m "It hasn't exactly been sunshine and rainbows today."
show k laugh
k "...You really aren't much for acting, are you, [name]?"

label p3d5_addAfter4:

stop music
play music Smile
show k flirt
k "Look... I already know about you and your plan to escape."
"...!"
"My blood ran cold."
show k bored
k "You know, take the plane, fly away from here... it wasn't hard to figure out."
"I tried to say something in my defense, but my voice wouldn't come out."
"It was all I could do to stand wide-eyed."
show k neutral
k "I know you and the others found the lab, got your memories back... well, at least the others did."
show k flirt
k "...And I know that every night, you all work together to try to find a way out."
show k bored
k "I mean, of course I'd know."
stop music
play music MiamiNights
show k flirt
k "...I'm the reason why you got this far."
m "What do you mean?"
show k sassy
k "Just follow me. You'll save all of us time."
show bg GamesRoomNight with dissolve
"We walked to the locked room near the games room."
"She took out her master key and span it around."
show k laugh
k "You never really thought a bunny could take a key from me, right?"
"Honestly, I don't know what to believe anymore."
show bg ProducerRoom with dissolve
"She opened the door."
hide k with dissolve
show v worried at pos10v with dissolve
show a surprised at pos25a with dissolve
show y worried at pos40y with dissolve
show s worried at pos70s with dissolve
show t worried at pos85t with dissolve
show k flirt at pos55k with dissolve
"The others were inside, looking as surprised as I was."
show a angry
a "Give me one good reason why I shouldn't kill you right now, Kat."
show k sassy
k "How about two?"
show k flirt
k "First - your inside man was never Four, it was me."
show a surprised
show k happy
k "I mean... come on! He wouldn't be smart enough for something like this."
show k flirt
k "Second - you only ever had a chance at escaping this island because of me."
show k sassy
k "Newsflash, Allie - those tanks never just \"bug\" out."
show a surprised
a "...You're the one who let me out of my tank."
show k flirt
k "The one and only."
show a worried
"Allie was at a loss for words, and I was no different."
show s worried
s "...What do you want, Kat?"
show k flirt
k "Honestly? The same thing as you guys."
show k sassy
k "I want off this crazy train. I want out."
show k flirt
k "I want you guys to include me in your little escape plan."
show a surprised
show s surprised
show t surprised
show v surprised
show y surprised
show k surprised
k "What? Do I have something on my face?"
show k laugh
k "As hard as it is to believe, the list of people who want to stay on this island is pretty short!"
show k surprised
m "Hell no! We can't trust you!"
show k worried
m "I... I'm not sure how, but I remember - I remember I tried to escape with you before."
m "I trusted you, I even fell for you."
show a surprised
a "Even five girls isn't enough! Unbelievable."
m "And then you betrayed me - and shot me!"
m "There's no way we could ever trust you. You're just going to stab us in the back."
show y worried
y "...Is that true, Kat?"
show k worried
k "...I'm ashamed to say it is."
show k serious
k "But I didn't have a choice."
show k worried
k "You know how it is with Damian. It doesn't matter if you share the same blood."
show k angry
k "He'll take the people you love hostage and use them to force you to dance to his tune."
show k sad
k "I'm sorry I betrayed you, [name]. I really am."
show k serious
show a sad
k "...But if I had to do it again, I'd do it again in a heartbeat - because there was someone I needed to save."
show k sad
k "...I know I must look like the villain to you, but believe me, I have people I care about too."
m "If you're so compassionate, how come you burned up our only way out of here!?"
show k serious
k "You're lucky I did, [name]."
show k angry
k "If you'd actually flown as planned, you'd all be at the bottom of the ocean right now."
show t surprised
t "What do you mean?"
show k serious
k "It's a cruel trick of Damian's. He knew there was a chance that people on this show would recover their memories, and try to escape."
show k worried
k "...So he made us build the hangar, and the plane."
show a worried
a "...It's the one place anyone trying to escape would go."
show k sad
k "Exactly."
show k serious
k "I've told you in the past, Allie. Never fly that plane, or take the boat, out of sight of this island."
show k angry
k "...If you did, you'd have blown up like fireworks."
show a worried
"That Allie and I were in that plane, which was little more than a flying deathtrap, sent a chill down my spine."
show k serious
k "Look, the simple reality is you need me to escape."
show k neutral
k "Without me, you won't even make it past the barrier."
show a surprised
a "What barrier?"
show k flirt
k "Exactly."
show k worried
k "...And though I hate it, I need you guys to help me and my... us escape."
show k serious
stop music
play music Twisting
"She reached her hand towards me for a handshake."
k "Allies?"
show v serious
v "...Let's discuss first."
hide k with dissolve
show y worried at pos30y with dissolve
show a worried at pos50a with dissolve
show v worried at pos10v with dissolve

"Kat leaned against a wall while the rest of us debated what to do."
show y worried
y "...Can we really trust her? This might just be another trap."
show y sad
y "It's not like it'd be the first by her you fall into, [name]."
m "...You're right."
show s worried
s "...That said, it's not like we have much to lose at this point."
show s sad
s "Even if she'd done terrible things to us in the past... we still need her to escape."
show a angry
a "..."
m "You alright, Allie?"
show a sad
a "I'm fine, I'm just angry at myself."
show t worried
t "Hey, don't beat yourself up about it."
show t happy
t "We're still alive. That's what counts."
m "She's right, you know?"
m "I'm... I'm not sure how I'm feeling right now either, but... we're alive."
m "That counts for something."
show a happy
a "...You're right, [name]."
m "And as much as I hate to say it..."
m "...I think we'll need Kat's help, trustworthy or not, if we want to stay that way."

menu:
    "...But we'll need to keep an eye on her":
        jump p3d5_addChoice9
    "We have to trust her.":
        jump p3d5_addChoice10

label p3d5_addChoice9:
m "...But we'll need to keep an eye on her."
show a neutral
a "I couldn't say it better myself."
jump p3d5_addAfter5

label p3d5_addChoice10:
m "...We have to trust her."
show a serious
a "...Sure."
show a angry
a "I'll be keeping an eye on her, though."
show a worried
a "We can't afford to blindly trust anyone who says they can help us."

label p3d5_addAfter5:

show a serious
a "...Alright, Kat. If you want our help, you're going to need to answer a few questions."

show v worried at pos10v with dissolve
show y worried at pos25y with dissolve
show a worried at pos40a with dissolve
show s worried at pos70s with dissolve
show t worried at pos85t with dissolve


show k neutral at pos55k with dissolve
k "Ask away."
show a serious
a "What the hell is this sick show for?"
show a angry
a "And why have you been forcing us to repeat it, over and over?"
show k serious
k "...As someone from the Resistance, it should be obvious to you."
show k worried
k "This is just one of hundreds of killing shows we air - shows that keep people scared, that keep people from organizing against the government."
show k serious
k "You want to paralyze people with fear? You broadcast exactly what will happen to you if you rise up."
show a angry
a "...You're monsters, you know that?"
show k sad
k "I don't disagree with you - but we're not in charge here."
show k angry
k "Some of us still have family to lose, Allie."
show k serious
show a serious
a "...Continue."
#k: From what I hear, you Resistance types aren't much better."
show k serious
k "...Before we air each show, we test them internally on test audiences, to see what kind of ratings they bring for the... fortunate, and what kind of... despair they bring... for the less fortunate."
show k worried
k "If they tested well enough, we'd air it, but it wasn't... efficient."
show k serious
k "But we couldn't just film a killing show over and over again to see which version of it rated best - you can't bring people back from the dead."
show k neutral
k "It was the same for the test audiences. You couldn't just make them watch multiple versions of a show, as they'd remember previous versions that would influence their opinions."
show k serious
k "There was no way to test multiple versions of a show, without losing the feeling that lives were really in danger."
show s surprised
s "...But my... the memory rewriter would have changed that."
show k worried
k "...It did."
show k serious
k "We were able to 'reuse' everybody. Our 'volunteer actors's, the test audiences."
show k worried
k "Since we could just make people forget what happened... we could film run after run of the show, where each was as if it were the first time to all of you."
show k serious
k "...And that's exactly what we've been doing here for the last two years."
"It was a lot to hear."
"I had a feeling, but... to know that people looked at us, like we were nothing but lab rats..."
"...While I genuinely was afraid for my life..."
"It's sickening."
"We were silent for a while."
show y worried
stop music
play music MiamiNights
y "...If you've been testing the show this long... when's the real thing?"
show k worried
k "There is no \"real thing\". It's only what version tests the best."
show k sad
k "That said... there's only so much time Damian is willing to spend on this show, and that time is almost up."
show k serious
k "...This is the last run of the show. If you don't escape before the end... you're all as good as dead."
show k worried
k "I know Damian and I've said that we'd let you and your chosen partner go if you achieve good enough ratings, but..."
m "...It's a lie, isn't it?"
show k sad
k "...Yeah."
show k serious
k "I'm sorry I've waited this long to try to help you guys."
show k worried
k "I've been too scared to risk it all... but I've nothing left to lose now."
show k neutral
"She extended her hand to me, for a handshake."
show k flirt
k "Allies? At least, till we're out of here?"
m "...I don't really have a choice this time either, huh?"
m "If you wanted to, you could report us right now."
show k serious
k "That's true... and my word would count for more than all of yours."
show k neutral
k "...But that wouldn't save the person I need to."
show k serious
k "Like it or not, we have to work together."
show a serious
a "...Then it's a deal."
"Allie shook Kat's hand."
show s worried
s "...Kat, are you sure you don't want to-"
show k worried
k "I'm fine, Scarlett. It's... not important anymore, and we don't have any time to waste."
show s sad
s "...If you say so."
show k serious
k "Anyway..."
show k serious
k "...The only time we can escape is the last day of the show. Between midnight, and just before the sun goes up."
show k neutral
k "That's when the boat comes, to welcome the \"newly engaged couple\", and that's the only way off this island alive."
show k serious
k "It also doubles as a supply ship. We use it to replenish between each run of the show."
show v worried
v "Are there no other planes on the island? A boat would be far slower."
show k serious
k "Unfortunately, it's not so easy."
show k neutral
k "There's a protective shell around the island, which performs two functions."
show k serious
show a surprised
k "First, it renders us invisible to satellite. It's the reason why your people couldn't find us, Allie."
k "Second, if anything bigger than a human being tries to get in or outside of the barrier..."
show k worried
k "It'll get fried... unless it's emitting a compatible IFF signal."
show k serious
k "The only way off the island that will have that signal is the boat."
show a serious
a "...I'm betting it'll be heavily guarded."
show k flirt
k "Well, yes... but not from people on it."
show k neutral
k "The ship itself will be run by a skeleton crew. It's the staff on the island who we'll have to watch out for."
m "That still leaves the question of how we'll deal with them."
m "Last time I checked, there's hundreds of them, and not even ten of us."
show y surprised
y "...Actually, it might not be so hard after all!"
show y happy
y "I've got a plan that just might work."
show y happy
y "...Though I have to admit, it's a little crazy."
show s flirt
s "I like the sound of that!"
show t worried
t "If it involves zombies again, I'm out!"
show y laugh
show s happy
show v surprised
show k surprised
"Yui explained her plan to us, with a renewed confidence that could inspire anyone to believe."
show y happy
y "Luckily, we still have tomorrow, so we have just the amount of time we need!"
show k flirt
k "...This just might work, Yui."
show a laugh
a "You're a mad genius!"
show y happy
y "Let's just say I've been holding back my... creativity till now..."
show s happy
s "It's crazier than anything I'd imagined - and crazy enough to work."
show v sassy
v "Let's get to work!"
show t surprised
t "...Wait, were we even listening to the same plan?"
#...If Terra thinks the plan is too crazy
#...It's a bad sign when the plan is too crazy for Terra."
hide a with dissolve
hide s with dissolve
hide t with dissolve
hide v with dissolve
hide y with dissolve
"The others went their seperate ways, to help prepare for Yui's plan."
show k serious at pos50k with easeinright
stop music
play music PastSadness
"But Kat stayed - our business wasn't finished just yet."
k "...What's up?"

menu:
    "How am I supposed to trust you?":
        jump p3d5_addChoice11
    "What's your game?":
        jump p3d5_addChoice12

label p3d5_addChoice11:
m "...I want to trust you Kat, I really do."
m "But you've burned me before."
m "How could I ever trust you now?"
show k sad
k "...That's fair."
jump p3d5_addAfter6

label p3d5_addChoice12:
m "...I want to trust you Kat, I really do."
m "...But you're up to something, aren't you?"
m "Just like every other time I trusted you."
show k sad
k "...I can't blame you for feeling that way."
show k worried
k "And I can't take back what I've done before."

label p3d5_addAfter6:

show k serious
k "The only thing I can say, to try to make you trust me, is that we both have people we care about, [name]."
show k sad
k "And that if you don't escape, then the person I care about will go down with you."
show k worried
k "...I'm not asking for you to put your neck out for me. You'll never have to."
show k serious
k "I'm asking for you to help somebody that you've never met, and you never will."
show k sad
k "...Somebody innocent."
"It's strange."
"This woman has put me through hell, treated me like a lab rat, and more, and yet..."
"...Somehow, I think she's telling the truth."
show k bored
k "Honestly, it doesn't really matter if you do trust me."
show k serious
k "You'll see tomorrow that I'm going along with Yui's plan either way."
m "...I'll trust you, Kat."
m "I'm sorry for yelling at you earlier."
show k laugh
k "Don't be! I literally shot you."
show k surprised
k "I think that earns you the right to be angry and more, no?"
show k neutral
m "...We've... well, I've gotten to know you over these past years."
m "Not for more than a couple weeks straight, but... I got to know you."
m "...And I think you're rude, and manipulative, and have no problem lying to my face."
show k surprised
k "Hey! Can we skip to the part where you compliment me?"
m "You're also incredibly crass, you keep secrets from everybody, and..."
show k angry
k "You finished?"
show k surprised
m "...But I don't think you're a bad person."
show k worried
m "Every time the show ran... you always talked to me, to make me feel like I wasn't alone."
m "And you made sure I never lost hope."
m "I know that was never part of the job. You didn't have to do that."
m "Yet you did it, over and over."
m "...It must have been so tiring to do that, over and over, full well knowing that we were doomed."
m "I don't know why you're doing all this... but I believe that you do care about helping people."
show k laugh
k "...I'm flattered, [name]."
show k flirt
k "But you've got me wrong."
m "...What do you mean?"
show k happy
k "Everything I've ever done for you, the others... it's been for my own selfish reasons."
show k flirt
k "It just happens to line up nicely."
show k laugh
k "...Though I appreciate the compliment."
"Unlike before... I couldn't tell if she was telling the truth."
hide k with dissolve
show bg Black with dissolve
"We went our seperate ways shortly after."
"I spent the rest of the night helping the others with preparing for the plan."
"I was exhausted when I went back to my room, but I still couldn't fall asleep for several hours."
"...It's as if something's on the tip of my tongue, but I just barely can't grasp it."
"Yet somehow, I know I'm closer than I've ever been."

stop sound
show bg Black
hide a
hide s
hide t
hide v
hide y
hide k
hide d
hide b1
hide b2
hide b3
hide b4
hide b5
with dissolve
window hide dissolve
$ renpy.pause(delay = 2.0, hard = True)

jump P3Day6
