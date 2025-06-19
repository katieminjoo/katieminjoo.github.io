---
title: Projects
theme: jekyll-theme-dinky
---

<details style="padding: 10px;">
<summary style="cursor: pointer; font-size: 1.5em; font-weight: bold;">
Location Optimization Project for Battery Swapping Stations
</summary>
<div markdown="1" style="margin-top: 10px; font-size: 1em;">

# Location Optimization Project for Battery Swapping Stations

>`Geospatial Data`  
>`Feature Engineering`  
>`XGBoost Regression`  
>`Map Visualization`

## Design
***
This project aimed to support location planning for expanding battery swapping stations (BSS) beyond Seoul using data-driven analysis.  
We predicted the expected usage (i.e., number of battery swaps) for each 250m × 250m grid across Korea to identify areas with high potential demand.

## Data
***
- **Target variable**: Actual number of battery swaps per grid in Seoul  
- **Grid unit**: 250m × 250m and 50m × 50m  
- **Data sources**:
  - **Public data** (Statistics Korea): population by gender and age group  
  - **Geospatial features**: slope data, distance to nearest subway station  
  - **Commercial data**: national convenience store locations, business listings  
  - **Mobility data**: telecom-based floating population, especially rider mobility

## Main Model / Technique
***
**`XGBoost Regressor`**  
We trained an XGBoost model to predict battery swap counts per grid using spatial and behavioral features.

- **Key features** that strongly influenced the model included:
  - Rider mobility  
  - Population density  
  - Slope (incline)  
  - Distance to the nearest subway station  
- The model achieved a **MAPE of 22%**, but given the limited training data (~300 samples), the performance was acceptable for guiding strategic decisions.

## Consideration
***
- Rather than focusing purely on modeling, this project emphasized **feature engineering and selection**.
- Data availability was limited to Seoul, so we trained the model on Seoul and analyzed **what made high-demand zones different**.
- Applying this model to other regions was not ideal due to varying local characteristics; general direction might hold, but not detailed precision.
- Visualization played a key role — we used `folium` and `geopandas` to build an interactive map that visualized demand predictions and priority areas.

## Collaboration & Deployment
***
- I played a central role in communicating between our modeling team and the counterpart business team, ensuring alignment and clarity at every step.
- The final interactive HTML-based map was handed off to the stakeholder team, who used it to determine the **priority order for station installation** in new regions.
- According to internal reports, the installation followed our model's recommendation, though validation will require post-installation data over several months.

![map sample](/assets/img/project/bss/bss_map_sample.png){:width="600px"}

## Result
***
- Built a deployable location recommendation pipeline using real-world constraints  
- Delivered a practical tool that guided **real installation decisions**  
- Strengthened the team’s understanding of **how data-driven tools can inform urban infrastructure planning**

## Future Ideas
***
- Collecting more data from other regions to support **transfer learning** and **region-specific fine-tuning**  
- Developing more localized models for mid- to small-sized cities based on their unique mobility and demographic characteristics

## Reflections
***
- Reinforced the importance of **feature quality over model complexity**  
- Learned the power of **effective communication** across functional teams  
- Realized how crucial it is to think about **how predictions are visualized and delivered**, not just how they're made

</div>
</details>

<details style="font-size: 1.0em; padding: 10px;">
<summary style="cursor: pointer; font-size: 1.5em; font-weight: bold;">Synthesis of animal facial expressions using StarGAN_v2</summary>
<div markdown="1" style="margin-top: 10px;">

