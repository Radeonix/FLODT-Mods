
label Day1Intro:

stop music

default persistent.AllieEnding = 0
default persistent.ScarlettEnding = 0
default persistent.TerraEnding = 0
default persistent.VioletEnding = 0
default persistent.YuiEnding = 0
default persistent.KatEnding = 0

menu:
    "I go by..."
    "He/Him":
        window hide dissolve
    "She/Her":
        window hide dissolve
    "They/Them":
        window hide dissolve
default playthrough = 1
default currentDay = 1
default allieAffection=0
default scarlettAffection=0
default terraAffection=0
default violetAffection=0
default yuiAffection=0
default meetAllie=0
default meetScarlett=0
default meetTerra=0
default meetViolet=0
default meetYui=0

default P1Date1="none" # label first pick
default P1Date2="none" # label second pick // the two main contendors!"
default P1Date3="none"
default P1Date4="none"
default P1Date5="none"
default P1Date6="none"
default P2Date1="none"
default P2Date2="none"
default P2Date3="none"
default P2Date4="none"
default P2Date5="none"
default P2Date6="none"
default P2Date7="none"
default P2Date8="none"
default P2Date9="none"

# START OF GAME

play sound MetalPipe
show bg Episode1 with dissolve
$ renpy.pause(delay = 2.0, hard = True) # wait
# pause 2.25

label MainStory:

$ dejaVu = 0

label WakeUp:
stop music
play music ItemStore2

scene bg black with fade
m "Zzzzz..."
with vpunch # replaces SHakeBackground

q "Hey, don't just lie there. Get up!"
m "Just 5 more minutes..."
with vpunch
q "You're the star of the show! You can't just sleep through it!"
m "Watch me... Zzzzz..."
q "Do you know what it feels like to be RKO'ed?"
q "You're about to find out."
jump hit

label yesdejavu:
    q "Ah, damn it. Now we're right back where we started."
    q "*sigh*"
    jump hit

label hit:
    stop music
    play sound MetalPipe
    with vpunch
    play music TheShowMustBeGo
    m "OWW!!!!"
    show bg PlaneBar with dissolve # with fade
    show k happy at mid with dissolve
    q "Rise and shine, sleepyhead."
    m "Ow ow ow... Did you just hit me?"

if dejaVu == 1:
    jump yesdejavu2
else:
    jump nodejavu2

label yesdejavu2:
    m "Wait, didn't this just happen?"
    show k laugh at mid
    q "Of course not! There's no way that I'd hit you twice."
    jump C1end

label nodejavu2:
    show k surprised at mid
    q "Nah, I just got here. I just chased off the person who hit you."
    show k flirt at mid

    menu:
        q "Really, you should be thanking me."

        "Thanks, I guess.":
            jump Thanks

        "I'm pretty sure that was you.":
            jump Doubt


label Thanks:
    m "Thanks, I guess."
    show k flirt at mid
    q "Don't mention it, it's all in a good day's work."
    jump C1end

label Doubt:
    m "No, I'm pretty sure that was you."
    show k sassy at mid
    m "What's with that look on your-"
    play sound MetalPipe
    with vpunch
    show bg Black with dissolve
    hide k
    $ dejaVu = 1
    $ dejaVu = 1
    jump yesdejavu

