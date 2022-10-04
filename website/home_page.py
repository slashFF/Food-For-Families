
from PIL import Image
import streamlit as st
im = Image.open("FF.jpg")
img = Image.open("home_page.jpg")

st.set_page_config(page_title="Food for families",
 page_icon="FF.jpg",
  layout="wide"
  )
st.title("Food for families")
img = Image.open("home_page.jpg")
st.image(img, caption=None, width=800,
use_column_width=None, clamp=False, channels="RGB", output_format="auto")


st.sidebar.success("This is the homepage:smirk:")
with st.container():
    st.title("Food bank awareness")
#-----WHAT I DO
with st.container():
    st.header("what is our goal?")
    st.write("Our goal is to raise awareness for food banks all across Toronto and tell people why food banks are important. We will tell you about the food banks across Toronto and their website, why people need food banks, tell stories about people who need food banks, and make the world a better place by bringing awareness to the incredible non-profitable organizations known as food banks.")
with st.container():
    st.header("Why do families need food banks?")
    st.write("A staggering 1 in 4 people are undernourished, but billions of pounds of food are wasted annually. Systems for food banks collect excess food and distribute it to those in need, involving all spheres of society (governments, business, and civil society) in the process.")
with st.container():
    st.header("Where can you donate?")
    st.write("There are many places in toronto where you can bring food, as well as find online websites many food banks across Toronto, for more information, <click here>")
with st.container():
    st.header("What can you donate?")
    st.write("For each and every food bank, you can donate any item that falls under these categories:")
    st.write("Canned meat / fish / vegetables / fruit ")
    st.write("Dry pasta")
    st.write("Peanut butter")
    st.write("Soup")
    st.write("Rice")
    st.write("Cold or hot cereal")
    st.write("Adult/kid diapers / sanitary products")
