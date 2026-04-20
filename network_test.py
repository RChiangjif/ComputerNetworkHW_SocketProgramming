#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Network Test Tool - 用於測試網路連線的工具
可檢查本機 IP、測試兩台設備之間的連通性
"""

import socket
import sys
import subprocess
import platform

def get_local_ip():
    """取得本機IP位址"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception as e:
        return f"Error: {e}"

def get_hostname():
    """取得本機主機名"""
    try:
        return socket.gethostname()
    except:
        return "Unknown"

def show_network_info():
    """顯示本機網路資訊"""
    print("\n" + "="*60)
    print("本機網路資訊")
    print("="*60)
    print(f"主機名稱: {get_hostname()}")
    print(f"本機 IP 位址: {get_local_ip()}")
    print("="*60 + "\n")

def test_ping(target_ip):
    """
    測試是否能 ping 通目標 IP
    Args:
        target_ip: 目標IP位址
    """
    print(f"\n正在 ping {target_ip}...")
    
    # 根據作業系統選擇 ping 命令
    param = "-n" if platform.system().lower() == "windows" else "-c"
    
    try:
        # Windows: ping -n 4  | macOS/Linux: ping -c 4
        result = subprocess.run(
            ["ping", param, "4", target_ip],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            print(f"✅ 成功 ping 通 {target_ip}")
            print("\n輸出:\n" + result.stdout)
            return True
        else:
            print(f"❌ 無法 ping 通 {target_ip}")
            print("\n輸出:\n" + result.stdout)
            return False
    
    except subprocess.TimeoutExpired:
        print(f"❌ Ping 超時")
        return False
    except FileNotFoundError:
        print("❌ 找不到 ping 命令")
        return False
    except Exception as e:
        print(f"❌ Ping 失敗: {e}")
        return False

def test_port_access(target_ip, target_port):
    """
    測試是否能連線到目標 IP:Port
    Args:
        target_ip: 目標IP位址
        target_port: 目標埠號
    """
    print(f"\n正在測試連線到 {target_ip}:{target_port}...")
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        
        result = sock.connect_ex((target_ip, target_port))
        sock.close()
        
        if result == 0:
            print(f"✅ 成功連線到 {target_ip}:{target_port}")
            print("   (說明: 該埠號已有服務在監聽)")
            return True
        else:
            print(f"❌ 無法連線到 {target_ip}:{target_port}")
            print("   (可能原因: 伺服器未啟動 / 埠號錯誤 / 防火牆阻擋)")
            return False
    
    except socket.timeout:
        print(f"❌ 連線超時")
        return False
    except Exception as e:
        print(f"❌ 連線測試失敗: {e}")
        return False

def interactive_mode():
    """互動模式"""
    print("\n" + "="*60)
    print("自動網路測試工具")
    print("="*60)
    
    # 顯示本機資訊
    show_network_info()
    
    while True:
        print("\n選擇測試選項:")
        print("1. 測試能否 ping 通另一台設備")
        print("2. 測試能否連線到目標 IP:Port")
        print("3. 顯示本機 IP 資訊")
        print("4. 結束程式")
        
        choice = input("\n請選擇 (1-4): ").strip()
        
        if choice == "1":
            target_ip = input("請輸入目標 IP 位址: ").strip()
            if target_ip:
                test_ping(target_ip)
        
        elif choice == "2":
            target_ip = input("請輸入目標 IP 位址: ").strip()
            try:
                target_port = int(input("請輸入目標埠號 (預設 5555): ").strip() or "5555")
            except ValueError:
                print("埠號必須是整數")
                continue
            
            if target_ip:
                test_port_access(target_ip, target_port)
        
        elif choice == "3":
            show_network_info()
        
        elif choice == "4":
            print("\n結束測試工具")
            break
        
        else:
            print("❌ 無效選擇，請再試一次")

def main():
    """主程式"""
    if len(sys.argv) > 1:
        # 命令行模式
        if sys.argv[1] == "info":
            # 只顯示本機資訊
            show_network_info()
        
        elif sys.argv[1] == "ping":
            # ping 目標 IP
            if len(sys.argv) > 2:
                test_ping(sys.argv[2])
            else:
                print("用法: python3 network_test.py ping <IP>")
        
        elif sys.argv[1] == "connect":
            # 連線到目標 IP:Port
            if len(sys.argv) > 2:
                target_ip = sys.argv[2]
                target_port = int(sys.argv[3]) if len(sys.argv) > 3 else 5555
                test_port_access(target_ip, target_port)
            else:
                print("用法: python3 network_test.py connect <IP> [Port]")
        
        else:
            print("有效命令: info | ping <IP> | connect <IP> [Port]")
    
    else:
        # 互動模式
        interactive_mode()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n程式被中斷")
    except Exception as e:
        print(f"\n錯誤: {e}")
