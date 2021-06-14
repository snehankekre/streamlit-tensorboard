import streamlit as st
from streamlit_tensorboard import st_tensorboard

st.set_page_config(
    page_title="streamlit-tensorboard",
    layout="centered",
    initial_sidebar_state="expanded",
    page_icon="🎈",
)

st.sidebar.header("Streamlit ❤️ TensorBoard")

st.sidebar.markdown('''
<small>Embed [TensorBoard](https://www.tensorflow.org/tensorboard) in Streamlit with [streamlit-tensorboard](https://github.com/snehankekre/streamlit-tensorboard).</small>
    ''', unsafe_allow_html=True)

st.sidebar.markdown('__How to install and import__')
st.sidebar.code('$ pip install streamlit-tensorboard')
st.sidebar.markdown('Import convention')
st.sidebar.code('from streamlit_tensorboard import st_tensorboard')

logdir = "/app/streamlit-tensorboard/examples/logs/fit/20210613-221927"
port = 6006

st_tensorboard(logdir=logdir, port=port, width=1080)


st.code(
    """
import streamlit as st
from streamlit_tensorboard import st_tensorboard
import tensorflow as tf
import datetime
import random

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

def create_model():
    return tf.keras.models.Sequential(
        [
            tf.keras.layers.Flatten(input_shape=(28, 28)),
            tf.keras.layers.Dense(512, activation="relu"),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(10, activation="softmax"),
        ]
    )

model = create_model()
model.compile(
    optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
)

logdir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=logdir, histogram_freq=1)

model.fit(
    x=x_train,
    y=y_train,
    epochs=5,
    validation_data=(x_test, y_test),
    callbacks=[tensorboard_callback],
)

# Start TensorBoard
st_tensorboard(logdir=logdir, port=6006, width=1080)
"""
, language="python")

