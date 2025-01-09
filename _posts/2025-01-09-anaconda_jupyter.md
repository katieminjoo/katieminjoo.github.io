---
title: How to add a Conda environment as a kernel in Jupyter Notebook
date: 2025-01-09 19:30:00 +0900
categories: [Tips]
tags: [python, jupyter, anaconda, vscode]
toc: true
comments: true
published: true
sitemap:
  changefreq: daily
  priority: 1.0
---

## Activate Environment
`conda activate (env_name)`
## Install ipykernel
`pip instll ipykernel`
## Add the Environment as a Jupyter Kernel
`python -m ipykernel install --user --name (env_name) --display-name (env_name)`