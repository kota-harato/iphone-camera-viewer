import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("カメラアプリ")

# カメラのキャプチャ
def capture_image():
    run = st.checkbox('カメラを起動')
    cam_placeholder = st.empty()
    
    if run:
        # Webカメラの映像を表示する
        cap = cv2.VideoCapture(0)  # カメラを起動

        if not cap.isOpened():
            st.error("カメラが起動できません")
            return None

        ret, frame = cap.read()  # 画像をキャプチャ
        if ret:
            # OpenCVのBGRからRGBに変換
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            cam_placeholder.image(frame, channels="RGB")  # 画像を表示

        cap.release()

# 画像のキャプチャボタン
if st.button('画像をキャプチャ'):
    image = capture_image()
    if image:
        st.image(image, caption="キャプチャされた画像")

# ファイルを選択してアップロード
uploaded_file = st.file_uploader("画像をアップロード", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="アップロードされた画像")

st.write("iPhoneのSafariを使っている場合、カメラのアクセスを許可する必要があります。")
