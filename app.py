import ldclient
from ldclient.config import Config
import random
import streamlit as st
from csv_writer import write_participants_to_csv
from generate import generate_ideas
from webscraper import scrape_hackathon_page
import hashlib
import os

# Function to read the previous hash from a file
def read_previous_hash(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return file.read().strip()
    return None

# Sidebar for user input
st.sidebar.header("Enter your details")
hackathon_link = st.sidebar.text_input("Hackathon Link", value="https://ai-devsummit-2024-hackathon.devpost.com/")
devpost_username = st.sidebar.text_input("Devpost Username", value="gclark0812@gmail.com")
devpost_password = st.sidebar.text_input("Devpost Password", type="password", value="SecurePrivatePassword")

hackathon_description = st.sidebar.text_area("Hackathon Description", height=200, value="""JOIN DEVELOPERS & HACKERS AT THE DEVELOPERWEEK AI/ML 2024 HACKATHON PARTNERED WITH AWS, LAUNCHDARKLY, GITHUB & CONVEX!
You'll be hands-on building new apps, bots, and more -- using Amazon Bedrock Generative UI + LaunchDarkly!  Hackathon participants will compete for $33,200+ in cash, products and prizes.

The DeveloperWeek AI/ML 2024 Hackathon sponsored by AWS is co-located with Day 2 of the LaunchDarkly Galaxy 24 conference on May 22, 2024, at Pier 27 in San Francisco. Admission to the hackathon is free, but hackathon participants are invited to join the rest of the Galaxy 24 & Dev Day events via a special discount code and seperate registation (contact us for more details). 

Hackathon challenges & prizes are now Live!

May 22, 2024 - In-Person Hackathon

9:00 AM - 5:30 PM

Pier 27 - San Francisco, CA

 Register via Eventbrite.
Create a Devpost account and click Register on the Devpost DeveloperWeek AI/ML 2024 Hackathon page.
Check out the full Hackathon schedule!
Review full Hackathon Instructions here!
* All Hackathon Attendees must be pre-registered on Eventbrite & Devpost.

REQUIREMENTS
Age - 18 years and older. 

Citizenship - Participants from any country are allowed to participate. Visa support letters are not supplied to Hackathon Pass Holders.

Location - Participants must be onsite at Pier 27 to participate. 

Team Size - Teams can range in size from 1-5 people. 

Registration - Must register via Eventbrite & Devpost prior to Hackathon.

PRIZES
$33,200 in prizes
 AWS/LaunchDarkly Hackathon Challenge - Generative AI + Feature Flags
1st Place:$5,000 USD Cash Prize + Amazon Echos(Up to 5) + DevNetwork Premium All-Access Passes to all 2024 virtual conferences + Announcement in DeveloperWeek email to 60,000 subscribers listing your team and project. Plus, $5,000 worth of essential developer tools (GitHub, etc) and complimentary CodeCrafters memberships. All Values of the amazon echo prizes will be sent at USD
2nd Place:$3,000 cash USD Cash Prize
3rd Place:$2,500 Cash Prize

In this challenge, participants are invited to harness the cutting-edge power of Amazon Bedrock generative AI alongside the dynamic capabilities of LaunchDarkly feature flags to create innovative applications that push the boundaries of technology.

Use Amazon Bedrock generative AI:

Your task is to develop an application that taps into Amazon Bedrock generative AI capabilities and LaunchDarkly feature flags to enhance the user experience. Utilize any of the foundational models provided by Bedrock to infuse your application with intelligent and creative capabilities. Whether you're generating text, images, music, or even code, let your imagination run wild.

Integrate LaunchDarkly feature flags into your application to:

Enable dynamic, real-time modification of experimental generative AI features on the fly.
Seamless A/B testing or experimentation.
Managing targeted entitlements within your application.
Or whatever other creative feature flag uses you can think of!

Your application can serve any purpose or solve any problem, but to qualify for prizes, it must leverage both Amazon Bedrock generative AI and LaunchDarkly feature flags. We're looking for creativity, innovation, and technical prowess in your implementation of Bedrock and LaunchDarkly within your application.

** VISIT THE DEVELOPERWEEK TABLE TO RECEIVE YOUR FREE AWS BEDROCK LOGIN**

Judging Criteria:

Creativity and Innovation: Does the application do something unique and innovative and/or utilize Amazon Bedrock and LaunchDarkly feature flags in a creative way?
Level of Completion: How well-developed and polished is your application? Have you fully integrated Bedrock and LaunchDarkly features?
Use of Bedrock and LaunchDarkly: How effectively have you utilized the capabilities of Amazon Bedrock generative AI and LaunchDarkly feature flags to enhance your application? Are you showcasing the full potential of these technologies?

We can't wait to see what groundbreaking applications you'll create using the power of Amazon Bedrock and LaunchDarkly.

Resources:

Amazon Bedrock:
Amazon Bedrock Developer Experience: https://aws.amazon.com/bedrock/developer-experience/
Introduction to Amazon Bedrock: https://youtu.be/ab1mbj0acDo
Getting started workshop: https://catalog.us-east-1.prod.workshops.aws/workshops/a4bdb007-5600-4368-81c5-ff5b4154f518/en-US
Amazon Bedrock Resources: https://aws.amazon.com/bedrock/resources/
Prompt engineering guidelines: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-engineering-guidelines.html
Knowledge bases for Amazon Bedrock: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html
Agents for Amazon Bedrock: https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html
Sample codes: https://docs.aws.amazon.com/bedrock/latest/userguide/service_code_examples.html
QuickStart PoC: https://github.com/aws-samples/genai-quickstart-pocs

LaunchDarkly:

Getting started documentation: https://docs.launchdarkly.com/home/getting-started
Getting started with experimentation: https://docs.launchdarkly.com/home/about-experimentation
Using LaunchDarkly for entitlements: https://docs.launchdarkly.com/guides/flags/entitlements

 Best All-Student Team
1st Place - Github Prize Pack - $200 Cash Value

AWS/LaunchDarkly Hackathon Challenge - Generative AI + Feature Flags

Team of all students - High school, college or university, or bootcamp (need proof of enrollment or student email)

 Build Your Backend with Convex
First Place - $2,500 USD
Every application needs data, even when integrating AI, and Convex offers a powerful backend-as-a-service for builders. Integrating Convex is easy via their client libraries for Python, Rust, React and JavaScript. Hackathon participants who integrate Convex as their backend infrastructure within their application qualify for an additional prize.

 Convex + AI = ❤️
First Place - $2,500 USD

Yes, even AI applications need backend data, and Convex fits this requirement perfectly. As you build your Bedrock application, there are a number of ways you can integrate Convex to enhance your user experience. This challenge prize will be awarded to the team that creates the most compelling combination of Bedrock’s AI with Convex’s backend-as-a-service.""")  # Double the default height
hackathon_sponsors = st.sidebar.text_input("Hackathon Sponsors (comma separated, no spaces)", value="AWS,LaunchDarkly,GitHub,Convex")

# Main panel
st.title("Hackathon Team Finder")
st.subheader("By Boopesh S., Walter T., And Griffin C.")

# Submit button
if st.sidebar.button("Submit"):
    if hackathon_link:
        # Calculate the hash of the current hackathon link
        current_hash = hashlib.md5(hackathon_link.encode()).hexdigest()
        previous_hash = read_previous_hash('previous_hash.txt')

        # Check if the hackathon link has changed
        if current_hash != previous_hash:
            participants = scrape_hackathon_page(hackathon_link, devpost_username, devpost_password)
            if participants:
                st.write(f"Scraped {len(participants)} participants.")
                write_participants_to_csv(participants, filename=f"{current_hash}.csv")
                st.write("Data written to participants.csv.")
            else:
                st.write("Failed to scrape participants.")
        else:
            st.write("Hackathon link has not changed. No need to scrape again.")
        
        st.write("Generating ideas...")
        content = generate_ideas(hackathon_description, hackathon_sponsors)
        st.write(content)
    else:
        st.write("Please enter a hackathon link.")

# Initialize LaunchDarkly client with your LaunchDarkly API key
api_key = "api-7f74da19-c8ce-439a-ae76-1e0fb3485987"
ldclient.set_config(Config(api_key))
ld_client = ldclient.get()

# Check if the resume feature is enabled for this user
feature_key = "show_resume_feature"

# Construct the user object with context kind (user) and attribute (key)
user = {
    "key": random.randint(1, 10000),  # User ID
    "name": devpost_username  # Name attribute
}

# Evaluate the feature flag based on the user object
st.write(user)
st.write(ld_client.variation(feature_key, user, True))
resume_feature_enabled = ld_client.variation(feature_key, hackathon_link, False)
