import streamlit as st

st.title("My web app - Aha!!!")
st.title("_Streamlit_ is :blue[cool] :sunglasses:")
st.title("_Streamlit_ is :red[hot] :fire:")

st.header("Learning streamlit for the first time...!!!")

st.subheader("dancing: dink ka chaka.....")

agree = st.checkbox("I agree")
A = st.checkbox("A")
B = st.checkbox("B")
C = st.checkbox("C")
D = st.checkbox("D")
if agree:
    st.write("Great!")
if A:
    st.write("apple!")
if B:
    st.write("ball!")
st.divider()

if C:
    st.write("cat!")
if D:
    st.write("dog!")

with st.echo():
    st.write('This code will be printed')

st.divider()

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

st.text("This is text\n[and more text](that's not a Markdown link).")

st.html(
    "<p><span style='text-decoration: line-through double red;'>Oops</span>!</p>"
)

import pandas as pd
import numpy as np
st.header("dataframe...!!!")
df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)

st.header("data editor...!!!")

df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

st.header("Table...!!!")
df = pd.DataFrame(
    np.random.randn(10, 5), columns=("col %d" % i for i in range(5))
)

st.table(df)

st.header("Metric...!!!")
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

st.header("area chart...!!!")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)

st.header("bar chart...!!!")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.bar_chart(chart_data)


st.header("Line chart...!!!")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)


st.header("Map...!!!")
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=["lat", "lon"],
)
st.map(df)


st.header("Scatter chart...!!!")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.scatter_chart(chart_data)



st.header("sunrise...!!!")
st.image("./sunrise.jpg", caption="Sunrise by the mountains")