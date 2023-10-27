# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the name of the character.

# Declare Character Speakers
#define e2 = Character(" ", window_background="gui/textbox_trans.png")
#define a = Character("Aphrodite", namebox_background=AlphaMask(Solid("#ff69b4"), "gui/namebox.png"))

# the _(' X ') is to enable translation of names

define n = Character(" ", namebox_background=AlphaMask(Solid("#000000"), "gui/namebox.png", show_two_window=True))
define m = Character(_('You'), namebox_background=AlphaMask(Solid("#000000"), "gui/namebox.png", show_two_window=True))

define a = Character(_('Allie'), namebox_background=AlphaMask(Solid("#000000"), "gui/namebox.png", show_two_window=True))
define k = Character(_('Kat'), namebox_background=AlphaMask(Solid("#000000"), "gui/namebox.png", show_two_window=True))
define s = Character(_('Scarlett'), namebox_background=AlphaMask(Solid("#000000"), "gui/namebox.png"))
define t = Character(_('Terra'), namebox_background=AlphaMask(Solid("#000000"), "gui/namebox.png"))
define v = Character(_('Violet'), namebox_background=AlphaMask(Solid("#000000"), "gui/namebox.png"))
define y = Character(_('Yui'), namebox_background=AlphaMask(Solid("#000000"), "gui/namebox.png"))

define d = Character(_('Damian'), namebox_background=AlphaMask(Solid("#000000"), "gui/namebox.png", show_two_window=True))
define b1 = Character(_('One'), namebox_background=AlphaMask(Solid("#000000"), "gui/namebox.png", show_two_window=True))
define b2 = Character(_('Two'), namebox_background=AlphaMask(Solid("#000000"), "gui/namebox.png"))
define b3 = Character(_('Three'), namebox_background=AlphaMask(Solid("#000000"), "gui/namebox.png"))
define b4 = Character(_('Four'), namebox_background=AlphaMask(Solid("#000000"), "gui/namebox.png"))
define b5 = Character(_('Five'), namebox_background=AlphaMask(Solid("#000000"), "gui/namebox.png"))
define b = Character(_('Brothers Five'), namebox_background=AlphaMask(Solid("#000000"), "gui/namebox.png"))

define q = Character(_('???'), namebox_background=AlphaMask(Solid("#000000"), "gui/namebox.png"))

define all = Character(_('All'), namebox_background=AlphaMask(Solid("#000000"), "gui/namebox.png"))
define crowd = Character(_('Crowd'), namebox_background=AlphaMask(Solid("#000000"), "gui/namebox.png"))

# Define Character Sprites
image a angry_hatless:
    "images/sprites/allie/Allie Angry Hatless.png"
    zoom 0.7
image a angry:
    "images/sprites/allie/Allie Angry.png"
    zoom 0.7
image a annoyed:
    "images/sprites/allie/Allie Annoyed.png"
    zoom 0.7
image a blush:
    "images/sprites/allie/Allie Blushing.png"
    zoom 0.7
image a happy:
    "images/sprites/allie/Allie Happy.png"
    zoom 0.7
image a laugh:
    "images/sprites/allie/Allie Laugh.png"
    zoom 0.7
image a neutral:
    "images/sprites/allie/Allie Neutral.png"
    zoom 0.7
image a sad:
    "images/sprites/allie/Allie Sad.png"
    zoom 0.7
image a sassy:
    "images/sprites/allie/Allie Sassy.png"
    zoom 0.7
image a serious:
    "images/sprites/allie/Allie Serious.png"
    zoom 0.7
image a surprised:
    "images/sprites/allie/Allie Surprised.png"
    zoom 0.7
image a worried:
    "images/sprites/allie/Allie Worried.png"
    zoom 0.7

image d angry:
    "images/sprites/damian/Damian Angry.png"
    zoom 0.7

image d annoyed:
    "images/sprites/damian/Damian Annoyed.png"
    zoom 0.7
image d evil_smile:
    "images/sprites/damian/Damian Evil Smile.png"
    zoom 0.7
image d happy:
    "images/sprites/damian/Damian Happy.png"
    zoom 0.7
image d laugh:
    "images/sprites/damian/Damian Laugh.png"
    zoom 0.7
image d neutral:
    "images/sprites/damian/Damian Neutral.png"
    zoom 0.7
image d sassy:
    "images/sprites/damian/Damian Sassy.png"
    zoom 0.7
image d serious:
    "images/sprites/damian/Damian Serious.png"
    zoom 0.7
image d surprised:
    "images/sprites/damian/Damian Surprised.png"
    zoom 0.7
image d worried:
    "images/sprites/damian/Damian Worried.png"
    zoom 0.7

image b1 angry:
    "images/sprites/grunt 1/Grunt 1 Angry.png"
    zoom 0.7
image b1 annoyed:
    "images/sprites/grunt 1/Grunt 1 Annoyed.png"
    zoom 0.7
image b1 blush:
    "images/sprites/grunt 1/Grunt 1 Blush.png"
    zoom 0.7
image b1 bored:
    "images/sprites/grunt 1/Grunt 1 Bored.png"
    zoom 0.7
image b1 condescending:
    "images/sprites/grunt 1/Grunt 1 Condescending.png"
    zoom 0.7
image b1 happy:
    "images/sprites/grunt 1/Grunt 1 Happy.png"
    zoom 0.7
image b1 laugh:
    "images/sprites/grunt 1/Grunt 1 Laugh.png"
    zoom 0.7
image b1 neutral:
    "images/sprites/grunt 1/Grunt 1 Neutral.png"
    zoom 0.7
image b1 sad:
    "images/sprites/grunt 1/Grunt 1 Sad.png"
    zoom 0.7
