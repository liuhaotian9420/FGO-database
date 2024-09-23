import json

# 阵营优势
ATTRIBUTE_ADVANTAGES = {
    "human": {
        "human": 1000,
        "sky": 1100,
        "earth": 900,
        "star": 1000,
        "beast": 1000
    },
    "sky": {
        "human": 900,
        "sky": 1000,
        "earth": 1100,
        "star": 1000,
        "beast": 1000
    },
    "earth": {
        "human": 1100,
        "sky": 900,
        "earth": 1000,
        "star": 1000,
        "beast": 1000
    },
    "star": {
        "human": 1000,
        "sky": 1000,
        "earth": 1000,
        "star": 1000,
        "beast": 1100
    },
    "beast": {
        "human": 1000,
        "sky": 1000,
        "earth": 1000,
        "star": 1100,
        "beast": 1000
    }
}

# 职介系数
CLASS_ATK_RATE = {
    "98": 1000,
    "99": 1000,
    "100": 1000,
    "1006": 1000,
    "saber": 1000,
    "archer": 950,
    "lancer": 1050,
    "rider": 1000,
    "caster": 900,
    "assassin": 900,
    "berserker": 1100,
    "shielder": 1000,
    "ruler": 1100,
    "alterEgo": 1000,
    "avenger": 1100,
    "demonGodPillar": 1000,
    "grandSaber": 1000,
    "grandArcher": 950,
    "grandLancer": 1050,
    "grandRider": 1000,
    "grandCaster": 900,
    "grandAssassin": 900,
    "grandBerserker": 1100,
    "beastII": 1000,
    "ushiChaosTide": 1000,
    "beastI": 1000,
    "moonCancer": 1000,
    "beastIIIR": 1000,
    "foreigner": 1000,
    "beastIIIL": 1000,
    "beastUnknown": 1000,
    "pretender": 1000,
    "beastIV": 1000,
    "beastILost": 1000,
    "uOlgaMarieAlienGod": 1000,
    "uOlgaMarie": 1000,
    "beast": 1000,
    "beastVI": 1000,
    "beastVIBoss": 1000,
    "uOlgaMarieFlare": 1000,
    "uOlgaMarieAqua": 1000,
    "beastEresh": 1000,
    "unknown": 1000,
    "agarthaPenth": 1100,
    "cccFinaleEmiyaAlter": 1000,
    "salemAbby": 1000,
    "OTHER": 1000,
    "ALL": 1000,
    "EXTRA": 1002,
    "MIX": 1000,
    "EXTRA1": 1000,
    "EXTRA2": 1000,
    "uOlgaMarieFlareCollection": 1000,
    "uOlgaMarieAquaCollection": 1000
}

# 职介优势
CLASS_ADVANTAGES = json.load(open("class_adv.json", "r"))

# 指令卡基础
face_card = json.load(open("face_card.json", "r"))
# 伤害
FACE_CARD_DAMAGE_RATE = { card:[static['adjustAtk'] for idx,static in data.items()] 
                         for card,data in face_card.items() 
                         if card in ['buster','quick','arts','extra']}
FACE_CARD_NP_GAIN_RATE = { card:[static['adjustTdGauge'] for idx,static in data.items()] 
                         for card,data in face_card.items() 
                         if card in ['buster','quick','arts','extra']}
FACE_CARD_STAR_GEN = { card:[static['adjustCritical'] for idx,static in data.items()] 
                         for card,data in face_card.items() 
                         if card in ['buster','quick','arts','extra']}
# 基础白值
ATK_MAX_BASE = {
           "5":11000,
           "4":9000,
           "3":7000,
           "2":6200,
           "1":5500,
           "0":6200
           }
ATK_MIN_BASE = {
           "5":1700,
           "4":1500,
           "3":1300,
           "2":1100,
           "1":1000,
           "0":1100    
}

MAX_LEVEL = {
           "5":90,
           "4":80,
           "3":70,
           "2":65,
           "1":60,
           "0":65  
}


# 职介倾向
CLASS_TENDANCY = {
    "HP": {
        "Saber": 1.01,
        "Archer": 0.98,
        "Lancer": 1.02,
        "Rider": 0.96,
        "Caster": 0.98,
        "Assassin": 0.95,
        "Berserker": 0.90,
        "Ruler": 1.00,
        "Avenger": 0.88,
        "Mooncancer": 1.05,
        "Alterego": 0.95,
        "Foreigner": 1.00,
        "Pretender": 0.95,
        "Shielder": 1.01,
        "Beast": 0.97
    },
    "ATK": {
        "Saber": 1.01,
        "Archer": 1.02,
        "Lancer": 0.98,
        "Rider": 0.97,
        "Caster": 0.94,
        "Assassin": 0.96,
        "Berserker": 1.03,
        "Ruler": 0.95,
        "Avenger": 1.05,
        "Mooncancer": 0.94,
        "Alterego": 1.02,
        "Foreigner": 1.00,
        "Pretender": 1.02,
        "Shielder": 0.99,
        "Beast": 1.03,
        "Grandcaster":1.00
    }
}
