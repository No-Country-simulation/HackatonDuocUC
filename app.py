from gpt_client import ask_openai

def main():
    prompt = "Dime una broma corta sobre Python"
    respuesta = ask_openai(prompt)
    print("Respuesta de OpenAI:", respuesta)

if __name__ == "__main__":
    main()