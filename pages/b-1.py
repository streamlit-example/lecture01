import streamlit as st

from views.page_urls import page_urls

page_urls(__file__)


abstract_ = """
### Python（基礎）
ごく最低限のPythonの記法を紹介します。  
- Streamlitを書くために少し偏った内容になっています。
- Pythonはほかのプログラミング言語同様、様々なことができますので、他の機能は適宜各自でご覧ください。

- 参考サイト
    - [note.nkmk.me](https://note.nkmk.me/)
    - [Python - Qiita](https://qiita.com/tags/python)
"""

basic_ = """
### 1. コメント
各行において、`#`以降の文字列はコードとして認識されません。  
例えば、以下のプログラムを実行すると、何も実行されません。
```Python
# hoge
```
### 2. 変数
変数は値を保存するために使用します。  
Pythonでは、変数を宣言するために特別なキーワードは必要ありません。
```Python
x = 5
y = "Hello"
```
### 3. データ型
Pythonの基本的なデータ型には、以下のようなものがあります。
- 整数（int）
- 浮動小数点数（float）
- 文字列（str）
- ブール値（bool）
```Python
a = 10       # int
b = 3.14     # float
c = "Python" # str
d = True     # bool
```
以下のように、データ型が途中で変わったり、intとfloatの演算をしたりしてもエラーにはなりません。
```Python
a = 10
a = a/3.14
a = "Python"
```

"""
control_ = """
### 1. 条件分岐
`if`、`elif`、`else`を使用します。  
分岐の内外はインデントの深さで区別します。
```Python
x = 10
if x > 0:
    print("正の数です")
elif x == 0:
    print("ゼロです")
else:
    print("負の数です")
```

### 2. ループ
`for`、`while`を使用します。  
ループ対象の内外はインデントの深さで区別します。
```Python
for i in range(5):
    print(i)

```
```Python
i = 0
while i < 5:
    print(i)
    i += 1

```

"""


function_ = """
### 1. 関数
`def`を用いて関数を定義できます。  
関数の内外はインデントの深さで区別します。  
例えば、以下のプログラムを実行すると `3` が出力されます。
```Python
def minus(a, b):
    answer = a - b
    return answer

c = minus(8, 5)
print(c)
```
上のプログラムを少しはしょって書くと以下のようになります。  
実行すると、上と同様 `3` が出力されます。
```Python
def minus(a, b):
    return a - b

print(minus(8, 5))
```
Pythonではインデントなしのコードが上から実行されていきます。  
以下のコードでは未定義の関数を呼び出そうとしてしまっているため、エラーが生じます。

```Python
print(minus(8, 5))

def minus(a, b):
    return a - b
```
関数の処理がエラーになるかどうかは、関数を定義するタイミングではなく実行時に判明します。
以下はエラーにならず、 `3` が出力されます。  
```Python
def func1():
    return k  # 定義されていない変数kが利用されている

def func2():
    return 3 / 0  # ゼロ割りになっている

print(8-5)
```
ただし、以下のような明らかな構文エラーは定義の段階でもはじかれます。
```Python
def func3():
    return 3+
```
"""


list_ = """
### 1. リスト
リストは複数の値を格納するためのデータ構造です。  
要素数はゼロから数えます。要素数に負の値を指定すると最後から数えた要素を出力できます。  
要素数は可変で、異なる型を同じリスト内に入れることもできます。

```Python
numbers = [1, 2, 3]
print(numbers[0])     # 1 と表示される
print(numbers[-2])    # 2 と表示される
numbers.append("xx")  # 新しい要素を追加
print(numbers)        # [1, 2, 3, "xx"] と表示される
```
### 2. 辞書
辞書はキーと値のペアを格納するデータ構造です。
```Python
person = {"name": "Alice", "age": 25}
print(person["name"])  # キー"name"の値を出力
person["age"] = 26     # 値を更新
print(person)

```
"""

import_ = """
### 1. 標準ライブラリのインポート
Pythonには多くの標準ライブラリが含まれており、`import`文でこれらを読み込んで使うことができます。  
例えば、`math`モジュールをインポートすることで、数学関連の関数を利用できるようになります。
```python
import math

print(math.sqrt(16))  # 4.0
```

### 2. 部分的なインポート
モジュール全体ではなく、特定の関数やクラスだけをインポートすることもできます。
```python
from math import sqrt, pi

print(sqrt(16))  # 4.0
print(pi)        # 3.141592653589793
```

### 3. 別名の使用
インポートしたモジュールや関数に別名（エイリアス）を付けることができます。  
これにより、名前が長いモジュールを短くして使うことができます。
```python
import numpy as np

array = np.array([1, 2, 3])
print(array)
```

### 4. 外部パッケージのインポート
標準ライブラリ以外にも、外部のパッケージをインストールして使うことができます。  
外部パッケージは通常、`pip`を使ってインストールします。（※これはコマンドプロンプトで実行するコードです！）
```sh
pip install streamlit
```
インストール後は標準ライブラリと同様に使用できます。
```python
import streamlit as st

st.title("Python（基礎）")
```

### 5. 自作モジュールのインポート
自分で作成したモジュールをインポートすることもできます。

フォルダ構成:
```
├─ main.py
├─ m1.py
└─ dir2
    └─ m2.py
```

`m1.py`:
```python
def greet1(name):
    return f"Hello, {name}!"
```

`m2.py`:
```python
def greet2(name):
    return f"Good morning, {name}!"
```

`main.py`:
```python
from m1 import greet1
from dir2.m2 import greet2

print(m1.greet1("Alice"))  # Hello, Alice!
print(m2.greet2("Bob"))  # Good morning, Bob!
```
"""


tabs = st.tabs(
    [
        "このセクションの概要　　　",
        "初歩　　　",
        "条件分岐・ループ　　　",
        "関数　　　",
        "リスト・辞書　　　",
        "インポート　　　",
    ]
)

with tabs[0]:
    abstract_
with tabs[1]:
    basic_
with tabs[2]:
    control_
with tabs[3]:
    function_
with tabs[4]:
    list_
with tabs[5]:
    import_
