import streamlit as st
import cv2
import numpy as np
from PIL import Image

# タイトル
st.title("カメラアプリ")

# カメラのキャプチャ
def capture_image():
    run = st.checkbox('カメラを起動')
    cam_placeholder = st.empty()
    
    if run:
        cap = cv2.VideoCapture(0)  # カメラを起動

        if not cap.isOpened():
            st.error("カメラが起動できません")
            return None

        ret, frame = cap.read()  # 画像をキャプチャ

        if ret:
            img_placeholder.image(frame, channels="BGR")  # 画像を表示

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
