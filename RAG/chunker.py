def split_by_headings(text, headings):
    sections = []
    current_section = "General"
    buffer = ""

    for line in text.split("\n"):
        for h in headings:
            if h.lower() in line.lower():
                if buffer:
                    sections.append((current_section, buffer))
                current_section = h
                buffer = ""
                break
        buffer += line + " "

    sections.append((current_section, buffer))
    return sections


def paragraph_chunking(sections, min_len=200, overlap_sentences=2):
    documents = []
    doc_id = 0

    for section, content in sections:
        sentences = content.split(". ")
        buffer = []
        i = 0

        while i < len(sentences):
            buffer.append(sentences[i])

            # create chunk when min_len reached
            if len(" ".join(buffer)) >= min_len:
                documents.append({
                    "id": f"DOC_{doc_id}",
                    "section": section,
                    "text": ". ".join(buffer).strip() + "."
                })
                doc_id += 1

                # 🔁 OVERLAP: keep last N sentences
                buffer = buffer[-overlap_sentences:]

            i += 1

        # leftover sentences
        if buffer:
            documents.append({
                "id": f"DOC_{doc_id}",
                "section": section,
                "text": ". ".join(buffer).strip() + "."
            })
            doc_id += 1

    return documents
