import pandas as pd
from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer
import numpy as np
from sklearn.model_selection import train_test_split
import argparse


LABELS = ["announcement","important","spam","casual","greeting"]


parser = argparse.ArgumentParser()
parser.add_argument('--csv', required=True)
parser.add_argument('--model', default='distilbert-base-uncased')
parser.add_argument('--out', default='./models/luna-clf')
args = parser.parse_args()


df = pd.read_csv(args.csv)
df = df[df['label'].isin(LABELS)]
label2id = {l:i for i,l in enumerate(LABELS)}
id2label = {i:l for l,i in label2id.items()}


df['labels'] = df['label'].map(label2id)
train_df, val_df = train_test_split(df, test_size=0.1, random_state=42, stratify=df['labels'])


tok = AutoTokenizer.from_pretrained(args.model)


def tok_fn(batch):
return tok(batch['text'], truncation=True, padding='max_length', max_length=128)


train_ds = Dataset.from_pandas(train_df[['text','labels']]).map(tok_fn, batched=True)
val_ds = Dataset.from_pandas(val_df[['text','labels']]).map(tok_fn, batched=True)


m = AutoModelForSequenceClassification.from_pretrained(args.model, num_labels=len(LABELS), id2label=id2label, label2id=label2id)


args_tr = TrainingArguments(
output_dir=args.out,
learning_rate=5e-5,
per_device_train_batch_size=32,
per_device_eval_batch_size=64,
num_train_epochs=3,
evaluation_strategy='epoch',
logging_steps=50,
load_best_model_at_end=True,
metric_for_best_model='f1',
)


from sklearn.metrics import f1_score, accuracy_score


def compute(p):
preds = np.argmax(p.predictions, axis=1)
f1 = f1_score(p.label_ids, preds, average='macro')
acc = accuracy_score(p.label_ids, preds)
return { 'f1': f1, 'acc': acc }


trainer = Trainer(model=m, args=args_tr, train_dataset=train_ds, eval_dataset=val_ds, compute_metrics=compute)
trainer.train()
trainer.save_model(args.out)