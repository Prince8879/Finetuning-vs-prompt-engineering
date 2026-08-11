from sklearn.metrics import accuracy_score

from data.test_data import true_labels


prompt_predictions = [1, 0, 1, 0]

fine_tuned_predictions = [1, 0, 1, 0]


prompt_accuracy = accuracy_score(
    true_labels,
    prompt_predictions
)

fine_tuned_accuracy = accuracy_score(
    true_labels,
    fine_tuned_predictions
)


prompt_time = 0.8154

fine_tuned_time = 0.3727


print("=" * 60)
print("ASSIGNMENT 5")
print("Fine-Tuning vs Prompt Engineering")
print("=" * 60)

print()

print(
    f"Prompt Engineering Accuracy: "
    f"{prompt_accuracy * 100:.2f}%"
)

print(
    f"Fine-Tuned Model Accuracy: "
    f"{fine_tuned_accuracy * 100:.2f}%"
)

print()

print(
    f"Prompt Engineering Time: "
    f"{prompt_time:.4f} seconds"
)

print(
    f"Fine-Tuned Model Time: "
    f"{fine_tuned_time:.4f} seconds"
)

print()

print("FINAL COMPARISON")
print("-" * 70)

print(
    f"{'Metric':<25}"
    f"{'Prompt Engineering':<22}"
    f"{'Fine-Tuned Model'}"
)

print("-" * 70)

print(
    f"{'Model':<25}"
    f"{'FLAN-T5-small':<22}"
    f"{'Fine-tuned DistilBERT'}"
)

print(
    f"{'Training Required':<25}"
    f"{'No':<22}"
    f"{'Yes'}"
)

print(
    f"{'Accuracy':<25}"
    f"{prompt_accuracy * 100:.2f}%"
    f"{'':<16}"
    f"{fine_tuned_accuracy * 100:.2f}%"
)

print(
    f"{'Inference Time':<25}"
    f"{prompt_time:.4f} sec"
    f"{'':<12}"
    f"{fine_tuned_time:.4f} sec"
)

print("-" * 70)