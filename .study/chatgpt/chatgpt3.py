import openai
openai.api_key = "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" # 請填寫您的 API key

prompt = "Hello, chatgpt" # 您可以編寫自己的對話提示

response = openai.Completion.create(
    engine="davinci", # 指定使用的 GPT-3 引擎
    prompt=prompt,
    temperature=0.7, # 控制生成文本的創造性和多樣性
    max_tokens=60, # 控制生成的文本長度
)

print(response.choices[0].text.strip()) # 打印生成的回答文本，去掉首尾空白字符

