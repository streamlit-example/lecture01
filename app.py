import streamlit as st

from views.page_urls import PAGES

st.set_page_config(layout="wide")


pages = {
    "top": [
        st.Page(PAGES.file, title=PAGES.title, icon=PAGES.icon),
    ]
}
for pp in PAGES.children:  # type: ignore
    pages[pp.title] = [st.Page(pp.file, title=pp.title, icon=pp.icon)]
    pages[pp.title] += [
        st.Page(p.file, title=p.title, icon=p.icon) for p in pp.children
    ]


pg = st.navigation(pages, position="hidden")


# streamlitのmenubarを隠す
HIDE_ST_STYLE = """
                <style>
                div[data-testid="stToolbar"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stDecoration"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                #MainMenu {
                visibility: hidden;
                height: 0%;
                }
                header {
                visibility: hidden;
                height: 0%;
                }
                footer {
                visibility: hidden;
                height: 0%;
                }
				        .appview-container .main .block-container{
                            padding-top: 1rem;
                            padding-right: 3rem;
                            padding-left: 3rem;
                            padding-bottom: 1rem;
                        }  
                        .reportview-container {
                            padding-top: 0rem;
                            padding-right: 3rem;
                            padding-left: 3rem;
                            padding-bottom: 0rem;
                        }
                        header[data-testid="stHeader"] {
                            z-index: -1;
                        }
                        div[data-testid="stToolbar"] {
                        z-index: 100;
                        }
                        div[data-testid="stDecoration"] {
                        z-index: 100;
                        }
                </style>
"""

# HIDE_ST_STYLEを適用
st.markdown(HIDE_ST_STYLE, unsafe_allow_html=True)

pg.run()
