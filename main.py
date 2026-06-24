import wikipedia
import llm

def main():
    with open("prompt/keyword_extractor.txt", "r") as f:
        extractor_prompt = f.read()
    # query = input("Enter a search query: ")
    query = "python is a popular beginner programming language"
    keyword_extractor = llm.LLM(None, "http://localhost:11434/api", "hf.co/unsloth/Qwen3.5-4B-GGUF:Q4_K_S", extractor_prompt)
    keywords = keyword_extractor.chat(query, None)
    print("Extracted keywords:", keywords)

if __name__ == "__main__":
    main()