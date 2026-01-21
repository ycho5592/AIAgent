import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError("Environment Variable wasn't found")
client = genai.Client(api_key=api_key)

response = client.models.generate_content(model="gemini-3-flash-preview", contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.")

print(response.text)

def main():
    print("Hello from aiagent!")


if __name__ == "__main__":
    main()
