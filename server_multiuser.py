#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TCP 猜拳遊戲 - 多人版伺服器"""
import socket
import random

# 自動獲取本機 IP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
server_ip = s.getsockname()[0]
s.close()

server_port = 5556
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((server_ip, server_port))
server_socket.listen(2)

print(f"多人版伺服器已啟動: {server_ip}:{server_port}")
print("等待2個客戶端連線...")

# 接受兩個客戶端
clients = {}
usernames = {}
scores = {"Server": 0}

for i in range(2):
    client_socket, client_address = server_socket.accept()
    clients[i] = client_socket
    print(f"客戶端 {i+1} 已連線: {client_address}")
    
    # 接收用戶名
    username = client_socket.recv(1024).decode('utf-8')
    usernames[i] = username
    scores[username] = 0
    
    # 發送歡迎訊息
    welcome_msg = f"Welcome Game {username}"
    client_socket.sendall(welcome_msg.encode('utf-8'))

print(f"兩個客戶端已連線：{usernames[0]}, {usernames[1]}")
print("開始進行 3 回合猜拳\n")

# 進行 3 回合
for round_num in range(1, 4):
    print(f"\n--- 第 {round_num} 回合 ---")
    
    # 接收兩個客戶端的選擇
    choices = {}
    for i in range(2):
        choice = clients[i].recv(1024).decode('utf-8').strip().lower()
        choices[i] = choice if choice in ['rock', 'paper', 'scissors'] else random.choice(['rock', 'paper', 'scissors'])
    
    # 計算勝負
    c0, c1 = choices[0], choices[1]
    
    if c0 == c1:
        # 平手，都不得分
        print(f"{usernames[0]}: {c0}, {usernames[1]}: {c1} -> 平手")
    elif (c0 == 'rock' and c1 == 'scissors') or \
         (c0 == 'paper' and c1 == 'rock') or \
         (c0 == 'scissors' and c1 == 'paper'):
        # 客戶端0贏
        scores[usernames[0]] += 1
        print(f"{usernames[0]}: {c0}, {usernames[1]}: {c1} -> {usernames[0]} 得1分")
    else:
        # 客戶端1贏
        scores[usernames[1]] += 1
        print(f"{usernames[0]}: {c0}, {usernames[1]}: {c1} -> {usernames[1]} 得1分")
    
    # 發送回合結果
    if c0 == c1:
        result_str = "draw"
    elif (c0 == 'rock' and c1 == 'scissors') or \
         (c0 == 'paper' and c1 == 'rock') or \
         (c0 == 'scissors' and c1 == 'paper'):
        result_str = f"{usernames[0]} win"
    else:
        result_str = f"{usernames[1]} win"
    
    result_msg = f"{usernames[0]}: {c0} | {usernames[1]}: {c1} | Result: {result_str}"
    for i in range(2):
        clients[i].sendall(result_msg.encode('utf-8'))

# 遊戲結束，發送計分板
print("\n" + "="*40)
print("遊戲結束 - 最終計分板")
print("="*40)
print("Name       | Score")
print("-"*40)

scoreboard = "遊戲結束 - 最終計分板\n"
for name, score in scores.items():
    print(f"{name:10} | {score}")
    scoreboard += f"{name:10} | {score}\n"

print("="*40)

# 發送計分板給兩個客戶端
for i in range(2):
    clients[i].sendall(scoreboard.encode('utf-8'))
    clients[i].close()

server_socket.close()
print("伺服器已關閉")
