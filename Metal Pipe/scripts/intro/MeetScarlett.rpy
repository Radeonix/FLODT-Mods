label MeetScarlett:

$ meetScarlett=1
show bg Library with dissolve
play music Sincerely
"The library was like a library out of a movie. Grand. Majestic."
"Nothing like your average library, which becomes a porn set after closing time."
"I took a few steps forward, and noticed a girl with red hair at the back of the library."
show s serious at pos50s with dissolve
play sound MetalPipe
"She was reading a magazine, or so it seemed from first glance."
"If you craned your head a bit to the side, you could see another book hidden behind the magazine."
play sound MetalPipe
"'A/B Testing after the Apocalypse - 1st Edition, by DB'."
m "Hey, what are you reading?"
show s surprised
q "Oh, this? Just another elementary -"
show s happy
q "I mean, an absolutely fetch truth tea bomb, yaassssss!"
m "..."
show s surprised
q "Can you believe that this one celebrity would, like, date another celebrity???"
q "I can't even! It's almost like they're people!"
m "I can see what you're actually reading, you know."
show s worried
q "...! Oh gosh, that's so embarassing."
m "Why would that be embarassing? The book you're actually reading sounds a lot more interesting."
show s sad
q "Where I come from, people make fun of people who... do what I do, I guess."
show s laugh
q "To them, a library is just a place to film porn after closing time."
m "*cough*"
show s neutral
s "I'm Scarlett, by the way. You're [name], correct?"
m "That's me. It's nice to meet you, Scarlett."
show s flirt
s "It's nice to meet you too, [name]."
m "I'm curious, so what are you actually reading?"
show s laugh
s "I thought you'd never ask!"
#@char Scarlet
#Her face lit up like fireworks. Wow."
show s surprised
s "Here, let me show -  Ah!"
stop music
play sound MetalPipe
"Scarlett dropped the magazine and the book behind it on the floor... revealing a second magazine in her hands."
play music RocketPower
m "Ah..."
show s worried
s "..."
hide s with dissolve
play sound MetalPipe
"She ran away so fast, I didn't even have a chance to say anything more."

if meetViolet == 1 and meetScarlett == 1 and meetTerra == 1 and meetAllie == 1:
    jump MetAllGirlsS

menu:
    "Guess there's not much left to do here. I'll head on down to..."

    "The Library" if meetScarlett != 1:
        jump MeetScarlett
    "The Kitchen" if meetViolet != 1:
        jump MeetViolet
    "The Games Room" if meetTerra != 1:
        jump MeetTerra
    "The Backyard" if meetAllie != 1:
        jump MeetAllie

label MetAllGirlsS:

stop music
play music ItemStore2
play sound MetalPipe
k "Alright, alright, enough messing around."
k "If you're on the show, and you're not an underpaid grunt, come to the main entrance of the mansion."
"I guess that includes me. I should start heading over."
with vpunch
k "That includes you too, Terra! I can see you playing, you know!"
t "You're not the boss of me!"
"What have I gotten myself into?"
jump MetAllGirls
