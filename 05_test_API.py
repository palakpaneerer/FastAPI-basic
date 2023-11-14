# python側で04_main.pyで作ったAPIを叩く

import requests
import json

def main():
    url = 'http://127.0.0.1:8000/item/'
    body = {
        "name": "T",
        "discription": "aaa",
        "price": 5980,
        "tax": 1.1
        }

    # json.dumps()は辞書型をJson形式に直す。
    res = requests.post(url, json.dumps(body))
    print(res.json)

if __name__ == "__main__":
    main()
