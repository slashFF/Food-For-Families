import streamlit as st
from PIL import Image
st.set_page_config(page_title="Food for families",
 page_icon="FF.jpg",
  layout="wide"
  )
st.sidebar.success("Food banks across Toronto and what time they're available")
st.title("Food banks you can find across Toronto")
with st.container():
    st.header("Fort York")
    img = Image.open("FY.jpg")
    st.image(img, caption=None, width=250,
    use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.write("https://fyfb.com")
    st.write("Monday - Closed")
    st.write("Tuesday - 9 am - 12pm")
    st.write("Wednesday - 9 am - 12 pm")
    st.write("Thursday - 9 am - 12pm")
    st.write("Friday 9am -12pm")
    st.write("Saturday 9am - 12pm")
    st.write("Sunday - 12 - 1pm")
with st.container():
    st.header("Churches on the hill")
    img = Image.open("COH.jpg")
    st.image(img, caption=None, width=250,
    use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.write("https://www.cothfoodbank.ca/")
    st.write("Monday - 6 - 8pm")
    st.write("Tuesday - Closed")
    st.write("Wednesday - 10:30 am - 12:30pm")
    st.write("Thursday - Closed")
    st.write("Friday - Closed")
    st.write("Saturday - Closed")
    st.write("Sunday - Closed")
with st.container():
    st.header("Allan Garden Food Bank")
    st.write("https://allangardensfoodbank.net/")
    st.write("Monday - Closed")
    st.write("Tuesday - Closed")
    st.write("Wednesday - Closed")
    st.write("Thursday - 12:30 - 3pm")
    st.write("Friday - Closed")
    st.write("Saturday - Closed")
    st.write("Sunday - Closed")
with st.container():
    st.header("Avenue Road Food Bank")
    img = Image.open("ARFB.jpg")
    st.image(img, caption=None, width=250,
    use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.write("https://www.churchofthemessiah.ca/avenue-road-food-bank/")
    st.write("Monday - 9am - 12pm")
    st.write("Tuesday - 9am - 12pm")
    st.write("Wednesday - 9am - 12pm")
    st.write("Thursday - 9am - 12pm")
    st.write("Friday - Closed")
    st.write("Saturday - Closed")
    st.write("Sunday - 10:30am - 12pm")