image b1 serious:
    "images/sprites/grunt 1/Grunt 1 Serious.png"
    zoom 0.7
image b1 sassy:
    "images/sprites/grunt 1/Grunt 1 Sassy.png"
    zoom 0.7
image b1 surprised:
    "images/sprites/grunt 1/Grunt 1 Surprised.png"
    zoom 0.7
image b1 worried:
    "images/sprites/grunt 1/Grunt 1 Worried.png"
    zoom 0.7

image b2 angry:
    "images/sprites/grunt 2/Grunt 2 Angry.png"
    zoom 0.7
image b2 annoyed:
    "images/sprites/grunt 2/Grunt 2 Annoyed.png"
    zoom 0.7
image b2 blush:
    "images/sprites/grunt 2/Grunt 2 Blush.png"
    zoom 0.7
image b2 bored:
    "images/sprites/grunt 2/Grunt 2 Bored.png"
    zoom 0.7
image b2 condescending:
    "images/sprites/grunt 2/Grunt 2 Condescending.png"
    zoom 0.7
image b2 happy:
    "images/sprites/grunt 2/Grunt 2 Happy.png"
    zoom 0.7
image b2 laugh:
    "images/sprites/grunt 2/Grunt 2 Laugh.png"
    zoom 0.7
image b2 neutral:
    "images/sprites/grunt 2/Grunt 2 Neutral.png"
    zoom 0.7
image b2 sad:
    "images/sprites/grunt 2/Grunt 2 Sad.png"
    zoom 0.7
image b2 serious:
    "images/sprites/grunt 2/Grunt 2 Serious.png"
    zoom 0.7
image b2 sassy:
    "images/sprites/grunt 2/Grunt 2 Sassy.png"
    zoom 0.7
image b2 surprised:
    "images/sprites/grunt 2/Grunt 2 Surprised.png"
    zoom 0.7
image b2 worried:
    "images/sprites/grunt 2/Grunt 2 Worried.png"
    zoom 0.7

image b3 angry:
    "images/sprites/grunt 3/Grunt 3 Angry.png"
    zoom 0.7
image b3 annoyed:
    "images/sprites/grunt 3/Grunt 3 Annoyed.png"
    zoom 0.7
image b3 blush:
    "images/sprites/grunt 3/Grunt 3 Blush.png"
    zoom 0.7
image b3 bored:
    "images/sprites/grunt 3/Grunt 3 Bored.png"
    zoom 0.7
image b3 condescending:
    "images/sprites/grunt 3/Grunt 3 Condescending.png"
    zoom 0.7
image b3 happy:
    "images/sprites/grunt 3/Grunt 3 Happy.png"
    zoom 0.7
image b3 laugh:
    "images/sprites/grunt 3/Grunt 3 Laugh.png"
    zoom 0.7
image b3 neutral:
    "images/sprites/grunt 3/Grunt 3 Neutral.png"
    zoom 0.7
image b3 sad:
    "images/sprites/grunt 3/Grunt 3 Sad.png"
    zoom 0.7
image b3 serious:
    "images/sprites/grunt 3/Grunt 3 Serious.png"
    zoom 0.7
image b3 sassy:
    "images/sprites/grunt 3/Grunt 3 Sassy.png"
    zoom 0.7
image b3 surprised:
    "images/sprites/grunt 3/Grunt 3 Surprised.png"
    zoom 0.7
image b3 worried:
    "images/sprites/grunt 3/Grunt 3 Worried.png"
    zoom 0.7

image b4 angry:
    "images/sprites/grunt 4/Grunt 4 Angry.png"
    zoom 0.7
image b4 annoyed:
    "images/sprites/grunt 4/Grunt 4 Annoyed.png"
    zoom 0.7
image b4 blush:
    "images/sprites/grunt 4/Grunt 4 Blush.png"
    zoom 0.7
image b4 bored:
    "images/sprites/grunt 4/Grunt 4 Bored.png"
    zoom 0.7
image b4 condescending:
    "images/sprites/grunt 4/Grunt 4 Condescending.png"
    zoom 0.7
image b4 happy:
    "images/sprites/grunt 4/Grunt 4 Happy.png"
    zoom 0.7
image b4 laugh:
    "images/sprites/grunt 4/Grunt 4 Laugh.png"
    zoom 0.7
image b4 neutral:
    "images/sprites/grunt 4/Grunt 4 Neutral.png"
    zoom 0.7
image b4 sad:
    "images/sprites/grunt 4/Grunt 4 Sad.png"
    zoom 0.7
image b4 serious:
    "images/sprites/grunt 4/Grunt 4 Serious.png"
    zoom 0.7
image b4 sassy:
    "images/sprites/grunt 4/Grunt 4 Sassy.png"
    zoom 0.7
image b4 surprised:
    "images/sprites/grunt 4/Grunt 4 Surprised.png"
    zoom 0.7
image b4 worried:
    "images/sprites/grunt 4/Grunt 4 Worried.png"
    zoom 0.7

image b5 angry:
    "images/sprites/grunt 5/Grunt 5 Angry.png"
    zoom 0.7
image b5 annoyed:
    "images/sprites/grunt 5/Grunt 5 Annoyed.png"
    zoom 0.7
image b5 blush:
    "images/sprites/grunt 5/Grunt 5 Blush.png"
    zoom 0.7
image b5 bored:
    "images/sprites/grunt 5/Grunt 5 Bored.png"
    zoom 0.7
image b5 condescending:
    "images/sprites/grunt 5/Grunt 5 Condescending.png"
    zoom 0.7
image b5 happy:
    "images/sprites/grunt 5/Grunt 5 Happy.png"
    zoom 0.7
image b5 laugh:
    "images/sprites/grunt 5/Grunt 5 Laugh.png"
    zoom 0.7
image b5 neutral:
    "images/sprites/grunt 5/Grunt 5 Neutral.png"
    zoom 0.7
image b5 sad:
    "images/sprites/grunt 5/Grunt 5 Sad.png"
    zoom 0.7
image b5 serious:
    "images/sprites/grunt 5/Grunt 5 Serious.png"
    zoom 0.7
image b5 sassy:
    "images/sprites/grunt 5/Grunt 5 Sassy.png"
    zoom 0.7
image b5 surprised:
    "images/sprites/grunt 5/Grunt 5 Surprised.png"
    zoom 0.7
image b5 worried:
    "images/sprites/grunt 5/Grunt 5 Worried.png"
    zoom 0.7

image k angry:
    "images/sprites/kat/Katherine Angry.png"
    zoom 0.7
image k annoyed:
    "images/sprites/kat/Katherine Annoyed.png"
    zoom 0.7
image k blush:
    "images/sprites/kat/Katherine Blushing.png"
    zoom 0.7
image k bored:
    "images/sprites/kat/Katherine Bored.png"
    zoom 0.7
image k happy:
    "images/sprites/kat/Katherine Happy.png"
    zoom 0.7
image k laugh:
    "images/sprites/kat/Katherine Laugh.png"
    zoom 0.7
image k neutral:
    "images/sprites/kat/Katherine Neutral.png"
    zoom 0.7
image k sad:
    "images/sprites/kat/Katherine Sad.png"
    zoom 0.7
image k sassy:
    "images/sprites/kat/Katherine Sassy.png"
    zoom 0.7
image k serious:
    "images/sprites/kat/Katherine Serious.png"
    zoom 0.7
image k surprised:
    "images/sprites/kat/Katherine Surprised.png"
    zoom 0.7
image k flirt:
    "images/sprites/kat/Katherine Flirt.png"
    zoom 0.7
image k worried:
    "images/sprites/kat/Katherine Worried.png"
    zoom 0.7

image s angry:
    "images/sprites/scarlett/Scarlett Angry.png"
    zoom 0.7
image s annoyed:
    "images/sprites/scarlett/Scarlett Annoyed.png"
    zoom 0.7
image s flirt:
    #"images/sprites/scarlett/Scarlett Flirt.png"
    "images/Mod_Images/scarlett/Scarlett_Choccy_Milk.png"
    zoom 0.9
image s happy:
    "images/sprites/scarlett/Scarlett Happy.png"
    zoom 0.7
image s laugh:
    "images/sprites/scarlett/Scarlett Laugh.png"
    zoom 0.7
image s neutral:
    "images/sprites/scarlett/Scarlett Neutral.png"
    zoom 0.7
image s sad:
    "images/sprites/scarlett/Scarlett Sad.png"
    zoom 0.7
image s sassy:
    "images/sprites/scarlett/Scarlett Sassy.png"
    zoom 0.7
image s serious:
    "images/sprites/scarlett/Scarlett Serious.png"
    zoom 0.7
image s surprised:
    "images/sprites/scarlett/Scarlett Surprised.png"
    zoom 0.7
image s worried:
    "images/sprites/scarlett/Scarlett Worried.png"
    zoom 0.7
image s tease:
    "images/sprites/scarlett/Scarlett Tease.png"
    zoom 0.7

image t angry:
    "images/sprites/terra/Terra Angry.png"
    zoom 0.7
image t annoyed:
    "images/sprites/terra/Terra Annoyed.png"
    zoom 0.7
image t blush:
    "images/sprites/terra/Terra Blushing.png"
    zoom 0.7
image t condescending:
    "images/sprites/terra/Terra Condescending.png"
    zoom 0.7
image t gaming:
    "images/sprites/terra/Terra Gaming.png"
    zoom 0.7
image t happy:
    "images/sprites/terra/Terra Happy.png"
    zoom 0.7
#image t laugh = "images/sprites/terra/Terra Laugh.png"
image t neutral:
    "images/sprites/terra/Terra Neutral.png"
    zoom 0.7
image t sad:
    "images/sprites/terra/Terra Sad.png"
    zoom 0.7
#image t sassy = "images/sprites/terra/Terra Sassy.png"
image t serious:
    "images/sprites/terra/Terra Serious.png"
    zoom 0.7
image t surprised:
    "images/sprites/terra/Terra Surprised.png"
    zoom 0.7
image t worried:
    "images/sprites/terra/Terra Worried.png"
    zoom 0.7

#image t bored = "images/sprites/terra/Terra Bored.png"

image v angry:
    "images/sprites/violet/Violet Angry.png"
    zoom 0.7
image v annoyed:
    "images/sprites/violet/Violet Annoyed.png"
    zoom 0.7
image v blush:
    "images/sprites/violet/Violet Blushing.png"
    zoom 0.7
image v happy:
    "images/sprites/violet/Violet Happy.png"
    zoom 0.7
image v laugh:
    "images/sprites/violet/Violet Laughing.png"
    zoom 0.7
image v neutral:
    "images/sprites/violet/Violet Neutral.png"
    zoom 0.7
image v sad:
    "images/sprites/violet/Violet Sad.png"
    zoom 0.7
image v sassy:
    "images/sprites/violet/Violet Sassy.png"
    zoom 0.7
image v serious:
    "images/sprites/violet/Violet Serious.png"
    zoom 0.7
image v surprised:
    "images/sprites/violet/Violet Surprised.png"
    zoom 0.7
image v worried:
    "images/sprites/violet/Violet Worried.png"
    zoom 0.7

image y angry:
    "images/sprites/yui/Yui Angry.png"
    zoom 0.7
