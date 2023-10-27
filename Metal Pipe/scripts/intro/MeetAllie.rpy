label MeetAllie:

$ meetAllie=1
show bg Hills with dissolve
play music AlmostNew
"Wow. Calling this a backyard is like calling what happened to the Titanic a leak. The field goes farther than the eye can see."
"My eyes were quickly drawn to a girl running laps across the field."
"She's quick! She's getting closer, and closer, and..."
show a happy at pos50a with easeinright
"She slid to a stop in front of me."
show a laugh
a "Howdy, I'm Allie! It's nice to meet ya!"
show a happy
a "You're [name], right?"
m "That's -"
show a laugh

menu:
    a "Aah, I don't really care. Care for a jog, though?"

    "Sure!":
        jump SureJog
    "No thanks":
        jump NoJog

label SureJog:
    m "Sure, that sounds -"
    jump StartJog

label NoJog:
    m "Actually, I'd rather -"
    jump StartJog

label StartJog:
stop music
play music LeGrandChase
with vpunch
show a sassy
a "Alright, LET'S GOOOOO!!!!!!"
#@spawn ShakeCharacterlabel1 params:Allie,0 wait:false
play sound MetalPipe
with vpunch
"She grabbed my hand and pulled me with her at breakneck speed."
$ renpy.sound.play("audio/sfx/running_on_grass.mp3", loop=True) # running on grass
with vpunch
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH!!!!"
"She's so fast!! It takes all I have just to keep pace with her."
"The wind on my face feels nice, though. For some reason, I feel like I've missed this."
with vpunch
"Actually, I don't think I've ever gone this fastAAAAAAAAAAAAAAAAAAHHH!!"
show a laugh
a "Come on, come on! Keep it up! We'll have you in tip-top shape in no time, soldier!"
"Whatever nice thoughts I had floating in my head were thrown out by my newly assigned drill sergeant."
"I thought I signed up for a dating show, not a fitness show...!"
with vpunch
"*huff* *huff*"
"Alright, alright... I'm starting to hit a comfortable pace."
show a sassy
a "Is that all you've got?"
"Allie was widening the distance between us, with a smile on her face."
"Call me simple, but I started to run as fast as I could."
with vpunch
m "Ahhhh!!!!!!!!!"
"I gained more and more speed, and watched as Allie slowly fell behind."
show a surprised
a "Wow, you're running even faster than my dad did when he left."
with vpunch
show a sassy
"What the -"
"I unconsciously slowed down, my face contorted with shock."
"In just that single moment, she caught up, and quickly surpassed me."
show a laugh
a "I'm kidding, geez! No need to take everything so seriously."
show a happy
a "The bastard died before he ever got a chance to."
m "Oh, I'm so s-"
show a angry
a "Don't be, I killed him myself."
with vpunch
show a sassy
"Wha -"
show a laugh
a "The look on your face is hilarious!"
show a happy
a "Don't worry so much, [name]. I'm kidding, kidding."
show a angry
a "Or am I?"
"I felt my heart start to give out less from the running, and more from the emotional rollercoaster."
"..."
stop music
show a happy
play music CheeryMonday
stop sound # RunGrass
"We finished jogging a few minutes later."
"I'm completely out of breath."
show a laugh
a "That was fun, [name]!"
m "*huff*"
show a neutral
a "Let's run again sometime."
"I fell to my knees to catch my breath, and watched as she walked away effortlessly."
show a sassy
a "But you'll have to be faster than that to keep up with me, suitor!"
hide a with dissolve
"I laid on the grass, like an obese walrus gasping for air."
"Is this how I die?"
"*huff* *huff*"
"I don't think I'll have to be worried about telling Allie the truth, with how hard it is to breathe."
"*huff*"
"...I think I'll live, at least for now."
"I rolled onto my back and relaxed for a moment."

if meetViolet == 1 and meetScarlett == 1 and meetTerra == 1 and meetAllie == 1:
    jump MetAllGirlsA

menu:
    "After I get up, I guess I'll head on over to..."

    "The Library" if meetScarlett != 1:
        jump MeetScarlett
    "The Kitchen" if meetViolet != 1:
        jump MeetViolet
    "The Games Room" if meetTerra != 1:
        jump MeetTerra
    "The Backyard" if meetAllie != 1:
        jump MeetAllie


label MetAllGirlsA:
stop music
play music ItemStore2
play sound MetalPipe
k "Alright, alright, enough messing around."
k "If you're on the show, and you're not an underpaid grunt, come to the front of the mansion."
"I guess that includes me. I should start heading over."
with vpunch
k "That includes you too, Terra! I can see you playing, you know!"
t "You're not the boss of me!"
"What have I gotten myself into?"
jump MetAllGirls