label C1end:
    q "Anyway, what was your name again?"
    m "Oh, my name's..."
    with vpunch
    m "...I can't remember my name!"

    show k surprised at mid
    q "Wait, what? I swear, I didn't even hit you that hard!"
    m "So you did hit me!"
    q "That's not important! Try to remember!"
    show k worried at mid
    q "If you can't remember anything, we're both going to be in big trouble."
    m "Why's that?"
    show k serious at mid
    q "We can talk about why after. What was your name?"
    m "...! It's..."

    $ name = renpy.input(_('My name is...'), length=14)


    m "My name's [name]. It's [name]!"
    m "I can't remember anything else, though."
    show k surprised at mid
    q "Wow, I should try hitting my accountant sometime."
    show k worried at mid
    q "Do you remember where we are, what you're doing here?"
    m "No, I can't remember a thing. Everything's so foggy..."
    show k happy at mid
    q "Alright, I can give you the rundown. You're on a reality TV show called {i}Find Love or Die Trying{/i} - though we just call it {i}Find Love{/i} for the... uninformed."
    show k neutral at mid
    k "I'm the producer - The name's Kat."
    show k happy at mid
    k "The premise is that you, the {i}suitor{/i}, are living with five beautiful women, and one of them is your soulmate."
    m "I haven't even met them yet, how would you know one of them is my soulmate?"
    show k flirt at mid
    k "That's just how it is, welcome to Reality TV!"
    show k happy at mid
    k "You'll get to know two of the girls over the next six days, over three dates with each of them."
    show k neutral at mid
    k "Then on the seventh day, you'll have to ask one of them to marry you at the final ceremony!"
    show k laugh at mid
    m "That seems... straightforward enough to me."
    show k flirt at mid
    k "Not so fast, partner!"
    show k neutral at mid
    k "The girl you choose will be given a choice - whether or not they accept your proposal."
    show k happy at mid
    k "If she says yes, you two will get to fade off into the sunset in a gold-plated yacht on the last day."
    show k laugh at mid
    k "Happily ever after, forever. Except without the yacht. It's a loaner."
    show k neutral at mid
    stop music
    play music Smile
    show k serious at mid
    k "If she says no..."
    show k flirt at mid

    k "...Well, we're going to have to kill you."
    m "Wait, what? Killed?"
    m "You're joking, right?"
    play sound MetalPipe

    show k sassy at r
    show d laugh at dl with dissolve
    d "Now that's the reaction I wanted to see!"
    m "???"
    show d happy at dl
    d "Really, you look like I just took a shit in your cereal!"
    m "What's going on? Who are you?"
    show d laugh at dl
    d "Oh, where are my manners."
    show d neutral at dl
    d "The name's Damian. Damian Black."
    show d serious at dl
    d "I'm the CEO of Royal Black Media, the biggest network for Battle Royale games on the planet."
    m "Battle Royale games? Like computer games?"
    show d surprised at dl
    d "You been living under a rock's stink-ass armpit?"
    show d sassy at dl
    d "Real people killing each other is in this season."
    m "What...?"
    show d annoyed at dl
    d "Well, *was* in this season. I swear, I put in hard and honest work into making top-of-the-line killing shows, and what do I get for it..."
    show d evil_smile at dl
    d "So we're trying a new kind of killing game. Spicing a little romance on top for the people who fart dreams and bake cakes out of rainbows."
    show d laugh at dl
    d "That's where you come in. And hey, it's not a bad deal!"
    show d neutral at dl
    d "You might find love! Or die. Whatever."
    show d laugh at dl
    d "Just put on a good show for me, hmm?"
    show b1 serious at br2 with dissolve # look left?
    q "Excuse me, Mr. Black?"
    show d annoyed at dl
    d "What is it, One?"
    show b1 worried at br2
    b1 "We're missing one of the aerial cameras for the back fields."
    show d laugh at dl
    d "Well, that's my cue. The intern ain't gonna shoot himself."
    show d evil_smile at dl
    d "Give 'em hell, Kit Kat."
    show k sassy at r
    k "You don't need to tell me twice."
    hide d with dissolve
    hide b1 with dissolve
    show k neutral at mid with dissolve
    stop music
    play music MysteryLoop
    show k annoyed at mid


    m "Look, I don't know what's going on here, but I'm getting out of here."
    m "For starters, I can barely remember my own name, let alone if I already have a partner."
    show k laugh at mid
    k "If that's what you're worried about, you didn't!"
    show k sassy at mid
    k "And not for a lack of trying."
    m "How would you know that?"
    show k bored at mid
    "Kat sighed." # label narrator
    show k serious at mid
    k "Look, you don't have a choice."
    show k annoyed at mid
    k "Damian will kill you if you try to escape, or if you tell any of the girls about the truth behind the show."
    m "...The girls don't know?"
    show k serious at mid
    k "They have no idea that your life is in danger - they just think it's a regular dating show about finding your soulmate, called {i}Find Love{/i}."
    show k annoyed at mid
    k "If you tell any of them the truth, you won't just get yourself killed. You'll get them killed as well."
    m "How could you -"
    show k angry at mid
    k "I don't make the rules, [name]. I'm sorry."
    show k laugh at mid
    k "Really, you're a pretty serious person, [name]!"
    show k happy at mid
    k "Most people would be a little happier to hear that they're alone in paradise with five beautiful women."
    show k sassy at mid
    k "What's there to worry about?"
    m "Oh, you know, the whole getting executed thing if the girl I ask says no, the little bit with not remembering who the hell I am."
    show k annoyed at mid
    k "...How about this."
    show k neutral at mid
    k "I need my show to be successful and run according to plan."
    show k flirt at mid
    k "And you want your memories back, and presumably, to leave this show alive."
    show k surprised at mid
    m "That depends on what the memories are, but yes."
    show k neutral at mid
    k "If you'll be a good suitor for my show, I'll help you get your memories back."
    show k happy at mid
    k "It's really not a bad deal. Most people would kill for a chance like this."
    show k surprised at mid
    k "Seriously! All you have to do is get to know five lovely women, and ask one out."
    show k happy at mid
    k "I'll be with you every step of the way, off-camera. Before you know it, I'm sure you'll be having lots of fun!"
    show k sassy at mid
    k "Who knows, you may even fall in love. You wouldn't be the first!"
    show k neutral at mid
    k "But if you survive the whole show, I promise that I'll tell you everything you want to know."
    show k happy at mid


    menu:
        k "Pinky promise. How does that sound?"

        "Sounds like a deal.":
            jump HellYeah

        "No thanks, get me outta here!":
            jump NTY

