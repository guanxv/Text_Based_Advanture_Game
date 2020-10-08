race_desc = [
    "(DW)Dwarf              - Bold, hardy, warrior, miner, long memory and grudges",
    "(MD)Mountain Dwarf     - Strong, hardy, rugged, tall for a dwarf",
    "(HD)Hill Dwarf         - Keen senses, deep intuition, remarkable resilience",
    "(EL)Elf                - Magical people of otherworldly grace, in but not of the world",
    "(WE)Wood Elf           - Keen senses and intuition, fleet feet, and stealth",
    "(HE)High Elf           - Keen mind and master of basic magic",
    "(DR)Drow               - Follow the god Lolth down the path of evil and corruption",
    "(HF)Halfling           - You love peace, food, hearth, and home",
    "(LH)Lightfoot Halfling - You can easily hide, are inclined to get along with others",
    "(SH)Stout Halfling     - Hardier than average and may be part dwarven blood",
    "(HU)Human              - Young, short-lived race, innovators and achievers",
    "(DB)Dragonborn         - A servant to dragons, a warrior, or a drifter",
    "(GN)Gnome              - You delight in life, are an inventor, explorer, and explorer",
    "(FG)Forest Gnome       - Knack for illusion and inherent quickness and stealth",
    "(HA)Half-Elf           - Curious, inventive, ambitious, love nature, artistic",
    "(HO)Half-Orc           - Adventurer with savage fury and barbaric customs",
    "(TF)Tiefling           - Demonic heritage, self-reliant, suspicious, drifter",
]

race_short = [
    "Dwarf",
    "Mountain Dwarf",
    "Hill Dwarf",
    "Elf",
    "Wood Elf",
    "High Elf",
    "Drow",
    "Halfling",
    "Lightfoot Halfling",
    "Stout Halfling",
    "Human",
    "Dragonborn",
    "Gnome",
    "Forest Gnome",
    "Half-Elf",
    "Half-Orc",
    "Tiefling",
]


class Race:
    def __init__(
        self,
        name,
        description,
        ability_mod,
        age_range,
        alignment,
        size_range,
        speed,
        language,
        traits,
    ):
        self.name = name
        self.description = description
        self.ability_mod = ability_mod
        self.age_range = age_range
        self.alignment = alignment
        self.size_range = size_range
        self.speed = speed
        self.language = language
        self.traits = traits


race_human = Race(
    "Human",
    "Young, short-lived race, innovators and achievers",
    {
        "Strength": 1,
        "Dexterity": 1,
        "Constitution": 1,
        "Intelligence": 1,
        "Wisdom": 1,
        "Charisma": 1,
    },
    [18, 100],
    "",
    "",
    30,
    "",
    "",
)

race_dwarf = Race(
    "Dwarf",
    "Bold, hardy, warrior, miner, long memory and grudges",
    {
        "Strength": 0,
        "Dexterity": 0,
        "Constitution": 2,
        "Intelligence": 0,
        "Wisdom": 0,
        "Charisma": 0,
    },
    [50, 350],
    "",
    [4, 5, 150],
    25,
    "",
    [["Darkvision", 60], ["Dwarven Resilience"]],
)

race_hdwarf = Race(
    "Hill Dwarf",
    "Strong, hardy, rugged, tall for a dwarf",
    {
        "Strength": 0,
        "Dexterity": 0,
        "Constitution": 2,
        "Intelligence": 0,
        "Wisdom": 1,
        "Charisma": 0,
    },
    [50, 350],
    "",
    [4, 5, 150],
    25,
    "",
    [["Darkvision", 60], ["Dwarven Resilience"]],
)

race_mdwarf = Race(
    "Mountain Dwarf",
    "Keen senses, deep intuition, remarkable resilience",
    {
        "Strength": 2,
        "Dexterity": 0,
        "Constitution": 2,
        "Intelligence": 0,
        "Wisdom": 0,
        "Charisma": 0,
    },
    [50, 350],
    "",
    [4, 5, 150],
    25,
    "",
    [["Darkvision", 60], ["Dwarven Resilience"]],
)

race_elf = Race(
    "Elf",
    "Magical people of otherworldly grace, in but not of the world",
    {
        "Strength": 0,
        "Dexterity": 2,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom": 0,
        "Charisma": 0,
    },
    [100, 700],
    "",
    [5, 6, 125],
    30,
    "",
    [["Darkvision", 60], ["Dwarven Resilience"]],
)
race_welf = Race(
    "Wood Elf",
    "Keen senses and intuition, fleet feet, and stealth",
    {
        "Strength": 0,
        "Dexterity": 2,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom": 1,
        "Charisma": 0,
    },
    [100, 700],
    "",
    [5, 6, 125],
    35,
    "",
    [["Darkvision", 60], ["Dwarven Resilience"]],
)
race_Helf = Race(
    "High Elf",
    "Keen mind and master of basic magic",
    {
        "Strength": 0,
        "Dexterity": 2,
        "Constitution": 0,
        "Intelligence": 1,
        "Wisdom": 0,
        "Charisma": 0,
    },
    [100, 700],
    "",
    [5, 6, 125],
    30,
    "",
    [["Darkvision", 60], ["Dwarven Resilience"]],
)

