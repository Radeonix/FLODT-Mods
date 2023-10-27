label MeetTerra:

$ meetTerra=1
show bg GamesRoomMorning with dissolve
play music BlippyTrance
$ renpy.sound.play("audio/ModSFX/metal_pipe.mp3", loop=True)
show t annoyed at pos50t with dissolve
"As I walked into the games room, my eyes were drawn to a girl playing on a handheld game device."
q "..."
show t annoyed
"She looked deep in thought as her fingers moved and pressed buttons at lightning speed."
show t happy
with vpunch # Terra,1
stop sound
q "Woo! New high score!"
show t sad
q "Aw man, it's a shame I can't submit it."
show t surprised
t "Oh, 'sup dude."
show t neutral
t "Do you know what happened to the internet?"
m "What?"
show t worried
t "Ever since I came to this island, I haven't been able to get any signal at all."
show t sad
show t annoyed  at pos50t
t "I'm... literally going to die at this rate."
m "You okay?"
show t sad  at pos50t_fall1
t "Tell my followers... they were... the best..."
show t annoyed  at pos50t_fall2
with vpunch
t "...*Bleh*"
hide t with dissolve
"..."
"What does a person even do in this situation?"
m "...Are you okay?"
with vpunch
play sound MetalPipe
k "No worries, [name]. She'll be fine."
m "Oh, Hey Kat. What's up?"
k "We had to turn off all the internet to make sure no spoilers for the show get out."
k "Terra's just a bit overdramatic about it. You'll get used to it."
show t worried  at pos50t
with vpunch # Terra,1
t "Yo! You tell me I'm being overdramatic when you literally sent us back into the stone age!"
show t worried  at pos50t
show t annoyed
t "...With games, and electricity, and other things, but still!"
show t sad
t "Aw, I was so excited to stream for everybody when I got here."
t ";-;"
m "You're a streamer?"
show t happy
t "Yessir! That I am!"
show t neutral
t "I'm mostly a variety game streamer, but I also stream real life, too!"
show t sad
t "And I can't now! QAQ"
m "Maybe you could just record things, and post them later?"
show t neutral
t "I guess that's what I'll have to do, but that's so last year."
show t surprised
t "By the way, what's this whole show about?"
m "Wait... what?"
show t worried
t "I honestly have no idea what I just got into, regarding... pretty much everything to do with this show."
m "You didn't even do a little bit of research before you decided to come here?"
show t condescending
with vpunch
with vpunch # Terra,1
t "Hey hey, don't get in my face about this!"
show t angry
t "From what I heard from Kat, you didn't either!"
m "Hey, amnesia and not doing a little bit of research are totally different!"
show t annoyed
t "I forgot to do my due diligence, and you forgot your life!"
show t happy
t "Same deal!"
m "It's not the same deal!"
show t neutral
m "...Anyway, it's a dating show called {i}Find Love{/i}."
m "Kat can explain the rules in more detail, but it's pretty much what you expect from any generic dating TV show."
m "And my name's [name]. I'm what Kat calls the suitor."
show t surprised
t "Huh."
show t annoyed
t "So it's like a visual novel dating sim game, except I'm stuck in it, rather than getting to play it myself?"
m "I guess so?"
show t neutral
t "Well, since this is a game..."
stop music
with vpunch #count:2
with vpunch # Terra,1
show t angry
play music RocketPower
t "I'm gonna win it!!!"
m "I'm not sure that's the right way to approach dating, but -"
show t annoyed
t "LOOK OUT WORLD, TERRA'S COMING!"
show t angry
t "AND SHE ALWAYS WINS!"
play sound MetalPipe
hide t with dissolve
"..."
"Terra ran off with a fiery look in her eyes."
"I've got no idea where she's headed."
"But who would?"


if meetViolet == 1 and meetScarlett == 1 and meetTerra == 1 and meetAllie == 1:
    jump MetAllGirlsT


"I guess there's nothing left to do here."
menu:
    "I might as well head on over to..."

    "The Library" if meetScarlett != 1:
        jump MeetScarlett
    "The Kitchen" if meetViolet != 1:
        jump MeetViolet
    "The Games Room" if meetTerra != 1:
        jump MeetTerra
    "The Backyard" if meetAllie != 1:
        jump MeetAllie

label MetAllGirlsT:
stop music
play music ItemStore2
play sound MetalPipe
k "Alright, alright, enough messing around."
k "If you're on the show, and you're not an underpaid grunt, come to the front entrance of the mansion."
"I guess that includes me. I should start heading over."
with vpunch
k "That includes you too, Terra! I can see you playing, you know!"
show t angry  at pos50t
t "You're not the boss of me, Kat!"
"What have I gotten myself into?"
jump MetAllGirls
