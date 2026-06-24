import bm25s
import Stemmer

def bm25_filter(key_words, documents: list[str], threshold=0.5):
    """
    Filters documents based on BM25 score with respect to the given keywords.

    :param keywords: List of keywords to search for.
    :param documents: List of documents (strings) to filter.
    :param threshold: Minimum BM25 score required for a document to be included in the results.
    :return: List of documents that meet the BM25 score threshold.
    """
    # Initialize BM25 model
    stemmer = Stemmer.Stemmer("english")
    corpus_tokens = bm25s.tokenize(documents, stopwords="en", stemmer=stemmer)

    # Create the BM25 model and index the corpus
    retriever = bm25s.BM25()
    retriever.index(corpus_tokens)

    query_tokens = bm25s.tokenize(" ".join(key_words), stemmer=stemmer)

    # Calculate BM25 scores for each document
    results, scores = retriever.retrieve(query_tokens, k=5)

    # Filter documents based on the threshold
    filtered_documents = []
    for i in range(results.shape[1]):
        doc, score = results[0, i], scores[0, i]
        if score >= threshold:
            filtered_documents.append(documents[doc])

    return filtered_documents