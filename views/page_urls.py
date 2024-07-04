import os
from dataclasses import dataclass, field
from typing import List, Optional

import streamlit as st

__LAYER_RATIO = [1, 9]


@dataclass
class Page:
    file: str
    title: str
    category: Optional[str] = None
    icon: Optional[str] = None
    children: Optional[List] = field(default_factory=list)


PAGES = Page(
    file="pages/home.py",
    title="Top",
    icon="🏠",
    children=[
        Page(
            file="pages/a.py",
            title="セットアップ",
            icon="🚀",
            category="a",
            children=[
                Page(file="pages/a-1.py", title="Python（基礎1）"),
                Page(file="pages/a-2.py", title="VSCode"),
                Page(file="pages/a-3.py", title="仮想環境"),
            ],
        ),
        Page(
            file="pages/b.py",
            title="ワイヤーフレーム",
            icon="🖼️",
            category="b",
            children=[
                Page(file="pages/b-1.py", title="Python（基礎2）"),
                Page(file="pages/b-2.py", title="UI定義（基礎）"),
                Page(file="pages/b-3.py", title="ドキュメントの参照"),
                Page(file="pages/b-4.py", title="ファイルの分割"),
            ],
        ),
        Page(
            file="pages/c.py",
            title="プロトタイプ",
            icon="🎮",
            category="c",
            children=[
                Page(file="pages/c-1.py", title="UI定義（応用）"),
            ],
        ),
    ],
)


def page_urls(opened_file):
    opened_file = os.path.basename(opened_file).split(".")[0]
    with st.sidebar:
        st.page_link(PAGES.file, label=PAGES.title)

        st.markdown("---")
        st.markdown("### Lectures")

        for pp in PAGES.children:
            st.page_link(pp.file, label=pp.title, icon=pp.icon)
            if pp.category in opened_file:
                _, col = st.columns(__LAYER_RATIO)
                for p in pp.children:
                    col.page_link(p.file, label=p.title)
