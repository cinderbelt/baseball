
import numpy as np

inning =1
class playerclass():
    def __init__(self,name):
        self.score=0
        self.name=name

    def pitching(self):
        global pitch
        if self == com:
            self.pitch= np.random.choice(2,1,p=[0.6,0.4])
        else:
            self.pitch = int(input('pitch'))


    def batting(self):
        global bat
        if self == com:
            if outcounts != 2:
                self.bat= np.random.choice(3,1,p=[0.53,0.4,0.07])

            else:
                self.bat = np.random.choice(2, 1, p=[0.6, 0.4])

        else:
            self.bat= int(input('bat'))



def game(atk,defend):
    global outcounts
    global inning

    outcounts =0
    strike=0
    ball=0
    base=[]
    while outcounts <3:
        atk.batting()
        defend.pitching()
        if atk.bat != 2:
            if defend.pitch != atk.bat:
                strike+=1
                if defend.pitch ==1:
                    print('call strike')
                else:
                    print('swing and a miss')
                if strike !=2:
                    if ball==0:
                        print(str(strike)+'strike'+' '+'no ball')
                    else:
                        print(str(strike) + 'strike' + ' ' + str(ball) + 'ball')
            elif defend.pitch==0:
                ball+=1
                print('ball')
                if ball !=3:
                    print(str(strike) + 'strike' + ' ' + str(ball) + 'ball')

            else:
                if base != [1,1,1]:
                    base.append(1)
                    strike=0
                    ball=0
                    print('hit')
                    print(sum(base),'runner on base')
                    if outcounts != 0:
                        print(outcounts, 'out')
                    else:
                        print('no out')

                else:
                    atk.score+=1
                    strike=0
                    ball=0
                    print('hit')
                    print('runner comes in and still full base')
                    print(atk.name + ':' + str(atk.score) +' ' +defend.name + ':', defend.score)
                    if outcounts != 0:
                        print(outcounts, 'out')
                    else:
                        print('no out')
        else:
            if defend.pitch == 1:
                if base != []:
                    atk.score += sum(base)+1
                else:
                    atk.score += 1
                    base=[0]
                print(sum(base)+1,'runhomerun')
                print(atk.name + ':' + str(atk.score) + ' '+defend.name + ':', defend.score)
                if outcounts != 0:
                    print(outcounts, 'out, base unloaded')
                else:
                    print('no out, base unloaded')
                base=[]
                strike=0
                ball=0
            else:
                print('big swing and a miss! inning end!')
                outcounts =3

        if strike ==2:
            outcounts +=1
            strike=0
            ball =0
            print('strike out')
            if outcounts != 3:
                print(str(outcounts)+'out')
        if ball ==3:
            if base != [1,1,1]:
                base.append(1)
                ball=0
                strike =0
                print('base on ball')
                print(sum(base), 'runner on base')
                if outcounts !=0:
                    print(outcounts, 'out')
                else:
                    print('no out')

            else:
                atk.score+=1
                ball=0
                strike =0
                print('base on ball')
                print('runner comes in and still full base')
                print(atk.name + ':' + str(atk.score)+' ' +defend.name + ':',defend.score)
                if outcounts !=0:
                    print(outcounts, 'out')
                else:
                    print('no out')

        if outcounts == 3:
            inning+=0.5
            if inning%1==0 and inning != 4:
                print('three out change')
                print('top of the',inning//1,'inning')
                print(atk.name + ':' + str(atk.score) + ' ' + defend.name + ':', defend.score)

            elif inning%1!=0 and inning != 4:
                print('three out change')
                print('bottom of the',inning//1,'inning')
                print(atk.name + ':' + str(atk.score) + ' ' + defend.name + ':', defend.score)


def main():
    playername=input('input your name')
    tb=input('top or bottom')
    player= playerclass(playername)
    global inning
    global com
    com=playerclass('com')
    if tb== 'top':
       while inning <4.0:
           game(player, com)
           game(com,player)
           if inning==4.0 and (player.score < com.score):
              print('com win')
              print('player:', player.score, ' com:', com.score)
              break
           if (player.score > com.score) and inning ==4.0:
               print('player win')
               print('player:', player.score, ' com:', com.score)
               break
           elif (player.score == com.score) and inning ==4.0:
               print('draw')
               print('player:', player.score, ' com:', com.score)
               break

    if tb== 'bottom':
        while inning < 4:
            game(com, player)
            game(player, com)
            if inning == 3.5 and (player.score > com.score):
                print('player win')
                print('player:',player.score,' com:',com.score)
                break

            if (player.score < com.score) and inning ==4:
                print('com win')
                print('player:', player.score, ' com:', com.score)
                break

            elif (player.score == com.score) and inning ==4:
                print('draw')
                print('player:', player.score, ' com:', com.score)
                break

main()