image y annoyed:
    "images/sprites/yui/Yui Annoyed.png"
    zoom 0.7
image y blush:
    "images/sprites/yui/Yui Blushing.png"
    zoom 0.7
image y happy:
    "images/sprites/yui/Yui Happy.png"
    zoom 0.7
image y laugh:
    "images/sprites/yui/Yui Laugh.png"
    zoom 0.7
image y neutral:
    "images/sprites/yui/Yui Neutral.png"
    zoom 0.7
image y sad:
    "images/sprites/yui/Yui Sad.png"
    zoom 0.7
#image y sassy = "images/sprites/yui/Yui Sassy.png"
image y serious:
    "images/sprites/yui/Yui Serious.png"
    zoom 0.7
image y shy:
    "images/sprites/yui/Yui Shy.png"
    zoom 0.7
image y surprised:
    "images/sprites/yui/Yui Surprised.png"
    zoom 0.7
image y worried:
    "images/sprites/yui/Yui Worried.png"
    zoom 0.7



# Backgrounds
image bg BeachEvening:
    "images/bg/beach_evening.png"
    zoom 0.5
image bg BeachMorning:
    "images/bg/beach_morning.png"
    zoom 0.5
image bg BeachNight:
    "images/bg/beach_night.png"
    zoom 0.5
image bg Black:
    "images/bg/Black.jpg"
    #zoom 0.5 #black.png
image bg black:
    "images/bg/Black.jpg"
    #zoom 0.5 #black.png
image bg Hills:
    "images/bg/bunny_field.png"
    zoom 0.5
image bg Coliseum:
    "images/bg/coliseum.png"
    zoom 0.78
image bg Episode1:
    "images/bg/episode_1_banner.png"
    #zoom 0.5
image bg Episode2:
    "images/bg/episode_2_banner.png"
    #zoom 0.5
image bg Episode3:
    "images/bg/episode_3_banner.png"
    #zoom 0.5
image bg Episode4:
    "images/bg/episode_4_banner.png"
    #zoom 0.5
image bg Episode5:
    "images/bg/episode_5_banner.png"
    #zoom 0.5
image bg Episode6:
    "images/bg/episode_6_banner.png"
    #zoom 0.5
image bg Episode7:
    "images/bg/episode_7_banner.png"
    #zoom 0.5
image bg GamesRoomEvening:
    "images/bg/gaming_room_evening.png"
    zoom 0.8
image bg GamesRoomMorning:
    "images/bg/gaming_room_morning.png"
    zoom 0.8
image bg GamesRoomNight:
    "images/bg/gaming_room_night.png"
    zoom 0.8
image bg HangarMorningBurns:
    "images/bg/hangar_burns_morning.png"
    zoom 0.4
image bg HangarNightBurns:
    "images/bg/hangar_burns_night.png"
    zoom 0.4
image bg HangarNoonBurns:
    "images/bg/hangar_burns_noon.png"
    zoom 0.4
image bg HangarMorning:
    "images/bg/hangar_morning.png"
    zoom 0.4
image bg HangarNight:
    "images/bg/hangar_night.png"
    zoom 0.4
image bg HangarNoon:
    "images/bg/hangar_noon.png"
    zoom 0.5
image bg Hospital:
    "images/bg/hospital.png"
    zoom 0.5
image bg KitchenMorning:
    "images/bg/kitchen_morning.png"
    zoom 0.8
image bg KitchenNight:
    "images/bg/kitchen_night.png"
    zoom 0.8
image bg KitchenNoon:
    "images/bg/kitchen_noon.png"
    zoom 0.8
image bg Lab:
    "images/bg/lab.png"
    zoom 0.65
image bg LakeEvening:
    "images/bg/lake_evening.png"
    zoom 0.54
image bg LakeMorning:
    "images/bg/lake_morning.png"
    zoom 0.54
image bg LakeNight:
    "images/bg/lake_night.png"
    zoom 0.54
image bg Library:
    "images/bg/library.png"
    zoom 0.4
image bg MansionEvening:
    "images/bg/mansion_evening.png"
    zoom 0.85
image bg MansionMorning:
    "images/bg/mansion_morning.png"
    zoom 0.85
image bg MansionNight:
    "images/bg/mansion_night.png"
    zoom 0.85
image bg MansionIndoorsNoon:
    "images/bg/mansion_indoors_noon.png"
    zoom 0.5
image bg MansionIndoorsMorning:
    "images/bg/mansion_indoors_morning.png"
    zoom 0.5
image bg MansionIndoorsNight:
    "images/bg/mansion_indoors_night.png"
    zoom 0.5

image bg Nightclub:
    "images/bg/nightclub.png"
    zoom 0.5

image bg PlaneBar:
     "images/bg/plane_morning.png"
     zoom 0.5

#image bg PlaneNight = "images/bg/plane_night.png"
image bg ProducerRoom:
    "images/bg/producer_room.png"
    zoom 0.37

image bg RoadEvening:
    "images/bg/road_evening.png"
    zoom 0.7
image bg RoadMorning:
    "images/bg/road_morning.png"
    zoom 0.7
image bg RoadNight:
    "images/bg/road_night.png"
    zoom 0.7
# image bg tv_background = "images/bg/tv_background.png"
image bg Palace:
    "images/bg/underwater_restaurant.png"
    zoom 0.54

image bg BoatMorning:
    "images/bg/yacht_morning.jpg"
    zoom 1
image bg BoatNight:
    "images/bg/yacht_night.jpg"
    zoom 1
image bg BoatNoon:
    "images/bg/yacht_noon.jpg"
    zoom 1

image bg RoomMorning:
    "images/bg/your_bedroom_morning.png"
    zoom 0.8
