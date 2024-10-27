---
title: Projects
theme: jekyll-theme-dinky
---

# Synthesis of animal facial expressions using Stargan-v2
[LINK](https://github.com/katieminjoo/stargan-v2)

>`Image Generation`  
>`Object Detection`  

![ef](/assets/img/project/starganv2/Stargan_v02.png){:width="400px"}

## Design
***
The project aims to create personalized pet emojis using EfficientDet for expression detection and StarGAN v2 for image generation, allowing users to quickly turn dog photos into corresponding emojis based on detected emotions (anger, happiness, sadness, yawning).

## Data
***
* Crawled about 5,000 pictures of dog pictures with keywords of [‘anger’, ‘happiness’, ‘sadness’, ‘yawning’].
* Made an annotation of dog face for every 400 pictures for each emotion. (Includes only when it's a front face, actual picture without duplication.)
* Cropped only the face part when it's at least 100 pixels for the width and height.

## Main model / Technique
***
**`Object Detection`**  
We used [EfficientDet](https://arxiv.org/abs/1911.09070) which is an object detection network based on EfficientNet -> Less Parameters, but better accuracy  
![ef](/assets/img/project/starganv2/Efficientdet_architecture.png){:width="600px"}

**`Image Generation`**  
We used [Starganv2](https://openaccess.thecvf.com/content_CVPR_2020/papers/Choi_StarGAN_v2_Diverse_Image_Synthesis_for_Multiple_Domains_CVPR_2020_paper.pdf) which can perform image-to-image translations for multiple domains using only a single model since we have 4 different domains that we want to transform from one to another.  
![ef](/assets/img/project/starganv2/stargan.png){:width="500px"}


## Consideration
***
![ef](/assets/img/project/starganv2/Stargan_v01.png){:width="400px"}  
This is the result after the image generation with Starganv2.

![ef](/assets/img/project/starganv2/Stargan_problem.png){:width="400px"}  
But we did have problems here. We want the breed and the color of the dog doesn't change. But when the model refers the domain image, that also got the color and the appearance of the dog.
but we want the breed and the color stays and only the facial expression changes.

So we added HistogramLoss to ensure the color and the breed stays same even after the image generation.
[HistoGAN](https://arxiv.org/abs/2011.11731)  

![ef](/assets/img/project/starganv2/Problem_solved.png){:width="400px"}  
After we added HistogramLoss, we got the result which has the breed and the color same.  


## More Idea !
***
Maybe we can try auto annotation tool such as CVAT



# Establishment of Knowledge Graphs using LLM
<!-- [LINK](https://github.com/katieminjoo/stargan-v2) -->

>`LLM`  
>`Knowledge Graph (KG)`  
>`NER(Named Entity Recognition)`  
> `RE(Relation Extraction)`    
![ef](/assets/img/project/KDI/KG_overall.png){:width="500px"}

## Design
***
This project aims to automate the extraction of entity relationships within reports on South Korea’s development policies and international cooperation, creating a knowledge graph to improve usability. By automatically identifying entities (such as events, policies, and institutions) and mapping their relationships, the project leverages advanced methodologies to enhance automation efficiency and accuracy in knowledge graph construction.

## Data
***
* Reports from KDI (Eng)
* CoNLL 2003 (Eng)
#### Preprocessing
- Coreference Resolution (Stanford CoreNLP)
- PDF to Text (Tika)

## Main model / Technique
***
`NER`  
* First, We manually BIO tagged all the named entity with TextAE 
* Then we trained We trained [BERT+CRF]() model to detect Named Entity from sentences.

>**The reason we use CRF(Conditional Random Field) together with BERT**  
CRF allows to have proper B-I-O sequential structure.
It learns the pattern so that we don't get B-O-I or I-B-O, but it ensures that we always get the right structure of B-I-O. Also I-ORG can't be followed after B-PER because they are the different entity.

`RE`  
We manually tagged all the relationship between the entities based on [Semeval-2010 task](https://arxiv.org/abs/1911.10422).
And trained [R-BERT](https://arxiv.org/abs/1905.08284) which is an enriching Pre-trained Language Model with Entity Information for Relation Classification.

`Knowled Graph (KG)`  
We used [Neo4j](https://neo4j-contrib.github.io/py2neo/) to build a Knowledge Graph and display the KG.

## Consideration
***


## Result
***
![ef](/assets/img/project/KDI/KG_example.png){:width="500px"}

## More Idea !
***

