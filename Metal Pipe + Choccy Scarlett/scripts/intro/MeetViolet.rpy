label MeetViolet:

$ meetViolet=1
play sound MetalPipe # loop:true
show bg KitchenMorning with dissolve
play music Morning
show b1 worried at pos60b with dissolve# former look:left at pos60
show b2 worried at pos75b with dissolve# former look:left at pos75
show b3 worried at pos90b with dissolve# former look:left at pos90
show v serious at pos30v with dissolve# former look:right at pos30
q "One.... These ribs are well done."
show b1 happy
b1 "Thank you, ma'am!!"
show v angry
with vpunch
q "They were supposed to be medium rare! Please remake them all before the hour is up."
show b1 sad
show v annoyed
b1 "I knew we should have just worked in accounting!"
show v laugh
q "Then I've just the opportunity for you, One - I've just bought one of the neighboring islands, and I need someone to balance the books."
show v happy
q "Please have that finished by nightfall - and don't forget about the ribs!"
show b1 worried
b1 "I take it back!!"
show v laugh
q "The side dishes are magnificent, Two! Keep it up, you diligent worker, you!"
show v happy
show b2 blush
b2 "Aw shucks! You're too kind, ma'am."
show b2 happy
b2 "I don't get what you're complaining about, bro."
show b2 laugh
b2 "Violet's amazing, and she's even volunteering to help us lowly peons!"
show v laugh
v "This soup is simply delightful! Good work, Three."
show b3 blush
b3 "T-Thank you, Violet! Man, she's a hundred times better than when Four bossed us around."
show b2 laugh
b2 "I couldn't agree more, bro!"
show v annoyed
v "One, if you insist on taking so long on the meatballs, perhaps we'll use your meatballs instead."
show v laugh
v "Just kidding. Though upon further thought, you'd never need them anyway, so maybe...?"
show b3 laugh
b3 "She's such an angel."
show b1 sad
b1 "Are we even talking about the same person?"
hide b1 with dissolve
hide b2 with dissolve
hide b3 with dissolve
m "Hey there - got a second to chat?"
show v surprised  at pos50v with dissolve # former look:left
v "Pardon me, I didn't see you there. Just one second."
show v sassy
v "I've got to clean up the soup that One set on fire earlier - is that even possible?"
m "Anything's possible if you put your mind to it."
show v worried
v "Evidently, the same is true... if you lack a mind completely. Ah, public education..."
show v laugh
v "...Just kidding."
show v laugh at pos30v with dissolve # former look:right
show b1 sad at pos60b with dissolve# former look:left
b1 "Hey, that was uncalled for!"
show b1 worried
show b2 worried at pos75b with dissolve # former look:left
b2 "Actually... we think the same about you on a daily basis."
show b3 laugh at pos90b with dissolve # former look:left
b3 "I can confirm that!"
show b1 sad
b1 "I wish mom never had you guys!"
hide b1 with dissolve
hide b2 with dissolve
hide b3 with dissolve

show v sassy  at pos50v with dissolve # former look:left
v "Apologies for the delay, I'm finished now. I'm Violet, Violet Valentine."
show v happy
v "The pleasure is yours, [name]."
m "You already know who I am?"
show v laugh
v "I imagine each contestant does - Flying all the way out here, for a whole week, for a blind date? ...No one could be that unintelligent."

if meetTerra == 0:
    jump pastTerraJoke

if meetTerra == 1:
    jump TerraJoke

label TerraJoke:
    show bg GamesRoomMorning # with dissolve
    hide v # with dissolve
    show t worried  at pos50t # with dissolve
    with vpunch
    t "*sneeze*"
    t "...?"
    hide t #with dissolve
    show bg KitchenMorning #with dissolve
    show v sassy at pos50v #with dissolve
    jump pastTerraJoke

label pastTerraJoke:
 # former look:left
v "I do hope you are worthy of being the suitor - you'll find that courting a lady is a different sport than the other girls."
show b2 surprised at pos85b with dissolve
b2 "It's true! She's one of the two daughters of the Valentine Family!"
show b3 laugh at pos15b with dissolve # former look:left
b3 "They're even richer than Royal Black Media!"
#show d annoyed
play sound MetalPipe
d "Alright, Three. Your pay's cut by 50\%. Enjoy your even shittier instant noodles."
show b3 sad
b3 "...Is it too late to go back to school?"
hide b3 with dissolve
hide b2 with dissolve
show v laugh  at pos50v # former look:left
v "I am, how to say, fascinated... I'd like to see what makes you so special."
show v sassy
v "You look... fairly average to me."
m "I guess you'll be in for a surprise, Violet."
show v happy
v "I do like a -"
stop music
#; BOOOM!!!"
stop sound # Kitchen
play sound MetalPipe
with vpunch
show v surprised

"A deafening explosion blasted through the kitchen."
show v annoyed
v "..."
show v laugh
play music Morning
v "The spaghetti tonight will be, how to say, a little different - I hope you do not mind."
m "You're not really putting One on the menu, right?"
show v neutral
v "....."
m "......."
show v laugh
hide v with dissolve
with vpunch
v "...One, why is there a hole in the ceiling?"
"...Looks like they'll be busy in the kitchen for a while."


if meetViolet == 1 and meetScarlett == 1 and meetTerra == 1 and meetAllie == 1:
    jump MetAllGirlsV

menu:
    "I decided to head over to..."

    "The Library" if meetScarlett != 1:
        jump MeetScarlett
    "The Kitchen" if meetViolet != 1:
        jump MeetViolet
    "The Games Room" if meetTerra != 1:
        jump MeetTerra
    "The Backyard" if meetAllie != 1:
        jump MeetAllie

label MetAllGirlsV:
    stop music
    play music ItemStore2
    play sound MetalPipe
    k "Alright, alright, enough messing around."
    k "If you're on the show, and you're not an underpaid grunt, come to the main entrance of the mansion."
    "...I guess that includes me. I should start heading over."
    with vpunch
    k "...That includes you too, Terra! I can see you playing, you know!"
    t "You're not the boss of me!"
    "...What have I gotten myself into?"
    jump MetAllGirls
