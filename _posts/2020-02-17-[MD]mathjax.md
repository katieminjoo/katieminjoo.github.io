---
layout: post
title: "[MD] Adding MathJax to a GitHub Pages"
date: 2020-02-17 15:43:00 +0800
categories: [Markdown, Mathjax]
tags: [github pages, Mathjax]
toc : true
comments: true
---
<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

깃헙 페이지에 때로는 수학식을 표현할 필요가 생깁니다.  
이번 글은 Mathjax을 사용해서 편리하게 수학식을 사용하는 방법을 적었습니다.  
참고한 자료는 이 곳[^footnote]에 남겨놨습니다.  

## 1. kramdown
대다수 깃헙 페이지는 kramdown 마크다운을 사용합니다. kramdown은 기본 [math engine](https://kramdown.gettalong.org/converter/html.html#math-support)으로 MathJax를 사용하기 때문에 우리는 MathJax를 통해서 간편하게 수학식을 표현할 수 있습니다. 따라서 만약 여러분이 kramdown을 사용하고있는지, config.yml를 통해서 확인해야합니다. 


## 2. mathjax: true
config.yml에서 kramdown을 사용하고 있는 것을 확인했다면, 그 밑에 `mathjax: true`를 입력해줍니다. 


## 3. Implement MathJax with Jekyll
kramdown이 기본적으로 MathJax를 사용하기는 하지만, 포스팅할 페이지를 자동적으로 MathJax 라이브러리에 연결시켜주지는 않습니다. MathJax는 언제까지나 자바스크립트 언어로 쓰여진 라이브러리의 일종이기 때문에 이를 사용하고 싶다면 포스팅할 페이지에서 아래와 같은 링크를 입력해주어야합니다.  
`<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>`  
> 위의 내용은 입력해도 포스팅에서는 보여지지가 않습니다.

  
본격적으로 사용방법은 참고자료의 예시를 통해 확인하겠습니다.


### example 1 : <kbd>$$...$$</kbd>  

you can use an inline formula $$\forall x \in R$$ like this one  
`you can use an inline formula $$\forall x \in R$$ like this one`   


### example 2 : <kbd>\\(...\\)</kbd>  

Here is an example MathJax inline rendering \\( 1/x^{2} \\)  
`Here is an example MathJax inline rendering \\( 1/x^{2} \\)`


### example 3 : <kbd>\\[...\\]</kbd>  

Here is a block rendering: \\[ \frac{1}{n^{2}} \\]  
`Here is a block rendering: \\[ \frac{1}{n^{2}} \\]`

  
    
    
### Reverse Footnote
[^footnote]: [**참고자료1**](http://themicronaut.github.io/theme-setup/)
