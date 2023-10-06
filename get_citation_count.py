import scholarly

def get_citation_count(title):
    search_query = scholarly.search_pubs(title)
    publication = next(search_query)
    citation_count = publication.citedby
    return citation_count

if __name__ == "__main__":
    paper_title = "Fault diagnosis for small samples based on attention mechanism"
    citation_count = get_citation_count(paper_title)
    print(f"Paper Title: {paper_title}")
    print(f"Citation Count: {citation_count}")

