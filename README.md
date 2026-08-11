

finetuning-vs-prompt-engineering/README.md

#  Fine-Tuning vs Prompt Engineering

## Objective

The objective of this assignment is to compare two approaches for NLP sentiment analysis:

1. Prompt Engineering
2. Fine-Tuned Model

The approaches are compared using:

- Accuracy
- Inference Time
- Resource Usage

---

## NLP Task

The selected task is:

**Sentiment Analysis**

The test dataset contains four sentences.

| Sentence | Label |
|---|---|
| I love this product | Positive |
| This is the worst experience | Negative |
| Amazing service | Positive |
| I hate this | Negative |

---

# Prompt Engineering

The prompt-based approach uses:

**google/flan-t5-small**

The model is not trained further.

Instead, a natural-language instruction is provided to the model:

```text
Classify the sentiment of the following sentence.

Return only one word:
Positive or Negative.
