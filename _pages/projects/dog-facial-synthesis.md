---
layout: page
title: Dog Facial Expression Synthesis with StarGAN_v2
permalink: /projects/dog-facial-synthesis/
---

# Dog Facial Expression Synthesis with Identity Preservation using StarGAN_v2
[LINK](https://github.com/katieminjoo/stargan-v2)

>`Image Generation`  
>`Object Detection`  
>`GAN Fine-tuning`  
>`Feature Preservation`

![ef](/assets/img/project/starganv2/Stargan_v02.png){:width="500px"}

## Design
***
This two-step pipeline detects a dog's facial expression using object detection and synthesizes expressive, emoji-like images using StarGAN v2.  
The goal was to convert pet photos into four emotions — anger, happiness, sadness, and yawning — while preserving their identity.

## Data
***
- **Dataset**: ~5,000 dog images collected via emotion-related keyword search  
- **Annotation**: 400 manually labeled images per emotion, filtered to exclude duplicates  
- **Preprocessing**: Cropped to frontal dog faces with a minimum resolution of 100×100 pixels

## Main Model / Technique
***
**`Object Detection`**  
We used [EfficientDet](https://arxiv.org/abs/1911.09070) for lightweight and accurate detection of dog faces.  
![ef](/assets/img/project/starganv2/Efficientdet_architecture.png){:width="700px"}

**`Image Generation`**  
We applied [StarGAN_v2](https://openaccess.thecvf.com/content_CVPR_2020/papers/Choi_StarGAN_v2_Diverse_Image_Synthesis_for_Multiple_Domains_CVPR_2020_paper.pdf) to translate detected dog faces into the target emotion domains.  
![ef](/assets/img/project/starganv2/stargan.png){:width="500px"}

## Consideration
***
While StarGAN v2 successfully generated diverse expressions, it introduced unwanted changes to fur color and breed appearance due to entangled domain features.  
To address this, we integrated **Histogram Loss** inspired by [HistoGAN](https://arxiv.org/abs/2011.11731), which helped decouple identity from expression.

- Before (color drift):
  ![ef](/assets/img/project/starganv2/Stargan_problem.png){:width="300px"}
- After Histogram Loss (color preserved):
  ![ef](/assets/img/project/starganv2/Problem_solved.png){:width="300px"}

This fine-tuning preserved fur color and breed, which was especially important for user personalization.

> This challenge highlighted a common issue in image-to-image translation:  
> the entanglement between domain-specific attributes (emotion) and instance-level features (identity).

## Result
***
After integrating Histogram Loss, we observed a clear improvement — the dog's color remained consistent while only the facial expression changed.  
Previously, results often altered the fur tone (e.g. turning a white dog brown), which broke the sense of identity.  
This update led to **more realistic and personalized outputs**, enabling pet owners to create emoji-style versions of their actual pets.

## Future Ideas
***
- Quantitatively evaluate outputs using emotion classification models or user surveys  
- Scale up annotation using auto-labeling tools such as CVAT  
- Fine-tune on a wider variety of breeds and emotional cues  
- Explore integration into a mobile or web-based personalization tool

