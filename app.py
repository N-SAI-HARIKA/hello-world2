import streamlit as st
from demo import area_of_circle

page=st.sidebar.selectbox("Select a page", ["Home","Area Calculator"])
if page=="Home":
    st.title("Welcome to the Hello World App")
    st.write("Use the sidebar to navigate to the area calculator.")
    st.stop()
if page=="Area Calculator":
    st.write("This is a simple app for calculating Area of Circle")
    radius=st.slider("Enter Radius of circle",min_value=0.0,max_value=100.0, value=1.0,step=0.1)
    if st.button("Calculate Area"):
        area=area_of_circle(radius)
        st.write(f"The area of the circle with radius {radius:.2f} is: {area:.2f}")