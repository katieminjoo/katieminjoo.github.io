---
title: How to add a Conda environment as a kernel in Jupyter Notebook
date: 2025-01-18 19:30:00 +0900
categories: [Tips]
tags: [python, jupyter, anaconda, vscode]
toc: true
comments: true
published: true
sitemap:
  changefreq: daily
  priority: 1.0
---
# Resolving XGBoost Installation Issues on M1 Mac with Conda Virtual Environment

If you're working on an M1 Mac and trying to run XGBoost within a Conda virtual environment, you may encounter issues like `libxgboost.dylib` failing to load due to missing dependencies such as OpenMP. This is a common problem when setting up XGBoost on macOS, particularly on M1 chips, because XGBoost requires OpenMP for multithreading support.

In this post, I'll guide you through the steps to resolve this issue and get XGBoost running smoothly.

---

## **Problem: XGBoost Fails to Load on M1 Mac**

You may see an error similar to this when trying to import or run XGBoost:

```
XGBoostError: XGBoost Library (libxgboost.dylib) could not be loaded.
Likely causes:
  * OpenMP runtime is not installed
  * You are running 32-bit Python on a 64-bit OS
```

The issue arises because XGBoost relies on OpenMP for parallel processing, and macOS (especially on M1) does not include OpenMP by default.

---

## **Solution: Steps to Fix the Issue**

Follow these steps to resolve the problem:

### **1. Activate Your Conda Virtual Environment**
First, ensure you're working in the correct Conda virtual environment:

```bash
conda activate <your_environment_name>
```

Replace `<your_environment_name>` with the name of your Conda environment.

---

### **2. Install OpenMP and Make Using Homebrew**
Use Homebrew to install the necessary dependencies (`make` and `libomp`):

```bash
brew install make libomp
```

These libraries are essential for enabling OpenMP support on macOS.

---

### **3. Install XGBoost**
After installing OpenMP, use `conda`, not pip to install XGBoost in your Conda environment:

```bash
conda install xgboost
```

This command installs the latest version of XGBoost compatible with your Python environment.

---