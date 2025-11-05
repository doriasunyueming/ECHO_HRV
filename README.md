# Echo HRV Project: Emotion Prediction from Heartbeats & Emotion Language System

This project is part of my bigger vision called Echo. 
The project is an attempt to make emotional states more visible and understandable through physiological signals. 
It’s my first step toward building a system that connects what we feel inside with something we can actually measure and work with.

## Table of Contents

- [ Project Motivation ] 
- [ Methods ]
  - [1. Data Source]
  - [2. Signal Processing]
  - [3. Modeling]
  - [4. Evaluation]
- [ Language Layer Development ]
- [ Innovation Points ]
- [ Reproducibility ]
- [ System Architecture ]
- [ Summary ]

## Project Motivation

For most of human history, science has looked outward — to the stars, to the cells, to everything beyond us.  
Echo begins in the opposite direction: looking inward, toward the quiet and complex universe that lives inside every human being.

This project focuses on people whose inner worlds often go unheard. The individuals who, for many different reasons, lose their ability to express what they feel or think.  
Alzheimer’s patients are one example. **But they are not the only ones**.  
Stroke survivors, individuals with degenerative brain conditions, or people experiencing emotional shutdown may also carry a world within them that no longer finds its way into language.  

The idea behind Echo isn’t about holding on to just a feeling.  
It’s about **understanding a person while they’re still here**, seeing and remebering them as whole human beings, not only through their words, but through the quiet signals that remain when language fails.

Through this HRV project, I’m taking the first technical step toward this vision. 
By using **heart rate variability (HRV)** as a physiological signal, the goal is to explore whether subtle changes in heartbeat can help us sense and interpret emotional states when words are no longer available.
 
HRV may seem like a small piece of the puzzle, but it’s where **Echo** begins. It's where the vision to make the invisible inner universe of human emotion understandable, recordable, and never forgotten starts to come true.


## Methods

### 1. Data Source
I used the **WESAD dataset**, which contains ECG recordings and emotion labels (positive, neutral, negative).  
This dataset allowed me to simulate real-world scenarios where individuals cannot verbally express emotions.

- Input: ECG signals  
- Sampling frequency: 700 Hz  
- Labels: positive / neutral / negative
### 2. Signal Processing
ECG signals were processed to detect R-peaks and extract HRV features:

- RMSSD (short-term variability)  
- SDNN (overall variability)  
- MeanNN (mean RR interval)  
- LF/HF ratio (sympathetic–parasympathetic balance)

These metrics reflect subtle changes in autonomic activity linked to emotional regulation.
### 3. Modeling
I trained baseline models **logistic regression** and **random forest** to classify emotional states based on HRV features.  
**K-fold cross-validation** was used to ensure model stability and avoid overfitting.
### 4. Evaluation
Results were visualized using ROC curves and confusion matrices.  
The goal was not to chase the highest accuracy but to demonstrate that **HRV alone carries emotional information**.

## Language Layer Development

This phase builds on the decoding pipeline to construct a **personalized emotional language ecosystem**.

### 1. Emotional Language Mapping  
- Map decoded emotional states into a personalized emotional lexicon (e.g., *lightness*, *overflow*, *fragmentation*).
### 2. Emotional Grammar System  
- Define combinatorial rules for emotional tokens, enabling richer semantic expression.
### 3. Timeline Visualization
- Display emotional language streams as a timeline, creating story-like “emotional diaries.”
### 4. Emotion–Interaction Loop 
- Real-time recognition and triggering of alerts or interventions — turning emotion from a static signal into an interactive element.

## Innovation Points

| 1 | Emotional Language Mapping | Translate HRV signals into a personalized emotional lexicon. |
| 2 | Emotional Grammar System | Combine emotional tokens to express richer states. |
| 3 | Timeline-based Visualization | Transform abstract signals into human-readable narratives. |
| 4 | Emotion–Interaction Loop | From passive emotion recognition to interactive feedback. |
| 5 | Body-as-Language Paradigm | Redefine how non-verbal individuals can be “heard.” |

## Results


## Reflections


## Reproducibility

You can reproduce the base pipeline with the following steps:

```bash
# 1. Clone the repository
git clone https://github.com/your-username/echo-project.git
cd echo-project

# 2. (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the HRV processing & modeling script
python src/run_pipeline.py --dataset wesad --model random_forest