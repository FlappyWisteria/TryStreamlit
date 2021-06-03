import streamlit as st
import numpy as np
import pandas as pd

from PIL import Image
import time


st.title("ようこそ!")

st.write("プログレスバーの表示")
"Start!"

latest_iteration = st.empty()
bar = st.progress(int(0))

for i in range(100):
    latest_iteration.text(f"Now loading~{i+1}")
    bar.progress(i + 1)
    time.sleep(0.01)
"Done!"

left_column, right_column = st.beta_columns(2)
button = left_column.button("押したらダメなボタン")
if button:
    right_column.write("ダメって言ったのに...")

expander1 = st.beta_expander("問い合わせ1")
expander1.write("問い合わせ1の回答")
expander2 = st.beta_expander("問い合わせ2")
expander2.write("問い合わせ2の回答")
expander3 = st.beta_expander("問い合わせ3")
expander3.write("問い合わせ3の回答")

st.sidebar.write("サイドバー")

text = st.sidebar.text_input("あなたの趣味は？")
"あなたの趣味:", text

option = st.sidebar.selectbox("あなたの好きな数字を入れてください:", list(range(1, 11)))
"あなたの好きな数字は", option,  "です"

condition = st.sidebar.slider("あなたの今の調子は？", 0, 100, 50)
"あなたの調子:", condition

st.write("Display Image")
if st.checkbox("Show Image"):
    img = Image.open("Mochids.jpg")
    st.image(img, caption="Mochids", use_column_width=True)

# if st.checkbox("Show Music"):
#     mp3_file = open("ファイル名.mp3", "rb")
#     mp3_bytes = mp3_file.read()
#     st.audio(mp3_bytes, format="audio/aac")

# if st.checkbox("Show Video"):
#     mp4_file = open("ファイル名.mp4", "rb")
#     mp4_bytes = mp4_file.read()
#     st.video(mp4_bytes, format="video/mp4")


df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=["lat", "lon"]
)

st.map(df)


"""
# h1
## h2
### h3

# サンプルコード
```python
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


st.title("Streamlit 超入門")

st.write("プログレスバーの表示")
"Start!"

latest_iteration = st.empty()
bar = st.progress(int(0))

for i in range(100):
    latest_iteration.text(f"Now loading ~~~ {i+1}")
    bar.progress(i + 1)
    time.sleep(0.01)
"Done!"

left_column, right_column = st.beta_columns(2)
button = left_column.button("押したらダメなボタン")
if button:
    right_column.write("ダメって言ったのに...")

expander1 = st.beta_expander("問い合わせ1")
expander1.write("問い合わせ1の回答")
expander2 = st.beta_expander("問い合わせ2")
expander2.write("問い合わせ2の回答")
expander3 = st.beta_expander("問い合わせ3")
expander3.write("問い合わせ3の回答")

st.sidebar.write("サイドバー")

text = st.sidebar.text_input("あなたの趣味は？")
"あなたの趣味:", text

option = st.sidebar.selectbox("あなたの好きな数字を入れてください:", list(range(1, 11)))
"あなたの好きな数字は", option,  "です"

condition = st.sidebar.slider("あなたの今の調子は？", 0, 100, 50)
"あなたの調子:", condition

st.write("Display Image")
if st.checkbox("Show Image"):
    img = Image.open("Mochids.jpg")
    st.image(img, caption="Mochids", use_column_width=True)
"""