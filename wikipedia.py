import wikipediaapi

def get_page(query):
    wiki = wikipediaapi.Wikipedia(user_agent='sane guess (merlin@example.com)', language='en')
    page = wiki.page(query)
    return {
        "title": page.title,
        "summary": page.summary
    }

# search wikipedia for a list of pages matching the query
def search_wikipedia(query):
    wiki = wikipediaapi.Wikipedia(user_agent='sane guess (merlin@example.com)', language='en')
    search_results = wiki.search(query, limit=3)
    return [
        result
        for result in search_results.pages
    ]