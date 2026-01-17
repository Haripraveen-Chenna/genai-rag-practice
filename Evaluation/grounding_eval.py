import re

def grounding_score(answer, context):
    a = set(re.findall(r'\b[a-zA-Z]{4,}\b', answer.lower()))
    c = set(re.findall(r'\b[a-zA-Z]{4,}\b', context.lower()))
    return round(len(a & c) / max(len(a), 1), 3)
