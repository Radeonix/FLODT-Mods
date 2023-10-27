label MeetYui:

$ meetYui=1
show bg MansionIndoorsMorning with dissolve
play music Wholesome
m "Anybody home?"
show y worried at pos50y with dissolve
"My eyes were drawn to a girl wearing a white dress, pacing around the lobby."
m "Hey, what's up?"
show y surprised
q "Woah! Didn't see you there, I'm so sorry!"
show y laugh
q "Oh my gosh! It's really you, [name]!"
m "That's me! How did you know my name?"
show y surprised
q "It hasn't been that long, has it?"
show y happy
y "It's me, Yui! Yui Fushikawa!"
m "...?"
show y neutral
y "We went to the same high school way back?"
m "Come again?"
show y annoyed
y "Yeesh! You haven't changed one bit!"
y "Always forgetting everything important!"
show y angry
y "GRRRRRR!!!"
m "Wait, calm down! I know how it sounds, but I've got amnesia!"
show y annoyed
y "You don't expect me to believe that, do you?"
show y angry
y "You can't lie to your student council president! That's perjury!"
m "It's true, really! I wouldn't lie about this."
show y worried
y "...You really can't remember anything?"
m "Really. I wouldn't joke about this, promise."
show y sad
y "...Oh."
show y angry
y "I can't believe you forgot -"
show y blush
y "...!"
y "On second thought, that may be a good thing!"
m "How on earth could it be good to forget everything?"
show y annoyed
y "You know, moving on from the past is the best way to live, and all that!"
show y happy
y "Everyone has things from high school they'd rather forget, right?"
show y blush
y "Ha. Ha. Ha."
show y shy
y "Yep, yep, yep. Mmhm."
show y happy
y "Heh heh heh. It's good to see you, [name]. You haven't changed."
show y laugh
y "It feels just like when we used to fool around back then."
show y blush
y "Er... fool around, in like a family friendly sort of way! Pinky promise!"
m "It's good to see you too, Yui."
m "What brings you out here?"
show y happy
y "Oh, you know."
show y neutral
y "To be honest, dating apps or shows and all that really aren't my thing."
show y laugh
y "But I saw that you were..."
show y blush
y "...!"
show y angry with vpunch
# with vpunch # Yui,1

y "Whattaya making me say!!"

show y neutral
y "Um, besides that, welcome to the mansion!"
show y surprised
y "It's ginormous."
show y annoyed #at pos50y
y "I'll spare you from embarrassing yourself asking me and show you where my room is."
show y surprised
y "Ah, wait a second! I haven't cleaned it up yet!"
play sound MetalPipe
hide y with dissolve

"She rushed off before I could get in a word. Somehow, I get the sense that this has happened before."
"I guess I'll see her later."

menu:
    "I should get back to exploring the house - where to next?"

    "The Library":
        jump MeetScarlett
    "The Kitchen":
        jump MeetViolet
    "The Games Room":
        jump MeetTerra
    "The Backyard":
        jump MeetAllie
