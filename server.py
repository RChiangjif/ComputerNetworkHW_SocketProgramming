#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TCP 猜拳遊戲 - 單人版伺服器"""
import socket
import random

# 自動獲取本機 IP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
server_ip = s.getsockname()[0]
s.close()

server_port = 5555
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((server_ip, server_port))
server_socket.listen(1)

print(f"伺服器已啟動: {server_ip}:{server_port}")
print("等待客戶端連線...")

# 接受客戶端
client_socket, client_address = server_socket.accept()
print(f"客戶端已連線: {client_address}")

# 接收用戶名
username = client_socket.recv(1024).decode('utf-8')
print(f"使用者: {username}")

# 發送歡迎訊息
welcome_msg = f"Welcome Game {username}"
client_socket.sendall(welcome_msg.encode('utf-8'))

# 遊戲迴圈 - 直到客戶端贏3次
wins = 0
round_num = 1

while wins < 3:
    # 接收客戶端選擇
    client_choice = client_socket.recv(1024).decode('utf-8').strip().lower()
    
    if client_choice not in ['rock', 'paper', 'scissors']:
        continue
    
    # 伺服器隨機出拳
    server_choice = random.choice(['rock', 'paper', 'scissors'])
    
    # 判斷勝負
    if client_choice == server_choice:
        result = 'draw'
    elif (client_choice == 'rock' and server_choice == 'scissors') or \
         (client_choice == 'paper' and server_choice == 'rock') or \
         (client_choice == 'scissors' and server_choice == 'paper'):
        result = 'win'
        wins += 1
    else:
        result = 'lose'
    
    print(f"第{round_num}回合: {client_choice} vs {server_choice} -> {result}")
    
    # 發送結果
    response = f"Server: {server_choice} | Result: {result}"
    client_socket.sendall(response.encode('utf-8'))
    
    round_num += 1

# 遊戲結束
client_socket.sendall(b"Game Over!")
print(f"遊戲結束！{username} 贏得3次")

client_socket.close()
server_socket.close()
