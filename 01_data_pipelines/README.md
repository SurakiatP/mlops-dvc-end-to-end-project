# 🔄 01_data_pipelines

This folder defines a **reproducible machine learning pipeline** using [DVC (Data Version Control)](https://dvc.org/). The pipeline automates each step from raw data preparation to model evaluation.

---

## 🌐 Overview

```
dvc-mlops-project/
└──01_data_pipelines/
   ├── dvc.yaml             # DVC pipeline stages
   ├── dvc.lock             # Auto-generated lockfile
   └── README.md            # This file
```

---

## 🔢 Pipeline Stages

### 1. `prepare`
**Converts `data/data.xml` to a cleaned CSV format.**
```bash
dvc stage add -n prepare \
  -d ../src/prepare.py -d ../data/data.xml \
  -o ../data/data.csv \
  python ../src/prepare.py ../data/data.xml ../data/data.csv
```

### 2. `featurize`
**Transforms raw CSV into ML-friendly features (e.g. TF-IDF from `Title`, `Body`, `Tags`).**
```bash
dvc stage add -n featurize \
  -d ../src/featurize.py -d ../data/data.csv \
  -o ../data/features.csv \
  python ../src/featurize.py ../data/data.csv ../data/features.csv
```

### 3. `train`
**Trains a regression model using the features.**
```bash
dvc stage add -n train \
  -d ../src/train.py -d ../data/features.csv \
  -o ../models/model.pkl \
  python ../src/train.py ../data/features.csv ../models/model.pkl
```

### 4. `evaluate`
**Evaluates model performance and writes metrics.**
```bash
dvc stage add -n evaluate \
  -d ../src/evaluate.py -d ../models/model.pkl -d ../data/features.csv \
  -o ../results/metrics.json \
  python ../src/evaluate.py ../models/model.pkl ../data/features.csv ../results/metrics.json
```

---

## 📊 DAG Graph

You can visualize your pipeline with:
```bash
dvc dag
```
```
         +---------+      
         | prepare |
         +---------+
              *
              *
              *
        +-----------+
        | featurize |
        +-----------+
         **        **
       **            *
      *               **
+-------+               *
| train |             **
+-------+            *
         **        **
           **    **
             *  *
        +----------+
        | evaluate |
        +----------+
```

---

## ⚡ Reproducing the Pipeline

To rerun the full pipeline:
```bash
dvc repro
```
Or run a specific stage:
```bash
dvc repro featurize
```

---

## 📄 Outputs
| Stage     | Output File                                | Description               |
|-----------|--------------------------------------------|---------------------------|
| prepare   | `../data/data.csv`                         | Cleaned CSV file          |
| featurize | `../data/features.csv`                     | Feature matrix            |
| train     | `../models/model.pkl`                      | Trained model artifact    |
| evaluate  | `../02_experiment_tracking/metrics.json`   | Evaluation metrics (JSON) |

---

## 📃 Notes
- This pipeline follows **modular MLOps principles**.
- Each stage is reproducible and can be tracked via Git + DVC.
- Customize `params.yaml` for hyperparameters.
- Logs are automatically generated into `dvc.lock`.

---

## 🌐 Resources
- [DVC Pipelines](https://dvc.org/doc/start/data-pipelines)
- [DVC Repro](https://dvc.org/doc/command-reference/repro)
- [Scikit-learn](https://scikit-learn.org/)

