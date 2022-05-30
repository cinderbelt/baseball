
import numpy as np
from socket import *

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', 8080))
serverSock.listen(1)

connectionSock, addr = serverSock.accept()

print(str(addr),'에서 접속이 확인되었습니다.')

data = connectionSock.recv(1024)
print('받은 데이터 : ', data.decode('utf-8'))

connectionSock.send('I am a server.'.encode('utf-8'))
print('메시지를 보냈습니다.')


inning =1
class playerclass():
    def __init__(self,name):
        self.score=0
        self.name=name

    def pitching(self):
        global pitch
        if self==player1:
            self.pitch = int(input('pitch'))
            connectionSock.send(str(self.pitch).encode('utf-8'))

        else:
            self.pitch=connectionSock.recv(1024)
            self.pitch=int(self.pitch.decode('utf-8'))



    def batting(self):
        global bat

        if self==player1:
            self.bat= int(input('bat'))
            connectionSock.send(str(self.bat).encode('utf-8'))
        else:
            self.bat=connectionSock.recv(1024)
            self.bat=int(self.bat.decode('utf-8'))



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
    connectionSock.send(playername.encode('utf-8'))
    tb=input('top or bottom')
    connectionSock.send(tb.encode('utf-8'))
    global player1
    player1= playerclass(playername)
    player2name=connectionSock.recv(1024)
    player2name=player2name.decode('utf-8')
    global player2
    player2=playerclass(player2name)
    global inning

    if tb== 'top':
       while inning <4.0:
           game(player1, player2)
           game(player2,player1)
           if inning==4.0 and (player1.score < player2.score):
              print('player2 win')
              print('player:', player1.score, ' player2:', player2.score)
              break
           if (player1.score > player2.score) and inning ==4.0:
               print('player win')
               print('player:', player1.score, ' player2:', player2.score)
               break
           elif (player1.score == player2.score) and inning ==4.0:
               print('draw')
               print('player:', player1.score, ' player2:', player2.score)
               break

    if tb== 'bottom':
        while inning < 4:
            game(player2, player1)
            game(player1, player2)
            if inning == 3.5 and (player1.score > player2.score):
                print('player win')
                print('player:',player1.score,' player2:',player2.score)
                break

            if (player1.score < player2.score) and inning ==4:
                print('player2 win')
                print('player:', player1.score, ' player2:', player2.score)
                break

            elif (player1.score == player2.score) and inning ==4:
                print('draw')
                print('player:', player1.score, ' player2:', player2.score)
                break

main()













