import streamlit as st
from csv_writer import write_participants_to_csv
from webscraper import scrape_hackathon_page
import hashlib

# Sidebar for user input
st.sidebar.header("Enter your details")
name = st.sidebar.text_input("Your Name (First and Last)")
hackathon_link = st.sidebar.text_input("Hackathon Link", value="https://ai-devsummit-2024-hackathon.devpost.com/")
devpost_username = st.sidebar.text_input("Devpost Username", value="gclark0812@gmail.com")
devpost_password = st.sidebar.text_input("Devpost Password", type="password", value="SecurePrivatePassword")

hackathon_description = st.sidebar.text_area("Hackathon Description", height=200)  # Double the default height
hackathon_sponsors = st.sidebar.text_input("Hackathon Sponsors (comma separated, no spaces)")

# Main panel
st.title("Hackathon Team Finder")
st.subheader("By Boopesh S., Walter T., And Griffin C.")

# Submit button
if st.sidebar.button("Submit"):
    if hackathon_link:
        participants = scrape_hackathon_page(hackathon_link, devpost_username, devpost_password)
        if participants:
            st.write(f"Scraped {len(participants)} participants.")
            write_participants_to_csv(participants, filename=f"{hashlib.md5(hackathon_link.encode()).hexdigest()}.csv")
            st.write("Data written to participants.csv. Starting generation...")
        else:
            st.write("Failed to scrape participants.")
    else:
        st.write("Please enter a hackathon link.")
