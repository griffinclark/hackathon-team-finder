import streamlit as st
from webscraper import scrape_hackathon_page
import hashlib

# Default hackathon link
default_hackathon_link = "https://ai-devsummit-2024-hackathon.devpost.com/"

# Sidebar for user input
st.sidebar.header("Enter your details")
name = st.sidebar.text_input("Your Name (First and Last)")
hackathon_link = st.sidebar.text_input("Hackathon Link", value=default_hackathon_link)
devpost_username = st.sidebar.text_input("Devpost Username")
devpost_password = st.sidebar.text_input("Devpost Password", type="password")

hackathon_description = st.sidebar.text_area("Hackathon Description", height=200)  # Double the default height
hackathon_sponsors = st.sidebar.text_input("Hackathon Sponsors (comma separated, no spaces)")

# Main panel
st.title("Hackathon Team Finder")
st.subheader("By Boopesh S., Walter T., Eli Z., And Griffin C.")

# Submit button
if st.sidebar.button("Submit"):
    if hackathon_link:
        # Hash the password before passing it
        page_title = scrape_hackathon_page(hackathon_link, devpost_username, devpost_password)
        st.write(f"Hello world! The title of the hackathon page is: {page_title}")
    else:
        st.write("Please enter a hackathon link.")
