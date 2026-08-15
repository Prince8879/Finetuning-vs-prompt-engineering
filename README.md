# Fine-Tuning vs Prompt Engineering

A practical NLP experiment comparing **Prompt Engineering** and **Fine-Tuning** for a **Sentiment Analysis** task.

The project evaluates both approaches using the same test sentences and compares:

* Accuracy
* Inference Time
* Training Requirement
* Model Architecture
* Implementation Complexity
* Resource Requirements

---

## 📌 Project Overview

This project demonstrates two different approaches to solving the same NLP classification problem.

### Approach 1 — Prompt Engineering

A pre-trained **FLAN-T5-small** model is instructed through a carefully designed prompt to classify text as either:

* Positive
* Negative

No additional model training is required.

### Approach 2 — Fine-Tuning

A pre-trained **DistilBERT** model is fine-tuned on the **SST-2 sentiment dataset** so that it becomes specialized for sentiment classification.

The resulting fine-tuned model is then used to classify the same test sentences.

---

## 🎯 Objective

The main objective is to understand the practical difference between:

> **Using a general-purpose language model with a prompt**

and

> **Training a pre-trained model for a specific NLP task**

The experiment measures how the two approaches perform when solving the same sentiment-analysis problem.

---

## 🧠 NLP Task

### Sentiment Analysis

The model receives a sentence and predicts whether its sentiment is:

* `Positive`
* `Negative`

### Test Dataset

The experiment uses four test sentences:

| # | Sentence                     | Expected Sentiment |
| - | ---------------------------- | ------------------ |
| 1 | I love this product          | Positive           |
| 2 | This is the worst experience | Negative           |
| 3 | Amazing service              | Positive           |
| 4 | I hate this                  | Negative           |

The corresponding numerical labels are:

```text
Positive = 1
Negative = 0
```

---

# 🏗️ Project Structure

```text
Finetuning-vs-prompt-engineering/
│
├── data/
│   └── test_data.py
│
├── image/
│   ├── Evaluate Fine Tuned Model.png
│   ├── Fianl Summmary.png
│   ├── Final Comaprison.png
│   ├── Fine Tune Model.png
│   ├── Fine Tuned Accuracy.png
│   ├── Load DistilBERT.png
│   ├── Prompt Engineering.png
│   ├── Test Fine Tuned Model.png
│   ├── Test Prompt Engineering.png
│   ├── Tokenization.png
│   └── Training Dataset.png
│
├── results/
│   └── result.txt
│
├── comparison.py
├── fine_tuned.py
├── prompt_based.py
├── requirements.txt
├── LICENSE
└── README.md
```

---

# ⚙️ Technologies Used

| Technology                | Purpose                          |
| ------------------------- | -------------------------------- |
| Python                    | Main programming language        |
| PyTorch                   | Deep learning framework          |
| Hugging Face Transformers | Pre-trained NLP models           |
| Hugging Face Datasets     | Dataset handling                 |
| scikit-learn              | Accuracy calculation             |
| pandas                    | Data processing                  |
| accelerate                | Model training/inference support |
| sentencepiece             | Tokenization support             |
| psutil                    | Resource monitoring              |

---

# 🤖 Models Used

## Prompt Engineering

The prompt-based implementation uses:

```text
google/flan-t5-small
```

FLAN-T5 is a text-to-text transformer model capable of following natural-language instructions.

The model is given a prompt similar to:

```text
Classify the sentiment of the following sentence.

Return only one word:
Positive or Negative.

Sentence: I love this product

Sentiment:
```

The model then generates the sentiment.

---

## Fine-Tuned Model

The fine-tuning approach uses:

```text
DistilBERT
```

The base DistilBERT model is trained on the:

```text
SST-2
```

sentiment dataset.

After fine-tuning, the model performs binary sentiment classification using:

```text
0 → Negative
1 → Positive
```

The inference script expects the trained model to be available in:

```text
./fine_tuned_model
```

> **Note:** The `fine_tuned_model` directory is not included in the current repository ZIP. It must be generated/downloaded separately before running `fine_tuned.py`.

---

# 🔬 Methodology

The experiment follows these steps.

## 1. Prepare Test Data

