import requests

# 設置API端點和請求頭
url = "https://api.chatgpt4.com/ask"
headers = {"Authorization": "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", "Content-Type": "application/json"}

# 構建請求體
data = {"text": "hello,chatgpt", "model": "chatgpt4"}

# 發送POST請求到API端點並取回結果
response = requests.post(url, headers=headers, json=data)
print(response.content)

result = response.json()

# 提取答案
answer = result["response"]["text"]

# 打印答案
print(answer)
