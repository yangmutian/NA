# NZ-A

[![Python Version](https://img.shields.io/badge/python-3.12-orange)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-Apache--2.0-blue)](https://opensource.org/licenses/Apache-2.0)
![Paper](https://img.shields.io/badge/Paper-green)
![Demo](https://img.shields.io/badge/Demo-red)

This repo provides code for NanoZyme-Agent (NZ-A), a framework equipped with LLM-based agents and customized AI toolkits for material research. 

Using NZ-A, researchers without programming expertise successfully identify six unreported rare earth-based peroxidase (POD)-like nanozymes from nearly 600k candidate materials within seconds. 

## Installation

NZ-A is intended to work with Python 3.12. Installation can be done via pip:

```
pip install -r requirements.txt
```

## Dataset

**Train**

This study incoprates [Wei dataset](http://nanozymes.net), [Dizyme dataset](https://dizyme.aicidlab.itmo.ru/), and [Huang dataset](https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.202201736) for model training. Researchers can download these datasets and replace `/data/train.csv`. In addition to open datasets, researchers can also replace `/data/train.csv` with their custom data to train personalized AI models.

**Screen**

The trained model is used to screen the nanozymes in [Materials Project](https://next-gen.materialsproject.org/), [Aflow](https://aflowlib.org/), and [OQMD](https://oqmd.org/). Researchers can download these datasets through corresponding API and replace `/data/test.csv`. Moreover, researchers can also replace `/data/test.csv` with their own data to screen personalized dataset.




# DEMO video
![demo](https://github.com/user-attachments/assets/967f84b5-8787-45e8-9064-d66169120fae)

# Research Instruction
## 1. Preparation
    Use pip to install openai, flask, langchain, pymatgen, catboost, matminer, scikit-learn, pandas, numpy
## 2. Trainging Model
    Replace the researchers' dataset with data/train.csv
    execute "python train.py"
## 3. Execute NA framework
    execute "python app.py" 
    Access http://127.0.0.1:5000/ via web browser
    Enter OpenAI API key
    Enter analysis query with natural language 
        (such as: Read material expressions from ./data/predict.csv, then use the model ./model/catboost_model.cbm to predict performance, finally perform rule matching to find elements containing Sc, Y, La, Ce, Pr, Nd, Pm, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, and save the results in ./data/result.csv)
