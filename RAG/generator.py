from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from rag.prompt import build_prompt

class Generator:
    def __init__(self, model_name):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    def generate(self, question, docs):
        context = "\n".join(d["text"] for d in docs)
        prompt = build_prompt(context, question)

        inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True)
        outputs = self.model.generate(**inputs, max_new_tokens=120, temperature=0.0)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
