---
layout: post
title: <i class="fab fa-markdown"> Adding icons</i>
date: 2020-02-18 13:08:00 +0800
categories: [Markdown, Tutorial]
tags: [github pages, fontawesome]
toc : true
comments: true
---

오늘은 fontawesome을 통해서 icon 이미지를 사용하는 방법에 대해 설명하려고 합니다.
HTML에서 간편히 사용할 수 있기 때문에, github 블로그에서도 유용하게 쓸 수 있습니다.

## fontawesome
fontawesome에는 우리가 상상할 수 있는 거의 모든 icon이 존재합니다. 무료로 Solid와 Brands 스타일을 사용할 수 있기 때문에 매우 유용합니다. 사용법은 아래와 같습니다.

<i class="fab fa-google"></i>
<i class="fab fa-facebook"></i>

```
<i class="fab fa-..."</i>
```
> brands style : 구글이나 인스타그램 등과 같은 브랜드의 아이콘을 제공합니다.

<i class="fas fa-medal"></i>
<i class="fas fa-camera"></i>

```
<i class="fas fa-..."</i>
```
> solid style : 기타 대다수 아이콘들을 제공합니다.  

원하는 이미지가 어떤 스타일로 존재하는지 확신이 들지 않을 때는 [fontawesome 홈페이지](https://fontawesome.com/)에서 검색을 통해 확인가능합니다.

![image1](/assets/img/sample/fontawesome.PNG)


## 포스트 제목에 icon 집어넣기
위와 같이 HTML과 유사한 형식으로 icon을 불러올 수 있다면, 활용을 자유롭게 할 수 있습니다.
블로그 사이드바 밑의 아이콘들도 위와 같은 방식에 하이퍼링크를 입힌 것입니다.

혹은 더 단순하게 글의 제목에도 아이콘을 집어넣을 수 있었습니다.  
이번 글의 제목은 마크다운의 이미지를 활용해서 제목에 집어넣은 것입니다.
```
layout: post
title: <i class="fas fa-markdown" title=" Adding icons"></i>
...
```
