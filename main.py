import wikipedia
import llm
import yake
import search
import summerisation
import jeperdy_prompt

def main():
    # query = input("Enter a search query: ")
    clue = "This country hosted the 2022 FIFA World Cup, which concluded with Argentina defeating France in the final at Lusail Stadium."
    # keyword_extractor = llm.LLM(None, "http://localhost:11434/api", "hf.co/unsloth/Qwen3.5-4B-GGUF:Q4_K_S", extractor_prompt)
    # keywords = keyword_extractor.chat(query, None)
    kw_extractor = yake.KeywordExtractor()
    keywords = [t[0] for t in kw_extractor.extract_keywords(clue)]
    wiki_pages = []
    for keyword in keywords:
        search_results = wikipedia.search_wikipedia(keyword)
        if not search_results:
            continue
        wiki_pages.extend(search_results)
    wiki_pages = list(set(wiki_pages))
    wiki_contents = []
    for page in wiki_pages:
        content = wikipedia.get_page(page)
        wiki_contents.append(content)
    bm25_filtered = search.bm25_filter(keywords, [content["summary"] for content in wiki_contents], threshold=0.5)
    sum_llm = llm.LLM(None, "http://localhost:11434/api", "hf.co/unsloth/Qwen3.5-4B-GGUF:Q4_K_S", summerisation.sum_prompt)
    summed = []
    """for i, content in enumerate(bm25_filtered):
        print(f"Summerizing content {i+1}/{len(bm25_filtered)}")
        summary = sum_llm.chat(content + "\n" + "input statement: " + clue, None)
        summed.append(summary)"""
    
    print("\n\nFinal Summarized Output:")
    jeperdy_llm = llm.LLM(None, "http://localhost:11434/api", "hf.co/unsloth/Qwen3.5-9B-MTP-GGUF:Q4_K_S", jeperdy_prompt.jeopardy_prompt)
    context = "\n".join(bm25_filtered)
    print("Jeopardy Context:", clue)
    print("\n\nJeopardy Question:")
    jeopardy_question = jeperdy_llm.chat(f"Clue: {clue}\nContext: {context}", None)
    print(jeopardy_question)

if __name__ == "__main__":
    main()