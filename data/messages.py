import random

REMINDER_MESSAGES = [
    # Original messages
    "Your army thirsts for battle... and water! Drink now to restore movement points.",
    "A wise ruler keeps their kingdom hydrated. Time for water!",
    "The Necromancers don't need water, but YOU do. Drink up!",
    "Even dragons take water breaks. Your turn, hero!",
    "Ancient wisdom says: 'He who drinks water, wins wars.' Trust the scroll.",
    "Your mana is running low! Restore it with H2O.",
    "Defend your health! Drink water before the enemy (dehydration) attacks.",
    "+1 Morale if you drink water in the next 5 minutes!",
    "Heroes don't get dehydrated. Prove you're worthy!",
    "The Water Elementals demand tribute. One glass, please.",
    "Your hero stands idle at the well. Time to drink!",
    "A traveling merchant offers you water. Accept? (Yes, always yes.)",
    "The Oracle foresees... you drinking water. Make it so!",
    "Your creatures grow restless. They sense your thirst. Hydrate!",
    "Rumor has it: the mightiest heroes drink 8 glasses a day.",
    "A treasure chest appears! Inside: the gift of hydration. Drink!",
    "The Grail whispers: 'Water is the true power.' Listen to it.",
    "Your weekly stats depend on this moment. Drink water!",
    "Visiting a town? First stop: the well. Hydrate, hero!",
    "The Archangels approve of hydration. Don't disappoint them.",

    # Creature references
    "The Titans have spoken from their cloud temples: DRINK WATER, MORTAL.",
    "A Black Dragon lands before you. Even it knows to stay hydrated between battles.",
    "Your Behemoths are getting cranky. They want you to drink water.",
    "The Archangels cast Resurrection... but only if you drink water first.",
    "A pack of Wolf Raiders circles your camp. They're judging your hydration levels.",
    "Your Phoenix rises from the ashes, reborn through the power of H2O.",
    "The Ancient Behemoth roars! Translation: 'Drink water or face my wrath!'",
    "Thunderbirds gather storm clouds. They're making it rain so you remember to drink.",
    "Your Naga Queens demand you visit the sacred waters. Drink up!",
    "The Hydra has 8 heads. You should drink 8 glasses. Coincidence? I think not.",
    "A Fairy Dragon giggles. 'Silly human forgot to drink water again!'",
    "Your Gold Dragons hoard treasure... and hydration tips. Listen to them.",
    "The Bone Dragons don't need water anymore. Don't end up like them.",
    "Your Cavaliers charge into battle! But first, a water break.",
    "The Dread Knight whispers: 'Even the undead respect proper hydration.'",
    "Your Arch Devils scheme in the shadows... about getting you to drink water.",
    "A Crystal Dragon appears! Its body is 100% minerals. Yours needs water.",

    # Town references
    "Castle's fountains flow with pure water. Take a sip, noble knight!",
    "In the Rampart, even the Dendroids drink from forest springs. Your turn.",
    "Tower wizards know: hydration boosts Intelligence. Drink!",
    "Inferno is hot. Very hot. You need water more than ever.",
    "The Necropolis has no water... don't let that be your fate.",
    "Dungeon dwellers survive on underground springs. Where's YOUR water?",
    "Stronghold warriors hydrate before every raid. Be like them!",
    "Fortress swamps are 90% water. Take the hint.",
    "Conflux elementals ARE water. Show them respect by drinking some.",
    "The Mage Guild library says: 'Hydration increases spell power by 100%*' (*not verified)",

    # Hero references
    "Sir Christian would never skip a water break. Neither should you.",
    "Crag Hack smashes enemies AND stays hydrated. True strength!",
    "Solmyr's Chain Lightning can't help you if you're dehydrated.",
    "Isra the Necromancer raises the dead, not the dehydrated. Drink!",
    "Lord Haart drinks water before every siege. Follow his example.",
    "Gelu's Sharpshooters aim better when hydrated. Science!",
    "Tazar leads Beastmasters who respect nature's gift: water.",
    "Adelaide blesses troops with water magic. Bless yourself with actual water.",
    "Dracon the Wizard says: 'Enchanters who drink water never forget spells.'",
    "Xeron commands Devils but still takes water breaks. Even evil hydrates.",

    # Spell references
    "Cast 'Cure' on yourself! Drink water to remove the Dehydration debuff.",
    "No need for Resurrection if you stay hydrated. Prevention > cure!",
    "Water Walking spell active! Now actually drink some water.",
    "Slow spell detected on your metabolism. Counter it with hydration!",
    "Your Prayer buff is expiring. Renew it with holy water... or tap water.",
    "Bless your body with the sacred ritual of drinking water.",
    "Haste spell wearing off? Water gives you natural energy!",
    "Summon Water Elemental... into your stomach. Drink!",
    "Dispel the curse of thirst! Drink water now!",
    "Blind to your thirst? Let me Dispel that for you: DRINK WATER.",

    # Artifact references
    "You found the Everflowing Crystal Cloak! It demands you drink water.",
    "The Boots of Speed work better with proper hydration. Trust me.",
    "Equip the Ring of Vitality! Step 1: Drink water.",
    "The Helm of Heavenly Enlightenment reveals a truth: you need water.",
    "Seeking the Grail? Stay hydrated for the long quest ahead.",
    "The Orb of Vulnerability makes enemies weak. Dehydration makes YOU weak.",
    "Angel Wings artifact found! Angels recommend 8 glasses daily.",
    "The Sandals of the Saint say: 'Holy heroes stay hydrated.'",
    "You equipped Armor of Wonder! It wonders why you haven't drunk water.",
    "The Pendant of Life keeps you alive. So does water. Drink!",
    "Centaur's Axe bonus: +2 Attack. Water bonus: +100% not being thirsty.",
    "The Cape of Conjuring boosts magic. Water boosts everything. Drink!",

    # Map features
    "You've discovered a Water Wheel! It generates gold AND reminds you to hydrate.",
    "The Fountain of Youth appears! Quick, drink from it (or your glass).",
    "A Watering Hole on the map! Your hero drinks. You should too.",
    "Swan Pond visited! +2 Luck if you also drink water right now.",
    "Mercenary Camp recruited! They demand payment: your hydration.",
    "The Redwood Observatory reveals: you haven't drunk water in a while.",
    "Marletto Tower bonus: +1 Defense. Water bonus: +1 Not Dying.",
    "You found a Mystical Garden! It grows best with water. So do you.",
    "Star Axis aligned! The stars say: 'Drink water, mortal.'",
    "Shrine of Magic Incantation visited! The incantation is 'drink water.'",

    # Combat & mechanics
    "LUCK BONUS! But only if you drink water in the next 60 seconds.",
    "Dehydration gives -2 to all stats. Counter it immediately!",
    "Enemy hero spotted! Prepare for battle by... drinking water first.",
    "Siege incoming! Stock up on water for the long fight ahead.",
    "Your army's morale drops when their leader is thirsty. Fix this!",
    "Critical hit chance increases with hydration. Unverified but probably true.",
    "Waiting for the enemy's turn? Perfect time for a water break!",
    "Auto-combat enabled for your water drinking. Just do it!",
    "Save game... but first, save yourself. Drink water.",
    "Loading screen tip: Heroes who drink water win 73% more battles.",

    # Funny & meta
    "Day 1 without water: The Imps are starting to look concerned.",
    "Plot twist: The real treasure was hydration all along.",
    "Achievement unlocked: 'Still Alive' - Drink water to maintain this status.",
    "The AI opponent always drinks water between turns. Stay competitive!",
    "Random event: A well appears in your kingdom! USE IT.",
    "Your advisor frantically waves a water bottle. Take the hint.",
    "In the grim darkness of Erathia, there is only... thirst. Fix that.",
    "Easter egg found: Drinking water makes the game (of life) easier!",
    "Speedrun strats: Hydration skips the 'Passing Out' cutscene.",
    "The Load Game screen asks: 'Did you drink water?' Answer wisely.",
    "Tutorial tip: Press DRINK to consume water. Do it now.",
    "Weekly quest: Drink 56 glasses of water. Progress: ???/56",
    "New DLC announced: 'The Hydration Expansion' - Now drink water!",
    "Patch notes v1.0.1: Fixed bug where hero forgot to drink water.",
    "The credits roll... 'Special thanks to: Water, for keeping us alive.'",
]

