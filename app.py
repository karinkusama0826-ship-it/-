import streamlit as st

# --- 設定（ここを好きな言葉に変えてください） ---
APP_TITLE = "QRコード読み取ってくれてありがとう！💝"
THANK_YOU_MESSAGE = "メッセージありがとうございます！お礼にこちらの特典をお受け取りください。"
SECRET_REPLY = "【運営者からのメッセージ】いつも頑張っていますね！毎日お疲れ様です！"
# 特典画像
IMAGE_URL =https://imgur.com/a/TNEBX9P


# --- アプリの画面構成 ---
st.set_page_config(page_title=APP_TITLE, page_icon="🎁")
st.title(APP_TITLE)
st.write("QRコードからのアクセスありがとうございます！")

with st.container():
    st.subheader("メッセージを送る")
    user_msg = st.text_area("今日がんばったことを教えてください", placeholder="例：いつも見てます！")
    send_btn = st.button("メッセージを送信して特典を見る")

if send_btn:
    if user_msg.strip() == "":
        st.error("何かメッセージを入力してくださいね。")
    else:
        st.balloons()
        st.success(THANK_YOU_MESSAGE)
        st.info(SECRET_REPLY)
        st.image(IMAGE_URL, caption="あなたのための特別画像です", use_container_width=True)