import pandas as pd
import datetime

df = pd.read_excel("seminars.xlsx").sort_values("date")
output = open("README.md", "w")
now = datetime.datetime.now().strftime("%Y-%m-%d")

output.write(f"""
# Shared Seminars Fall 2020

For more lists, see:
- [Academic Seminars and Conferences](https://akazachk.github.io/seminars) / Aleksandr M. Kazachkov
- [ResearchSeminars.org](https://researchseminars.org/)\n
""")

last_date = ""
for index, row in df.iterrows():

    url = row["url"]
    series = row["series"]
    title = row["title"]
    speaker = row["speaker"]
    date = row["date"].strftime("%B %d")

    if last_date != date:
        output.write(f"### {date}\n")
        last_date = date

    output.write(f"- {series} / [{title}]({url}) / {speaker}\n")

output.close()