DRINK_CONFIRMATIONS = [
    "Excellent! Your hero feels refreshed. +{gold} Gold, +{wood} Wood, +{ore} Ore!",
    "The troops cheer! Resources gained: +{gold} Gold, +{wood} Wood, +{ore} Ore",
    "Splendid hydration! Your treasury grows: +{gold} Gold, +{wood} Wood, +{ore} Ore",
    "A wise choice! +{gold} Gold, +{wood} Wood, +{ore} Ore added to your reserves.",
    "Your kingdom prospers! +{gold} Gold, +{wood} Wood, +{ore} Ore earned!",
    "The Water Elementals are pleased! +{gold} Gold, +{wood} Wood, +{ore} Ore!",
    "Victory! Each sip brings you closer to glory. +{gold} Gold, +{wood} Wood, +{ore} Ore",
]

LEVEL_UP_MESSAGES = [
    "LEVEL UP! You have evolved from {old_class} to {new_class}!",
    "Promotion! The {old_class} has become a mighty {new_class}!",
    "Glory! Your {old_class} transforms into {new_class}!",
]

STREAK_MESSAGES = {
    3: "ACHIEVEMENT UNLOCKED: Morale Boost! 3-day streak!",
    7: "ARTIFACT EARNED: Logistics! 7-day streak! Your movement is enhanced!",
    14: "LEGENDARY ARTIFACT: Angel Wings! 14-day streak! You can almost fly!",
    30: "THE GRAIL IS YOURS! 30-day streak! You are a true Hydration Champion!",
}

def get_random_reminder() -> str:
    return random.choice(REMINDER_MESSAGES)

def get_drink_confirmation(gold: int, wood: int, ore: int) -> str:
    msg = random.choice(DRINK_CONFIRMATIONS)
    return msg.format(gold=gold, wood=wood, ore=ore)

def get_level_up_message(old_class: str, new_class: str) -> str:
    msg = random.choice(LEVEL_UP_MESSAGES)
    return msg.format(old_class=old_class, new_class=new_class)
