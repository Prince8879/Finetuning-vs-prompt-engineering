%%writefile assignment-5-finetuning-vs-prompt-engineering/data/test_data.py

test_sentences = [
    "I love this product",
    "This is the worst experience",
    "Amazing service",
    "I hate this"
]

true_labels = [1, 0, 1, 0]

label_names = {
    0: "Negative",
    1: "Positive"
}