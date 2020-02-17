---
layout: post
title: "[MD] Adding MathJax to a GitHub Pages"
date: 2020-02-17 15:43:00 +0800
categories: [Markdown, Mathjax]
tags: [github pages, Mathjax]
toc : true
comments: true
---

깃헙 페이지에 때로는 수학식을 표현할 필요가 생깁니다.  
이번 글에서는 Mathjax을 사용해서 편리하게 수학식을 사용하는 방법에 대해서 알아보겠습니다.  
참고한 자료는 footnote[^footnote]에 남겨놨습니다.  

## kramdownn
대다수 깃헙 페이지는 kramdown 마크다운을 사용하고 있습니다. kramdown은 기본 [math engine](https://kramdown.gettalong.org/converter/html.html#math-support)으로 MathJax를 사용하기 때문에 우리는 MathJax를 통해서 간편하게 수학식을 표현할 수 있습니다. 따라서 만약 여러분이 kramdown을 사용하고있는지, config.yml를 통해서 확인해야합니다. 

## mathjax: true
kramdown을 사용하고 있는 것을 확인했다면, 그 밑에 `mathjax: true`를 입력하시면 됩니다.

## example 1

you can use an inline formula $$\forall x \in R$$ like this one  
`you can use an inline formula $$\forall x \in R$$ like this one  `

## example 2
Here is an example MathJax inline rendering \\( 1/x^{2} \\), and here is a block rendering: \\[ \frac{1}{n^{2}} \\]
`Here is an example MathJax inline rendering \\( 1/x^{2} \\), and here is a block rendering: \\[ \frac{1}{n^{2}} \\]`

$$
M = \left( \begin{array}{ccc}
x_{11} & x_{12} & \ldots \\
x_{21} & x_{22} & \ldots \\
\vdots & \vdots & \ldots \\
\end{array} \right)
$$
