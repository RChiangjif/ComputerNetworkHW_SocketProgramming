#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TCP 猜拳遊戲 - 客戶端"""
import socket

# 輸入伺服器資訊
server_ip = input("伺服器IP位址: ")
server_port = int(input("伺服器埠號 (預設5555): ") or "5555")

# 連線到伺服器
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))
print(f"已連線到 {server_ip}:{server_port}")

# 發送用戶名
username = input("輸入您的學號: ")
client_socket.sendall(username.encode('utf-8'))

# 接收歡迎訊息
welcome = client_socket.recv(1024).decode('utf-8')
print(welcome)

# 遊戲迴圈
while True:
    choice = input("輸入選擇 (rock/paper/scissors): ").strip().lower()
    
    if choice not in ['rock', 'paper', 'scissors']:
        continue
    
    # 發送選擇
    client_socket.sendall(choice.encode('utf-8'))
    
    # 接收結果
    response = client_socket.recv(1024).decode('utf-8')
    print(response)
    
    # 檢查遊戲是否結束
    if "Game Over" in response:
        break

client_socket.close()
