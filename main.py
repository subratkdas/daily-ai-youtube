import os
from pytrends.request import TrendReq
from google.genai import Client

client = Client(api_key=os.environ.get("GEMINI_API_KEY"))

def get_trending_topic():
    pytrend = TrendReq(hl='en-IN', tz=330)
    trending = pytrend.trending_searches(pn='india')
    topic = trending[0][0]  # top trending keyword
    return topic

def generate_script(topic):
    prompt = f"Write a powerful 25-second emotional motivational script inspired by this trending topic: {topic}. Use short punchy lines. Suitable for YouTube Shorts."
    result = client.models.generate_content(model="gemini-1.5-flash", contents=prompt)
    return result.text

if __name__ == "__main__":
    topic = get_trending_topic()
    script = generate_script(topic)
    print("🔥 Trending:", topic)
    print("\n📝 Script:\n", script)
