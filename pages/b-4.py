import streamlit as st

from views.page_urls import page_urls

page_urls(__file__)


abstract_ = """
### わからないことへの対処方法
わからないことが生じたときの対処法を紹介します。
"""


docs_ = """
### Streamlitの記法
以下のサイトにアクセスします。
- [Streamlit documentation](https://docs.streamlit.io/)

あるいは、コマンドプロンプトで以下コマンドを実行することで、このページを開くことができます。
```sh
streamlit docs
```

##### ポイント
- API reference の下に仕様がまとまっている
- ドキュメント内を検索できる（`ctrl + K`）
- バージョンごとの仕様が簡単に確認できる

##### 例
- ラジオボタンを横並びにしたい
- 表データの表示機能を色々知りたい

"""
python_ = """
### Pythonの記法
1. ググる

1. ChatGPTにきく
1. 3分経ってもわからなければわかりそうな人に聞く
1. わかりそうな人がいなければ公式ドキュメントを読む

"""
error_ = """
### エラーの解決方法
1. ググる

1. ChatGPTにきく
    - コードとエラーメッセージを貼り付ける
    - 下記の例のように、マークダウン記法で書くと精度が上がりやすい
    - 秘密にしたい情報は必ずマスキングする
1. 3分経ってもわからなければわかりそうな人に聞く
1. わかりそうな人がいなければ公式ドキュメントを読む

##### ChatGPTへの質問プロンプト例
    以下のPythonスクリプトを実行するとエラーが生じます。解決策を教えてください。

    ## コード
    ```
    def func3():
        return 3+
    ```

    ## エラーメッセージ
    ```
    SyntaxError: invalid syntax
    ```

回答は[こんな感じ](https://chatgpt.com/share/b9b367a2-37d1-4a14-ae85-d38a657d6f22)

"""

tabs = st.tabs(
    [
        "このセクションの概要　　　",
        "Streamlitの記法　　　",
        "エラーの解決方法　　　",
        "Pythonの記法　　　",
    ]
)

with tabs[0]:
    abstract_
with tabs[1]:
    docs_
with tabs[2]:
    error_
with tabs[3]:
    python_
