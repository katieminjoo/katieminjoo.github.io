---
title: <i class="far fa-chart-bar"> WANTED_assignment(1) </i>
date: 2022-02-21 14:00:00 +0800
categories: [wanted-pre-onboarding-ai]
tags: [deeplearning]
toc: true
comments: true
sitemap:
  changefreq: daily
  priority: 1.0
---


## Paperswithcode([https://paperswithcode.com/area/natural-language-processing](https://paperswithcode.com/area/natural-language-processing))에서 NLP sub task 중에 2개를 선택하여 본인 블로그에 정리해보세요. task 별로 아래 3가지 항목에 대해서 정리하세요.

1. ****Medical Named Entity Recognition****
    
    - task가 해결하고자 하는 문제가 무엇인가?
    
      - locate and classify named entities from unstructured natural language (especially in biomedical domain)
    
    - 데이터 소개(대표적인 데이터 1개)
    
      - task를 해결하기 위해 사용할 수 있는데 데이터가 무엇인가?
    
        ShARe/CLEF eHealth corpus
    
       - 데이터 구조는 어떻게 생겼는가?
    
        The dataset consists of deidentified clinical free-text notes from the MIMIC II database, version 2.5
    
        An unannotated clinical report dataset > each note was annotated by two professional coders trained for this task.
    
        and is evaluated on their abillity to automatically identify the boundaries of disorder named entities in the text.
    
        >> following disorder mentions are named entities.
        
        - Congenital Abnormality
        - Acquired Abnormality
        - Injury or Poisoning
        - Pathologic Function
        - Disease or Syndrome
        - Mental or Behavioral Dysfunction
        - Cell or Molecular Dysfunction
        - Experimental Model of Disease
        - Anatomical Abnormality
        - Neoplastic Process
        - Signs and Symptoms
    
        <data format>
    
        report name || annotation type || cui || char start || char end
        
        08100-027513-DISCHARGE_SUMMARY.txt||Disease_Disorder||c0332799||459||473
        
    - SOTA 모델 소개(대표적인 모델 1개)
    
      - task의 SOTA 모델은 무엇인가?
    
        ****BioELECTRA****
    
      - 해당 모델 논문의 요약에서 주요 키워드는 무엇인가?
    
        electra, discriminator, generator, encoder of the transformer, 
    
2. ****Few-shot NER****
    
    - task가 해결하고자 하는 문제가 무엇인가?
    
    Current approaches collect existing supervised NER datasets and reorganize them into the few-shot setting for empirical study. These strategies conventionally aim to recognize coarse-grained entity types with few examples, while in practice, most unseen entity types are fine-grained.
    
    so.. it is more focused on ‘fine-grained’ ner.
    
    - 데이터 소개(대표적인 데이터 1개)
    
    ****Few-NERD****
    
    - 데이터 구조는 어떻게 생겼는가?
    
     — a large-scaled human-annotated few-shot NER dataset with a hierarchy of 8 coarse-grained and 66 fine-grained entity types. 
    
    — it consists of 188,238 sentences from wikipedia and 4,601,160 words.
    
    — it is the first few-shot NER dataset and the largest humancrafted NER dataset.
    
    - SOTA 모델 소개(대표적인 모델 1개)
    
    - task의 SOTA 모델은 무엇인가?
    
    **ProtoBERT**
    
    - 해당 모델 논문의 요약에서 주요 키워드는 무엇인가?
    
    NER, few-shot, annotation, fine-grained