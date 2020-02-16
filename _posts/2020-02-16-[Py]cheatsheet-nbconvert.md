---
title: "[Python] Jupyter to Blogdown"
date: 2020-02-16 19:36:00 +0800
categories: [Python, nbconvert]
tags: [Jupyter, github blog]
toc : true
comments: true
---

깃헙 블로그는 다양한 방식으로 포스팅을 할 수가 있다.
이번 글에서는 jupyter notebook을 이용한 간단한 방법을 소개한다.[^notebook]

1. ipynb -> md
포스팅하길 희망하는 ipynb 파일과 동일한 위치에 있는 ipynb 파일에서 아래와 같이 작성한다.
```python
!jupyter nbconvert --to markdown USERNAME.ipynb
```
위의 코드를 실행하면, 새로운 MD 파일 하나와 폴더가 생성된다.
바꾸고자 했던 ipynb 파일명에 `_files`가 추가된 폴더에는 해당 ipynb안에 들어있던 이미지들이 포함되어있다.

[^notebook][링크](https://www.timlrx.com/2018/03/25/uploading-jupyter-notebook-files-to-blogdown/)의 자료를 참고하였다.
