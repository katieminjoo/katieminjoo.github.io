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
This project focuses on creating personalized pet emojis by detecting dog expressions with EfficientDet and generating corresponding emojis with StarGAN v2. This allows users to quickly transform dog photos into expressive emojis based on detected emotions (anger, happiness, sadness, and yawning).

## Data
***
* **Dataset**: Collected approximately 5,000 dog photos using emotion-based keywords [‘anger’, ‘happiness’, ‘sadness’, ‘yawning’].  
* **Annotation**: Annotated 400 images per emotion for front-facing dog faces, ensuring unique images without duplicates.  
* **Image Preprocessing**: Cropped images to focus on dog faces, with a minimum resolution of 100x100 pixels for both width and height.

## Main model / Technique
***
**`Object Detection`**  
[EfficientDet](https://arxiv.org/abs/1911.09070) was chosen as the object detection model for its accuracy and parameter efficiency, leveraging the EfficientNet backbone.  
![ef](/assets/img/project/starganv2/Efficientdet_architecture.png){:width="600px"}

**`Image Generation`**  
[StarGAN_v2](https://openaccess.thecvf.com/content_CVPR_2020/papers/Choi_StarGAN_v2_Diverse_Image_Synthesis_for_Multiple_Domains_CVPR_2020_paper.pdf) was used for image-to-image translation across multiple domains, which allowed transformations among four target expressions.  
![ef](/assets/img/project/starganv2/stargan.png){:width="500px"}


## Consideration
***
![ef](/assets/img/project/starganv2/Stargan_v01.png){:width="400px"}  
Here is the result after image generation using StarGAN v2.

![ef](/assets/img/project/starganv2/Stargan_problem.png){:width="400px"}  
While StarGAN v2 produced varied expressions, a challenge arose: the model also altered the dog’s breed and color based on the reference domain image.

To preserve the breed and color while altering only the facial expression, we integrated Histogram Loss from and color in the generated images.
[HistoGAN](https://arxiv.org/abs/2011.11731), which ensured consistent breed 

![ef](/assets/img/project/starganv2/Problem_solved.png){:width="400px"}  
After adding Histogram Loss, the results maintained the original breed and color, with only the facial expression changing.

## Future Ideas
***
Considering using an auto-annotation tool, such as CVAT, to improve annotation efficiency and accuracy.



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

## Future Ideas
***

