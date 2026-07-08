import streamlit as st
from PIL import Image

def generate_greeting(name, gender):
    """Return a personalised greeting based on name and gender."""
    title = "Mr." if gender == "Male" else "Ms."
    greeting = f"Welcome {title} {name.title()}!"
    return greeting

def get_level_description(level):
    """Return a word description for the numeric level."""
    descriptions = {
        1: "Beginner",
        2: "Elementary",
        3: "Intermediate",
        4: "Advanced",
        5: "Expert"
    }
    return descriptions[level]

# App title
st.title("Simple Streamlit Demo For CUC")

# Header and subheader
st.header("Welcome to My App")
st.subheader("An interactive Python web app")

# Display text and markdown
st.text("This is plain text.")
st.markdown("**This is bold markdown text.**")

# Display status messages
st.success("Operation successful!")
st.info("Here is some information.")
st.warning("This is a warning.")
st.error("An error occurred.")

# Image display
img = Image.open("dog.jpg")
st.image(img, width=200)

# Checkbox
if st.checkbox("Show message"):
   st.write("Checkbox is checked!")
   
# Radio button
gender = st.radio("Select Gender:", ['Male', 'Female'])

# Use the generate_greeting function instead of if/else
# (We need the name variable too, so this will work with the text input below)

# Selectbox (version 1)
# hobby = st.selectbox("Select a Hobby:", ['Dancing', 'Reading', 'Sports'])
# st.write("Your hobby is:", hobby)

# Selectbox - using a list variable instead of hardcoded values
hobbies = ["Dancing", "Reading", "Sports", "Gaming",
           "Cooking", "Music", "Photography", "Gardening"]

hobby = st.selectbox("Select your main hobby:", hobbies)
st.write("Your main hobby is:", hobby)

# Multiselect - lets the user pick more than one hobby
selected = st.multiselect("Pick all your hobbies:", hobbies)

# Dictionary mapping each hobby to a fun fact
hobby_facts = {
    "Dancing": "Dancing burns about 300 calories per hour.",
    "Reading": "The average person reads 12 books a year.",
    "Sports": "Regular exercise improves memory by 20%.",
    "Gaming": "The global gaming industry is worth $180 billion.",
    "Cooking": "The world's oldest recipe is over 4,000 years old.",
}
# Loop through the selected hobbies and display each one
if selected:
    st.write(f"You selected {len(selected)} hobbies:")
    for h in selected:
        st.write(f"  - {h}")
else:
    st.info("No hobbies selected yet.")
   
# Get the list of hobbies from the dictionary keys
hobbies = list(hobby_facts.keys())

# Selectbox using the dictionary keys as options
hobby = st.selectbox("Select a Hobby:", hobbies)

# Look up the fun fact from the dictionary
if hobby in hobby_facts:
    st.info(hobby_facts[hobby])
else:
    st.warning("No fun fact available for this hobby yet.")

# Slider
level = st.slider("Choose a level", 1, 5)
st.write(f"Your level: {get_level_description(level)}")

# Text input
name = st.text_input("Enter your name", "Type here...")
if st.button("Submit"):
    # Call the function with name and gender as arguments
    st.success(generate_greeting(name, gender))


