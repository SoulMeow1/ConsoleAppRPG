import os
import pandas as pd
import random as rd

class Player (object):
    def __init__(self, h, s, a, d):
        self.hp = h
        self.maxHp = h
        self.skills = s
        self.attack = a
        self.defense = d

    def printPlayerStatus(self):
        print("===== Player =====")
        print("= HP: ", self.hp)
        print("Attack: ", self.attack)
        print("Defense: ", self.defense)

    def printSkills(self, skillsDex):
        for i in self.skills:
            print(i, ": ", skillsDex.iloc[i]['Name'])

    def useSkill(self, skillsDex, choice, e, l):
        li = [int(x) for x in skillsDex.iloc[choice]['Value_range'].split(',')]
        att = skillsDex.iloc[choice]['Attribute_Affected']
        if att == 'HP':
            if li[0] < 0:
                i = rd.randint(li[1], li[0])
                e.hp += i - self.attack + e.defense
                if e.hp > e.maxHp:
                    e.hp = e.maxHp
                l.insertLog(f"Player used {skillsDex.iloc[choice]['Name']}! It deals {i} amount of damage.")
            else:#for now, this line will never run
                i = rd.randint(li[0], li[1])
                e.hp += i
                l.insertLog(f"Player used {skillsDex.iloc[choice]['Name']}! It deals {i} amount of damage.")

        elif att == 'Attack':
            if li[0] < 0:
                i = rd.randint(li[1], li[0])
                if e.attack + i >= 0:
                    e.attack += i
                    l.insertLog(f"Player used {skillsDex.iloc[choice]['Name']}! {e.name}'s attack has been reduced.")
                else:
                    l.insertLog(f"Player used {skillsDex.iloc[choice]['Name']}! But {e.name}'s attack cannot be reduced further.")
            else:
                i = rd.randint(li[0], li[1])
                if self.attack + i <= 15:
                    self.attack += i
                    l.insertLog(f"Player used {skillsDex.iloc[choice]['Name']}! Player's attack has been increased.")
                else:
                    l.insertLog(f"Player used {skillsDex.iloc[choice]['Name']}! But Player's attack cannot be increased further.")

        elif att == 'Defense':
            if li[0] < 0:
                i = rd.randint(li[1], li[0])
                if e.defense + i >= 0:
                    e.defense += i
                    l.insertLog(f"Player used {skillsDex.iloc[choice]['Name']}! {e.name}'s defense has been reduced.")
                else: 
                    l.insertLog(f"Player used {skillsDex.iloc[choice]['Name']}! But {e.name}'s defense cannot be reduced further.")
            else:
                i = rd.randint(li[0], li[1])
                if self.defense + i <= 15:
                    self.defense += i
                    l.insertLog(f"Player used {skillsDex.iloc[choice]['Name']}! Player's defense has been increased.")
                else:
                    l.insertLog(f"Player used {skillsDex.iloc[choice]['Name']}! But Player's defense cannot be increased further.")

        

