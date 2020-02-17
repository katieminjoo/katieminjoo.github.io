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
+ 해당 글은 각주(footnote[^footnote])의 글을 참고하여 제작되었습니다.
```
[^footnote]
```


### Reverse Footnote & 
[^footnote]: [**참고글**](https://github.com/cotes2020/jekyll-theme-chirpy/)  

```
[^footnote]: [**참고글**](https://github.com/cotes2020/jekyll-theme-chirpy/)  
```
> caret을 없애고, URL을 집어넣은 괄호를 연달아 써준다면, 하이퍼링크 기능을 사용할 수 있습니다.



## image

![Desktop View]({{ "/assets/img/sample/image.png" | "https://haehwan.github.io/" }})

```
![Desktop View]({{ "/assets/img/sample/image.png" | relative_url }})
```
> 사진을 클릭하면 URL을 타고 이동이 가능하다.  

```
![Desktop View](/assets/img/sample/image.png)
```
> 이미지만 간편히 올릴 수 있다.  
