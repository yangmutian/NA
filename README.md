# A framework for analyzing material properties using LLM-based agents and material science tools.

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
