# type hints の導入
# 型ヒントはpython3.5以降しか使用できない。
# あくまでヒント（注釈）なので、違う方が入力されてもエラーにはならない。

price: int = 100.0
tax: float = 1.1

def calc_price_inclduing_tax(price: int, tax: float) -> int:
    return int(price * tax)

if __name__ == "__main__":
    print(f'{calc_price_inclduing_tax(price=price, tax=tax)}円')
    
    
# リストと辞書の型ヒント
from typing import List, Dict

sample_list: List[int] = [1, 2, 3, 4]
sample_dict: Dict[str, str] = {'username': 'abcd'}




