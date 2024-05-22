# Hackathon Team Finder

Hackathon Team Finder is a web application that helps hackathon participants find suitable team members and generate project ideas. The app scrapes participant information from the provided hackathon link, processes it, and uses OpenAI's GPT-4 API to generate project ideas and suggest team members based on given criteria.

## Features

- Scrape participant data from Devpost hackathon page
- Suggest team members based on CSV data and project requirements
- Integration with LaunchDarkly for feature flag management

## Requirements

- Python 3.7+
- Streamlit
- AWS Account
- LaunchDarkly SDK
- CSV data

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/hackathon-team-finder.git
    cd hackathon-team-finder
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your API keys:
    - AWS auth info
    - LaunchDarkly SDK Key

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Open your web browser and navigate to the provided Streamlit URL.

3. Enter the hackathon link, Devpost username, and password in the sidebar.

4. Optionally, modify the hackathon description and sponsors.

5. Click the "Submit" button to scrape participant data and generate project ideas.

