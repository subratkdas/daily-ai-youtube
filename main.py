import os
import requests
from google.genai import Client

client = Client(api_key=os.environ.get("GEMINI_API_KEY"))

def get_trending_topic():
    url = "https://gtrends.hotkeywords.io/api/google-trends/daily?geo=IN"
    res = requests.get(url).json()
    topic = res["data"][0]["title"]
    return topic

def generate_script(topic):
    prompt = f"Write a viral short 20-second motivational script inspired by this trending Indian topic: {topic}. Short emotional lines. High energy. End with a strong closing punch."
    result = client.models.generate_content(model="gemini-1.5-flash", contents=prompt)
    return result.text

if __name__ == "__main__":
    topic = get_trending_topic()
    script = generate_script(topic)
    print("🔥 Trending:", topic)
    print("\n📝 Script:\n", script)