class Enemy(object):
    def __init(self):
        self.name = None
        self.hp = None
        self.maxHp = None
        self.skills = None
        self.attack = None
        self.defense = None

    def printEnemyStatus(self):
        print("===== ", self.name, " =====")
        print("HP: ", self.hp)
        print("Attack: ", self.attack)
        print("Defense: ", self.defense)
        print("Skills: ", self.skills)

    def genRandomEnemy(self, enemyDex, list):
        idx = rd.randint(0, len(list) - 1)
        idx = list[idx]
        self.name = enemyDex.iloc[idx]['Name']
        self.hp = enemyDex.iloc[idx]['HP']
        self.maxHp = self.hp
        self.attack = enemyDex.iloc[idx]['Attack']
        self.defense = enemyDex.iloc[idx]['Defense']
        self.skills = [int(x) for x in enemyDex.iloc[idx]['Skills_index'].split(',')]

    def useSkill(self, skillsDex, p1, l):
        idx = rd.randint(0, len(self.skills) - 1)
        idx = self.skills[idx]
        li = [int(x) for x in skillsDex.iloc[idx]['Value_range'].split(',')]
        att = skillsDex.iloc[idx]['Attribute_Affected']
        if att == 'HP':
            if li[0] < 0:
                i = rd.randint(li[1], li[0])
                p1.hp += i - self.attack + p1.defense
                if p1.hp > p1.maxHp:
                    p1.hp = p1.maxHp
                l.insertLog(f"{self.name} used {skillsDex.iloc[idx]['Name']}! It deals {i} amount of damage.")
            else:#for now, this line will never run
                i = rd.randint(li[0], li[1])
                p1.hp += i
                l.insertLog(f"{self.name} used {skillsDex.iloc[idx]['Name']}! It deals {i} amount of damage.")

        elif att == 'Attack':
            if li[0] < 0:
                i = rd.randint(li[1], li[0])
                if p1.attack + i >= 0:
                    p1.attack += i
                    l.insertLog(f"{self.name} used {skillsDex.iloc[idx]['Name']}! Player's attack has been reduced.")
                else:
                    l.insertLog(f"{self.name} used {skillsDex.iloc[idx]['Name']}! But Player's attack cannot be reduced further.")
            else:
                i = rd.randint(li[0], li[1])
                if self.attack + i <= 15:
                    self.attack += i
                    l.insertLog(f"{self.name} used {skillsDex.iloc[idx]['Name']}! {self.name}'s attack has been increased.")
                else: 
                    l.insertLog(f"{self.name} used {skillsDex.iloc[idx]['Name']}! But {self.name}'s attack cannot be increased further.")

        elif att == 'Defense':
            if li[0] < 0:
                i = rd.randint(li[1], li[0])
                if p1.defense + i >= 0:
                    p1.defense += i
                    l.insertLog(f"{self.name} used {skillsDex.iloc[idx]['Name']}! Player's defense has been reduced.")
                else:
                    l.insertLog(f"{self.name} used {skillsDex.iloc[idx]['Name']}! But Player's defense cannot be reduced further.")
            else:
                i = rd.randint(li[0], li[1])
                if self.defense + i <= 15:
                    self.defense += i
                    l.insertLog(f"{self.name} used {skillsDex.iloc[idx]['Name']}! {self.name}'s defense has been increased.")
                else: 
                    l.insertLog(f"{self.name} used {skillsDex.iloc[idx]['Name']}! But {self.name}'s defense cannot be increased further.")



class Skill (object):
    def __init__(self):
        self.name = None

class Log (object):
    def __init__(self):
        self.messages = None

    def insertLog(self, s):
        if self.messages == None:
            self.messages = [s]

        elif len(self.messages) == 10:
            self.messages = self.messages[:-1]
            self.messages = [s] + self.messages

        else: 
            self.messages.append(s)

    def printLog(self):
        if self.messages == None:
            return

        for s in self.messages:
            print(s)

def startMenu():
    choice = 0
    while choice != 3:
        os.system('cls')
        l.printLog()
        print("====== Console App RPG ======")
        print("= 1. New Game               =")
        print("= 2. New Game (hard)        =")
        print("= 3. Quit                   =")
        print("=                           =")
        print("== Developed By Ling Peng  ==")
        choice = int(input("choice: "))
        if choice == 1:
            newGame(0)
        elif choice == 2:
            newGame(1)
        elif choice == 3:
            print("Thanks for playing. Bye bye!")

    exit()

def newGame(difficulty):
    skillsDex = pd.read_csv('skillsDex_ver1.csv')
    enemyDex = pd.read_csv('enemyDex_ver1.csv')
    p1 = Player(100, [0, 4, 5, 6, 7, 8], 5, 5)
    e = Enemy()
    if difficulty == 0:
        e.genRandomEnemy(enemyDex, [0, 1, 2, 3, 4, 5])
    else:
        e.genRandomEnemy(enemyDex, [6, 7])

    while p1.hp > 0 and e.hp > 0:
        os.system('cls')
        l.printLog()
        p1.printPlayerStatus()
        print()
        e.printEnemyStatus()
        print()
        print("Actions: ")
        p1.printSkills(skillsDex)
        choice = int(input("What would you like to do: "))
        p1.useSkill(skillsDex, choice, e, l)
        e.useSkill(skillsDex, p1, l)

    if e.hp < 0:
        l.insertLog(f"You have defeated {e.name}!")

    else: 
        l.insertLog(f"{e.name} has defeated you!")

l = Log()
l.messages = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
startMenu()