Four predefined sentences are loaded from:

```text
data/test_data.py
```

The test labels are:

```python
true_labels = [1, 0, 1, 0]
```

---

## 2. Prompt Engineering

The FLAN-T5-small model is loaded using Hugging Face Transformers.

Each sentence is converted into an instruction-based prompt.

The model generates either:

```text
Positive
```

or:

```text
Negative
```

The generated result is converted into a numerical prediction.

---

## 3. Fine-Tuning

DistilBERT is fine-tuned using the SST-2 sentiment dataset.

The resulting model specializes in sentiment classification.

The fine-tuned model receives the raw sentence as input and predicts the sentiment class directly.

---

## 4. Evaluation

Both approaches are evaluated using:

```text
Accuracy
Inference Time
```

The results are then compared using:

```text
comparison.py
```

---

# 📊 Results

## Prompt Engineering

**Model:**

```text
google/flan-t5-small
```

**Training Required:**

```text
No
```

**Predictions:**

```text
[1, 0, 1, 0]
```

**Accuracy:**

```text
100.00%
```

**Measured Inference Time:**

```text
0.8154 seconds
```

---

## Fine-Tuned Model

**Base Model:**

```text
DistilBERT
```

**Training Required:**

```text
Yes
```

**Training Dataset:**

```text
SST-2
```

**Predictions:**

```text
[1, 0, 1, 0]
```

**Accuracy:**

```text
100.00%
```

**Measured Inference Time:**

```text
0.3727 seconds
```

---

# 🏆 Final Comparison

| Metric              | Prompt Engineering | Fine-Tuned Model      |
| ------------------- | ------------------ | --------------------- |
| Model               | FLAN-T5-small      | Fine-tuned DistilBERT |
| Training Required   | No                 | Yes                   |
| Training Dataset    | Not Required       | SST-2                 |
| Accuracy            | 100.00%            | 100.00%               |
| Inference Time      | 0.8154 sec         | 0.3727 sec            |
| Task Specialization | General            | Specialized           |
| Implementation      | Simpler            | More involved         |
| Training Resources  | Not Required       | Required              |

---

# 📈 Performance Analysis

Both approaches achieved:

```text
100.00% Accuracy
```

on the four test sentences.

However, the measured inference time was different.

### Prompt Engineering

```text
0.8154 seconds
```

### Fine-Tuned Model

```text
0.3727 seconds
```

The fine-tuned DistilBERT model therefore had the lower measured inference time in this experiment.

Approximate difference:

```text
0.8154 - 0.3727 = 0.4427 seconds
```

The fine-tuned model was approximately:

```text
54.3% faster
```

than the prompt-based approach in this particular measurement.

> This timing should not be treated as a universal benchmark because inference speed depends on hardware, software versions, model loading, input size, warm-up state, and implementation details.

---

# ⚖️ Prompt Engineering vs Fine-Tuning

## Prompt Engineering

### Advantages

* No model training required
* Easy to implement
* Faster development
* Can be used with general-purpose instruction-following models
* Easy to modify behavior by changing the prompt
* Useful for rapid experimentation

### Disadvantages

* Depends heavily on prompt quality
* General-purpose models may generate unnecessary output
* Inference can be slower depending on the model
* Behavior may be less consistent
* The model is not specifically specialized for the task

---

## Fine-Tuning

### Advantages

* Model becomes specialized for the target task
* Can provide consistent predictions
* Can reduce inference complexity
* Useful for production-specific NLP applications
* Can improve performance on sufficiently large and representative datasets

### Disadvantages

* Requires training data
* Requires additional computational resources
* Training takes additional time
* Requires model and training configuration
* Requires maintaining the trained model

---

# 🧪 Running the Project

## 1. Clone the Repository

```bash
git clone https://github.com/Prince8879/Finetuning-vs-prompt-engineering.git
```

