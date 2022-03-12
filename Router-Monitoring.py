# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 09:32:52 2020
@author: Jayden
"""
# import os
import sys
import os



### Header for TimeStamp ###
import time
from datetime import datetime

### Header for "dd:dd:dd" regexp ###
import re

### Header for TTS play ###
import winsound as ws
import wave
import pygame

### Window Console Font ###
from colorama import init, Fore
init(autoreset=True)

### Global Var
path = {(Skip Caused BY Security)}
old_router_log = {}
new_router_log = {}
diff_log = {}
result_log_list = []
result_log_dict = {(Skip Caused BY Security) }

### Play Beep Sound ###
def beepsound():
    freq = 2000    # range : 37 ~ 32767
    dur = 200     # ms
    ws.Beep(freq, dur) # winsound.Beep(frequency, duration)
    ws.Beep(freq, dur) # winsound.Beep(frequency, duration)
    ws.Beep(freq, dur) # winsound.Beep(frequency, duration)
    ws.Beep(freq, dur) # winsound.Beep(frequency, duration)
    ws.Beep(freq, dur) # winsound.Beep(frequency, duration)


### Play TTS ###
def play_sound() :
    for i in router_log_path :
        if diff_log[i][1] == 1:
            clock = pygame.time.Clock()
            play_path = os.getcwd()+"\\TTS\\" + i + '.wav'
            file_wav = wave.open(play_path)
            frequency = file_wav.getframerate()
            pygame.mixer.init(frequency=frequency)
            pygame.mixer.music.load(play_path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                clock.tick(1)
        else:
            continue
        
### Input Router Log's Path

def input_path(): 
    log_path=[]
    
    log_path.append(os.getcwd()+'\\log\\(Skip Caused BY Security)')
    (Skip Caused BY Security)
    j=0
    for i in path: 
        path[i] = log_path[j]
        j=j+1
    return path


### Read Router's Log ###
def read_log(router_log_path):
    router_log = {}   
    for i in router_log_path: 
        f = open(router_log_path[i],'r',encoding='UTF8',errors='ignore')
        router_log[i] = [f.readlines()]
#        router_log[i][0][len(router_log[i][0])-1] = router_log[i][0][len(router_log[i][0])-1] + '\n'
        f.close()  
    return router_log


### Confirm Log Format ###
def is_log(string):
    if re.search('\d{2}:\d{2}:\d{2}',string) != None : 
        return True
    else :
        return False


### Pasring Log Format ###
def parse_log(router_log):
    for i in router_log_path:         
        line_i = 0
        while line_i < len(router_log[i][0]):
            if is_log(router_log[i][0][line_i]) :
                line_i += 1
                continue
            else :
                del router_log[i][0][line_i]
                
                
### diff B-A ###
def is_diff(A_log, B_log):
    FLAG = False
    for i in router_log_path:
        diff_log[i] = [ list(set(B_log[i][0]) - set(A_log[i][0]))]
        diff_log[i].append([0])
        
        if diff_log[i][0]:
            diff_log[i][1] = 1
            FLAG = True
        else:
            diff_log[i][1] = 0    
    return FLAG

def collect():
    ### 수집 주기 10s ###
#    for i in range(10,0,-1):
    for i in range(4,0,-1):
        sys.stdout.write("■■■■■■■■")
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("■■■■■■■■■")
    sys.stdout.flush()
    print("")
    
def remove_dup(li):
    temp_set = set()
    res = []
    for e in li:
        if e not in temp_set:
            res.append(e)
            temp_set.add(e)
    return res

def compare(A_log, B_log) :    
    token=0
    if is_diff(A_log, B_log) == True :
        # token=1 활성화, result_log_list에 append
        token=1
        for i in router_log_path:        
            if diff_log[i][1]==1 :
                if len(result_log_dict[i]) == 0 :
                    result_log_dict[i].append(Fore.YELLOW +"<<<<<"+i+">>>>>")
                for j in range(0,len(diff_log[i][0])) :
                    result_log_dict[i].append(Fore.GREEN +i+">>>"+Fore.RED+diff_log[i][0][j].rstrip('\n'))
                    
    else:
        token=0
    
    log_token = 0
    for i in result_log_dict:
        if len(result_log_dict[i]) > 0:
            log_token = 1
            break;
        else :
            log_token = 0
    
    
    if token == 1:
        print_cycle(cycle)
        print(Fore.RED +"알람 발생-"+Fore.GREEN +"알람 리스트 초기화 시키기 위해서는 로딩 완료 까지 Enter를 누르고 계세요")
        print(Fore.GREEN+"==================================================================================")

        for i in result_log_dict:
            for j in range(0,len(result_log_dict[i])) :
                print(result_log_dict[i][j])
        beepsound()
        play_sound()                                   
        diff_log.clear()
    else :
        print_cycle(cycle)
        if log_token > 0 :            
            print(Fore.RED +"알람 발생-"+Fore.GREEN +"알람 리스트 초기화 시키기 위해서는 로딩 완료 까지 Enter를 누르고 계세요")
            print(Fore.GREEN+"==================================================================================")          
            for i in result_log_dict:
                for j in range(0,len(result_log_dict[i])) :
                    print(result_log_dict[i][j])
        else :
            print(Fore.YELLOW +"발생 알람 없음")

def print_cycle(cycle) :
    now = datetime.now()
    os.system('cls')
    print(Fore.RED + "==================================================================================")
    print("국제IPX 라우터 Log 감시")
    print(Fore.RED + "==================================================================================")    
    print(Fore.GREEN+"==================================================================================")
    print("현재 감시 Cycle Count : "+Fore.YELLOW+str(cycle)+Fore.GREEN+" - 현재 시각 : "+Fore.YELLOW+str(now.strftime("%Y-%m-%d %H:%M:%S")))
    print(Fore.GREEN + "==================================================================================")

###=============================================================================###
#루프 전, Log 파일 Path 입력 받기
router_log_path = input_path()
###=============================================================================###
### 1st Cycle ###
"1st Cycle print"
cycle=1
print_cycle(cycle)

"n-1 old_log read"
old_router_log = read_log(router_log_path)

"collecting n-1 new_log"
collect()

"n-1 new_log read"
new_router_log = read_log(router_log_path)

"Parsing - Timestamp Line만 추출"
parse_log(old_router_log)
parse_log(new_router_log)

"(n-1 old_log) & (n-1 new_log) compare"
compare(old_router_log, new_router_log)
###=============================================================================###
import keyboard
### Loop Start ###
while True:    
    ###=============================================================================###
    #Hooking
    if keyboard.is_pressed('enter'):
        os.system('cls')
        print_cycle(cycle)
        print("초기화 중")
        result_log_dict.clear()
        result_log_dict = {
         (Skip Caused BY Security)
        }
        for i in range(4,0,-1):
            sys.stdout.write("■■■■■■■■")
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write("■■■■■■■■■")
        sys.stdout.flush()
        print("\n초기화 완료")
        time.sleep(0.5)
        print_cycle(cycle)
        print(Fore.YELLOW +"발생 알람 없음")        
    ###=============================================================================###        
    else :
        ###=============================================================================###
        "Cycle ++"
        cycle=cycle+1
        
        "collecting n old_log"
        collect()
        
        "n old_log read"
        old_router_log = read_log(router_log_path)
        
        "n old_log parse"
        parse_log(old_router_log)    
        
        "(n-1 new_log) & (n old_log) compare"
        compare(new_router_log, old_router_log) 
        ###=============================================================================###
        
        cycle=cycle+1    
        "collecting n new_log"
        collect()
        
        "n new_log read"
        new_router_log = read_log(router_log_path)
        
        "n new_log parse"
        parse_log(new_router_log)
                            
        " (n old_log) & (n new_log) compare "
        compare(old_router_log, new_router_log)
        ###=============================================================================###     
