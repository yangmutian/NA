# NZ-A

[![Python Version](https://img.shields.io/badge/python-3.12-orange)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-Apache--2.0-blue)](https://opensource.org/licenses/Apache-2.0)
![Paper](https://img.shields.io/badge/Paper-green)
![Demo](https://img.shields.io/badge/Demo-red)

This repo provides code for NanoZyme-Agent (NZ-A), a framework equipped with LLM-based agents and customized AI toolkits for material research. 

Using NZ-A, researchers successfully identify six unreported rare earth-based peroxidase (POD)-like nanozymes from nearly 600k candidate materials within seconds. 

**Note: The current repo ONLY represents a minimal implementation and will be iteratively refined throughout the peer-review process.**

## :zap: Online Demo

We are developing an ​​online demo​​ for researchers ​​without any programming expertise​​. The current interface is shown below, and the ​​web service​​ will be released during the peer-review process.

https://github.com/user-attachments/assets/079f1dd4-bf7d-4ce0-8ea5-b17a24886967

## :package: Installation

NZ-A is intended to work with Python 3.12. Installation can be done via pip:

```
pip install -r requirements.txt
```

## :books: Dataset

**Train dataset**

This study incoprates [Wei dataset](http://nanozymes.net), [Dizyme dataset](https://dizyme.aicidlab.itmo.ru/), and [Huang dataset](https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.202201736) for model training. Researchers can download these datasets and replace `/data/train.csv`. In addition to open datasets, researchers can also replace `/data/train.csv` with their custom data to train personalized AI models.

**Screen dataset**

The trained model is used to screen the nanozymes in [Materials Project](https://next-gen.materialsproject.org/), [Aflow](https://aflowlib.org/), and [OQMD](https://oqmd.org/). Researchers can download these datasets through corresponding API and replace `/data/test.csv`. Moreover, researchers can also replace `/data/test.csv` with their own data to screen personalized dataset.

## :robot: Training Model
Before execute NZ-A, researchers should train the AI model through the following command:

```
python train.py
```

## :rocket: Launching NZ-A
Researchers should launch NZ-A trhough the folloing command:
```
python app.py
```
Then, NZ-A can be accessed in http://127.0.0.1:5000/ via web browser.

After entering [DeepSeek API key](https://api-docs.deepseek.com/), researchers can perform nanozymes screening through natural language :grin:

## :scroll: Citation
We will update this block after the corresponding manuscript acceptance. 

## :bookmark: License
This project is licensed under the Apache-2.0 License.
