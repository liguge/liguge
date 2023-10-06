import requests

def get_citation_count(doi):
    url = f"https://api.crossref.org/works/{doi}"
    response = requests.get(url)
    data = response.json()
    citation_count = data['message']['reference-count']
    return citation_count

if __name__ == "__main__":
    doi = "YOUR_PAPER_DOI_HERE"
    citation_count = get_citation_count(doi)
    print(f"Paper DOI: {doi}")
    print(f"Citation Count: {citation_count}")
