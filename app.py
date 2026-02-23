import streamlit as st

# --- 設定（ここを好きな言葉に変えてください） ---
APP_TITLE = "読者限定！プレゼント受け取り会場"
THANK_YOU_MESSAGE = "メッセージありがとうございます！お礼にこちらの特典をお受け取りください。"
SECRET_REPLY = "【運営者からのメッセージ】いつも応援ありがとうございます。これからも頑張ります！"
# 特典画像（今はサンプルです。あとで自分の画像のURLに変えられます）
IMAGE_URL = "https://placehold.jp/24/cc9999/ffffff/400x300.png?text=Special%20Gift"

# --- アプリの画面構成 ---
st.set_page_config(page_title=APP_TITLE, page_icon="🎁")
st.title(APP_TITLE)
st.write("QRコードからのアクセスありがとうございます！")

with st.container():
    st.subheader("メッセージを送る")
    user_msg = st.text_area("感想やメッセージを教えてください👇", placeholder="例：いつも見てます！")
    send_btn = st.button("メッセージを送信して特典を見る")

if send_btn:
    if user_msg.strip() == "":
        st.error("何かメッセージを入力してくださいね。")
    else:
        st.balloons()
        st.success(THANK_YOU_MESSAGE)
        st.info(SECRET_REPLY)
        st.image(IMAGE_URL, caption="あなたのための特別画像です", use_container_width=True)