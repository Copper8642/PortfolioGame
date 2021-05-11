from random import *

#The class that holds the player's attributes
class Hero:
    def __init__(self) -> None:
        self.maxhealth = 100
        self.health = 100
        self.mana = 10
        self.inventory = [Weapon1, Weapon2, Weapon3, Potion]
        self.spells = [Spell1, Spell2, Spell3]
        self.equipped = None

#The class that holds the enemy goblin's attributess
class Goblin:
    def __init__(self) -> None:
        self.health = 100
        self.stylesknown = [None, "Defensif Walle", "Develrysh Danse", "Angre Agreshin"]
        self.style = None

#The class that will represent the player's weapons and potion(s)
class Item:
    def __init__(self, name, damage, heal, style_counter, type) -> None:
        self.name = name
        self.damage = damage
        self.heal = heal
        self.style_counter = style_counter
        self.type = type
    def __repr__(self) -> str:
        return self.name
    def __str__(self) -> str:
        return self.name

#The class that represents the player's spells
class Spell:
    def __init__(self, name, damage, heal, cost) -> None:
        self.name = name
        self.damage = damage
        self.heal = heal
        self.cost = cost
    def __repr__(self) -> str:
        return self.name
    def __str__(self) -> str:
        return self.name

#The things in the game
Weapon1 = Item("Shaerpend Blaed", 8, 0, "Defensif Walle", "weapon")
Weapon2 = Item("Elfin Lonbow", 7, 0, "Develrysh Danse", "weapon")
Weapon3 = Item("Strongspeer", 8, 0, "Angre Agreshin", "weapon")
Potion = Item("Helt Poshun", 0, 15, None, "potion")
Spell1 = Spell("Fyrebol", 12, 0, 4)
Spell2 = Spell("Healeth", 0, 10, 3)
Spell3 = Spell("Vim Drainth", 8, 4, 3)
Player = Hero()
Enemy = Goblin()

#An Intro
print("Ye art un warrion mosteth verilous and coureouth, bont befoeth the, un Goblin!\n")
print("It wouldth best wisen for ye te drawnth un weapen.\n")

#The function for choosing an item to wield
def Inventory():
    for item in Player.inventory:
        if item.type == "weapon":
            print(f"Yout knapsaque hath un {item.name} whicheth dealth {item.damage} and provent powerr agenst te Goblin styles ef {item.style_counter}.")
        else:
            print(f"Ye stilleth care un {item.name} whicheth healun ye fo {item.heal} vim und singuleth thyme.")
    if Potion in Player.inventory:
        use_item = input("Whicheth itom wouldth ye liek te holld?  Ort arst the hearn fo te poshun?\n").upper()
    else:
        use_item = input("Whicheth itom wouldth ye liek te holld?\n").upper()
    chosen_item = []
    for thing in Player.inventory:
        if thing.name.upper().startswith(use_item):
            chosen_item.append(thing)
    if len(chosen_item) == 0:
        print("Yeeth appur te not chosn anething.\n")
        Inventory()
    elif len(chosen_item) > 1:
        print(f"Yu culd haff ment ant uff thees: {chosen_item}.\n")
        Inventory()
    elif len(chosen_item) == 1:
        if chosen_item[0].type == "weapon":
            Player.equipped = chosen_item[0]
            print(f"Ye holld te {Player.equipped}\n")
        elif chosen_item[0].type == "potion":
            if Player.equipped != None:
                Player.health = min(Player.maxhealth, Player.health + chosen_item[0].heal)
                print(f"Ya drunk yer onle {chosen_item[0]} and now have {Player.health} health.\n")
                Player.inventory.remove(chosen_item[0])
            else:
                print("Ye shuld greb un weapen beforth ye drinque!\n")
                Inventory()

Inventory()


