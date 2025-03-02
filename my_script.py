from transformers import pipeline

pipe = pipeline("text-generation", model="distilbert/distilgpt2")

text = pipe("Hello,I have best friend name Ansori jancuk ?", max_length=50)

print(text[0]['generated_text'])
