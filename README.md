# TCP 猜拳遊戲 - Socket Programming 作業

完整的 Socket Programming 作業實現。

## 📁 文件

```
client.py              - TCP 客戶端
server.py             - 單人版伺服器
server_multiuser.py   - 多人版伺服器（加分項）
network_test.py       - 網路測試工具
README.md            - 本文件
SETUP_GUIDE.md       - 詳細設置說明
```

## 🎮 遊戲規則

- **輸入**: rock / paper / scissors
- **邏輯**: Rock 贏 Scissors，Scissors 贏 Paper，Paper 贏 Rock
- **單人版**: 客戶端連贏 3 次結束
- **多人版**: 3 回合猜拳，最後計分

## 🚀 快速開始

### 環境要求
- Python 3.6+
- 兩台設備在同一 WiFi
- 防火牆已關閉

### 單人版測試

**設備1（伺服器）:**
```bash
python3 server.py
```

**設備2（客戶端）:**
```bash
python3 client.py
# 輸入伺服器 IP（預設埠 5555）
# 輸入您的學號
```

### 多人版測試

**設備1（伺服器）:**
```bash
python3 server_multiuser.py  # 埠 5556
```

**設備2、3（客戶端）:**
```bash
python3 client.py  # 埠 5556
```

### 網路測試

```bash
python3 network_test.py
```

## ⚠️ 重要提醒

- ❌ 禁止用 127.0.0.1 或 localhost
- ❌ 禁止使用 Flask 框架
- ❌ 禁止用 1 台設備（必須 2 台）
- ✅ 單人版必須輸入學號
- ✅ 代碼要清晰有註釋

## 📊 代碼簡介

| 文件 | 行數 | 功能 |
|------|------|------|
| server.py | 72 | 單人版伺服器，接收客戶端，進行猜拳遊戲 |
| client.py | 41 | 客戶端，連線伺服器，輸入選擇 |
| server_multiuser.py | 96 | 多人版伺服器，支援 2 個客戶端，3 回合計分 |
| **核心代碼** | **209** | **簡潔高效** |

## ✅ 交付清單

繳交時需要：
- [ ] `client.py`
- [ ] `server.py`
- [ ] `server_multiuser.py`
- [ ] `學號_Socket_Programming.pdf` (含截圖)
- [ ] 打包為 `學號_Socket_Programming.zip`

## 📖 詳細說明

查看 **SETUP_GUIDE.md** 詳細了解：
- 如何查看本機 IP
- 分步驟運行說明
- 故障排除

## 🎓 預期分數

| 項目 | 分數 |
|------|------|
| 基本功能（TCP、猜拳、3 次勝利） | 80 分 |
| 多人版（加分項） | 20 分 |
| **總計** | **100 分** |

## 💡 提示

1. 先用 `network_test.py` 測試網路連通性
2. 單人版測試成功後再進行多人版
3. 截圖要包含：ipconfig、連線訊息、遊戲過程、計分板
4. 報告要有技術說明（TCP 流程、遊戲邏輯）
