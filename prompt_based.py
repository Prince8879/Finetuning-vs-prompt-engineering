%%writefile assignment-5-finetuning-vs-prompt-engineering/prompt_based.py

import time

from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM
)

from data.test_data import (
    test_sentences
)


MODEL_NAME = "google/flan-t5-small"


tokenizer = AutoTokenizer.from_pretrained(
    MODEL_NAME
)

model = AutoModelForSeq2SeqLM.from_pretrained(
    MODEL_NAME
)

model.eval()


def predict_sentiment(text):

    prompt = f"""
Classify the sentiment of the following sentence.

Return only one word:
Positive or Negative.

Sentence: {text}

Sentiment:
"""

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True
    )

    outputs = model.generate(
        **inputs,
        max_new_tokens=5
    )

    result = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return result.strip()


def main():

    predictions = []

    start_time = time.time()

    print("\nPrompt-Based Results\n")

    for text in test_sentences:

        result = predict_sentiment(text)

        print("Text:", text)
        print("Prediction:", result)
        print()

        if result.lower().startswith("positive"):
            predictions.append(1)
        else:
            predictions.append(0)

    end_time = time.time()

    print("Predictions:", predictions)

    print(
        f"Processing Time: "
        f"{end_time - start_time:.4f} seconds"
    )


if __name__ == "__main__":
    main()