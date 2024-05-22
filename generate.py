
idea_generation_prompt = """For this hackathon (details below), give me five project ideas that I might want to do to win the hackathon. Focus on the following criteria:
1/ These projects should be able to be done by a small team in the time alotted 
2/ These projects should be able to be done by a team of students
3/ These projects MUST use software from the sponsors. Describe how software from each of the sponsors can be integrated into each project after describing what the project is

Your project description should be one paragraph, and 3-5 sentences. Projects should be split by '$$$' so that I can parse them easily.

Hackathon Details:
"""

team_selection_prompt = """ For this project (details below), find me five team members that would be good to work on this project. Focus on the following criteria:
1/ They should have skills different from each other
2/ Assume that I am the PM and have no relevant skills unless my resume says otherwise (if my resume is not included, then assume that I'm useless)

For each person, say their name and once sentence about why their particular mix of skills and interests is helpful
"""

