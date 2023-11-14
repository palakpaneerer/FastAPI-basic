from fastapi import FastAPI

# インスタンス化 空箱の製作
app = FastAPI()

"""
# デコレーター 機能：appにアクセスがあれば以降を実行する。
# asyncは非同期処理（他の処理と並行して実行できる。）asyncが無くてもエラーにはならない。
@app.get("/")
async def index():
    return {"message": "Hello World"}
"""

# コマンドプロンプトで以下を実行する。
# cd ディレクトリへ移動
# python {filename.py} ファイル実行
    # 例：python 04_main.py
# uvicorn {filename}:app --reload
    # 例：uvicorn 04_main:app --reload

# URLにアクセスする 
# → デコレータのget methodが反応 
# → web画面上に{"message": "Hello World"}が表示される。


# Swagger = Restful API 統一された API の仕様書
# http://127.0.0.1:8000/docsで勝手に記載してくれているdocを見ることができる。

# 他の手段としてredocでも同様の内容を見られる。
# http://127.0.0.1:8000/redoc



# デコレータのアクセス先をhttp://127.0.0.1:8000/helloにする。
@app.get("/hello")
async def index():
    return {"message": "Hello World"}

"""
# デコレータ、関数共に引数を使用できる。= パスパラメーター
@app.get("/countries/{country_name}")
async def country(country_name):
    return {"country_name": country_name}
"""

# 型ヒントで引数の値を制限することができる。
# intに設定したら、str型、float型でアクセスするとエラーが出る。
@app.get("/countries/{country_name}")
async def country(country_name: int):
    return {"country_name": country_name}


# 以下のデコレーターは一つ上のパスにも当てはまり、
# 型ヒントでstrは排除されるので、エラーとなる。
@app.get("/countries/japan")
async def country(country_name: str):
    return {"country_name": "This is Japan"}



# クエリパラメータ
# https://twitter.com/search?q=python&src=typed_query
# ?以降がクエリパラメータ
# デコレータで定義：パスパラメータ
# defのみで定義：クエリパラメータ


"""
# クエリパラメータの作成
# 以下でもアクセスできるようになる。
# http://127.0.0.1:8000/countries/?country_name=america&country_no=3
# web画面の表示結果: {"country_name":"america","country_no":3}
@app.get("/countries/")
async def country(country_name: str = 'japan', country_no: int = 1):
    return {
        "country_name": country_name,
        "country_no": country_no
        }
"""

# team_name: パスパラメータ
# city_name: クエリパラメータ
@app.get("/teams/{team_name}")
async def country(team_name: str = 'The Avengers', city_name: str = 'new york'):
    return {
        "team_name": team_name,
        "city_name": city_name
        }


# オプションパラメータ
from typing import Optional

@app.get("/fruits/{fruits_name}")
async def country(fruits_name: Optional[str] = None, taste: Optional[str] = None):
    return {
        "fruits_name": fruits_name,
        "taste": taste
        }



# リクエストボディ (postメソッド)
from pydantic import BaseModel

# モデルの定義
class Item(BaseModel):
    name: str
    discription: Optional[str] = None
    price: int
    tax: Optional[float] = None

# インスタンス化    
app = FastAPI()

# ここにアクセスすれば、以下が実行される。
# 型ヒントは上記で定義したものclass Itemのものにする。
@app.post("/item/")
async def create_item(item: Item):
    return {"message": f"{item.name}は、税込み価格{int(item.price * item.tax)}円です。"}
    
        




