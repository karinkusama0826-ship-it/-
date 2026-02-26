import streamlit as st

# --- 設定（ここは自由に変えてね） ---
APP_TITLE = "QRコード読み込んでくれた人限定特典💝"
# あなたが教えてくれたGoogleフォームのURL
GOOGLE_FORM_URL = "https://forms.gle/g4ixRxTMvLtsfX6d8"

# --- アプリの画面構成 ---
st.set_page_config(page_title=APP_TITLE, page_icon="🎀")
st.title(APP_TITLE)

st.write("今日もお疲れ様です！")
st.write("下の入力欄にメッセージを書いて、「送信」ボタンを押してください。")

# 入力エリア
user_msg = st.text_area("今日頑張ったことなど、大変だったこと教えてね👇")

# 送信ボタン
if st.button("メッセージを送信して特典を見る"):
    if user_msg:
        st.success("ありがとうございます！メッセージを受け付けました。")
        st.write("最後に下の「確認ボタン」を押して完了してください👇")
        
        # Googleフォームへ飛ばすボタン（ここにメッセージを添えて飛ばす）
        st.link_button("✨ここを押して特典を受け取る", "https://forms.gle/CD4CWmi4d7UQnDCm7")
        
        st.info("※上のボタンを押すと、メッセージがスプレッドシートに保存され、特典が表示されます。")
    else:
        st.warning("メッセージを入力してください。")