image bg RoomNight:
    "images/bg/your_bedroom_night.png"
    zoom 0.8
image bg RoomNoon:
    "images/bg/your_bedroom_noon.png"
    zoom 0.8

# Define CGs
image bg AllieBoat:
    "images/cg/allie_boat.png"
    zoom 0.5
image bg BoatEndingAllie:
    "images/cg/allie_ending.png"
    zoom 0.5
image bg AllieRollerblading:
    "images/cg/allie_rollerblading.png"
    zoom 0.5

image bg KatControl:
    "images/cg/kat_control.png"
    zoom 0.5
image bg TrueEndingKat:
    "images/cg/kat_ending.png"
    zoom 0.5
image bg KatInYourRoom:
    "images/cg/kat_in_your_room.png"
    zoom 0.5
image bg KatShootingYou:
    "images/cg/kat_shoots_you_sad.png"
    zoom 0.5
image bg KatShootingYouSmug:
    "images/cg/kat_shoots_you_smirk.png"
    zoom 0.5

image bg BoatEndingScarlett:
    "images/cg/scarlett_ending.jpg" # the only JPG by accident lol
    zoom 0.5
image bg ScarlettNightclub:
    "images/cg/scarlett_nightclub.png"
    zoom 0.5
image bg ScarlettReading:
    "images/cg/scarlett_reading.png"
    zoom 0.5
image bg ScarlettShooting:
    "images/cg/scarlett_shooting.png"
    zoom 0.5

image bg TerraGaming:
    "images/cg/terra_gaming.png"
    zoom 0.5
image bg BoatEndingTerra:
    "images/cg/terra_ending.png"
    zoom 0.5
image bg TerraProposal:
    "images/cg/terra_proposal.png"
    zoom 0.5

image bg VioletBaking:
    "images/cg/violet_baking.png"
    zoom 0.76
image bg BoatEndingViolet:
    "images/cg/violet_ending.png"
    zoom 0.5
image bg VioletPicnic:
    "images/cg/violet_picnic.png"
    zoom 0.5

image bg YuiHoldingBunny:
    "images/cg/yui_bunny.png"
    zoom 0.5
image bg BoatEndingYui:
    "images/cg/yui_ending.png"
    zoom 0.5
image bg YuiInField:
    "images/cg/yui_field.png"
    zoom 0.5

# Define OST
define audio.AlmostBliss = "audio/ost/Almost Bliss.mp3"
define audio.AlmostNew = "audio/ost/Almost New.mp3"
define audio.Americana = "audio/ost/Americana.mp3"
define audio.Bittersweet = "audio/ost/Bittersweet.mp3"
define audio.BlippyTrance = "audio/ost/Blippy Trance.mp3"
define audio.CarpeDiem = "audio/ost/Carpe Diem.mp3"
define audio.CheeryMonday = "audio/ost/Cheery Monday.mp3"
define audio.CrinolineDreams = "audio/ost/Crinoline Dreams.mp3"
define audio.DevastationAndRevenge = "audio/ost/Devastation and Revenge.mp3"
define audio.DrumLoop = "audio/ost/Drum Loop 1 140bpm.wav"
define audio.EbbsAndFlows = "audio/ost/Ebbs And Flows Preview by Kevin MacLeod.mp3"
define audio.ElectricCabello = "audio/ost/Electric Cabello.mp3"
define audio.Eternity = "audio/ost/Eternity.mp3"
define audio.FutureGladiator = "audio/ost/Future Gladiator.mp3"
define audio.GettingItDone = "audio/ost/Getting it Done.mp3"
define audio.HalfMystery = "audio/ost/Half Mystery.mp3"
define audio.ICanFeelItComing = "audio/ost/I Can Feel it Coming.mp3"
define audio.JazzBrunch = "audio/ost/Jazz Brunch.mp3"
define audio.LeGrandChase = "audio/ost/Le Grand Chase.mp3"
define audio.LeavingHome = "audio/ost/Leaving Home.mp3"
define audio.LoveTheme = "audio/ost/Love Theme FLODT.mp3"
define audio.MasterDisorder = "audio/ost/Master Disorder.mp3"
define audio.Meadow = "audio/ost/Meadow.wav"
define audio.JazzInParis = "audio/ost/Jazz-In-Paris.mp3"
define audio.MiamiNights = "audio/ost/Miami Nights - Extended Theme.mp3"
define audio.Morning = "audio/ost/Morning Theme FLODT.mp3"
define audio.MoveForward = "audio/ost/Move Forward.mp3"
define audio.MovementProposition = "audio/ost/Movement Proposition.mp3"
define audio.NightInVenice = "audio/ost/Night in Venice.mp3"
define audio.Overcast = "audio/ost/Overcast.mp3"
define audio.PastSadness = "audio/ost/Past Sadness.mp3"
define audio.PromisingRelationship = "audio/ost/Promising Relationship.mp3"
define audio.RavingEnergy = "audio/ost/Raving Energy.mp3"
define audio.RocketPower = "audio/ost/Rocket Power.mp3"
define audio.RomanticJazz = "audio/ost/Romantic Jazz FLODT.mp3"
define audio.RunAmok = "audio/ost/Run Amok.mp3"
define audio.RynosTheme = "audio/ost/Rynos Theme.mp3"
define audio.scores_short = "audio/ost/Scores SHORT.wav"
define audio.ShavingMirror = "audio/ost/Shaving Mirror.mp3"
define audio.MysteryLoop = "audio/ost/Short Mystery LOOP.wav"
define audio.Sincerely = "audio/ost/Sincerely.mp3"
define audio.SmileEnding = "audio/ost/Smile Ending FLODT.mp3"
define audio.Smile = "audio/ost/Smile! Everyone can see FLODT.mp3"
define audio.SmoothLovin = "audio/ost/Smooth Lovin.mp3"
define audio.TakeAChance = "audio/ost/Take a Chance.mp3"
define audio.TechLive = "audio/ost/Tech Live.mp3"
define audio.TheShowMustBeGo = "audio/ost/The Show Must Be Go.mp3"
define audio.TouchingMomentsOne = "audio/ost/Touching Moments One - Pulse.mp3"
define audio.TouchingMoments = "audio/ost/Touching Moments One - Pulse.mp3"
#define audio.touching_moments_two = "audio/ost/Touching Moments One - Pulse 1.mp3"
define audio.Trailer = "audio/ost/Trailer FLODT.mp3"
define audio.Twisting = "audio/ost/Twisting.mp3"
define audio.Wholesome = "audio/ost/Wholesome.mp3"
define audio.ElectroCabello = "audio/ost/Electro Cabello.mp3"


