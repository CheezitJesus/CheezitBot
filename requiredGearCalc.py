class Hero:
    def __init__(self,name,attack,defense,health,speed,critChance,critDamage,effectiveness,effectResist):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.health = health
        self.speed = speed
        self.critChance = critChance
        self.critDamage = critDamage
        self.effectiveness = effectiveness
        self.effectResist = effectResist

    def printStats(self):
        print(self.name + ":")
        print("Attack: " + str(self.attack))
        print("Defense: " + str(self.defense))
        print("Health: " + str(self.health))
        print("Speed: " + str(self.speed))
        print("Crit Chance: " + str(self.critChance))
        print("Crit Damage: " + str(self.critDamage))
        print("Effectiveness:" + str(self.effectiveness))
        print("Effect Resist: " + str(self.effectResist))

def addMainStats(hero,mainStatList):
    instanceHero = hero
    instanceHero.attack += mainStatList[0]
    instanceHero.health += mainStatList[1]
    instanceHero.defense += mainStatList[2]
    for i in range(3,6):
        stat = mainStatList[i][0]
        type = mainStatList[i][1]
        value = mainStatList[i][2]
        if type == "percent":
            if stat == "attack":
                instanceHero.attack += int(hero.attack*value)
            elif stat == "defense":
                instanceHero.defense += int(hero.defense*value)
            elif stat == "health":
                instanceHero.health += int(hero.health*value)
            elif stat == "speed":
                pass
            elif stat == "critChance":
                pass
            elif stat == "critDamage":
                pass
            elif stat == "effectiveness":
                pass
            elif stat == "effectResist":
                pass
        elif type == "flat":
            if stat == "attack":
                instanceHero.attack += value
            elif stat == "defense":
                instanceHero.defense += value
            elif stat == "health":
                instanceHero.defense += value
            elif stat == "speed":
                instanceHero.speed += value
            elif stat == "critChance":
                instanceHero.critChance += value
            elif stat == "critDamage":
                instanceHero.critDamage += value
            elif stat == "effectiveness":
                instanceHero.effectiveness += value
            elif stat == "effectResist":
                instanceHero.effectResist += value
    return instanceHero

def getHero():
    print("Enter a hero to configure in the following format:")
    print("NAME ATTACK DEFENSE HEALTH SPEED CRITCHANCE CRITDAMAGE EFFECTIVENESS EFFECTRESIST")
    heroString = input("")


tywin = Hero("Tywin",821,648,6751,110,15,150,18,0)
tywin.printStats()
tywinMainStatlist = [525,2825,310,["effectiveness","flat",70],["health","percent",.65],["speed","flat",45]]
tywinNew = addMainStats(tywin,tywinMainStatlist)
tywinNew.printStats()

