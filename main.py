import os
import requests
from google.genai import Client

client = Client(api_key=os.environ.get("GEMINI_API_KEY"))

NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

def get_trending_topic():
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}"
    res = requests.get(url).json()
    headline = res["articles"][0]["title"]
    return headline

def generate_script(topic):
    prompt = f"Write a viral motivational 20-second YouTube Shorts script inspired by: {topic}. Use 1–2 line sentences, emotional tone, simple English, powerful ending call-to-action."
    result = client.models.generate_content(model="gemini-1.5-flash", contents=prompt)
    return result.text

if __name__ == "__main__":
    topic = get_trending_topic()
    script = generate_script(topic)
    print("Trending:", topic)
    print("\nScript:\n", script)
