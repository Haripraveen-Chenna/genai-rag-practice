import re

def extract_keywords(text, top_n=8):
    words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return sorted(freq, key=freq.get, reverse=True)[:top_n]
