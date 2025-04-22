from flask import Flask, request, jsonify, render_template
import requests
import certifi
from transformers import pipeline
from flask_caching import Cache
import os
import asyncio
import aiohttp
import torch

os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

app = Flask(__name__)
cache = Cache(app, config={"CACHE_TYPE": "SimpleCache", "CACHE_DEFAULT_TIMEOUT": 300})

# Asynchronous function to fetch Wikipedia content
async def fetch_wikipedia_full_content_async(topic):
    try:
        url = "https://en.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "format": "json",
            "prop": "revisions",
            "rvprop": "content",
            "titles": topic,
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params, ssl=False) as response:
                if response.status == 200:
                    data = await response.json()
                    pages = data["query"]["pages"]

                    page = next(iter(pages.values()))
                    if "revisions" in page:
                        full_text = page["revisions"][0]["*"]
                        return full_text
                    else:
                        return "Page not found or no content available!"
                else:
                    return f"Error: Received status code {response.status}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Use caching to avoid redundant API calls
@app.route("/summarize", methods=["POST"])
def summarize():
    try:
        data = request.json
        topic = data.get("topic", "")

        if not topic:
            return jsonify({"error": "Topic is required"}), 400

        if cache.get(topic):
            full_content = cache.get(topic)
        else:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            full_content = loop.run_until_complete(fetch_wikipedia_full_content_async(topic))
            cache.set(topic, full_content)

        if "Error" in full_content or "Page not found" in full_content:
            return jsonify({"response": full_content})

        # Optimized summarization
        summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", device=0 if torch.cuda.is_available() else -1)
        max_input_length = 1024
        chunks = [full_content[i : i + max_input_length] for i in range(0, len(full_content), max_input_length)]
        summaries = [summarizer(chunk, max_length=200, min_length=50, do_sample=False)[0]["summary_text"] for chunk in chunks]
        summary = " ".join(summaries)

        return jsonify({"response": summary})
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
