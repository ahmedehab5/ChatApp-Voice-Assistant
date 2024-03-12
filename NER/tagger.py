import torch
from transformers import AutoModelForTokenClassification, AutoTokenizer
from transformers import pipeline
from NER.helpers import split_sentences

def NER(text):
  # Load the model
  device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
  tokenizer = AutoTokenizer.from_pretrained("hatmimoha/arabic-ner")
  model = AutoModelForTokenClassification.from_pretrained("hatmimoha/arabic-ner")

  nlp = pipeline("ner", model=model, tokenizer=tokenizer)

  # Tag the text
  sentences = split_sentences(text)

  annotations = nlp(sentences)

  entities = []
  tags = []
  for sentence in annotations:
    for item in sentence:
      if item["word"].startswith("##"):
        entities[-1] = entities[-1] + item["word"].replace("##", "")
      else:
        entities.append(item["word"])
        tags.append(item["entity"])


  #for item, label in zip(entities, tags):
  #  print(item + "\t" + label)

  return entities, tags