# missing SFX
define audio.DoorKnock = "audio/sfx/door_knock.mp3"
define audio.Shutdown = "audio/sfx/magic_spell.wav"
define audio.PlaneCrash = "audio/sfx/explosion.mp3"
# Define SFX
define audio.AnimeShine = "audio/sfx/anime_shine.mp3"
define audio.BambooHit = "audio/sfx/bamboo_hit.mp3"
define audio.Waves = "audio/sfx/beach_waves.mp3"
define audio.BookDrop = "audio/sfx/book_drop.mp3"
define audio.CameraShutter = "audio/sfx/camera_shutter.mp3"
define audio.CasualWin = "audio/sfx/casual_win.wav"
define audio.ControllerSounds = "audio/sfx/controller.mp3"
define audio.DarkAndEmpty = "audio/sfx/dark_empty_loop.wav"
define audio.DoorClose = "audio/sfx/door_wood_close.wav"
define audio.DoorOpen = "audio/sfx/door_wood_open.wav"
define audio.Engine = "audio/sfx/engine_loop.wav"
define audio.Explosion = "audio/sfx/explosion.mp3"
define audio.Glitch1 = "audio/sfx/glitch_1.mp3"
define audio.Glitch2 = "audio/sfx/glitch_2.mp3"
define audio.Gunshot = "audio/sfx/gunshot.wav"
define audio.Handcuffs = "audio/sfx/handcuffs.mp3"
define audio.Hit = "audio/sfx/hit.mp3"
define audio.Intercom = "audio/sfx/intercom_pa_chime.mp3"
define audio.ItemStore2 = "audio/sfx/item_store_loop.wav"
define audio.Kitchen = "audio/sfx/kitchen_ambiance.mp3"
#define audio.magic_spell = "audio/sfx/magic_spell.wav"
define audio.MetalImpact = "audio/sfx/metal_impact.wav"
define audio.Minigun = "audio/sfx/minigun.mp3"
define audio.MysteryHarp = "audio/sfx/mystery_harp.wav"
define audio.MysteryPiano = "audio/sfx/mystery_piano.wav"
define audio.PageFlip = "audio/sfx/page_flip.mp3"
define audio.GroupRun = "audio/sfx/people_running.mp3"
define audio.Rollerblade = "audio/sfx/rollerblade_skating.mp3"
define audio.RunGrass = "audio/sfx/running_on_grass.mp3"
define audio.WalkingOnDirt = "audio/sfx/walking_on_dirt.mp3"
define audio.whispering_loop = "audio/sfx/whispering_loop.wav"
define audio.Whoosh = "audio/sfx/whoosh_air.wav"

# Define Custom Sprite Positions for Kat
define mid = Position(xpos=0.5, ypos=1.84)#ypos=1.4)
define l = Position(xpos=0.33, ypos=1.84)
define r = Position(xpos=0.67, ypos=1.84)
define r2 = Position(xpos=0.9, ypos=1.84)
define l2 = Position(xpos=0.1, ypos=1.84)

# Define Damian Sprite Positions for the Intro
define dl = Position(xpos=0.33, ypos=1.91)

# Define Brothers Positions for the Intro
define bl2 = Position(xpos=0.1, ypos=1.91)
define bl = Position(xpos=0.33, ypos=1.91)
define bm = Position(xpos=0.5, ypos=1.91)
define br = Position(xpos=0.67, ypos=1.91)
define br2 = Position(xpos=0.9, ypos=1.91)
define b6 = Position(xpos=0.8, ypos=1.84) # for kat when b6 are around

# Define Generic Positions
define pos5 = Position(xpos=0.05, ypos=1.84)
define pos10 = Position(xpos=0.10, ypos=1.84)
define pos15 = Position(xpos=0.15, ypos=1.84)
define pos20 = Position(xpos=0.20, ypos=1.84)
define pos25 = Position(xpos=0.25, ypos=1.84)
define pos30 = Position(xpos=0.3, ypos=1.84)
define pos35 = Position(xpos=0.35, ypos=1.84)
define pos40 = Position(xpos=0.4, ypos=1.84)
define pos45 = Position(xpos=0.45, ypos=1.84)
define pos50 = Position(xpos=0.5, ypos=1.84)
define pos55 = Position(xpos=0.55, ypos=1.84)
define pos60 = Position(xpos=0.6, ypos=1.84)
define pos65 = Position(xpos=0.65, ypos=1.84)
define pos70 = Position(xpos=0.7, ypos=1.84)
define pos75 = Position(xpos=0.75, ypos=1.84)
define pos80 = Position(xpos=0.8, ypos=1.84)
define pos85 = Position(xpos=0.85, ypos=1.84)
define pos90 = Position(xpos=0.9, ypos=1.84)
define pos95 = Position(xpos=0.95, ypos=1.84)
define pos100 = Position(xpos=1, ypos=1.84)

