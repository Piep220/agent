import os, sys

from dotenv import load_dotenv

from google import genai



def main():
    if len(sys.argv) == 1:
        print("no sys arg provided")
        sys.exit(1)
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    print("Hello from agent!")
    
    model = "gemini-2.0-flash-001"
    #contents = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    contents = sys.argv[1]
    response = client.models.generate_content(model=model, contents=contents)
    
    print("Response:")
    print(response.text)
    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    print("Response tokens:", response.usage_metadata.candidates_token_count)


if __name__ == "__main__":
    main()
