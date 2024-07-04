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

- その他高度な機能
    - セッション状態管理
    - データキャッシング
    - マルチページアプリ
    - 並列処理

- カスタムコンポーネント
    - [いい感じのStreamlitのコンポーネント集](https://qiita.com/papasim824/items/b6aef456644321af0010)
    - [カスタムコンポーネントの作り方](https://qiita.com/papasim824/items/ea4cb1b49ba4d71b0aca)


"""

words_ = """
### ヘッダー、タイトル

### Markdown

### LateX


"""

widget_ = """
### インプット

### ボタン

### マルチセレクト

### アップローダー

### チェックボックス

"""

layout_ = """
### サイドバー

### タブ

### カラム
- 縦もできるようになったっぽい


"""

data_ = """
### 静的な表

### 動的な表

### 

"""

figure_ = """
### グラフ

##### Tips
- ChatGPTを使うと意外といろんなグラフが書けるので、ダメもとで聞いてみるのもよさそう

"""

dialog_ = """
### ダイアログボックス


"""


tabs = st.tabs(
    [
        "このセクションの概要　",
        "テキスト　",
        "ウィジェット　",
        "レイアウト　",
        "表データ　",
        "グラフ　",
        "ダイアログボックス　",
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
