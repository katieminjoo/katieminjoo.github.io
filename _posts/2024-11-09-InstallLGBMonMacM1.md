---
title: Installing LightGBM on an M1 Mac
date: 2024-11-09 17:30:00 +0900
categories: [Machine Learning]
tags: [machinelearning]
toc: true
comments: true
published: true
sitemap:
  changefreq: daily
  priority: 1.0
---

While setting up LightGBM on my M1 Mac, I discovered that the default pip install lightgbm command does not work due to compatibility issues with Apple Silicon and libomp dependencies.

After trying various fixes, including setting environment variables and reinstalling libomp via Homebrew, I still encountered installation errors with:

`pip install lightgbm --no-binary :all:`

After some research, I found a solution that worked: creating a new Conda environment and installing LightGBM using Conda-Forge:
```
conda install \
   --yes \
   -c conda-forge \
   'lightgbm>=3.3.3'
```
This approach successfully installed LightGBM without further issues.

For more details and troubleshooting options, I found this [Stack Overflow](https://stackoverflow.com/questions/74568115/is-lightgbm-available-for-mac-m1) discussion useful.