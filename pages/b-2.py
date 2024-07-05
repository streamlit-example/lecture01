import streamlit as st

from views.page_urls import page_urls

page_urls(__file__)


abstract_ = """
### UI定義（基礎）
Streamlitを用いたUI定義の方法について、基礎的な内容を紹介します。  
[ワイヤーフレームのサンプル](https://wireframe-example-rammpl3kzfse7okypdcutk.streamlit.app/)は、
この章に記載の機能を組み合わせて書かれています。  

##### 今回触れない内容の例
- メディア表示
    - 画像
    - 動画
    - 音声
- ステータス表示
    - プログレスバー
    - スピナー

- その他
    - Streamlitの機能を使う
        - セッション状態管理
        - データキャッシング
        - マルチページアプリ
    - 他のライブラリと組み合わせる
        - API連携
        - 並列処理

- カスタムコンポーネント
    - [いい感じのStreamlitのコンポーネント集](https://qiita.com/papasim824/items/b6aef456644321af0010)
    - [カスタムコンポーネントの作り方](https://qiita.com/papasim824/items/ea4cb1b49ba4d71b0aca)


"""

words_ = """
### タイトルなど

```
st.title("タイトル")
st.header("ヘッダー", divider="gray")
st.subheader('_Streamlit_ is :blue[cool] :sunglasses:')
```
🎈 emojiはべた貼りでも利用可です。

### Markdown
```
text = \"""
## 見出し1
### 見出し2
箇条書きの例
- 1つめ
    - xxx
    - yyy
- 2つめ
    - zzz
- 3つめ

### 見出し3
箇条書きの例（数字バージョン）
1. 1つめ
    1. aa
    1. bb
1. 2つめ
1. 3つめ
\"""

text # または　st.markdown(text)
```

### LateX
```
st.latex(r\"""\\frac{\partial^2 u}{\partial t^2} = c^2 \\frac{\partial^2 u}{\partial x^2}\""")
```

"""

widget_ = """
### インプット
```
a1 = st.text_input("Write something")
a2 = st.number_input("あなたの年齢を教えてください", value=25)
a1
a2

```
### ボタン

```
b1 = st.button("＋")
b2 = st.button("－")
if b1:
    "⭐"
if b2:
    st.rerun()
```

### マルチセレクト
```
c = st.multiselect("Status", options=["a", "b", "c"])
c
```

### アップローダー
```
file = st.file_uploader("Files", accept_multiple_files=True)
for f in files:
    f.name
```
🎈 [ダウンロードボタン](https://docs.streamlit.io/develop/api-reference/widgets/st.download_button)もあります。
### チェックボックス
```
d = st.checkbox("Edit Mode")
if d:
    "✅"

```
"""

layout_ = """
### サイドバー
```
st.sidebar.title("サイドバー")
```
### タブ
```
tabs = st.tabs(["tab 1", "tab 2", "tab 3"])
with tabs[0]:
    st.title("1つめ")

with tabs[1]:
    st.title("2つめ")

with tabs[2]:
    st.title("3つめ")

```
### カラム
```
c1 = st.columns(3)
c1[0].text_input("c1_0")
c1[1].text_input("c1_1")
c1[2].text_input("c1_2")

c2 = st.columns([2, 5])
c2[0].text_input("c2 せまい")
c2[1].text_input("c2 ひろい")
```
🎈 `Version 1.36.0`では [要素をいい感じに揃えられる機能](https://docs.streamlit.io/develop/api-reference/layout/st.columns#:~:text=Adjust%20vertical%20alignment%20to%20customize%20your%20grid%20layouts.)
が追加されました。
"""

data_ = """
### 表
読み込んだデータを表示します。
```
st.dataframe(data, width=2500, hide_index=True)
```
🎈 動的な表については次回取り上げられればと思います。
- [st.data_editor](https://docs.streamlit.io/develop/api-reference/data/st.data_editor)
- [Column configuration](https://docs.streamlit.io/develop/api-reference/data/st.column_config)

"""

figure_ = """
### グラフ
読み込んだデータをグラフ化します。
```
st.bar_chart(df, x="Name", y="Rate")
```
🎈 ChatGPTを使うと意外といろんなグラフが書けるので、ダメもとで聞いてみるのもよさそうです
- [例](xx)

"""

dialog_ = """
### データの読み込み（pandas）
`pandas`という外部ライブラリをインストールすることで、データ整形の機能が利用できるようになります。  
今回のコードではcsvの読み込みのみを利用しています。
```
import pandas as pd

df = pd.read_csv("./assets/data.csv", encoding="utf-8")
```

### ダイアログボックス
```
@st.experimental_dialog("確認")
def dialog1():
    st.write("Are you sure you want to xxx?")
    st.text_input("Any Comments:")
    if st.button("OK"):
        st.success("done xxx succesfully")

if st.button("Enter")
    dialog1()
```
🎈 バックグラウンドで処理しながらダイアログボックスを表示するなどもできるはず（未確認）

"""


tabs = st.tabs(
    [
        "このセクションの概要　",
        "テキスト　",
        "ウィジェット　",
        "レイアウト　",
        "表データ　",
        "グラフ　",
        "その他　",
    ]
)

with tabs[0]:
    abstract_
with tabs[1]:
    words_
with tabs[2]:
    widget_
with tabs[3]:
    layout_
with tabs[4]:
    data_
with tabs[5]:
    figure_
with tabs[6]:
    dialog_

