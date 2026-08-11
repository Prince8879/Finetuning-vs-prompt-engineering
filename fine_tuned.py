%%writefile assignment-5-finetuning-vs-prompt-engineering/fine_tuned.py

import time

import torch

from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification
)

from data.test_data import (
    test_sentences
)


MODEL_PATH = "./fine_tuned_model"


tokenizer = AutoTokenizer.from_pretrained(
    MODEL_PATH
)

model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_PATH
)

model.eval()


def predict_sentiment(text):

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True
    )

    with torch.no_grad():

        outputs = model(**inputs)

    prediction = outputs.logits.argmax(
        dim=-1
    ).item()

    return prediction


def main():

    predictions = []

    start_time = time.time()

    print("\nFine-Tuned Model Results\n")

    for text in test_sentences:

        prediction = predict_sentiment(text)

        predictions.append(prediction)

        result = (
            "Positive"
            if prediction == 1
            else "Negative"
        )

        print("Text:", text)
        print("Prediction:", result)
        print()

    end_time = time.time()

    print("Predictions:", predictions)

    print(
        f"Processing Time: "
        f"{end_time - start_time:.4f} seconds"
    )


if __name__ == "__main__":
    main()