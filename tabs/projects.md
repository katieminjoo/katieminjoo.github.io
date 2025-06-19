---
title: Projects
theme: jekyll-theme-dinky
---

<!-- project 1 -->
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

![map sample](/assets/img/project/bss/bss_map_sample.png){:width="500px"}

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

<!-- project 2 -->
<details style="padding: 10px;">
<summary style="cursor: pointer; font-size: 1.5em; font-weight: bold;">
Dog Facial Expression Synthesis with Identity Preservation using StarGAN_v2
</summary>
<div markdown="1" style="margin-top: 10px; font-size: 1em;">

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

</div>
</details>

<!-- project 3 old ver -->
<!-- <details style="padding: 10px;">
<summary style="cursor: pointer; font-size: 1.5em; font-weight: bold;">Establishment of Knowledge Graphs using LLM</summary>
<div markdown="1" style="margin-top: 10px; font-size: 1em;">

# Establishment of Knowledge Graphs using LLM
<!-- [LINK](https://github.com/katieminjoo/stargan-v2) -->
<!-- 
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
</details> -->

<!-- Project 3 -->
<details style="padding: 10px;">
<summary style="cursor: pointer; font-size: 1.5em; font-weight: bold;">
Policy Knowledge Graph Construction from Korean Development Reports Using BERT and R-BERT
</summary>
<div markdown="1" style="margin-top: 10px; font-size: 1em;">

# Policy Knowledge Graph Construction from Korean Development Reports Using BERT and R-BERT

>`NLP`  
>`Named Entity Recognition (NER)`  
>`Relation Extraction (RE)`  
>`Knowledge Graph`  
>`Neo4j`  
![ef](/assets/img/project/KDI/KG_overall.png){:width="500px"}
## Design
***
Developed an NLP pipeline that automatically extracts entities and relations from Korean development policy reports (e.g. Korean Economic Development History, KSP reports) and builds a structured, searchable knowledge graph using Neo4j.  
The project aimed to improve the usability of government reports and enable policy analysts to trace entities, institutions, and policies over time.

## Data & Preprocessing
***
- **Documents**:  
  - Korean Economic Development History (331 pages)  
  - 137 Modularization Reports  
  - 19 KSP Policy Advisory Reports  
- **Additional data**: SCOPUS abstract API used to supplement rare tag categories
- **Preprocessing techniques**:
  - PDF to text using Apache Tika
  - Coreference resolution using Stanford CoreNLP (ML-based model)
  - Manual BIO2 tagging using [TextAE](https://textae.github.io/) for NER and relation tagging
  - Filtering out inconsistent terminology or extremely rare entity types for model stability

## Main Models & Techniques
***
**`Named Entity Recognition (NER)`**  
- Model: BERT + CRF  
- Tagging: BIO2 scheme  
- Entity types: Institution, Region, Structure, Year, Policy, Event, Term (7 total)  
- Achieved up to **F1 score: 0.87** after tuning  
- CRF enabled valid BIO structure learning (e.g. avoiding I-tags without B-prefix)

**`Relation Extraction (RE)`**  
- Model: [R-BERT](https://arxiv.org/abs/1905.08284) (fine-tuned on custom dataset in [Semeval-2010 task](https://arxiv.org/abs/1911.10422) 8 format)  
- Defined 9 relation types: e.g. Product-Producer, Cause-Effect, Entity-Origin (bidirectional)  
- **F1 score: 0.90** on test set

**`Knowledge Graph (KG)`**  
- Database: [Neo4j](https://neo4j-contrib.github.io/py2neo/) using py2neo  
- Standardized relation directions for consistent KG structure  
- Enforced uniqueness constraints on node names to avoid duplication  
- Final output: **13,341 entities** and **15,823 relations** integrated into a live KG

## Result
***
![ef](/assets/img/project/KDI/KG_example.png){:width="500px"}
- Successfully constructed an interactive KG representing Korea’s development experiences
- Enabled entity-based queries (via Cypher) and visual exploration (via Neo4j Bloom)
- Example use cases:
  - “Incheon Airport” node connects to institutions (e.g. MOLIT), events (e.g. IMF Crisis), and policies
  - Entity timelines trace policy evolution by year or topic
- Used internally by KDI analysts for case study identification and cross-policy tracing

## Challenges & Considerations
***
- Data sparsity in certain entity/relation classes; addressed with SCOPUS abstracts
- Inconsistent PDF formatting required manual parsing and filtering
- Ambiguity in defining domain-specific entity/relation types (e.g. “Term” vs “Policy”)
- Learned the importance of preprocessing and class balance through ablation testing

## Team Collaboration
***
- Conducted in a team of 6 researchers, with subteams for NER, RE, and KG
- Led coordination and tracking through Slack and Notion (calendar, to-do DB, document embeds)
- Weekly meetings to align on progress and resolve modeling challenges
- Team structure (2 members per subtask) enabled parallel experimentation and fast iteration

## Reflection
***
- This was my first hands-on application of NLP theory to a real-world document corpus  
- Reinforced the importance of preprocessing and annotation in applied NLP  
- NER and RE can unlock scalable knowledge extraction from government documents  
- Knowledge Graphs are powerful tools not just for search, but for surfacing hidden policy patterns  
- I’m excited to explore their potential across other domains like healthcare or education

</div>
</details>

<!-- Project 4 old -->
<!-- <details style="padding: 10px;">
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

<!-- ## Future Ideas
***

</div>
</details> -->

<!-- Project 4 -->
<details style="padding: 10px;">
<summary style="cursor: pointer; font-size: 1.5em; font-weight: bold;">Anomaly Detection for Welding Defect Identification</summary>
<div markdown="1" style="margin-top: 10px; font-size: 1em;">

# Anomaly Detection for Welding Defect Identification

>`Anomaly Detection`  
>`Feature Engineering`  
>`Sensor Data Analysis`

![ef](/assets/img/project/Anomaly/AnomalyDetection.png){:width="600px"}

## Design
***
Built an end-to-end anomaly detection system to identify welding defects during battery manufacturing. Emphasis was placed on optimizing feature extraction from time-series sensor data and using both traditional and deep learning models for robust detection.

The goal was not to maximize traditional accuracy metrics but to detect as close to **99% of actual defects** as possible in a real-time production setting.

## Data
***
* **Source**: Time-series sensor data collected from laser welding equipment in production lines.
* **Preprocessing**: Applied Short-Time Fourier Transform (STFT) to convert raw signals into time-frequency representations for image-based classification.  
![STFT Example](/assets/img/project/Anomaly/stft_welding_example.png){:width="500px"}
> The image shows an example of a time-series sensor signal (top) and its corresponding STFT (Short-Time Fourier Transform) representation (bottom). The STFT transforms the raw signal into a time-frequency domain image, enabling the model to capture frequency patterns over time. This was particularly useful for identifying subtle anomalies in the welding process.

## Main Models / Techniques
***
* **Isolation Forest**  
* **Local Outlier Factor (LOF)**  
* **Support Vector Machine (SVM)**  
* **1D-CNN using STFT image input**  
* **STFT / FFT**  

These models were compared in terms of their ability to detect anomalous patterns in sensor behavior, with CNN delivering robust performance when trained on STFT-transformed inputs.

## Consideration
***
One of the most critical and challenging aspects of this project was **threshold tuning**. Determining the optimal cutoff for anomaly scores is essential for balancing false positives and false negatives in production environments. Fixed thresholds often led to either high false alarms or missed defects.

This required deep collaboration with field engineers who operated and maintained the welding equipment. Their domain knowledge helped define operationally viable and interpretable thresholds, integrating human expertise into model decisions.

## Result
***
* Successfully implemented a real-time defect detection monitoring system in the production environment.
* The system was able to detect **up to 99% of defective cases**, greatly improving quality assurance compared to the previous manual method.
* Model predictions were integrated into a dashboard UI for live monitoring by on-site teams.
* Due to the lack of labeled data, traditional accuracy, precision, or recall metrics were not the main focus; instead, the primary success metric was the proportion of actual welding defects that could be flagged and intercepted early.

## Future Ideas
***
* Automate and personalize thresholding methods using adaptive techniques.
* Explore ensemble detection frameworks that blend unsupervised and supervised signals.
* Collect more labeled data over time to enable more structured evaluation and model comparison.

</div>
</details>


<!-- Project 5 Old ver -->
<!-- <details style="padding: 10px;">
<summary style="cursor: pointer; font-size: 1.5em; font-weight: bold;">
Time Series Regression for Electrode Surface Temperature Optimization</summary>
<div markdown="1" style="margin-top: 10px; font-size: 1em;">

# Time Series Regression for Electrode Surface Temperature Optimization

>`Regression Modeling`  
>`Customized Deep Learning`   


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

</div>
</details> -->

<!-- Project 5 new -->
<details style="padding: 10px;">
<summary style="cursor: pointer; font-size: 1.5em; font-weight: bold;">
Time Series Regression for Electrode Surface Temperature Optimization</summary>
<div markdown="1" style="margin-top: 10px; font-size: 1em;">

# Time Series Regression for Electrode Surface Temperature Optimization

>`Regression Modeling`  
>`Customized Deep Learning`   

## Objective
***
The drying process in electrode manufacturing had long relied on a rule-based system that struggled to accommodate variations in real-world process conditions.  
Sometimes the heating was too aggressive, resulting in overheating; other times, it wasn’t enough—leading to persistent low temperatures. Engineers had to monitor every cycle and manually adjust inputs depending on factors like idle time or ambient conditions.

To solve this, we aimed to develop and deploy a machine learning model that dynamically adapts to changing production conditions and intelligently controls the heating process—minimizing both overheating and inefficiency.

## Data
***
- Time-series sensor data collected during the drying process  
- Data granularity: millisecond intervals  
- Preprocessing included downsampling, normalization, and control point alignment

## Model & Techniques
***
- LSTM  
- 1D-CNN  
- Attention Mechanisms  

We selected these architectures due to the inherently sequential and process-oriented nature of the data. Since heating decisions depend on how the process unfolds over time, temporal modeling was key.

For example:  
- 1D-CNN captured localized signal patterns efficiently.  
- LSTM handled longer-term dependencies.  
- Attention allowed the model to dynamically focus on crucial time slices and features related to surface temperature dynamics.

## Modeling Strategy
***
Rather than using a fixed dataset format, we iterated on how the data should be structured to highlight the most informative points:
- Separated features by importance and fed them into separate streams  
- Combined lower-priority features into the first LSTM layer and concatenated high-priority inputs later  
- Optimized model structure through experimental stacking and architectural tuning

## System Comparison
***
| Aspect                | Rule-based Control System         | ML-based Predictive System            |
|-----------------------|------------------------------------|----------------------------------------|
| Control Method        | Static thresholds                  | Dynamic adjustment via real-time data |
| Thresholds            | Manual tuning                      | Model-optimized thresholds             |
| Human Intervention    | Frequent operator input            | Fully automated operation              |
| Drying Consistency    | Inconsistent drying results        | Adaptive and consistent drying         |
| Defect Risk           | High                               | Minimized temperature deviation        |

## Result
***
- Deployed at Ultium Cells Plant (GM–LG joint venture) in Ohio, USA  
- Improved target surface temperature accuracy from ~50% to ~95%  
- Replaced manual rule-based system with adaptive predictive control  
- Reduced operator intervention and improved system responsiveness

![temperature_accuracy_improvement](sandbox:/mnt/data/temperature_accuracy_improvement.png?_chatgptios_conversationID=685186c2-b5f8-8013-92f9-c1717b1a8989&_chatgptios_messageID=e873e905-7c59-4fec-8aa9-01f8ffa0e590)

![1dcnn_prediction_curve](sandbox:/mnt/data/1dcnn_prediction_curve.png?_chatgptios_conversationID=685186c2-b5f8-8013-92f9-c1717b1a8989&_chatgptios_messageID=e873e905-7c59-4fec-8aa9-01f8ffa0e590)

![feature_correlation_improvement](sandbox:/mnt/data/feature_correlation_improvement.png?_chatgptios_conversationID=685186c2-b5f8-8013-92f9-c1717b1a8989&_chatgptios_messageID=e873e905-7c59-4fec-8aa9-01f8ffa0e590)

## Field Feedback
***
On-site engineers reported a significant reduction in manual tasks.  
Previously, operators had to supervise and adjust machine settings depending on idle time or abnormal conditions.  
With the new model, machines auto-adjusted to varying conditions while maintaining consistent results—earning strong positive feedback from the team.

## Business Impact
***
- Real-time optimization of the drying process  
- Estimated $100,000 in annual savings  
- Increased product consistency and reduced defect-related waste

## Reflections
***
This project helped me understand the importance of:
- Designing domain-specific representations for sensor data  
- Capturing temporal dynamics in manufacturing pipelines  
- Building modular architectures for experimentation  
- Maintaining close collaboration with engineers for real-world deployment feasibility

</div>
</details>
