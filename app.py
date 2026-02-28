import streamlit as st

# --- 設定 ---
APP_TITLE = "QRコード読み込んでくれた人限定特典💝"
# あなたのフォームのURL（埋め込み用）
FORM_URL = "https://forms.gle/WHBNKPHY6iGsfjpi8"

st.set_page_config(page_title=APP_TITLE, page_icon="🎀")

st.title(APP_TITLE)
st.write("今日もお疲れ様です！メッセージを送ると、この画面に特典リンクが表示されます🤍")

# --- Googleフォームをアプリの中にそのまま表示する魔法 ---
st.components.v1.iframe(FORM_URL, height=700, scrolling=True)

st.divider()
st.caption("※送信ボタンを押した後、画面に表示されるリンクから特典を受け取ってください。")