# Define Kat Positions
define pos5k = Position(xpos=0.05, ypos=1.83)
define pos10k = Position(xpos=0.10, ypos=1.83)
define pos15k = Position(xpos=0.15, ypos=1.83)
define pos20k = Position(xpos=0.20, ypos=1.83)
define pos25k = Position(xpos=0.25, ypos=1.83)
define pos30k = Position(xpos=0.3, ypos=1.83)
define pos35k = Position(xpos=0.35, ypos=1.83)
define pos40k = Position(xpos=0.4, ypos=1.83)
define pos45k = Position(xpos=0.45, ypos=1.83)
define pos50k = Position(xpos=0.5, ypos=1.83)
define pos55k = Position(xpos=0.55, ypos=1.83)
define pos60k = Position(xpos=0.6, ypos=1.83)
define pos65k = Position(xpos=0.65, ypos=1.83)
define pos70k = Position(xpos=0.7, ypos=1.83)
define pos75k = Position(xpos=0.75, ypos=1.83)
define pos80k = Position(xpos=0.8, ypos=1.83)
define pos85k = Position(xpos=0.85, ypos=1.83)
define pos90k = Position(xpos=0.9, ypos=1.83)
define pos95k = Position(xpos=0.95, ypos=1.83)
define pos100k = Position(xpos=1, ypos=1.83)


# Define Allie Positions
define pos5a = Position(xpos=0.05, ypos=1.78)
define pos10a = Position(xpos=0.10, ypos=1.78)
define pos15a = Position(xpos=0.15, ypos=1.78)
define pos20a = Position(xpos=0.20, ypos=1.78)
define pos25a = Position(xpos=0.25, ypos=1.78)
define pos30a = Position(xpos=0.3, ypos=1.78)
define pos35a = Position(xpos=0.35, ypos=1.78)
define pos40a = Position(xpos=0.4, ypos=1.78)
define pos45a = Position(xpos=0.45, ypos=1.78)
define pos50a = Position(xpos=0.5, ypos=1.78)
define pos55a = Position(xpos=0.55, ypos=1.78)
define pos60a = Position(xpos=0.6, ypos=1.78)
define pos65a = Position(xpos=0.65, ypos=1.78)
define pos70a = Position(xpos=0.7, ypos=1.78)
define pos75a = Position(xpos=0.75, ypos=1.78)
define pos80a = Position(xpos=0.8, ypos=1.78)
define pos85a = Position(xpos=0.85, ypos=1.78)
define pos90a = Position(xpos=0.9, ypos=1.78)
define pos95a = Position(xpos=0.95, ypos=1.78)
define pos100a = Position(xpos=1, ypos=1.78)

# Define Scarlett Positions
define pos5s = Position(xpos=0.05, ypos=1.83)
define pos10s = Position(xpos=0.10, ypos=1.83)
define pos15s = Position(xpos=0.15, ypos=1.83)
define pos20s = Position(xpos=0.20, ypos=1.83)
define pos25s = Position(xpos=0.25, ypos=1.83)
define pos30s = Position(xpos=0.3, ypos=1.83)
define pos35s = Position(xpos=0.35, ypos=1.83)
define pos40s = Position(xpos=0.4, ypos=1.83)
define pos45s = Position(xpos=0.45, ypos=1.83)
define pos50s = Position(xpos=0.5, ypos=1.83)
define pos55s = Position(xpos=0.55, ypos=1.83)
define pos60s = Position(xpos=0.6, ypos=1.83)
define pos65s = Position(xpos=0.65, ypos=1.83)
define pos70s = Position(xpos=0.7, ypos=1.83)
define pos75s = Position(xpos=0.75, ypos=1.83)
define pos80s = Position(xpos=0.8, ypos=1.83)
define pos85s = Position(xpos=0.85, ypos=1.83)
define pos90s = Position(xpos=0.9, ypos=1.83)
define pos95s = Position(xpos=0.95, ypos=1.83)
define pos100s = Position(xpos=1, ypos=1.83)




# Define Terra Positions
define pos5t= Position(xpos=0.05, ypos=1.82)
define pos10t = Position(xpos=0.10, ypos=1.82)
define pos15t = Position(xpos=0.15, ypos=1.82)
define pos20t = Position(xpos=0.20, ypos=1.82)
define pos25t = Position(xpos=0.25, ypos=1.82)
define pos30t = Position(xpos=0.3, ypos=1.82)
define pos35t = Position(xpos=0.35, ypos=1.82)
define pos40t = Position(xpos=0.4, ypos=1.82)
define pos45t = Position(xpos=0.45, ypos=1.82)
define pos50t = Position(xpos=0.5, ypos=1.82)
define pos55t = Position(xpos=0.55, ypos=1.82)
define pos60t = Position(xpos=0.6, ypos=1.82)
define pos65t = Position(xpos=0.65, ypos=1.82)
define pos70t = Position(xpos=0.7, ypos=1.82)
define pos75t = Position(xpos=0.75, ypos=1.82)
define pos80t = Position(xpos=0.8, ypos=1.82)
define pos85t = Position(xpos=0.85, ypos=1.82)
define pos90t = Position(xpos=0.9, ypos=1.82)
define pos95t = Position(xpos=0.95, ypos=1.82)
define pos100t = Position(xpos=1, ypos=1.82)

define pos50t_fall1 = Position(xpos=0.5, ypos=1.90)
define pos50t_fall2 = Position(xpos=0.5, ypos=2.10)


