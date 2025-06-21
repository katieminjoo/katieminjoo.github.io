---
layout: page
title: Time Series Regression for Electrode Surface Temperature Optimization
permalink: /projects/electrode-temperature/
---

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
![diagram](/assets/img/project/electrode/A_flowchart_diagram_illustrates_the_architecture_o.png){:width="500px"}

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
![temperature_accuracy_improvement](/assets/img/project/electrode/temperature_accuracy_improvement.png){:width="500px"}
- Replaced manual rule-based system with adaptive predictive control  
- Reduced operator intervention and improved system responsiveness


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

