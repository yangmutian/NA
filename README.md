# NZ-A

[![Python Version](https://img.shields.io/badge/python-3.12-orange)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-Apache--2.0-blue)](https://opensource.org/licenses/Apache-2.0)
![Paper](https://img.shields.io/badge/Paper-green)
![Demo](https://img.shields.io/badge/Demo-red)

This repo provides code for NZ-A, a framework for the material research equipped with LLM-based agents and customized AI toolkits. Using NZ-A, researchers without programming expertise successfully identify six unreported rare earth-based peroxidase (POD)-like nanozymes from nearly 600k candidate materials within seconds. 

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
