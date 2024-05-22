import csv
import concurrent.futures

idea_generation_prompt = """For this hackathon (details below), give me five project ideas that I might want to do to win the hackathon. Focus on the following criteria:
1/ These projects should be able to be done by a small team in the time alotted 
2/ These projects should be able to be done by a team of students
3/ These projects MUST use software from the sponsors (last line). Describe how software from each of the sponsors can be integrated into each project after describing what the project is

Your project description should be one paragraph, and 3-5 sentences. Projects should be split by '$$$' so that I can parse them easily.

Hackathon Details:
"""

team_selection_prompt = """ For this project (details below), find me five team members from the uploaded CSV that I gave you that would be good to work on this project. Focus on the following criteria:
1/ They should have skills different from each other
2/ Assume that I am the PM and have no relevant skills unless my resume says otherwise (if my resume is not included, then assume that I'm useless)

It is CRITICAL that the team member names you give me are real people pulled from your knowledge base, specifically from the CSV (or data pasted below if provided). You will get a $1 tip if you do this proeprly. 

For each person, say their name and once sentence about why their particular mix of skills and interests is helpful
"""

def get_content_from_llm(prompt):
    x = openai.ChatCompletion.create(
        model="gpt-4-1106-preview",
        messages=[{"role": "user", "content": prompt}]
    )
    content = x['choices'][0]['message']['content']
    print(content)
    return content


def generate_ideas(description, sponsors):
    full_idea_prompt = idea_generation_prompt + "\n" + description + "\n" + sponsors
    ideas_text = get_content_from_llm(full_idea_prompt)
    ideas = ideas_text.split("$$$")

    ideas_with_teams = []

    # Function to generate team for an idea
    def generate_team_for_idea(idea):
        full_team_prompt = team_selection_prompt + "\n" + idea 
        team_text = get_content_from_llm(full_team_prompt)
        return idea, team_text

    # Use ThreadPoolExecutor to run team generation in parallel
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_idea = {executor.submit(generate_team_for_idea, idea): idea for idea in ideas}
        for future in concurrent.futures.as_completed(future_to_idea):
            idea, team = future.result()
            ideas_with_teams.append((idea, team))
    
    return ideas_with_teams
        