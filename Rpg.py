import random
import time


#Alpha 1.01

#Next updates to add:
#More character classes
#Dark Knight Flaming sword 25% inital dmg burn



def MonsterGen(stats):
    global Skill
    MonsterStats = {}


    if Skill <= 3.5:
        MonsterStats["Health"] = random.randint(int(Skill * 75),int(Skill * 125))
        MonsterStats["Attack"] = random.randint(int(Skill * 7),int(Skill * 12))
        MonsterStats["Speed"] = random.randint(int(Skill * 75),int(Skill * 125))
        MonsterStats["Magic"] = random.randint(int(Skill * 3.5),int(Skill * 6))
        MonsterStats["Rarity"] = "D"

    elif Skill <= 22 and Skill > 3.5:
        if random.randint(1,4) <= 3: 
            MonsterStats["Health"] = random.randint(int(Skill * 100),int(Skill * 150))
            MonsterStats["Attack"] = random.randint(int(Skill * 10),int(Skill * 15))
            MonsterStats["Speed"] = random.randint(int(Skill * 100),int(Skill * 150))
            MonsterStats["Magic"] = random.randint(int(Skill * 5),int(Skill * 10))
            MonsterStats["Rarity"] = "C"
        else:
            MonsterStats["Health"] = random.randint(int(Skill * 75),int(Skill * 125))
            MonsterStats["Attack"] = random.randint(int(Skill * 7),int(Skill * 12)) 
            MonsterStats["Speed"] = random.randint(int(Skill * 75),int(Skill * 125))
            MonsterStats["Magic"] = random.randint(int(Skill * 3.5),int(Skill * 6))
            MonsterStats["Rarity"] = "D"

    elif Skill <= 105 and Skill > 22:
        if random.randint(1,4) <= 3: 
            MonsterStats["Health"] = random.randint(int(Skill * 150),int(Skill * 200))
            MonsterStats["Attack"] = random.randint(int(Skill * 15),int(Skill * 20))
            MonsterStats["Speed"] = random.randint(int(Skill * 150),int(Skill * 200))
            MonsterStats["Magic"] = random.randint(int(Skill * 10),int(Skill * 15))
            MonsterStats["Rarity"] = "B"
        elif random.randint(1,4) <= 3: 
            MonsterStats["Health"] = random.randint(int(Skill * 100),int(Skill * 150))
            MonsterStats["Attack"] = random.randint(int(Skill * 10),int(Skill * 15))
            MonsterStats["Speed"] = random.randint(int(Skill * 100),int(Skill * 150))
            MonsterStats["Magic"] = random.randint(int(Skill * 5),int(Skill * 10))
            MonsterStats["Rarity"] = "C"
        else:
            MonsterStats["Health"] = random.randint(int(Skill * 75),int(Skill * 125))
            MonsterStats["Attack"] = random.randint(int(Skill * 7),int(Skill * 12))
            MonsterStats["Speed"] = random.randint(int(Skill * 75),int(Skill * 125))
            MonsterStats["Magic"] = random.randint(int(Skill * 3.5),int(Skill * 6))
            MonsterStats["Rarity"] = "D"
    elif Skill <= 400 and Skill > 105:
        if random.randint(1,4) <= 3: 
            MonsterStats["Health"] = random.randint(int(Skill * 200),int(Skill * 250))
            MonsterStats["Attack"] = random.randint(int(Skill * 20),int(Skill * 25))
            MonsterStats["Speed"] = random.randint(int(Skill * 200),int(Skill * 250))
            MonsterStats["Magic"] = random.randint(int(Skill * 15),int(Skill * 20))
            MonsterStats["Rarity"] = "A"
        elif random.randint(1,4) <= 3: 
            MonsterStats["Health"] = random.randint(int(Skill * 150),int(Skill * 200))
            MonsterStats["Attack"] = random.randint(int(Skill * 15),int(Skill * 20))
            MonsterStats["Speed"] = random.randint(int(Skill * 150),int(Skill * 200))
            MonsterStats["Magic"] = random.randint(int(Skill * 10),int(Skill * 15)) 
            MonsterStats["Rarity"] = "B"
        elif random.randint(1,4) <= 3: 
            MonsterStats["Health"] = random.randint(int(Skill * 100),int(Skill * 150))
            MonsterStats["Attack"] = random.randint(int(Skill * 10),int(Skill * 15))
            MonsterStats["Speed"] = random.randint(int(Skill * 100),int(Skill * 150))
            MonsterStats["Magic"] = random.randint(int(Skill * 5),int(Skill * 10))
            MonsterStats["Rarity"] = "C"
        else:
            MonsterStats["Health"] = random.randint(int(Skill * 75),int(Skill * 125))
            MonsterStats["Attack"] = random.randint(int(Skill * 7),int(Skill * 12))
            MonsterStats["Speed"] = random.randint(int(Skill * 75),int(Skill * 125))
            MonsterStats["Magic"] = random.randint(int(Skill * 3.5),int(Skill * 6))
            MonsterStats["Rarity"] = "D"
    elif Skill <= 400 and Skill >= 1400:
        if random.randint(1,4) <= 3: 
            MonsterStats["Health"] = random.randint(int(Skill * 250),int(Skill * 300))
            MonsterStats["Attack"] = random.randint(int(Skill * 25),int(Skill * 30))
            MonsterStats["Speed"] = random.randint(int(Skill * 250),int(Skill * 300))
            MonsterStats["Magic"] = random.randint(int(Skill * 20),int(Skill * 25))
            MonsterStats["Rarity"] = "S"
        elif random.randint(1,4) <= 3: 
            MonsterStats["Health"] = random.randint(int(Skill * 200),int(Skill * 250))
            MonsterStats["Attack"] = random.randint(int(Skill * 20),int(Skill * 25))
            MonsterStats["Speed"] = random.randint(int(Skill * 200),int(Skill * 250))
            MonsterStats["Magic"] = random.randint(int(Skill * 15),int(Skill * 20))
            MonsterStats["Rarity"] = "A"
        elif random.randint(1,4) <= 3: 
            MonsterStats["Health"] = random.randint(int(Skill * 150),int(Skill * 200))
            MonsterStats["Attack"] = random.randint(int(Skill * 15),int(Skill * 20))
            MonsterStats["Speed"] = random.randint(int(Skill * 150),int(Skill * 200))
            MonsterStats["Magic"] = random.randint(int(Skill * 10),int(Skill * 15))
            MonsterStats["Rarity"] = "B"
        elif random.randint(1,4) <= 3: 
            MonsterStats["Health"] = random.randint(int(Skill * 100),int(Skill * 150))
            MonsterStats["Attack"] = random.randint(int(Skill * 10),int(Skill * 15))
            MonsterStats["Speed"] = random.randint(int(Skill * 100),int(Skill * 150))
            MonsterStats["Magic"] = random.randint(int(Skill * 5),int(Skill * 10))
            MonsterStats["Rarity"] = "C"
        else:
            MonsterStats["Health"] = random.randint(int(Skill * 75),int(Skill * 125))
            MonsterStats["Attack"] = random.randint(int(Skill * 7),int(Skill * 12))
            MonsterStats["Speed"] = random.randint(int(Skill * 75),int(Skill * 125))
            MonsterStats["Magic"] = random.randint(int(Skill * 3.5),int(Skill * 6))
            MonsterStats["Rarity"] = "D"
    else:
        if random.randint(1,4) <= 3: 
            MonsterStats["Health"] = random.randint(int(Skill * 300),int(Skill * 350))
            MonsterStats["Attack"] = random.randint(int(Skill * 30),int(Skill * 35))
            MonsterStats["Speed"] = random.randint(int(Skill * 300),int(Skill * 350))
            MonsterStats["Magic"] = random.randint(int(Skill * 25),int(Skill * 30))
            MonsterStats["Rarity"] = "BOSS"
        elif random.randint(1,4) <= 3: 
            MonsterStats["Health"] = random.randint(int(Skill * 250),int(Skill * 300))
            MonsterStats["Attack"] = random.randint(int(Skill * 25),int(Skill * 30))
            MonsterStats["Speed"] = random.randint(int(Skill * 250),int(Skill * 300))
            MonsterStats["Magic"] = random.randint(int(Skill * 20),int(Skill * 25))
            MonsterStats["Rarity"] = "S"
        elif random.randint(1,4) <= 3: 
            MonsterStats["Health"] = random.randint(int(Skill * 200),int(Skill * 250))
            MonsterStats["Attack"] = random.randint(int(Skill * 20),int(Skill * 25))
            MonsterStats["Speed"] = random.randint(int(Skill * 200),int(Skill * 250))
            MonsterStats["Magic"] = random.randint(int(Skill * 15),int(Skill * 20))
            MonsterStats["Rarity"] = "A"
        elif random.randint(1,4) <= 3: 
            MonsterStats["Health"] = random.randint(int(Skill * 150),int(Skill * 200))
            MonsterStats["Attack"] = random.randint(int(Skill * 15),int(Skill * 20))
            MonsterStats["Speed"] = random.randint(int(Skill * 150),int(Skill * 200))
            MonsterStats["Magic"] = random.randint(int(Skill * 10),int(Skill * 15))
            MonsterStats["Rarity"] = "B"
        elif random.randint(1,4) <= 3: 
            MonsterStats["Health"] = random.randint(int(Skill * 100),int(Skill * 150))
            MonsterStats["Attack"] = random.randint(int(Skill * 10),int(Skill * 15))
            MonsterStats["Speed"] = random.randint(int(Skill * 100),int(Skill * 150))
            MonsterStats["Magic"] = random.randint(int(Skill * 5),int(Skill * 10))
            MonsterStats["Rarity"] = "C"
        else:
            MonsterStats["Health"] = random.randint(int(Skill * 75),int(Skill * 125))
            MonsterStats["Attack"] = random.randint(int(Skill * 7),int(Skill * 12))
            MonsterStats["Speed"] = random.randint(int(Skill * 75),int(Skill * 125))
            MonsterStats["Magic"] = random.randint(int(Skill * 3.5),int(Skill * 6))
            MonsterStats["Rarity"] = "D"
        
        
        
            

    
    return MonsterStats
