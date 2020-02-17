---
title: "[MD] Text and Typography"
date: 2020-02-16 17:46:00 +0800
categories: [Markdown, Text]
tags: [github pages, markdown, cheatsheet]
toc : true
comments: true
---


## 글자 편집
+ 제목 역할을 위한 글씨크기는 우물 정자 두 개가 가장 적당하다.

***

## 줄 긋기
 + 별표 3개로 간단히 해결할 수 있다.  

***

## 키보드 표시
<kbd>키보드</kbd>에 있는 자판처럼 보이고 싶다면, kbd를 활용하자.

***

## image
### github에 저장한 이미지 불러오기
![Desktop View](/assets/img/sample/round_avartar.png)
```
![Desktop View](/assets/img/sample/image.png)
```
### image address 활용하기
![Desktop View](https://e-playonline.com/wp-content/uploads/2019/05/ngu.jpg)
```
![Desktop View](https://e-playonline.com/wp-content/uploads/2019/05/ngu.jpg)
```
> 마크다운에서는 <kbd>"</kbd>를 쓰는 경우가 거의 없습니다. 이미지로 불러올 때, 링크를 걸 때 모두 마찬가지입니다.
***


## footnote
+ 해당 글은 각주(footnote[^footnote])의 글을 참고하여 제작되었습니다.  

[^footnote]: [**참고글**](https://github.com/cotes2020/jekyll-theme-chirpy/)  

```
[^footnote]
```
  
***  

### Reverse Footnote & Link
Footnote는 마크다운에서 글을 쓰는 순서와 상관없이 항상 글 가장 마지막에 주석내용이 등장합니다. 각주를 달고 싶은 내용이 생각나면, 바로 밑에 그 내용을 적더라도 알아서 가장 마지막에 해당 내용이 순서대로 나타나기 때문에 글을 편하게 쓸 수 있게 됩니다.  

각주에 해당하는 단어를 똑같이 입력해주고 : 뒤에 내용을 적어주면 됩니다.
```
[^footnote]: ...
```
> <kbd>:</kbd> 을 빼먹을 때가 많으므로 유의해야합니다.

본 글에서는 각주내용으로 [링크](https://haehwan.github.io/)를 달았습니다. 링크도 각주와 유사한 방법으로 달 수 있습니다. caret을 없애고, URL을 집어넣은 괄호를 연달아 써주기만 하면 됩니다.
```
[**링크**](https://haehwan.github.io/)  
```
이미지로 링크 연결하기.
[![Desktop View](/assets/img/sample/round_avatar.png)](https://haehwan.github.io/)

최종적으로 위에서 만들었던 각주는 다음과 같이 만들었습니다.
```
[^footnote]: [**참고글**](https://github.com/cotes2020/jekyll-theme-chirpy/)
```
