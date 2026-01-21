import os
from dotenv import load_dotenv
from google import genai



def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("Environment Variable wasn't found")
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(model="gemini-3-flash-preview", contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.")

    if response.usage_metadata is None:
        raise RuntimeError("Failed API rqueest: no usage_metadata property")

    prompt_token = response.usage_metadata.prompt_token_count
    response_token = response.usage_metadata.candidates_token_count


    print(f"Prompt tokens: {prompt_token}")
    print(f"Response tokens: {response_token}")

    print(response.text)

if __name__ == "__main__":
    main()