label HellYeah:
    stop music
    play music ShavingMirror
    m "Sounds like a deal."
    show k flirt at mid
    k "That's the spirit, sugar!"
    show k happy at mid
    k "Who knows, you might even be thanking me for this one day."
    m "We'll see about that."
    show k sassy at mid
    k "Trust me, I'll make sure that this show will be the best time of your life."
    show k laugh at mid
    k "It'll be so great, that everything after will feel like a disappointment!"
    m "That's a depressing way to look at it. What if I ended up with one of the girls after the show?"
    stop music
    jump postResponse

label NTY:
    m "No thanks, I'm getting out of here."
    show k bored at mid
    k "...And where would you go?"
    m "Home, of course."
    show k sassy at mid
    k "And where is home?"
    m "...Uhhh..."
    show k flirt at mid
    k "Thought so!"
    show k bored at mid
    k "Look, things will be a lot easier for the both of us if we just work together."
    show k serious at mid
    k "I'll make sure nothing crazy happens to you, and that you'll probably get home safe."
    show k neutral at mid
    k "More importantly, playing along gives you a chance to survive. Doesn't that sound better than getting killed for sure?"
    m "..."
    show k worried at mid
    k "You heard what Damian was going to do to the intern."
    m "..."
    stop music
    play music TheShowMustBeGo

    show k sassy at mid
    k "There's going to be free food!"
    m "...Alright, fine. I'll give it a shot."
    show k flirt at mid
    k "You won't regret it, promise!"
    stop music
    jump postResponse

