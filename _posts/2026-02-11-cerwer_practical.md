---
layout: post
title: "[Speech Recognition] How to Compute CER and WER Using jiwer"
categories: [Machine Learning, Speech Recognition]
tags: [cer, wer, jiwer, asr, stt, evaluation]
---

In my previous post, I explained what CER (Character Error Rate) and WER (Word Error Rate) are and why CER is often preferred for Korean ASR evaluation.

Today, I’ll walk through how to compute CER and WER in Python using one of the most widely used libraries: **jiwer**.

---

## ✅ Why jiwer?

`jiwer` is a lightweight Python library that:

- Implements standard Levenshtein-based CER/WER
- Supports normalization pipelines
- Allows sentence-level and corpus-level evaluation
- Is widely used in research and industry experiments

Install it with:

```bash
pip install jiwer
```

## 1️⃣ Basic Example (Single Sentence)
```
from jiwer import cer, wer

reference = "오늘 날씨가 좋다"
hypothesis = "오늘날씨가 좋다"

print("CER:", cer(reference, hypothesis))
print("WER:", wer(reference, hypothesis))
```
CER measures character-level differences.
WER measures word-level differences.

## 2️⃣ Corpus-Level CER (Multiple Sentences)
If you have multiple sentence pairs:
```
references = [
    "안녕하세요 여러분",
    "오늘 날씨가 좋다",
]

hypotheses = [
    "안녕 하세요 여러분",
    "오늘날씨가 좋다",
]

overall_cer = cer(references, hypotheses)
overall_wer = wer(references, hypotheses)

print("Overall CER:", overall_cer)
print("Overall WER:", overall_wer)
```
Passing lists computes the total edit distance across all sentences.

This is the correct way to compute corpus-level CER/WER.

## 3️⃣ Adding Light Preprocessing
In practice, you often want to normalize text before computing CER/WER.

For example:
	•	Remove extra spaces
	•	Remove punctuation
	•	Convert to lowercase (for English)
```
from jiwer import cer
import re

def normalize_text(s):
    s = str(s).strip()
    s = re.sub(r"[^\w\s가-힣]", "", s)
    s = re.sub(r"\s+", " ", s)
    return s

references = [normalize_text(r) for r in references]
hypotheses = [normalize_text(h) for h in hypotheses]

print("Normalized CER:", cer(references, hypotheses))
```
Normalization rules should always be clearly documented when reporting metrics.

## 4️⃣ Sentence-Level Error Analysis
You can compute CER per sentence:
```
sentence_cer = [
    cer(r, h)
    for r, h in zip(references, hypotheses)
]

for i, score in enumerate(sentence_cer):
    print(f"Sentence {i+1}: {score:.3f}")
```
This is useful when you want to analyze which utterances are problematic.

## 5️⃣ Interpreting CER
As a general rule of thumb:
	•	< 5% → Very strong performance
	•	5–10% → Commercially acceptable
	•	15%+ → Errors clearly noticeable

(Interpretation depends on language and domain.)

## Final Thoughts

jiwer makes it easy to compute CER and WER using the standard definitions.

When evaluating ASR systems:
	•	Be consistent with preprocessing
	•	Clearly document normalization rules
	•	Distinguish between sentence-level and corpus-level metrics

If you’re working with Korean ASR, CER is often the more stable and informative metric.