def Rpg():
    global Skill
    Skill = 0.25
    print("You wake up and you can't remeber what had happened before\n")
    name = input("What is your name?")
    MagicType = input("What do you want to do with your Magic?\n1: Healing\n2: Damage\n")
    Class = input("What type of class do you want to be?\n1: Tank(+50 Health)\n2: Knight(+10 Health, +8 Attack)\n3: Scout(+15 Speed, -30% Monster Hit Chance)"
                  + "\n4: Wizard(-20 Health, +15 Magic)\n5: Swordsman(+10 Speed, +5 Attack)\n6: Assassin(Insight Ability)\n7: Dark Knight(Flaming Sword, +5 Health, +4 Attack)")
    game_run = True
    PlayerDead = False
    HitChance = 90
    MonHitChance = 90
    Hincrease = 1.25
    DmgPer = 100
    Insight = 0
    OneShot = 0
    BurnCooldown = 0
    BurnPer = 0

    HLv3 = False
    ALv3 = False
    SLv3 = False
    MLv3 = False
    HLv7 = False
    ALv7 = False
    SLv7 = False
    MLv7 = False
    HLv15 = False
    ALv15 = False
    SLv15 = False
    MLv15 = False
    HLv30 = False
    ALv30 = False
    SLv30 = False
    MLv30 = False

    minion = ""

    DeathCount = 0
    gold = 0
    HealthItems = [["Health Canister","Iron Armor","Iridium Armor"],[500,2500,15000]]
    AttackItems = [["Iron Sword","Giant Sword","Dark Pulser"],[500,2500,15000]]
    SpeedItems = [["Running Shoes","Winged Sandals","Practically Teleportation"],[500,2500,15000]]
    MagicItems = [["Small Wand", "Gandalf's Staff","Staff of Chony"],[500,2500,15000]]
    MiscItems = [["Less Missing", "Change Magic Type (1 Use)","OP Late Game Buff"],[15000,5000,500000]]
    
    oldstats = {}
    stats = {"Health":random.randint(75,125), "Attack": random.randint(7,12), "Speed": random.randint(75,125), "Magic": random.randint(7,12)}
    if Class == "1":
        stats["Health"] += 50
        HealthItems[0].append("20% less damage")
        HealthItems[0].append("50% less damage")
        HealthItems[1].append(20000)
        HealthItems[1].append(150000)
    elif Class == "2":
        stats["Health"] += 10
        stats["Attack"] += 8
    elif Class == "3":
        stats["Speed"] += 15
        MonHitChance -= 30
    elif Class == "4":
        stats["Health"] -= 20
        stats["Magic"] += 15
    elif Class == "5":
        stats["Speed"] += 10
        stats["Attack"] += 5
    elif Class == "6":
        Insight = 50
        OneShot = 30
        MiscItems[0].append("20% more insight")
        MiscItems[0].append("30% more one shot chance")
        MiscItems[1].append(30000)
        MiscItems[1].append(75000)
    elif Class == "7":
        stats["Health"] += 5
        stats["Attack"] += 4
        MiscItems[0].append("20% more burn")
        MiscItems[0].append("40% more burn")
        MiscItems[1].append(40000)
        MiscItems[1].append(90000)
        BurnPer = 30
    else:
        print("You didn't choose a class so you were give the hobo class(+5 Health, +5 Attack, +5 Speed, +5 Magic)")
        stats["Health"] += 5
        stats["Attack"] += 5
        stats["Speed"] += 5
        stats["Magic"] += 5
        
    oldstats["Health"] = stats["Health"]
    oldstats["Attack"] = stats["Attack"]
    oldstats["Speed"] = stats["Speed"]
    oldstats["Magic"] = stats["Magic"]

    
    
    SkillLevel = {"Health": 1, "Attack": 1, "Speed": 1, "Magic": 1}

    while game_run == True:

        Monster = MonsterGen(stats)
        OldMonster = Monster["Health"] + Monster["Speed"] + Monster["Magic"] + Monster["Attack"]
        print("Skill level: " + str(int(Skill)))
        print("Your Stats: \nHealth: " + str(stats["Health"]) + "\nAttack: " + str(stats["Attack"]) + "\nSpeed: " + str(stats["Speed"]) + "\nMagic: " + str(stats["Magic"]))
        print("Enemies Stats: \nHealth: " + str(Monster["Health"]) + "\nAttack: " + str(Monster["Attack"]) + "\nSpeed: " + str(Monster["Speed"]) + "\nMagic: " + str(Monster["Magic"]))

        enter = input("A level " + str(Monster["Rarity"]) + " monster appeared\n1: Auto\n2: Manual\n")
        
        BurnDmg = 0
        BurnCooldown = 0

        fight = True
        MonsterDead = False
        
        while fight == True:
            if enter == "2":
                choice = input("What action do you want to do?\nHealth: " + str(stats["Health"]) + "\nEnemies Health: " + str(Monster["Health"]) + "\n1: Attack\n2: Use Magic\n")
            else:
                choice = "1"
                print("Health: " + str(stats["Health"]) + "\nEnemies Health: " + str(Monster["Health"]))


            check = False
            try:
                if choice == "1":
                    pass
            except TypeError:
                check = True
            if check == False:
                if choice == "1":
                    if stats["Speed"] >= Monster["Speed"]:
                        #You attacking Monster (You have higher speed)
                        stop = False
                        msg = ""
                        Buff = len(str(stats["Speed"])) + len(str(stats["Attack"]))
                        if Class == "6" and random.randint(1,100) <= Insight and random.randint(1,100) <= OneShot+Buff:
                            print("You oneshot the enemy")
                            Monster["Health"] = 0
                        elif ALv30 == True and random.randint(1,100) <= 40:
                            Monster["Health"] = 0
                            print("You destroyed the enemy")
                        else:
                            if random.randint(1,100) <= HitChance:
                                att = random.randint(int(stats["Attack"]/1.5),int(stats["Attack"]*1.3))
                                msg = "You attacked the monster "
                                if stats["Speed"] >= 500 and random.randint(1,100) <= HitChance and stop == False and Class == "5":
                                    att += random.randint(int(stats["Attack"]/1.5),int(stats["Attack"]*1.5))
                                    msg = "You got a critical hit "
                                else:
                                    stop = True
                                if stats["Speed"] >= 4500 and random.randint(1,100) <= HitChance-20 and stop == False and Class == "5":
                                    att += random.randint(int(stats["Attack"]/1.5),int(stats["Attack"]*1.5))
                                    msg = "You got a double critical hit "
                                else:
                                    stop = True
                                if stats["Speed"] >= 15000 and random.randint(1,100) <= HitChance-40 and stop == False and Class == "5":
                                    att += random.randint(int(stats["Attack"]/1.5),int(stats["Attack"]*1.9))
                                    msg = "You got a triple critical hit "
                                else:
                                    stop = True
                                if stats["Speed"] >= 15000 and random.randint(1,100) <= HitChance and stop == False and SLv30 == True and Class == "5":
                                    att += random.randint(int(stats["Attack"]/1.5),int(stats["Attack"]*1.9))
                                    msg = "You got a Quadra critical hit "
                                else:
                                    stop = True
                                if random.randint(1,100) <= HitChance and stop == False and SLv30 == True and Class == "5":
                                    att += random.randint(int(stats["Attack"]/1.5),int(stats["Attack"]*1.9))
                                    msg = "You got a Penta critical hit "
                                else:
                                    stop = True
                                print(str(msg) + str(att) + " damage")
                                Monster["Health"] -= att
                                if Class == "7"and BurnCooldown == 0:
                                    BurnCooldown = 3
                                    BurnDmg = int(att * (BurnPer/100))
                                if Class == "7" and BurnCooldown != 0:
                                    print("You burnt the enemy for " + str(BurnDmg) + " damage")
                                    BurnCooldown -= 1
                                    
                            else:
                                print("You attempted to hit the monster, but missed")
                                if Class == "7" and BurnCooldown != 0:
                                        print("You burnt the enemy for " + str(BurnDmg) + " damage")
                                        BurnCooldown -= 1
                            if minion != "":
                                att = random.randint(int(stats["Attack"]/5),int(stats["Attack"]/2))
                                print("Your minion " + str(minion) + " hit the monster for " + str(att) + " damage")
                                Monster["Health"] -= att
                        if Monster["Health"] <= 0:
                            
                            MonsterDead = True
                            
                        #Monster Attacks you (You have higher speed)
                        if random.randint(1,4) <= 3 and MonsterDead == False:
                            if random.randint(1,100) <= MonHitChance:
                                att = random.randint(int(Monster["Attack"]/1.5),int(Monster["Attack"]*1.3))
                                print("You were hit by the monster for " + str(att) + " damage")
                                stats["Health"] -= int(att * (DmgPer/100))
                            else:
                                print("The monster went to hit you, but it missed you")
                                
                            if stats["Health"] <= 0:
                                fight = False
                                PlayerDead = True
                        else:
                            if MonsterDead == False:
                                if random.randint(1,100) <= MonHitChance - 20:
                                    heal = int(Monster["Magic"] * (random.randint(37,100)/100))
                                    print("The monster was healed for " + str(heal) + " health")
                                    Monster["Health"] += heal
                                else:
                                    print("The monster tried to heal, but it failed")
                    else:
                        #Monster Attacks you (They have higher speed)
                        if random.randint(1,4) <= 3:
                            if random.randint(1,100) <= MonHitChance:
                                att = random.randint(int(Monster["Attack"]/1.5),int(Monster["Attack"]*1.3))
                                print("You were hit by the monster for " + str(att) + " damage")
                                stats["Health"] -= int(att * (DmgPer/100))
                            else:
                                print("The monster went to hit you, but it missed you")
                                
                            if stats["Health"] <= 0:
                                PlayerDead = True
                        else:
                            if random.randint(1,100) <= MonHitChance - 20:
                                heal = int(Monster["Magic"] * (random.randint(37,100)/100))
                                print("The monster was healed for " + str(heal) + " health")
                                Monster["Health"] += heal
                            else:
                                print("The monster tried to heal, but it failed")

                        #You attack monster (They have higher speed)
                        
                        if PlayerDead == False:
                            stop = False
                            msg = ""
                            Buff = len(str(stats["Speed"])) + len(str(stats["Attack"]))
                            if Class == "6" and random.randint(1,100) <= Insight and random.randint(1,100) <= OneShot+Buff:
                                print("You oneshot the enemy")
                                Monster["Health"] = 0
                            elif ALv30 == True and random.randint(1,100) <= 40:
                                Monster["Health"] = 0
                                print("You destroyed the enemy")
                            else:
                                if random.randint(1,100) <= HitChance:
                                    att = random.randint(int(stats["Attack"]/1.5),int(stats["Attack"]*1.3))
                                    msg = "You attacked the monster "
                                    if stats["Speed"] >= 500 and random.randint(1,100) <= HitChance and stop == False and Class == "5":
                                        att += random.randint(int(stats["Attack"]/1.5),int(stats["Attack"]*1.5))
                                        msg = "You got a critical hit "
                                    else:
                                        stop = True
                                    if stats["Speed"] >= 4500 and random.randint(1,100) <= HitChance-20 and stop == False and Class == "5":
                                        att += random.randint(int(stats["Attack"]/1.5),int(stats["Attack"]*1.5))
                                        msg = "You got a double critical hit "
                                    else:
                                        stop = True
                                    if stats["Speed"] >= 15000 and random.randint(1,100) <= HitChance-40 and stop == False and Class == "5":
                                        att += random.randint(int(stats["Attack"]/1.5),int(stats["Attack"]*1.9))
                                        msg = "You got a triple critical hit "
                                    else:
                                        stop = True
                                    if random.randint(1,100) <= HitChance and stop == False and SLv30 == True and Class == "5":
                                        att += random.randint(int(stats["Attack"]/1.5),int(stats["Attack"]*1.9))
                                        msg = "You got a Quadra critical hit "
                                    else:
                                        stop = True
                                    if random.randint(1,100) <= HitChance and stop == False and SLv30 == True and Class == "5":
                                        att += random.randint(int(stats["Attack"]/1.5),int(stats["Attack"]*1.9))
                                        msg = "You got a Penta critical hit "
                                    else:
                                        stop = True
                                    print(str(msg) + str(att) + " damage")
                                    Monster["Health"] -= att

                                    if Class == "7"and BurnCooldown == 0:
                                        BurnCooldown = 3
                                        BurnDmg = int(att * (BurnPer/100))
                                    if Class == "7" and BurnCooldown != 0:
                                        print("You burnt the enemy for " + str(BurnDmg) + " damage")
                                        BurnCooldown -= 1
                            
                                else:
                                    print("You attempted to hit the monster, but missed")
                                    if Class == "7" and BurnCooldown != 0:
                                        print("You burnt the enemy for " + str(BurnDmg) + " damage")
                                        BurnCooldown -= 1
                                if minion != "":
                                    att = random.randint(int(stats["Attack"]/5),int(stats["Attack"]/2))
                                    print("Your minion " + str(minion) + " hit the monster for " + str(att) + " damage")
                                    Monster["Health"] -= att
                            if Monster["Health"] <= 0:
                                MonsterDead = True
                else:
                    if stats["Speed"] >= Monster["Speed"]:
                        #You use your magic(You have higher speed)
                        if MagicType == "1":
                            heal = int(stats["Magic"] * (random.randint(75,200)/100))
                            if heal + stats["Health"] >= oldstats["Health"]:
                                heal = oldstats["Health"] - stats["Health"]
                                stats["Health"] = oldstats["Health"]
                                print("You healed yourself for " + str(heal))
                            else:
                                stats["Health"] += heal
                                print("You healed yourself for " + str(heal))
                        else:
                            if random.randint(1,100) <= HitChance:
                                att = random.randint(int(stats["Magic"]/2.5),int(stats["Magic"]*1.3))
                                print("You cast a spell upon monster for " + str(att) + " damage")
                                Monster["Health"] -= att
                            else:
                                print("You attempted to cast your magic, but the spell fizzled")
                            if minion != "":
                                att = random.randint(int(stats["Attack"]/5),int(stats["Attack"]/2))
                                print("Your minion " + str(minion) + " hit the monster for " + str(att) + " damage")
                                Monster["Health"] -= att
                            if Monster["Health"] <= 0:
                                MonsterDead = True
                            

                        #Monster attacks you(You have higher speed)
                        if random.randint(1,4) <= 3 and MonsterDead == False:
                            if random.randint(1,100) <= MonHitChance:
                                att = random.randint(int(Monster["Attack"]/1.5),int(Monster["Attack"]*1.3))
                                print("You were hit by the monster for " + str(att) + " damage")
                                stats["Health"] -= int(att * (DmgPer/100))
                            else:
                                print("The monster went to hit you, but it missed you")
                                
                            if stats["Health"] <= 0:
                                fight = False
                                PlayerDead = True
                        else:
                            if random.randint(1,100) <= MonHitChance - 20:
                                heal = int(Monster["Magic"] * (random.randint(75,200)/100))
                                print("The monster was healed for " + str(heal) + " health")
                                Monster["Health"] += heal
                            else:
                                print("The monster tried to heal, but it failed")
                    else:
                        #Monster Attacks you (They have higher speed)
                        if random.randint(1,4) <= 3:
                            if random.randint(1,10) <= 9:
                                att = random.randint(int(Monster["Attack"]/1.5),int(Monster["Attack"]*1.3))
                                print("You were hit by the monster for " + str(att) + " damage")
                                stats["Health"] -= int(att * (DmgPer/100))
                            else:
                                print("The monster went to hit you, but it missed you")
                                
                            if stats["Health"] <= 0:
                                PlayerDead = True
                        else:
                            if random.randint(1,10) <= 7:
                                heal = int(Monster["Magic"] * (random.randint(75,200)/100))
                                print("The monster was healed for " + str(heal) + " health")
                                Monster["Health"] += heal
                            else:
                                print("The monster tried to heal, but it failed")

                        #You use your magic(They have higher speed)
                        if PlayerDead != True:
                            if MagicType == "1":
                                heal = int(stats["Magic"] * (random.randint(75,200)/100))
                                if heal + stats["Health"] >= oldstats["Health"]:
                                    heal = oldstats["Health"] - stats["Health"]
                                    stats["Health"] = oldstats["Health"]
                                    print("You healed yourself for " + str(heal))
                                else:
                                    stats["Health"] += heal
                                    print("You healed yourself for " + str(heal))
                            else:
                                if random.randint(1,100) <= HitChance:
                                    att = random.randint(int(stats["Magic"]/2.5),int(stats["Magic"]*1.3))
                                    print("You cast a spell upon monster for " + str(att) + " damage")
                                    Monster["Health"] -= att
                                else:
                                    print("You attempted to cast your magic, but the spell fizzled")
                                if minion != "":
                                    att = random.randint(int(stats["Attack"]/5),int(stats["Attack"]/2))
                                    print("Your minion " + str(minion) + " hit the monster for " + str(att) + " damage")
                                    Monster["Health"] -= att
                                if Monster["Health"] <= 0:
                                    MonsterDead = True
                        
                            
                                            
            if MonsterDead == True:
                goldGain = random.randint(int(OldMonster*0.5), int(OldMonster*1.5))
                
                gold += goldGain
                print("You found " + str(goldGain) + " gold\nGold: " + str(gold))
                Skill *= float(random.randint(125,135)/100)
                fight = False
                ask = input("What skill do you want to upgrade?\n1: Lvl " + str(SkillLevel["Health"]) + " Health\n2: Lvl " + str(SkillLevel["Attack"]) + " Attack\n3: Lvl "
                            + str(SkillLevel["Speed"]) + " Speed\n4: Lvl " + str(SkillLevel["Magic"]) + " Magic\n")
                check = False
                try:
                    if ask == "1":
                        pass
                except TypeError:
                    check = True
                
                stats["Health"] = oldstats["Health"]
                if check == False:
                    if ask == "1":
                        SkillLevel["Health"] += 1
                        stats["Health"] = int(stats["Health"] * Hincrease)
                        oldstats["Health"] = int(oldstats["Health"] * Hincrease)
                    if ask == "2":
                        SkillLevel["Attack"] += 1
                        stats["Attack"] = int(stats["Attack"] * 1.5)
                        oldstats["Attack"] = int(oldstats["Attack"] * 1.5)
                    if ask == "3":
                        SkillLevel["Speed"] += 1
                        stats["Speed"] = int(stats["Speed"] * 1.5)
                        oldstats["Speed"] = int(oldstats["Speed"] * 1.5)
                    if ask == "4":
                        SkillLevel["Magic"] += 1
                        stats["Magic"] = int(stats["Magic"] * 1.4)
                        oldstats["Magic"] = int(oldstats["Magic"] * 1.4)


                #Level up rewards
                if SkillLevel["Health"] == 3 and HLv3 == False:
                    HLv3 = True
                    print("You found some body armor (+50 Health)")
                    stats["Health"] += 50
                    oldstats["Health"] += 50

                if SkillLevel["Attack"] == 3 and ALv3 == False:
                    ALv3 = True
                    print("You found a bronze sword (+3 attack)")
                    stats["Attack"] += 3
                    oldstats["Attack"] += 3
                if SkillLevel["Speed"] == 3 and SLv3 == False:
                    SLv3 = True
                    print("You found boots of swiftness (+100 Speed)")
                    stats["Speed"] += 100
                    oldstats["Speed"] += 100
                if SkillLevel["Magic"] == 3 and MLv3 == False:
                    MLv3 = True
                    print("You found a rusty wand (+20 Magic)")
                    stats["Magic"] += 20
                    oldstats["Magic"] += 20

                if SkillLevel["Health"] == 7 and HLv7 == False:
                    HLv7 = True
                    print("You come across some health potions (+700 Health)")
                    stats["Health"] += 700
                    oldstats["Health"] += 700

                if SkillLevel["Attack"] == 7 and ALv7 == False:
                    ALv7 = True
                    print("You found the Deathbringer sword (+50 attack)")
                    stats["Attack"] += 50
                    oldstats["Attack"] += 50
                if SkillLevel["Speed"] == 7 and SLv7 == False:
                    SLv7 = True
                    print("You found an old car (+500 Speed)")
                    stats["Speed"] += 500
                    oldstats["Speed"] += 500
                if SkillLevel["Magic"] == 7 and MLv7 == False:
                    MLv7 = True
                    print("You found a wand with a pheonix feather (+80 Magic)")
                    stats["Magic"] += 80
                    oldstats["Magic"] += 80

                if SkillLevel["Health"] == 15 and HLv15 == False:
                    HLv15 = True
                    print("You found the legendary Pills (+70000 Health)")
                    stats["Health"] += 70000
                    oldstats["Health"] += 70000

                if SkillLevel["Attack"] == 15 and ALv15 == False:
                    ALv15 = True
                    print("You found the Epic Hand Cannon (+2000 attack)")
                    stats["Attack"] += 2000
                    oldstats["Attack"] += 2000
                if SkillLevel["Speed"] == 15 and SLv15 == False:
                    SLv15 = True
                    print("You found a rocket ship (+20000 Speed)")
                    stats["Speed"] += 20000
                    oldstats["Speed"] += 20000
                if SkillLevel["Magic"] == 15 and MLv15 == False:
                    MLv15 = True
                    print("You found the magic black hole (+3000 Magic)")
                    stats["Magic"] += 3000
                    oldstats["Magic"] += 3000


                
                if SkillLevel["Health"] == 30 and HLv30 == False:
                    HLv30 = True
                    print("You unlocked the super high health scaling ability\n now every levelup gives you 2 times as much health")
                    Hincrease = 2
                if SkillLevel["Attack"] == 30 and ALv30 == False:
                    ALv30 = True
                    print("You got a killers instinct\nYou now have a 40% chance to oneshot an enemy every round")
                    if Class == "6":
                        Insight += 30
                if SkillLevel["Speed"] == 30 and SLv30 == False:
                    SLv30 = True
                    print("You unlocked the mighty quadruaple critical and pentuple critical")
                if SkillLevel["Magic"] == 30 and MLv30 == False:
                    MLv30 = True
                    minion = input("You warped time and space and now have a minion\nWhat shall you name him?")
                    stats["Magic"] += 3000
                    oldstats["Magic"] += 3000

                    
                ask = input("Do you want to go to the shop?\n1: Yes\n2: No")
                if ask == "1":
                    print("Gold: "  + str(gold))
                    choice = input("What section of the shop do you want to go to?\n1: Health Buffs\n2: Attack Buffs\n3: Speed Buffs\n4: Magic Buffs\n5: Misc.")
                    if choice == "1":
                        if Class != "1":
                            choice = input("1: " + str(HealthItems[0][0]) + " " + str(HealthItems[1][0]) + " Gold\n2: " + str(HealthItems[0][1]) + " " + str(HealthItems[1][1])  + " Gold\n3: " +str(HealthItems[0][2]) + " " + str(HealthItems[1][2]) + " Gold")
                        else:
                            choice = input("1: " + str(HealthItems[0][0]) + " " + str(HealthItems[1][0]) + " Gold\n2: " + str(HealthItems[0][1]) + " "
                                           + str(HealthItems[1][1])  + " Gold\n3: " +str(HealthItems[0][2]) + " "
                                           + str(HealthItems[1][2]) + " Gold\n4: " + str(HealthItems[0][3]) + " " + str(HealthItems[1][3])
                                           + "Gold\n5: " + str(HealthItems[0][4])+" "+str(HealthItems[1][4]) + " Gold")
                        if choice == "1":
                            if HealthItems[0][0] == "Bought":
                                pass
                            else:
                                if gold >= HealthItems[1][0]:
                                    stats["Health"] *= 1.2
                                    oldstats["Health"] *= 1.2
                                    gold -= 500
                                    HealthItems[0][0] = "Bought"
                                    HealthItems[1][0] = "None"
                        if choice == "2":
                            if HealthItems[0][1] == "Bought":
                                pass
                            else:
                                if gold >= HealthItems[1][1]:
                                    stats["Health"] *= 2
                                    oldstats["Health"] *= 2
                                    gold -= 2500
                                    HealthItems[0][1] = "Bought"
                                    HealthItems[1][1] = "None"

                        if choice == "3":
                            if HealthItems[0][2] == "Bought":
                                pass
                            else:
                                if gold >= HealthItems[1][2]:
                                    stats["Health"] *= 4
                                    oldstats["Health"] *= 4
                                    gold -= 15000
                                    HealthItems[0][2] = "Bought"
                                    HealthItems[1][2] = "None"
                        if choice == "4" and Class == "1":
                            if MiscItems[0][3] == "Bought":
                                pass
                            else:
                                if gold >= MiscItems[1][3]:
                                    DmgPer -= 20
                                    
                                    gold -= MiscItems[1][3]
                                    MiscItems[0][3] = "Bought"
                                    MiscItems[1][3] = "None"
                        if choice == "5" and Class == "1":
                            if MiscItems[0][4] == "Bought":
                                pass
                            else:
                                if gold >= MiscItems[1][4]:
                                    DmgPer -= 50
                                    
                                    gold -= MiscItems[1][4]
                                    MiscItems[0][4] = "Bought"
                                    MiscItems[1][4] = "None"


                    elif choice == "2":
                        choice = input("1: " + str(AttackItems[0][0]) + " " + str(AttackItems[1][0]) + " Gold\n2: " + str(AttackItems[0][1]) + " " + str(AttackItems[1][1])  + " Gold\n3: " +str(AttackItems[0][2]) + " " + str(AttackItems[1][2]) + " Gold")
                        if choice == "1":
                            if AttackItems[0][0] == "Bought":
                                pass
                            else:
                                if gold >= AttackItems[1][0]:
                                    stats["Attack"] *= 1.2
                                    oldstats["Attack"] *= 1.2
                                    gold -= AttackItems[1][0]
                                    AttackItems[0][0] = "Bought"
                                    AttackItems[1][0] = "None"
                        if choice == "2":
                            if AttackItems[0][1] == "Bought":
                                pass
                            else:
                                if gold >= AttackItems[1][1]:
                                    stats["Attack"] *= 2
                                    oldstats["Attack"] *= 2
                                    gold -= AttackItems[1][1]
                                    AttackItems[0][1] = "Bought"
                                    AttackItems[1][1] = "None"

                        if choice == "3":
                            if AttackItems[0][2] == "Bought":
                                pass
                            else:
                                if gold >= AttackItems[1][2]:
                                    stats["Attack"] *= 4
                                    oldstats["Attack"] *= 4
                                    gold -= AttackItems[1][2]
                                    AttackItems[0][2] = "Bought"
                                    AttackItems[1][2] = "None"

                    elif choice == "3":
                        choice = input("1: " + str(SpeedItems[0][0]) + " " + str(SpeedItems[1][0]) + " Gold\n2: " + str(SpeedItems[0][1]) + " " + str(SpeedItems[1][1])  + " Gold\n3: " +str(SpeedItems[0][2]) + " " + str(SpeedItems[1][2]) + " Gold")
                        if choice == "1":
                            if SpeedItems[0][0] == "Bought":
                                pass
                            else:
                                if gold >= SpeedItems[1][0]:
                                    stats["Speed"] *= 1.2
                                    oldstats["Speed"] *= 1.2
                                    gold -= SpeedItems[1][0]
                                    SpeedItems[0][0] = "Bought"
                                    SpeedItems[1][0] = "None"
                        if choice == "2":
                            if SpeedItems[0][1] == "Bought":
                                pass
                            else:
                                if gold >= SpeedItems[1][1]:
                                    stats["Speed"] *= 2
                                    oldstats["Speed"] *= 2
                                    gold -= SpeedItems[1][1]
                                    SpeedItems[0][1] = "Bought"
                                    SpeedItems[1][1] = "None"

                        if choice == "3":
                            if SpeedItems[0][2] == "Bought":
                                pass
                            else:
                                if gold >= SpeedItems[1][2]:
                                    stats["Speed"] *= 4
                                    oldstats["Speed"] *= 4
                                    gold -= SpeedItems[1][2]
                                    SpeedItems[0][2] = "Bought"
                                    SpeedItems[1][2] = "None"
                    elif choice == "4":
                        choice = input("1: " + str(MagicItems[0][0]) + " " + str(MagicItems[1][0]) + " Gold\n2: " + str(MagicItems[0][1]) + " " + str(MagicItems[1][1])  + " Gold\n3: " +str(MagicItems[0][2]) + " " + str(MagicItems[1][2]) + " Gold")
                        if choice == "1":
                            if MagicItems[0][0] == "Bought":
                                pass
                            else:
                                if gold >= MagicItems[1][0]:
                                    stats["Magic"] *= 1.2
                                    oldstats["Magic"] *= 1.2
                                    gold -= MagicItems[1][0]
                                    MagicItems[0][0] = "Bought"
                                    MagicItems[1][0] = "None"
                        if choice == "2":
                            if MagicItems[0][1] == "Bought":
                                pass
                            else:
                                if gold >= MagicItems[1][1]:
                                    stats["Magic"] *= 2
                                    oldstats["Magic"] *= 2
                                    gold -= MagicItems[1][1]
                                    MagicItems[0][1] = "Bought"
                                    MagicItems[1][1] = "None"

                        if choice == "3":
                            if MagicItems[0][2] == "Bought":
                                pass
                            else:
                                if gold >= MagicItems[1][2]:
                                    stats["Magic"] *= 4
                                    oldstats["Magic"] *= 4
                                    gold -= MagicItems[1][2]
                                    MagicItems[0][2] = "Bought"
                                    MagicItems[1][2] = "None"
                    elif choice == "5":
                        if len(MiscItems[0]) == 3:
                            choice = input("1: " + str(MiscItems[0][0]) + " " + str(MiscItems[1][0]) + " Gold\n2: " + str(MiscItems[0][1]) + " " + str(MiscItems[1][1])  + " Gold\n3: " +str(MiscItems[0][2]) + " " + str(MiscItems[1][2]) + " Gold")
                        if Class == "6" or Class == "7":
                            choice = input("1: " + str(MiscItems[0][0]) + " " + str(MiscItems[1][0]) + " Gold\n2: " + str(MiscItems[0][1]) + " "
                                           + str(MiscItems[1][1])  + " Gold\n3: " +str(MiscItems[0][2]) + " "
                                           + str(MiscItems[1][2]) + " Gold\n4: " + str(MiscItems[0][3]) + " " + str(MiscItems[1][3])
                                           + "Gold\n5: " + str(MiscItems[0][4])+" "+str(MiscItems[1][4]) + " Gold")
                            
                        if choice == "1":
                            if MiscItems[0][0] == "Bought":
                                pass
                            else:
                                if gold >= MiscItems[1][0]:
                                    HitChance = 110
                                    gold -= MiscItems[1][0]
                                    MiscItems[0][0] = "Bought"
                                    MiscItems[1][0] = "None"
                        if choice == "2":
                            if MiscItems[0][1] == "Bought":
                                pass
                            else:
                                if gold >= MiscItems[1][1]:
                                    if MagicType == "1":
                                        MagicType = "2"
                                    else:
                                        MagicType == "1"
                                    gold -= MiscItems[1][1]
                                    MiscItems[0][1] = "Bought"
                                    MiscItems[1][1] = "None"

                        if choice == "3":
                            if MiscItems[0][2] == "Bought":
                                pass
                            else:
                                if gold >= MiscItems[1][2]:
                                    stats["Magic"] *= 100
                                    oldstats["Magic"] *= 100
                                    stats["Attack"] *= 100
                                    oldstats["Attack"] *= 100
                                    stats["Speed"] *= 100
                                    oldstats["Speed"] *= 100
                                    stats["Health"] *= 100
                                    oldstats["Health"] *= 100
                                    Hitchance = 1000
                                    
                                    gold -= MiscItems[1][2]
                                    MiscItems[0][2] = "Bought"
                                    MiscItems[1][2] = "None"
                        if choice == "4" and Class == "6":
                            if MiscItems[0][3] == "Bought":
                                pass
                            else:
                                if gold >= MiscItems[1][3]:
                                    Insight += 20
                                    
                                    gold -= MiscItems[1][3]
                                    MiscItems[0][3] = "Bought"
                                    MiscItems[1][3] = "None"
                        if choice == "5" and Class == "6":
                            if MiscItems[0][4] == "Bought":
                                pass
                            else:
                                if gold >= MiscItems[1][4]:
                                    OneShot += 20
                                    
                                    gold -= MiscItems[1][4]
                                    MiscItems[0][4] = "Bought"
                                    MiscItems[1][4] = "None"
                        if choice == "4" and Class == "7":
                            if MiscItems[0][3] == "Bought":
                                pass
                            else:
                                if gold >= MiscItems[1][3]:
                                    BurnPer += 20
                                    
                                    gold -= MiscItems[1][3]
                                    MiscItems[0][3] = "Bought"
                                    MiscItems[1][3] = "None"
                        if choice == "5" and Class == "7":
                            if MiscItems[0][4] == "Bought":
                                pass
                            else:
                                if gold >= MiscItems[1][4]:
                                    BurnPer += 40
                                    
                                    gold -= MiscItems[1][4]
                                    MiscItems[0][4] = "Bought"
                                    MiscItems[1][4] = "None"
                        
                    else:
                        print("That is not a shop number")
                        

                                
            if PlayerDead == True:
                DeathCount += 1
                if DeathCount != 4:
                    PlayerDead = False
                    Skill /= 3
                    print("You died")
                    ask = input("Do you want to continue?\n1: Yes\n2: No")
                    if ask == "2":
                        run = False
                        game_run = False
                        fight = False
                    else:
                        fight = False
                else:
                    run = False
                    game_run = False
                    fight =  False
                
                                
    print("You lost\nSkill level: " + str(int(Skill)))

Rpg()
    