#The loop, which SHOULD have had attack, and spell, and perhaps status separated into different functions, like inventory was
while Player.health > 0 and Enemy.health > 0:
    playerturn = ""
    playerturn = input("It esth yon tyrn!  Whot dost ye doeth?\n  Type 'Attack' 'Spell' 'Inventory' or 'Status'\n").lower()
    if playerturn == "attack":
        if Player.equipped.style_counter != Enemy.style:
            print(f"Yout del {Player.equipped.damage} tost yeth Goblin wiff yer {Player.equipped}.\n")
            Enemy.health -= Player.equipped.damage
        if Player.equipped.style_counter == Enemy.style:
            print(f"Yoult countr te Goblin's {Enemy.style} style, dealing {Player.equipped.damage + 3} wef yons {Player.equipped}.\n")
            Enemy.health -= Player.equipped.damage + 3
    elif playerturn == "spell":
        whatspell = input(f"Whot spellcastery wouldth ye leik ton cahst?\n {Spell1} costs {Spell1.cost} mana. {Spell2} costs {Spell2.cost} mana. {Spell3} costs {Spell3.cost} mana.\n Ye haff {Player.mana} mana.\n").upper()
        chosen_spell = []
        for spell in Player.spells:
            if spell.name.upper().startswith(whatspell):
                chosen_spell.append(spell)
        if len(chosen_spell) == 0:
            print("Yeeth appur te not chosn anething.\n")
            continue
        elif len(chosen_spell) > 1:
            print(f"Yu culd haff ment ant uff thees: {chosen_spell}.\n")
            continue
        elif len(chosen_spell) == 1:
            chosen_spell = chosen_spell[0]
            if chosen_spell.cost <= Player.mana:
                print(f"Yu cahst {chosen_spell}. {'Yount deelth ' + str(chosen_spell.damage) + ' damaj. '  if chosen_spell.damage > 0 else ''}{'Yo healeth ' + str(chosen_spell.heal) + ' helt. ' if chosen_spell.heal > 0 else ''}Yoll spents {chosen_spell.cost} mana.\n")
                Enemy.health -= chosen_spell.damage
                Player.health = min(Player.maxhealth, Player.health + chosen_spell.heal)
                Player.mana -= chosen_spell.cost
            else:
                print("Ya don heff le mana!\n")
                continue
    elif playerturn == "inventory":
        Inventory()
    elif playerturn == "status":
        print(f"Yon hav {Player.health} oud uf {Player.maxhealth} healt, az wel az {Player.mana} mana.  Th Goblin stel hath {Enemy.health} helt leff {'and is in ' + Enemy.style + 'stance' if Enemy.style != None else ''}.\n")
        continue
    if Enemy.health <= 0:
        print("Unf Goblin est deadened!  Thou art victorio!\n")
        break
    print("Thel Goblin acteth!")
    this_turns_damage = randint(5,12)
    Player.health -= this_turns_damage
    print(f"Thon Goblin dealeth {this_turns_damage} damaag ton thee.\n")
    if Player.health <= 0:
        print("Yonth art deadened et defeath ignobly\n")
        break
    style_change = randint(0,9)
    if style_change == 0 and Enemy.style != Enemy.stylesknown[0]:
        print("Thou Goblin dropeths al stanse et stile.")
        Enemy.style = Enemy.stylesknown[0]
    if style_change == 1 and Enemy.style != Enemy.stylesknown[1]:
        print(f"Thou Goblin adopteth {Enemy.stylesknown[1]} stylne.\n")
        Enemy.style = Enemy.stylesknown[1]
    if style_change == 2 and Enemy.style != Enemy.stylesknown[2]:
        print(f"Thou Goblin adopteth {Enemy.stylesknown[2]} stylne.\n")
        Enemy.style = Enemy.stylesknown[2]
    if style_change == 3 and Enemy.style != Enemy.stylesknown[3]:
        print(f"Thou Goblin adopteth {Enemy.stylesknown[3]} stylne.\n")
        Enemy.style = Enemy.stylesknown[3]