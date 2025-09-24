from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import argparse


LABELS=["announcement","important","spam","casual","greeting"]


p = argparse.ArgumentParser()
p.add_argument('--model', default='./models/luna-clf')
p.add_argument('text')
args = p.parse_args()


tok = AutoTokenizer.from_pretrained(args.model)
m = AutoModelForSequenceClassification.from_pretrained(args.model)


inputs = tok(args.text, return_tensors='pt', truncation=True)
with torch.no_grad():
logits = m(**inputs).logits
pred = logits.argmax(-1).item()
print(LABELS[pred])