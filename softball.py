#!/Users/otukutun/dev/python/default33/bin/python
# -*- coding: utf-8 -*-
from os import system
import sys
import random
import time

def say(name,position,dajun):
    system('say ' + str(name) + 'のポジションは' + str(position) + 'でだじゅんわ' +  str(dajun) + 'ばんです')

def output_score():
    return random.randint(1,10)

def decide_position(position):
    position_num = random.sample(position,1)

def decide_dajun(position):
    dajun_num = random.sample(dajun,1)

def main():
    argvs = sys.argv #引数を格納したリスト
    del argvs[0]
    argc = len(argvs)
    if argc == 0:
        print('引数を指定してください。')
        sys.exit()

    test = []
    dajun = [1,2,3,4,5,6,7,8,9]
    position = ['ピッチャー','キャッチャー','いちるい','にるい','さんるい','ショート','ライト','センター','レフト']
    for i in argvs:
        position_num = random.sample(position,1)
        dajun_num = random.sample(dajun,1)
        test.append({'name' : i, 'position': position_num[0],'dajun': dajun_num[0] })
        position.remove(position_num[0])
        #position.pop(position_num)
        dajun.remove(dajun_num[0])
        #dajun.pop(dajun_num[0])
    for i in test:
        say(i['name'],i['position'],i['dajun'])
        print(i['name'] + 'のポジションは' + str(i['position']) + 'で、打順は' + str(i['dajun']) + 'です')
        time.sleep(0.3)

if __name__ == '__main__':
    main()
