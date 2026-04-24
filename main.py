from dotenv import load_dotenv
import json

from graph import build_graph

load_dotenv()


app = build_graph()

user_request = input("What job are you looking for? ")

result = app.invoke({
    "user_request": user_request,
    "keywords": "",
    "target_role": "",
    "location": "",
    "remote": False,
    "jobs": [],
    "final_answer": ""
})

final_data = json.loads(result["final_answer"])

print("\nSummary:")
print(final_data["summary"])

print("\nTop Jobs:")
for index, job in enumerate(final_data["jobs"], start=1):
    print(f"\n{index}. {job['title']}")
    print(f"Company: {job['company']}")
    print(f"Location: {job['location']}")
    print(f"URL: {job['url']}")
    print(f"Why relevant: {job['relevance_reason']}")