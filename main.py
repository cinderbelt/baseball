import random
class player():
    def __init__(self,name):
        self.score=0
        self.name=name

    def pitching(self):
        if self == com:
            pitch= random.randint(0,1)
        else:
            pitch = int(input('pitch'))


    def batting(self):
        if self == com:
            if outcounts != 2:
                bat= random.randint(0,2)

            else:
                bat= random.randint(0,1)

        else:
            bat= int(input('bat'))



def game(atk,defend):
    global outcounts
    outcounts =0
    strike=0
    ball=0
    base=[0,0,0,0]
    while outcounts <3:
        atk.batting()
        defend.pitching()
        if atk.bat != 2:
            if defend.pitch != atk.bat:
                strike+=1
            elif defend.pitch==0:
                ball+=1

            else:
                if base != [1,1,1,1]:
                    base.append(1)

                else:
                    atk.score+=1
        else:
            if defend.pitch == 1:
                atk.score += sum(base)
                base=[0,0,0,0]
            else:
                outcounts =3

        if strike ==2:
            outcounts +=1
            strike=0
        if ball ==3:
            if base != [1,1,1,1]
                base.append(1)
                ball=0
            else:
                atk.score+=1
                ball=0

def main():
    playername=input('input your name')
    tb=input('top or bottom')
    player=player(playername)
    com=player('com')
    inning=1
    if tb== 'top':
       while outcounts <3:
           game(player,com)
           if outcounts==3:







