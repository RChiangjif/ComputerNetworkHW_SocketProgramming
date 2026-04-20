# PDF 報告範本（Copy 並貼入 Word/Google Docs）

---

## 姓名(Name):
## 學號(Student ID):

---

## I. 環境配置（Environment Configuration）

| | 裝置1 (Device 1) | 裝置2 (Device 2) |
|---|---|---|
| **IP** | 192.168.x.x | 192.168.x.x |
| **Port** | 5555 | - |

---

## II. 過程圖片(Procedure Screenshots)

### 1. 裝置1的IP截圖(Screenshot of Device 1's IP address):
```
[貼入 ipconfig/ifconfig 截圖]
顯示伺服器設備的 IP 位址
```

### 2. 裝置2的IP截圖(Screenshot of Device 2's IP address):
```
[貼入 ipconfig/ifconfig 截圖]
顯示客戶端設備的 IP 位址
```

### 3. Client 成功連線到Server端的截圖(Screenshot of successful Client-Server connection):
```
[貼入客戶端連線成功的終端截圖]
顯示：已連線到 [Server IP]:5555
```

### 4. Client 收到 Server "Welcome你的學號"截圖(Screenshot of Client receiving "Welcome [Your Student ID]" from Server):
```
[貼入終端截圖]
清晰顯示：Welcome Game [Your Student ID]
```

### 5. Client 輸入自己的拳，並且收到 Server 回傳的結果截圖(Screenshot of Client inputting "Rock-Paper-Scissors" move and receiving results from Server):
```
[貼入至少 3 回合的互動截圖]
須包含：
- 客戶端輸入：rock / paper / scissors
- 伺服器回傳結果：Server: [choice] | Result: [win/lose/draw]
- 顯示至少 3 個回合的完整互動
```

### 6. Client 成功贏Server三次的截圖(Screenshot of Client successfully winning three times against the Server):
```
[貼入遊戲結束的終端截圖]
清晰顯示：Game Over 或類似訊息
確認客戶端已贏得 3 次
```

---

## III. 程式運作(Program Operation)
### 請詳細說明自己的程式架構(Please describe your program architecture in detail):

### Server.py 流程：
1. **自動取得本機IP** - 使用 socket 連接到 8.8.8.8:80 取得真實 IP
2. **建立 Socket** - `socket.socket(AF_INET, SOCK_STREAM)`
3. **綁定 IP 和埠號** - `bind((server_ip, 5555))`
4. **開始監聽** - `listen(1)` 等待客戶端連線
5. **接受連線** - `accept()` 接受客戶端
6. **接收用戶名** - `recv()` 取得客戶端學號
7. **發送歡迎訊息** - `sendall()` 發送 "Welcome Game [學號]"
8. **遊戲迴圈** - 直到客戶端贏 3 次：
   - 接收客戶端選擇
   - 伺服器隨機出拳
   - 判斷勝負並回傳結果

### Client.py 流程：
1. **輸入伺服器資訊** - IP 位址和埠號
2. **建立 Socket** - `socket.socket(AF_INET, SOCK_STREAM)`
3. **連線到伺服器** - `connect((server_ip, port))`
4. **發送用戶名** - `sendall()` 發送學號
5. **接收歡迎訊息** - `recv()` 接收並顯示
6. **遊戲迴圈** - 不斷：
   - 輸入選擇 (rock/paper/scissors)
   - 發送選擇到伺服器
   - 接收結果
   - 檢查是否贏得 3 次

### 贏/輸判定邏輯：
- Rock 贏 Scissors
- Scissors 贏 Paper
- Paper 贏 Rock
- 相同則為平手

---

## IV. 加分項(Bonus)
### 請解釋自身撰寫的多用戶連線程式架構(Please explain the architecture of your multi-user connection program):

### Server_multiuser.py 架構：

#### 1. **連線管理**
- 使用 for 迴圈接受 2 個客戶端連線
- 每個客戶端存儲在字典中：`clients[0]` 和 `clients[1]`
- 保存用戶名和 socket 連接

#### 2. **遊戲流程**
- **第 1-3 回合**（固定 3 回合）：
  - 從各客戶端接收選擇
  - 比較兩個選擇，判斷獲勝者
  - 發送該回合結果給兩個客戶端

#### 3. **計分規則**
依據作業要求，採用「每回合一分制」：
- 如果兩個選擇相同 → 都不得分
- 如果一個贏 → 該玩家得 1 分
- 如果兩個都贏（如都出 rock，都贏 scissors）→ 兩個都得 1 分
  - 例如：Client1 出 rock，Client2 出 rock → 平手（都不得分）
  - 例如：Client1 出 rock，Client2 出 scissors → Client1 得 1 分

#### 4. **計分板**
在第 3 回合後顯示最終計分表：
```
Name       | Score
-----------+-------
Server     | 0
[User1]    | 2
[User2]    | 1
```

#### 5. **技術實現細節**
- 使用字典存儲客戶端連接和用戶名
- 使用字典存儲計分狀態
- 簡化流程，無須多線程（因為順序接收和處理）
- 清晰的邏輯流，易於理解和調試

---

## V. 遇著的困難與解決方案(Challenges and Solutions)

### 困難 1：IP 位址自動偵測
- **問題**：每次啟動伺服器需手動輸入 IP
- **解決**：使用 socket 連接到 8.8.8.8:80 自動取得本機 IP

### 困難 2：兩台設備連線
- **問題**：必須確保連線成功
- **解決**：使用 network_test.py 先驗證網路連通性

### 困難 3：計分邏輯
- **問題**：多人版的複雜計分規則
- **解決**：清楚分析規則，實現簡潔的比對邏輯

---

## VI. 心得(Reflection)

通過本作業，我學到了：
1. TCP socket programming 的基本實現
2. Client-Server 架構的設計與通訊
3. Python network 模組的使用
4. 簡潔高效的代碼設計

---

**作業完成日期(Completion Date)**: [日期]

