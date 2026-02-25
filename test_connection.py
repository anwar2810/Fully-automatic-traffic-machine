import os
import requests
from dotenv import load_dotenv

# 自動抓取你資料夾裡的 .env 檔案
load_dotenv()

PAGE_ID = "387332884466098" # 你的手持式電動冷切鋸粉專
ACCESS_TOKEN = os.getenv('FB_PAGE_TOKEN') # 程式會自動去 .env 找你的令牌

def check_fb():
    print(f"--- 華叔連線測試開始 ---")
    if not ACCESS_TOKEN:
        print("❌ 錯誤：找不到 FB_PAGE_TOKEN！請檢查 .env 內容。")
        return

    url = f"https://graph.facebook.com/v19.0/{PAGE_ID}?fields=name&access_token={ACCESS_TOKEN}"
    try:
        res = requests.get(url)
        if res.status_code == 200:
            name = res.json().get('name')
            print(f"✅ 連線成功！")
            print(f"目前對接到粉專：{name}")
        else:
            print(f"❌ 連線失敗，臉書回傳：{res.text}")
    except Exception as e:
        print(f"⚠️ 發生系統錯誤：{e}")

if __name__ == "__main__":
    check_fb()