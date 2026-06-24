import bm25s

def bm25_filter(key_words, documents: list[str], threshold=0.5):
    """
    Filters documents based on BM25 score with respect to the given keywords.

    :param keywords: List of keywords to search for.
    :param documents: List of documents (strings) to filter.
    :param threshold: Minimum BM25 score required for a document to be included in the results.
    :return: List of documents that meet the BM25 score threshold.
    """
    # Initialize BM25 model
    bm25 = bm25s.BM25(documents)

    # Calculate BM25 scores for each document
    scores = bm25.get_scores(key_words)

    # Filter documents based on the threshold
    filtered_documents = [doc for doc, score in zip(documents, scores) if score >= threshold]

    return filtered_documents