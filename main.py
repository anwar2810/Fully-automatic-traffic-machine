import os
import requests
from openai import OpenAI
from dotenv import load_dotenv
import base64

load_dotenv()

client = OpenAI()

# 1.生成圖片
img = client.images.generate(
    model="gpt-image-1",
    prompt="台灣工地鋼筋師傅使用冷切鋸施工，真實感",
    size="1024x1024"
)

image_base64 = img.data[0].b64_json

with open("post.png","wb") as f:
    f.write(base64.b64decode(image_base64))

print("圖片完成")

# 2.生成文案

text = client.responses.create(
    model="gpt-4.1",
    input="寫一篇吸引工地師傅的FB貼文，推廣冷切鋸"
)

caption = text.output_text

print("文案完成")

# 3.發FB

page_id = os.getenv("FB_PAGE_ID")
token = os.getenv("FB_PAGE_TOKEN")

url = f"https://graph.facebook.com/{page_id}/photos"

requests.post(url, data={
    "caption": caption,
    "access_token": token
}, files={
    "source": open("post.png","rb")
})

print("FB 發布完成")