---
title: <i class="fas fa-database"> Algorithm Analysis</i>
date: 2020-03-14 09:20:00 +0800
categories: [Programming, Algorithm]
tags: [Algorithm Analysis, Asymptotic notation]
toc: true
comments: true
sitemap :
  changefreq : daily
  priority : 1.0
---

<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

임의의 숫자들을 크기 순서대로 재배열해주는 방법은 [Bubble sort, Quick sort, Merge sort](https://www.cs.cmu.edu/~adamchik/15-121/lectures/Sorting%20Algorithms/sorting.html) 등 다양합니다. 이들은 모두 같은 결과값을 반환하지만, 연산 방식이 달라서 걸리는 시간과 필요한 메모리 양 등이 큰 차이를 가집니다. 그리고 이는 비단 재배열 문제에 국한되는 일이 아니라, 더욱 복잡한 모델에서도 같은 현상이 나타납니다.

따라서 우리는 여러 알고리즘 중에서도 좋은 알고리즘을 찾아내고 이를 계속 발전시켜나갈 필요가 있습니다. 오늘은 이에 대한 내용을 소개합니다.

# Algorithm Analysis
좋은 알고리즘과 나쁜 알고리즘을 구분하는 기준은 <b>효율성</b>입니다. 효율적인 알고리즘이란 기본적으로 execution에 필요한 resources 양이 적은 프로그램을 뜻합니다. 과연 프로그램을 실행하는데 필요한 자원은 어떤 것이 있을까요? 대표적으로 아래와 같은 자원들이 필요합니다.  

1. 메모리
2. communication bandwidth
3. running time

메모리와 통신 bandwidth도 중요하지만 사실 제일 중요한 것은 계산시간입니다. 메모리나 bandwidth는 돈을 주고 살 수 있지만, 시간은 돈을 주고도 살 수 없기 때문입니다. 그래서 대다수 알고리즘 분석은 <b>running time을 추측</b>(estimate)하는데 목적을 두고 있습니다. 우리는 이러한 분석을 통해서 좋은 알고리즘을 선별하고 계속해서 발전시켜 나가게 됩니다.

## time complexity
앞서서 running time에 대한 분석을 가리켜 time complexity(시간복잡도)라고 부릅니다. 그런데 사실 계산시간을 비교하는 것은 실행환경에 크게 영향을 받습니다. 예를 들어, 컴퓨터 사양이 좋고, data set 크기가 작으면 아무리 나쁜 알고리즘이더라도 계산시간은 얼마 안 걸리기 때문입니다.

따라서 running time을 estimate할 때에는 실행시간을 측정하는 대신 <b>연산의 실행 횟수</b>를 셉니다. 간단한 예제를 살펴보겠습니다.  

```python
def sum(a, b) :
    res = 0
    for i in range(a, b):
        res = res + i
    return res
```

위의 함수는 입력받은 두 수 사이에 있는 값들을 더해주는 알고리즘입니다. 이 경우 해당 연산에 필요한 실행 횟수는 총 2N+2입니다. `res = 0`과 `res = res + i`를 각각 한 번씩 실행해주고, for 구문 안의 2줄은 각각 N번씩 실행해야하기 때문입니다. 그런데 아래와 같은 예제는 이처럼 간단하지 않습니다.  

```python
def bubble(lst) :
    for i1 in range(0, n) :
        for i2 in range(i1+1, n):
            if lst[i1] < lst[i2] : 
                lst[i1], lst[i2] = lst[i2], lst[i1]
    print(cnt, lst)
```  

위의 예제는 [bubble sort](https://en.wikipedia.org/wiki/Bubble_sort)를 파이썬에서 실행하는 함수로, 데이터 구조는 list를 사용하여 nested for loop 구문을 통해 list 안의 숫자들을 크기 순서로 재배열해줍니다. bubble sort의 실행 횟수를 세주는 것이 쉽지 않은 이유는 <b>if 구문</b>이 포함되어 있기 때문입니다. 예를 들어, 운이 좋게 `[3, 2, 1]`을 입력받았다면 위의 알고리즘은 if 구문 안의 내용을 실행시킬 필요가 없게 됩니다. 반면에 `[1, 2, 3]`과 같이 입력받아다면 모든 반복마다 if 구문을 실행해주게 됩니다. 즉 데이터의 크기 N이 동일하더라도 그 값이 달라지게 되는 것입니다. 

그렇기 때문에 우리는 다양한 시간복잡도를 구할 수 있게 됩니다. 실제로 다양한 실행횟수들의 평균 (*평균 시간복잡도*, average-case analysis)를 구하기도 하고, 가장 오래 걸리는 경우를 기준으로 잡는 worst-case analysis를 사용하기도 합니다.  

## Asymptotic notation
asymptotic notation(점근 표기법)은 시간복잡도를 간단하게 표현하는 표기법입니다. 당연히 시간복잡도가 다양했던 것처럼, 점근 표기법도 다양합니다. 예를 들어 최선의 경우에 해당하는 시간복잡도는 간편하게 $$\Omega$$(빅-오메가)로 표기하고, 최악의 경우는 $$O$$(빅-오)로, 평균은 $$\theta$$(빅-세타) 표기하는 식입니다.

