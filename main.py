import random

player_hp =100
enemy_hp=100
flag= True
critical = 0
print("Welcome to my turn Based Combat Game")
print("Just enter the no. corresponding to the options to play the game")
print("Tip before Starting - Heavy and Chain Attacks are OP but at the cost of something!!")


def enemyAtt(rem):
    global critical
    if(critical>5):
        print("You suffered a hit from the curse")
        rem -=75
        critical=0
    global enemy_hp
    r= random.randint(1,2)
    x=random.randint(1,5)
    if(enemy_hp>25):
        if(r==1 and x!=2):
            r=random.randint(1,3)
            if(r==1):
                print("Enemy did Light Attack ")
                rem-=20
            elif(r==2):
                print("Enemy did Strong Attack ")
                rem-=25
            elif(r==3):
                print("Enemy did Chain Attack ")
                rem -= 50
        else:
            print("The enemy Stumbled")
    else:
        if(x!=2):
            enemy_hp+=25
            print("Enemy used Heal")
        else:
            print("The enemy Stumbled")

    return rem



def showSt():
    global player_hp
    global enemy_hp
    print("The Health points remaining for the enemy are",enemy_hp)
    print("The Heath points remaining for you are",player_hp)

while (flag):
    print("Enter Your Choice:\n 1 - Physical Attack \n 2 - Defense")
    n = int(input())

    if (n == 1):
        print("Enter Your Choice:\n 1 - Light Attack \n 2 - Strong Attack \n 3 - Chain Attack")
        n = int(input())
        rand = random.randint(0, 2)
        if (rand != 0 and n == 1):
            print("You chose light Attack")
            enemy_hp -= 20
            player_hp = enemyAtt(player_hp)
            if (player_hp <= 0):
                print("Looks Like You died")
                flag = False
                break
            elif (enemy_hp <= 0):
                print("Amazing Victory")
                flag = False
                break
            showSt()

        elif (rand != 0 and n == 2):
            print("You chose heavy Attack")
            enemy_hp -= 25
            critical+=1
            player_hp=enemyAtt(player_hp)
            if (player_hp <= 0):
                print("Even the blades of Zeus weren't Able to help the hero!! You Died")
                flag = False
                break
            elif (enemy_hp <= 0):
                print("You are just Amazing")
                flag = False
                break
            showSt()
        elif (rand != 0 and n == 3):
            print("You chose Chain Attack")
            enemy_hp -= 50
            critical+=2;
            player_hp = enemyAtt(player_hp)
            if (player_hp <= 0):
                print("Thy fate Was decided from the Start !! You LOSE")
                flag = False
                break
            elif (enemy_hp <= 0):
                print("What do we expect from a hero!! you WON")
                flag = False
                break
            showSt()
        else:
            print("Your Attack Missed")
            player_hp=enemyAtt(player_hp)
            if (player_hp <= 0):
                print("You Lost")
                flag = False
                break
            elif (enemy_hp <= 0):
                print("Yow Won!!")
                flag = False
                break
            showSt()
    elif (n == 2):
        print("Enter Your Choice:\n 1 - Guard \n 2 - Heal")
        n = int(input())
        rand = random.randint(0, 2)
        if (n == 1 and rand != 0):
            print("You were able to guard the enemy's Attack")
        elif (n == 1 and rand != 0):
            print("You healed 20 points")
            player_hp += 20
            player_hp=enemyAtt(player_hp)
            if (player_hp <= 0):
                print("You Lost")
                flag = False
            elif (enemy_hp <= 0):
                print("Yow Won!!")
                flag = False
            showSt()
        else:
            print("Sorry Bud, Your defensive measures failed !!")
            player_hp=enemyAtt(player_hp)
            if (player_hp <= 0):
                print("You Lost")
                flag = False
            elif (enemy_hp <= 0):
                print("Yow Won!!")
                flag = False
            showSt()
















