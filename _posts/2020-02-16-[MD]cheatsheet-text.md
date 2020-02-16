---
title: "[MD] Text and Typography"
date: 2020-02-16 17:46:00 +0800
categories: [Markdown, Text]
tags: [github pages, markdown, footnote, kbd, image]
toc : true
comments: true
---


## 글자 편집
+ 제목 역할을 위한 글씨크기는 우물 정자 두 개가 가장 적당하다.


## 줄 긋기
 + 별표 3개로 간단히 해결할 수 있다.  

***


## 키보드 표시
<kbd>키보드</kbd>에 있는 자판처럼 보이고 싶다면, kbd를 활용하자.


## footnote
```
[^footnote]
```
+ 해당 글의 원본을 각주(footnote[^footnote])처리하였습니다.
+ 현재까지 한글단어에 각주를 집어넣는 것은 지원이 안되는 것처럼 보입니다. 대신에 다음과 같은 방법[^ ]으로 대체할 수 있을지 모릅니다.
+ caret을 없애고, URL을 집어넣은 괄호를 연달아 써준다면, 하이퍼링크가 된다.


## image
![Desktop View]({{ "/assets/img/sample/image.png" | relative_url }})
```
![Desktop View]({{ "/assets/img/sample/image.png" | relative_url }})
```


## Reverse Footnote
[^footnote]: [**원본**](https://github.com/cotes2020/jekyll-theme-chirpy/)  
[^ ]: empty space
