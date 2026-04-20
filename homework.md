本次作業要求使用 Python 撰寫基於 TCP 的猜拳程式，請務必點擊下方連結詳讀 HackMD 說明，並下載附件範本參考。
中文作業詳細說明 (HackMD)：
https://hackmd.io/@usAeZgLVTb2gJ1TqnWEcsA/Byiv11robg
請注意，本次作業較為複雜，請盡早開始準備。

繳交作業時，務必按照以下幾點規定：

本次作業需繳交壓縮檔（zip），請將所需的 3 個（或 4 個）檔案一併壓縮。檔案缺少任一項者(client, server, 或 PDF），本次作業以零分計算。
PDF 檔案內容請依照範例撰寫，並確保截圖內容清晰完整，能清楚對應作業要求。
本作業強烈建議使用兩台電腦進行 TCP 連線測試：
Server 與 Client 需在同一網路環境
若有困難，請於報告中註明或來信求助助教
直接使用 127.0.0.1（localhost）者不予計分

本作業必須使用 Python 撰寫，且禁止使用 Flask 或其他高階網路框架，其他細節請參考網站的程式要求。
請確保程式可正常執行，且具備基本可讀性（適當命名與註解），否則將依情況扣分。
請將zip檔案命名為「學號_Socket_Programming.zip」並上傳 moodle 作業區（範例：F00000000_Socket_Programming.zip）。
其他作業規範請閱讀作業說明若有任何問題請寄信向助教詢問。


一、作業目標
請使用 Python 撰寫一個以 socket programming 為基礎的 TCP 猜拳程式，了解 client/server 架構、TCP 連線流程，以及基本的雙向訊息傳輸機制。

二、作業要求
程式語言 本作業必須使用 Python 完成。
禁止使用Flask 等相關函數、套件 (禁止跳過設定IP步驟就進行連線)
鼓勵同學們使用兩台設備 (對於只有一台設備的同學，可與同學互相借用設備，輪流擔任 server/client)
三、環境配置
請同學先去自己的cmd打開並輸入 ipconfig 查看自己的IP
並強烈建議找同學使用兩台電腦進行TCP連線測試
若無法雙機，請在報告中註明
直接使用 127.0.0.1者不予計分

在cmd 輸入ipconfig 範例


並把查詢到的(Server/Client)電腦設備的IP放在程式的TCP連線設定之中

Note : 請確保 server 與 client 的電腦同時連接在同一個 WiFi 或同一個行動熱點，否則無法正常連線。
Note : 為了順利完成連線，請同學確保server與client的防火牆有關閉

四、程式要求
連線架構
所有 client 與 server 之間必須使用 TCP 建立可靠的、全雙工的點對點連線。
Server 端需完成：
* 使用 bind() 綁定指定 IP/port
* 使用 listen() 監聽連線
* 接受 client 的連線請求
Client 端需完成：
* 使用 connect() 連到server端的 IP/port

互動流程
當 client 成功連上 server並輸入user_name後，server 必須與client 進行文字互動，例如：
client 輸入 name : P76141259
server 發送 " Welcome Game P76141259" 給該client才開始遊戲

Note： P76141259 代表user_name， 請各位同學輸入自己的學號! 否則斟酌扣分

猜拳功能
client 需能與 server 進行一對一猜拳。
猜拳可使用以下三種輸入：
rock/paper/scissors
server 每回合需回傳：
server 出的拳
本回合結果（win / lose / draw）

Ex:
在回合一猜拳，結果由 server勝出
server 端顯示 server win
client 端顯示 client lose

Note : server 出拳的邏輯可由rand() 函數實現，這部分沒有規定，同學可自行設計

遊戲規則
單人連線 :
client 輸入自己想要出的拳，server 隨機出拳
直到client 成功贏 server 3 次，遊戲才結束

多人連線 :
一個 server以及兩個client完成三回合的猜拳
每回合的勝者得一分，平手或是出現互咬的情形則都為零分
請同學注意 這裡是以"回合" 計算
假設 : 某回合中，總共有兩個剪刀 一個布
則兩個出剪刀的得一分 出布的得0分 依此類推

五、評分標準
A. 基本要求（80 分）

檔案完整性（5 分）
需繳交：
client.py
server.py
你的學號_Socket_Programming.pdf
缺少任一檔案者，本次作業以零分計算。

TCP Server 建立正確（10 分）
server.py 需正確完成：
socket 建立
bind()
listen()
接受 client 連線

TCP Client 連線正確（15 分）
client.py 需正確完成：
socket 建立
connect()
成功連到 server

連線後對話互動（15 分）
client 成功連線後，server 能主動發送提示訊息
例如: " Welcome Game 學號 " 才開始遊戲

一對一猜拳功能（15 分）
需完成完整猜拳流程：
client 可輸入猜拳選項
server 可接收並處理
server 回傳自己的出拳與該回合結果
可以正確完成多回合猜拳

使用兩台設備進行猜拳互動 (20 分)
因為只使用自己一台設備的話，會有出現資料傳輸只經過OS-level 的問題
請同學務必找到兩台設備進行連線，此項占 20 分。
對於只有一台設備的同學，可與同學借用設備，輪流擔任 server/client。

B. 加分項（20 分）
多人連線猜拳伺服器
若將 server.py 設計成可同時允許兩個 client 連線並進行猜拳，則可獲得此加分。
請同學寫在 server_multiuser.py 這個py file裡面，以免跟單人版的server搞混。

Hint: multi-threading

加分標準
1)可接受兩個 client 連線：(10 分)
2)設計一個記分板在給定的回合結束時顯示，例如:遊戲結束後同步顯示到各client的畫面上 : (10 分)
EX :

Name   | Score
-------|-------
Server |  1
User1  |  2
User2  |  0
六、繳交內容
請繳交以下內容：
請將三個檔案壓縮成zip檔

    你的學號_Socket_Programming.zip
        ├──client.py	
        ├──server.py           //這個是單人版的server
        ├──server_multiuser.py //這個是多人版的server
        └──你的學號_Socket_Programming.pdf
報告內容包含：

使用的電腦IP/port
關於單人版本的程式截圖，需包含：
裝置1 與 裝置2 的 ipconfig 截圖
client 成功連線到 server
client 收到 server 回傳的 "Welcome Game 學號"
client 與 server 完成猜拳互動
client 成功贏 server 3 次
多人版本的程式設計過程
須包含 :
server 可接收兩個 client的截圖
server/ client 畫面的計分板截圖
七、注意事項
本作業必須使用 Python，但禁止使用Flask相關套件。
通訊協定必須使用 TCP。
請務必仔細閱讀上述規定，禁止使用127.0.0.1這個IP以及確保上傳的檔案完整。
若程式無法正常執行，將依情況扣分。
請保持程式可讀性，命名清楚，並適度加入註解。
多人連線版本的兩個 client name可不用自己的學號，但是單人版本的client name要用自己的學號
多人連線的版本遊戲結束條件請由「完成三回合猜拳」去決定，不要用單一用戶贏三次當作終止條件! 例如 : 三回合後 server user1 user2 三者各自贏了幾次
對於作業說明有不清楚的地方，請同學來信詢問。