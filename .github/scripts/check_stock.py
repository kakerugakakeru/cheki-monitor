```python
import requests
import sys

NTFY_URL = "https://ntfy.sh/kakerugakakeru7"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "ja,en-US;q=0.9,en;q=0.8",
}

PRODUCTS = [
    {
        "name": "ヨドバシ instax mini 1パック（10枚）",
        "url": "https://www.yodobashi.com/product/100000001003891482/",
        "in_stock": ["カートに入れる", "在庫あり"],
        "out_of_stock": ["品切れ", "販売終了", "在庫なし"],
    },
    {
        "name": "ヨドバシ instax mini 2パック（20枚）",
        "url": "https://www.yodobashi.com/product/100000001003891483/",
        "in_stock": ["カートに入れる", "在庫あり"],
        "out_of_stock": ["品切れ", "販売終了", "在庫なし"],
    },
    {
        "name": "フジフィルムモール miniフィルム",
        "url": "https://mall-jp.fujifilm.com/shop/c/c306010/",
        "in_stock": ["カートに入れる", "ショッピングカートに入れる", "在庫あり"],
        "out_of_stock": ["品切れ", "SOLD OUT", "在庫なし"],
    },
]

def send_notification(name, url):
    try:
        requests.post(
            NTFY_URL,
            data=f"在庫復活！今すぐチェック\n{url}".encode("utf-8"),
            headers={
                "Title": f"チェキフィルム在庫あり: {name}".encode("utf-8"),
                "Priority": "urgent",
                "Tags": "shopping_cart",
            },
            timeout=10,
        )
        print(f"  通知送信: {name}")
    except Exception as e:
        print(f"  通知失敗: {e}")

def check(product):
    try:
        resp = requests.get(product["url"], headers=HEADERS, timeout=30)
        html = resp.text

        for kw in product["in_stock"]:
            if kw in html:
                print(f"[在庫あり] {product['name']} ({kw})")
                send_notification(product["name"], product["url"])
                return

        for kw in product["out_of_stock"]:
            if kw in html:
                print(f"[品切れ] {product['name']} ({kw})")
                return

        print(f"[不明] {product['name']} - ステータス判定できず (HTTP {resp.status_code})")

    except Exception as e:
        print(f"[エラー] {product['name']}: {e}")

if __name__ == "__main__":
    print("チェキフィルム在庫チェック開始")
    for p in PRODUCTS:
        check(p)
    print("完了")
```

貼り付けたら右上の緑の **Commit changes...** ボタンを押して、もう一度 **Commit changes** を押してください。