race_drow = Race(
    "Dwarf",
    "Follow the god Lolth down the path of evil and corruption",
    {
        "Strength": 0,
        "Dexterity": 2,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom": 0,
        "Charisma": 1,
    },
    [100, 700],
    "",
    [5, 6, 125],
    30,
    "",
    [["Darkvision", 120], ["Dwarven Resilience"]],
)
race_halfling = Race(
    "Halfling",
    "You love peace, food, hearth, and home",
    {
        "Strength": 0,
        "Dexterity": 2,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom": 0,
        "Charisma": 0,
    },
    [20, 150],
    "",
    [3, 3, 42],
    25,
    "",
    [["Darkvision", 60], ["Dwarven Resilience"]],
)
race_lhalfling = Race(
    "Lightfoot Halfling",
    "You can easily hide, are inclined to get along with others",
    {
        "Strength": 0,
        "Dexterity": 2,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom": 0,
        "Charisma": 1,
    },
    [20, 150],
    "",
    [3, 3, 42],
    25,
    "",
    [["Darkvision", 60], ["Dwarven Resilience"]],
)
race_shalfling = Race(
    "Stout Halfling",
    "Hardier than average and may be part dwarven blood",
    {
        "Strength": 0,
        "Dexterity": 2,
        "Constitution": 1,
        "Intelligence": 0,
        "Wisdom": 0,
        "Charisma": 0,
    },
    [20, 150],
    "",
    [3, 3, 42],
    25,
    "",
    [["Darkvision", 60], ["Dwarven Resilience"]],
)
race_dragonborn = Race(
    "Dragonborn",
    "A servant to dragons, a warrior, or a drifter",
    {
        "Strength": 2,
        "Dexterity": 0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom": 0,
        "Charisma": 1,
    },
    [15, 80],
    "",
    [6, 7, 250],
    30,
    "",
    [["Darkvision", 60], ["Dwarven Resilience"]],
)
race_gnome = Race(
    "Gnome",
    "You delight in life, are an inventor, explorer, and explorer",
    {
        "Strength": 0,
        "Dexterity": 0,
        "Constitution": 0,
        "Intelligence": 2,
        "Wisdom": 0,
        "Charisma": 0,
    },
    [40, 500],
    "",
    [3, 4, 42],
    25,
    "",
    [["Darkvision", 60], ["Dwarven Resilience"]],
)
race_fgnome = Race(
    "Forest Gnome",
    "Knack for illusion and inherent quickness and stealth",
    {
        "Strength": 0,
        "Dexterity": 1,
        "Constitution": 0,
        "Intelligence": 2,
        "Wisdom": 0,
        "Charisma": 0,
    },
    [40, 500],
    "",
    [3, 4, 42],
    25,
    "",
    [["Darkvision", 60], ["Dwarven Resilience"]],
)

race_rgnome = Race(
    "Rock Gnome",
    "Knack for illusion and inherent quickness and stealth",
    {
        "Strength": 0,
        "Dexterity": 0,
        "Constitution": 1,
        "Intelligence": 2,
        "Wisdom": 0,
        "Charisma": 0,
    },
    [40, 500],
    "",
    [3, 4, 42],
    25,
    "",
    [["Darkvision", 60], ["Dwarven Resilience"]],
)

race_ha_elf = Race(
    "Half-Elf",
    "Curious, inventive, ambitious, love nature, artistic",
    {
        "Strength": 0,
        "Dexterity": 1,
        "Constitution": 0,
        "Intelligence": 1,
        "Wisdom": 0,
        "Charisma": 2,
    },
    [20, 180],
    "",
    [5, 6, 150],
    30,
    "",
    [["Darkvision", 60], ["Dwarven Resilience"]],
)
race_horc = Race(
    "Half-Orc",
    "Adventurer with savage fury and barbaric customs",
    {
        "Strength": 2,
        "Dexterity": 0,
        "Constitution": 1,
        "Intelligence": 0,
        "Wisdom": 0,
        "Charisma": 0,
    },
    [14, 75],
    "",
    [5, 6, 180],
    30,
    "",
    [["Darkvision", 60], ["Dwarven Resilience"]],
)

race_tiefling = Race(
    "Tiefling",
    "Demonic heritage, self-reliant, suspicious, drifter",
    {
        "Strength": 0,
        "Dexterity": 0,
        "Constitution": 0,
        "Intelligence": 1,
        "Wisdom": 0,
        "Charisma": 2,
    },
    [18, 100],
    "",
    [5, 6, 150],
    30,
    "",
    [["Darkvision", 60], ["Dwarven Resilience"]],
)

races = [
    race_dwarf,
    race_mdwarf,
    race_hdwarf,
    race_elf,
    race_welf,
    race_Helf,
    race_drow,
    race_halfling,
    race_lhalfling,
    race_shalfling,
    race_human,
    race_dragonborn,
    race_gnome,
    race_fgnome,
    # race_rgnome,
    race_ha_elf,
    race_horc,
    race_tiefling,
]


class_desc = [
    "Barbarian - The relentless combatant fueld by fury.",
    "Bard      - A story witty storyteller or musician.",
    "Cleric    - A holy man capable of helaing wounds.",
    "Druid     - A nomad devoted to the powers of Nature",
    "Fighter   - The skilled combatant and strategist.",
    "Monk      - A martial artist pulling bodily powers.",
    "Paladin   - A novice fighter bolstered by divine magic.",
    "Ranger    - One who blends wilderness knowledge and martial ability",
    "Rogue     - The theif, assassin, and stealthy character.",
    "Sorcerer  - A magic user who draws power from within.",
    "Warlock   - Pacted to a deity for empowering spells.",
    "Wizard    - Keeper of arcane secrets and manipulator of magic.",
]

# Class Descriptions - https://redd.it/2e9vzl

class_short = [
    "Barbarian",
    "Bard",
    "Cleric",
    "Druid",
    "Fighter",
    "Monk",
    "Paladin",
    "Ranger",
    "Rogue",
    "Sorcerer",
    "Warlock",
    "Wizard",
]