label postResponse:
    play music ShavingMirror
    show k laugh at mid
    k "Anyway, without further ado..."
    show k happy at mid
    k "Let's get started with the show!"
    show k neutral at mid
    k "Follow me, I'll take you to where you'll meet our lovely contestants."
    show k sassy at mid
    "Kat grabbed me by the hand and pulled me along."
    show k annoyed at mid
    k "Remember, you can't tell anyone the truth about this dating game."
    show k serious at mid
    k "No matter what, just smile. Got it?"
    m "Got it."
    hide k with dissolve
    show bg Black with dissolve

    "We stepped out of the bar together."
    "I didn't realize it at first, but it was a bar in a small airplane."
    "I guess I must've been flown here."
    "We walked until we saw a mansion in the distance."

    show bg MansionMorning with dissolve
    m "Wow. It's huge."
    m "I can't imagine how expensive this place is."
    show k laugh at mid with dissolve
    k "You'd be surprised!"
    show k neutral at mid
    k "Since we're all the way in some forgotten corner of New Asia, the land comes pretty cheap."
    m "New Asia?"
    show k sassy at mid
    k "Have you never read the news in the past decade?"
    m "Memory loss, remember?"
    show k bored at mid
    k "Right."
    show k neutral at mid
    k "Well, I sure hope you haven't forgotten how to talk to girls."
    show k angry at mid
    k "Five! Four! Three! Two! One!"
    m "Wait, what? We're starting already?"
    show k bored at b6 with dissolve
    k "Not quite."
    stop music
    play music JazzInParis
    #show k bored at b6 with dissolve
    show b1 angry at bl2 with dissolve
    b1 "To give the world top tier enjoyment!"
    show b2 angry at bl with dissolve
    b2 "To protect our ass from unemployment!"
    show b3 angry at bm with dissolve
    b3 "To make the world believe in fate and love!"
    show b4 angry at br with dissolve
    b4 "We work like slaves for the shills above!"
    show b5 angry at br2 with dissolve
    b5 "We're the Brothers Five!"

    show b1 with vpunch
    play sound MetalPipe
    b1 "One!"
    show b2 with vpunch
    play sound MetalPipe
    b2 "Two!"
    show b3 with vpunch
    play sound MetalPipe
    b3 "Three!"
    show b4 with vpunch
    play sound MetalPipe
    b4 "Four!"
    show b5 with vpunch
    play sound MetalPipe
    b5 "Five!"
    b "Prepare to - "
    stop music
    play music ShavingMirror
    show k serious at b6 with dissolve
    k "Get the set ready, I want to start filming yesterday."
    show b1 sad at bl2
    show b2 sad at bl
    show b3 sad at bm
    show b4 sad at br
    show b5 sad at br2
    show k serious at b6
    b2 "Oh."
    show b2 sad
    b4 "I guess we're not important enough to finish our intros."
    b3 "Whose idea was it to work in the TV industry, anyway?"
    show b5 angry
    b5 "This wouldn't have happened if we had just decided to be accountants!"
    show k annoyed
    k "Wait by the mansion doors, and thank me later."
    hide b3 with dissolve
    show k angry at mid with dissolve
    k "It's show time people, let's get to work!"
    play sound MetalPipe
    hide b1 with dissolve
    hide b2 with dissolve
    hide b3 with dissolve
    hide b4 with dissolve
    hide b5 with dissolve
    hide k with dissolve
    stop sound
    stop music
    play music CarpeDiem
    "I walked to the doors."
    play sound MetalPipe

    k "Hey [name]! Can you hear me?"
    with vpunch
    "Kat's voice boomed across the Island, though she was nowhere in sight."
    m "...Kat?"
    k "I wasn't kidding when I said I'd be with you every step of the way."
    k "As long as you're on this island, I'll be able to see, hear, and even talk to you."
    k "Just think of me as a cuter and sexier 'Big Brother'."
    m "That doesn't sound nearly as good as you think it does."
    k "Hey, how else could we film the show?"
    k "You really want to meet the love of your life with a camera sticking out of your head?"
    m "Good point."
    k "Anyway, head on into the mansion already, and go meet the girls!"
    k "I recommend checking out the library, the kitchen, the games room, and the backyard. *Wink* *Wink* *Nudge* *Nudge*"
    k "From here on out, the cameras are rolling. Don't be stupid."
    k "I'll seeya later, sweet cheeks! Kat out."

    m "Alright, I'm finally here. There's only one thing left to do..."

    menu:
        "Open the door":
            jump Open

label Open:
    jump MeetYui