```bash
cd Finetuning-vs-prompt-engineering
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Prompt Engineering

Run:

```bash
python prompt_based.py
```

The script loads:

```text
google/flan-t5-small
```

and performs sentiment classification using prompt engineering.

Expected predictions:

```text
[1, 0, 1, 0]
```

---

# ▶️ Run Fine-Tuned Model

The fine-tuned model must first be available at:

```text
./fine_tuned_model
```

Once the model is available, run:

```bash
python fine_tuned.py
```

Expected predictions:

```text
[1, 0, 1, 0]
```

---

# 📊 Run Comparison

To compare the recorded results:

```bash
python comparison.py
```

The comparison script calculates accuracy using:

```python
accuracy_score()
```

and displays the final comparison between the two approaches.

---

# 📁 Results

The recorded experiment results are available in:

```text
results/result.txt
```

The repository also contains screenshots documenting different stages of the experiment.

These are located in:

```text
image/
```

The screenshots include:

* Training Dataset
* Tokenization
* Loading DistilBERT
* Fine-Tuning Model
* Fine-Tuned Accuracy
* Evaluating Fine-Tuned Model
* Testing Fine-Tuned Model
* Prompt Engineering
* Testing Prompt Engineering
* Final Comparison
* Final Summary

---

# 🔍 Key Findings

The experiment demonstrates that both approaches can successfully solve a simple sentiment-analysis task.

### Prompt Engineering

```text
100% Accuracy
0.8154 sec
No Training
```

### Fine-Tuning

```text
100% Accuracy
0.3727 sec
Requires Training
```

Therefore:

* Prompt engineering is simpler and requires no additional training.
* Fine-tuning requires additional data and computational resources.
* Fine-tuning produced the lower measured inference time in this experiment.
* Both approaches produced identical predictions on the selected test set.

---

# ⚠️ Important Limitation

The evaluation uses only **four test sentences**.

Therefore, the reported:

```text
100% Accuracy
```

should **not** be interpreted as evidence that either approach achieves 100% accuracy on real-world sentiment-analysis datasets.

A larger and more diverse test dataset would be required for a meaningful benchmark.

Other factors that should be evaluated in a larger experiment include:

* Precision
* Recall
* F1 Score
* Confusion Matrix
* Inference latency
* Memory usage
* CPU/GPU utilization
* Model size
* Training time
* Dataset size

---

# 🚀 Future Improvements

Possible improvements to this project include:

### 1. Larger Test Dataset

Use hundreds or thousands of unseen samples instead of four manually selected sentences.

### 2. More Evaluation Metrics

Add:

```text
Precision
Recall
F1 Score
Confusion Matrix
```

### 3. Resource Monitoring

Measure:

```text
RAM Usage
CPU Usage
GPU Usage
Model Size
```

### 4. Automated Benchmarking

Run both models multiple times and calculate:

```text
Average Inference Time
Minimum Inference Time
Maximum Inference Time
Standard Deviation
```

### 5. Visualization

Create charts comparing:

* Accuracy
* Inference time
* Memory usage
* Model size
* Training cost

### 6. Larger Models and Datasets

Compare different transformer architectures and evaluate how model size affects performance.

---

# 📚 Learning Outcomes

This project provides practical understanding of:

* Natural Language Processing
* Sentiment Analysis
* Transformer Models
* FLAN-T5
* DistilBERT
* Prompt Engineering
* Transfer Learning
* Fine-Tuning
* Tokenization
* Model Inference
* Model Evaluation
* Hugging Face Transformers
* PyTorch
* Dataset Handling

---

# 👨‍💻 Author

**Prince Tiwari**

GitHub:

https://github.com/Prince8879

Project Repository:

https://github.com/Prince8879/Finetuning-vs-prompt-engineering

LinkedIn:

https://www.linkedin.com/in/prince-tiwari-2549b7383/

---

# 📄 License

This project is distributed under the license included in the repository.

See:

```text
LICENSE
```

for more information.

---

## ⭐ Conclusion

This experiment shows the fundamental difference between **Prompt Engineering** and **Fine-Tuning**.

Prompt engineering allows a general-purpose model to perform a task without additional training, making it quick and easy to implement.

Fine-tuning requires additional training but produces a model specifically adapted to the target task.

For this experiment, both approaches achieved **100% accuracy on the four selected test sentences**, while the fine-tuned DistilBERT model recorded a lower inference time.

The experiment also demonstrates why evaluation on a sufficiently large and representative dataset is essential before drawing conclusions about real-world model performance.