# Define Violet Positions
define pos5v = Position(xpos=0.05, ypos=1.79)
define pos10v = Position(xpos=0.10, ypos=1.79)
define pos15v = Position(xpos=0.15, ypos=1.79)
define pos20v = Position(xpos=0.20, ypos=1.79)
define pos25v = Position(xpos=0.25, ypos=1.79)
define pos30v = Position(xpos=0.3, ypos=1.79)
define pos35v = Position(xpos=0.35, ypos=1.79)
define pos40v = Position(xpos=0.4, ypos=1.79)
define pos45v = Position(xpos=0.45, ypos=1.79)
define pos50v = Position(xpos=0.5, ypos=1.79)
define pos55v = Position(xpos=0.55, ypos=1.79)
define pos60v = Position(xpos=0.6, ypos=1.79)
define pos65v = Position(xpos=0.65, ypos=1.79)
define pos70v = Position(xpos=0.7, ypos=1.79)
define pos75v = Position(xpos=0.75, ypos=1.79)
define pos80v = Position(xpos=0.8, ypos=1.79)
define pos85v = Position(xpos=0.85, ypos=1.79)
define pos90v = Position(xpos=0.9, ypos=1.79)
define pos95v = Position(xpos=0.95, ypos=1.79)
define pos100v = Position(xpos=1, ypos=1.79)


# Define Yui Positions
define pos5y = Position(xpos=0.05, ypos=1.76)
define pos10y = Position(xpos=0.10, ypos=1.76)
define pos15y = Position(xpos=0.15, ypos=1.76)
define pos20y = Position(xpos=0.20, ypos=1.76)
define pos25y = Position(xpos=0.25, ypos=1.76)
define pos30y = Position(xpos=0.3, ypos=1.76)
define pos35y = Position(xpos=0.35, ypos=1.76)
define pos40y = Position(xpos=0.4, ypos=1.76)
define pos45y = Position(xpos=0.45, ypos=1.76)
define pos50y = Position(xpos=0.5, ypos=1.76)
define pos55y = Position(xpos=0.55, ypos=1.76)
define pos60y = Position(xpos=0.6, ypos=1.76)
define pos65y = Position(xpos=0.65, ypos=1.76)
define pos70y = Position(xpos=0.7, ypos=1.76)
define pos75y = Position(xpos=0.75, ypos=1.76)
define pos80y = Position(xpos=0.8, ypos=1.76)
define pos85y = Position(xpos=0.85, ypos=1.76)
define pos90y = Position(xpos=0.9, ypos=1.76)
define pos95y = Position(xpos=0.95, ypos=1.76)
define pos100y = Position(xpos=1, ypos=1.76)


# Define Damian Positions
define pos5d = Position(xpos=0.05, ypos=1.91)
define pos10d = Position(xpos=0.10, ypos=1.91)
define pos15d = Position(xpos=0.15, ypos=1.91)
define pos20d = Position(xpos=0.20, ypos=1.91)
define pos25d = Position(xpos=0.25, ypos=1.91)
define pos30d = Position(xpos=0.3, ypos=1.91)
define pos35d = Position(xpos=0.35, ypos=1.91)
define pos40d = Position(xpos=0.4, ypos=1.91)
define pos45d = Position(xpos=0.45, ypos=1.91)
define pos50d = Position(xpos=0.5, ypos=1.91)
define pos55d = Position(xpos=0.55, ypos=1.91)
define pos60d = Position(xpos=0.6, ypos=1.91)
define pos65d = Position(xpos=0.65, ypos=1.91)
define pos70d = Position(xpos=0.7, ypos=1.91)
define pos75d = Position(xpos=0.75, ypos=1.91)
define pos80d = Position(xpos=0.8, ypos=1.91)
define pos85d = Position(xpos=0.85, ypos=1.91)
define pos90d = Position(xpos=0.9, ypos=1.91)
define pos95d = Position(xpos=0.95, ypos=1.91)
define pos100d = Position(xpos=1, ypos=1.91)

# Define Brothers Positions
define pos5b = Position(xpos=0.05, ypos=1.91)
define pos10b = Position(xpos=0.10, ypos=1.91)
define pos15b = Position(xpos=0.15, ypos=1.91)
define pos20b = Position(xpos=0.20, ypos=1.91)
define pos25b = Position(xpos=0.25, ypos=1.91)
define pos30b = Position(xpos=0.3, ypos=1.91)
define pos35b = Position(xpos=0.35, ypos=1.91)
define pos40b = Position(xpos=0.4, ypos=1.91)
define pos45b = Position(xpos=0.45, ypos=1.91)
define pos50b = Position(xpos=0.5, ypos=1.91)
define pos55b = Position(xpos=0.55, ypos=1.91)
define pos60b = Position(xpos=0.6, ypos=1.91)
define pos65b = Position(xpos=0.65, ypos=1.91)
define pos70b = Position(xpos=0.7, ypos=1.91)
define pos75b = Position(xpos=0.75, ypos=1.91)
define pos80b = Position(xpos=0.8, ypos=1.91)
define pos85b = Position(xpos=0.85, ypos=1.91)
define pos90b = Position(xpos=0.9, ypos=1.91)
define pos95b = Position(xpos=0.95, ypos=1.91)
define pos100b = Position(xpos=1, ypos=1.91)


$ renpy.music.register_channel("ambient","sfx",True,tight=True)

# System Variables


# The game starts here.

label start:

    default tvShowName = _('Find Love or Die Trying')
    default tvShowFakeName = _('Find Love')
    default countryName = _('New Asia')
    default yourTitle= _('suitor')
    default theirTitle= _('soulmate candidate')
    default theirTitlePlural= _('soulmate candidates')
    default name = _('You')

    jump Day1Intro