# Synthesis of animal facial expressions using Stargan-v2
[LINK](https://github.com/katieminjoo/stargan-v2)

>`Image Generation`  
>`Object Detection`  

![ef](/assets/img/project/starganv2/Stargan_v02.png){:width="500px"}

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
![ef](/assets/img/project/starganv2/Efficientdet_architecture.png){:width="700px"}

**`Image Generation`**  
[StarGAN_v2](https://openaccess.thecvf.com/content_CVPR_2020/papers/Choi_StarGAN_v2_Diverse_Image_Synthesis_for_Multiple_Domains_CVPR_2020_paper.pdf) was used for image-to-image translation across multiple domains, which allowed transformations among four target expressions.  
![ef](/assets/img/project/starganv2/stargan.png){:width="500px"}


## Consideration
***
![ef](/assets/img/project/starganv2/Stargan_v01.png){:width="500px"}  
Here is the result after image generation using StarGAN v2.

![ef](/assets/img/project/starganv2/Stargan_problem.png){:width="300px"}  
While StarGAN v2 produced varied expressions, a challenge arose: the model also altered the dog’s breed and color based on the reference domain image.

To preserve the breed and color while altering only the facial expression, we integrated Histogram Loss from and color in the generated images.
[HistoGAN](https://arxiv.org/abs/2011.11731), which ensured consistent breed 

![ef](/assets/img/project/starganv2/Problem_solved.png){:width="300px"}  
After adding Histogram Loss, the results maintained the original breed and color, with only the facial expression changing.

## Future Ideas
***
Considering using an auto-annotation tool, such as CVAT, to improve annotation efficiency and accuracy.


</div>
</details>

<details style="padding: 10px;">
<summary style="cursor: pointer; font-size: 1.5em; font-weight: bold;">Establishment of Knowledge Graphs using LLM</summary>
<div markdown="1" style="margin-top: 10px; font-size: 1em;">

# Establishment of Knowledge Graphs using LLM
<!-- [LINK](https://github.com/katieminjoo/stargan-v2) -->

>`LLM`  
>`Knowledge Graph (KG)`  
>`Named Entity Recognition (NER)`  
> `Relation Extraction (RE)`    

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
**`Named Entity Recognition (NER)`**  
* First, We manually BIO tagged all the named entity with TextAE 
* Then we trained We trained [BERT+CRF]() model to detect Named Entity from sentences.

>**The reason we use CRF(Conditional Random Field) together with BERT**  
CRF allows to have proper B-I-O sequential structure.
It learns the pattern so that we don't get B-O-I or I-B-O, but it ensures that we always get the right structure of B-I-O. Also I-ORG can't be followed after B-PER because they are the different entity.

**`Relation Extraction (RE)`**  
We manually tagged all the relationship between the entities based on [Semeval-2010 task](https://arxiv.org/abs/1911.10422).
And trained [R-BERT](https://arxiv.org/abs/1905.08284) which is an enriching Pre-trained Language Model with Entity Information for Relation Classification.

**`Knowled Graph (KG)`**  
We used [Neo4j](https://neo4j-contrib.github.io/py2neo/) to build a Knowledge Graph and display the KG.

## Consideration
***
* The lack of tagged Named Entities and Relation Entities leads to class imbalance in the dataset, resulting in insufficient model training.

## Result
***
![ef](/assets/img/project/KDI/KG_example.png){:width="500px"}

## Future Ideas
***
Considering using a better version of NER model such as GliNER
</div>
</details>


<details style="padding: 10px;">
<summary style="cursor: pointer; font-size: 1.5em; font-weight: bold;">Anomaly Detection for Welding Defect Identification</summary>
<div markdown="1" style="margin-top: 10px; font-size: 1em;">

# Anomaly Detection for Welding Defect Identification

>`Anomaly Detection`  
>`Feature Engineering`   

![ef](/assets/img/project/Anomaly/AnomalyDetection.png){:width="600px"}

## Design
***
Performed extensive feature engineering to extract and select key features from sensor data, optimizing inputs for anomaly detection models using clustering techniques, CNN and isolation-based methods, achieving 99% accuracy in identifying welding defects.

## Data
***
* Time-series seonsor data generated in laser welding production

## Main model / Technique
***
**`Isolation Forest`**  
**`Local Outlier Factor (LOF)`**  
**`Support Vector Machine (SVM)`**  
**`CNN`**  
**`STFT / FFT`**  
We applied the Short-time Fourier Transform (STFT) technique to analyze non-stationary signals by segmenting them into narrow time intervals. This transformation allowed us to convert our time series data into an STFT representation, making patterns more discernible. After transforming the data into STFT images, we trained a CNN model to effectively capture and learn the patterns within the time-series data.

## Consideration
***
In AI-based time-series anomaly detection research for automated monitoring, one of the biggest challenges is setting the anomaly score threshold to distinguish between normal and abnormal conditions in real-world applications. This is a crucial task that, when done manually, requires significant expertise and time. Many existing anomaly detection approaches use fixed thresholds, but these can result in high false alarm rates or low anomaly detection rates. To establish an optimal threshold, we focused on clear communication and collaboration, not only with the data analysis team but also with the on-site engineering team, who directly manage the equipment.


## Result
***
Led the end-to-end deployment process, including model development, real-time prediction, and UI integration, successfully implementing a real-time defect detection monitoring system in production environments.  
<!-- ![ef](/assets/img/project/KDI/KG_example.png){:width="500px"} -->

## Future Ideas
***

</div>
</details>



<details style="padding: 10px;">
<summary style="cursor: pointer; font-size: 1.5em; font-weight: bold;">
Time Series Regression for Electrode Surface Temperature Optimization</summary>
<div markdown="1" style="margin-top: 10px; font-size: 1em;">

# Time Series Regression for Electrode Surface Temperature Optimization

>`Regression Modeling`  
>`Customized Deep Learning`   

<!-- ![ef](/assets/img/project/Anomaly/AnomalyDetection.png){:width="600px"} -->

## Design
***
* Developed and deployed an ML-based predictive model using time series regression techniques to optimize the drying process in battery manufacturing, leveraging 1D CNN, LSTM, and Attention mechanisms for enhanced accuracy.  



## Data
***
* Time-series data generated in production

## Main model / Technique
***
**`LSTM`**  
**`1D-CNN`**  
**`Attention`**  

## Consideration & Thoughts
***
This project consisted of two main parts: modeling and deployment. Unlike other projects, this one was particularly challenging because we had to define the dataset structure specifically for training the model. The data we received from the equipment was in millisecond intervals, but there were key control points and timing requirements for the model deployment that needed to be considered.

It wasn’t just about building a model with a fixed dataset; we had to determine how to structure the dataset to highlight which points would be most informative and impactful for our model. To explore various dataset configurations, I experimented by stacking multiple neural networks to find the optimal model structure. For example, instead of feeding the entire dataset into a single network input, I separated features based on their importance. When I wanted the model to focus on a specific feature, I created two input streams, feeding less critical features into an initial LSTM layer and later concatenating the more important feature data with the output of this layer.

This project allowed me to experiment extensively with different modeling and data engineering techniques, making it both challenging and enjoyable.

## Result
***
- Successfully implemented the solution at the Ultium Cells plant (GM-LG joint venture) in Ohio, USA, achieving a significant increase in target temperature accuracy from 50% to 95%.
- Conducted ongoing remote monitoring and troubleshooting to fine-tune the model, leading to an estimated annual cost savings of $100,000.
<!-- ![ef](/assets/img/project/KDI/KG_example.png){:width="500px"} -->


</div>
</details>


