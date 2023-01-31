import streamlit as st

st.sidebar.title("Application for Graduation")

name = st.sidebar.text_input("Your Name (cat)", "Whiskers McFadden", key="name_input")

human = st.sidebar.text_input("Sponsoring Human", "Nice warm gorilla who feeds me", key="human_input")

degree = st.sidebar.text_input("Desired Degree", "e.g. Catchelor of Science, Meowsters, Doctor of Furlosophy", key="degree_input")

major = st.sidebar.text_input("Desired Major", "e.g. String Theory, Human Psychology, Canine Kinesiology", key="major_input")

grad_date = st.sidebar.text_input("Desired date of graduation", "April 1, 2023", key="graduation_date_input")

courses = st.sidebar.text_input("Courses completed", "(hint: make something up)", key="courses_input")

thesis = st.sidebar.text_input("Name of final thesis project", "e.g. The Incomprehensibility of Other Cats, How Dumb Are Dogs? A Sociohistorical Analysis.", key="thesis_input")

life_experience = st.sidebar.text_input("In lieu of a final thesis, relevant life experience may apply. Please detail why you qualify for graduation with this degree at this time.", "", key="life_experience_input")


st.title("Felinity College")

# Your Name (cat)

# Name of Sponsor (human)

# Town, Principality, State, Kingdom you wish to see printed on your degree

st.write(name)

# Desired Degree

st.write(degree)

# Desired Major

st.write(major)

# Desired date of graduation

st.write(grad_date)

# Courses completed

st.write(courses)

# Thesis title

st.write(thesis)

# Relevant Life Experience

st.write(life_experience)


