import random

REMINDER_MESSAGES = [
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
