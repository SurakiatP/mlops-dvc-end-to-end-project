# 🧪  02_experiment_tracking

This directory (`02_experiment_tracking`) contains metrics, plots, and reports generated during model training and evaluation. It's designed to track the results of experiments systematically using DVCLive integrated with DVC.

---

## 📁 Directory Structure

```
02_experiment_tracking/
├── metrics/
│   └── metrics.json                 # JSON metrics from model evaluation
├── plots/
│   ├── metrics/                     # Auto-generated metrics (.tsv files)
│   │   ├── eval_accuracy.tsv
│   │   ├── eval_precision.tsv
│   │   ├── eval_recall.tsv
│   │   └── eval_f1.tsv
│   └── images/                      # All generated plot images
│       ├── confusion_matrix.png
│       ├── eval_accuracy.png
│       ├── eval_precision.png
│       ├── eval_recall.png
│       └── eval_f1.png
├── reports/
│   └── report.md                    # Markdown summary report
└── README.md                        # This file
```

---

## 🛠️ How to Generate Experiment Results

### 1.Run experiments from the `01_data_pipelines` directory

```bash
cd ../01_data_pipelines
dvc repro
```

### 2.Check the outputs in this folder (`02_experiment_tracking`)

- Metrics: `metrics/metrics.json`
- Plots: `plots/images/*.png` and `plots/metrics/*.tsv`
- Experiment summary: `report.md`
---

## 📊 Metrics Tracked

The default metrics tracked include:

- Accuracy
- Precision
- Recall
- F1 Score

Additional metrics can be easily added or customized in the `train.py` and `evaluate.py` scripts under `src/`.

---

## 🔄 Comparing Experiments with DVC

To quickly compare multiple experiments, run

```bash
dvc metrics diff
```
Or visualize changes over time with

```bash
dvc plots diff
```
---
## 🚨 Troubleshooting

- Missing results or plots?
  Run `dvc repro --force` from `01_data_pipelines` to regenerate outputs.

- Incorrect folder structure?
  Ensure paths in `train.py`, `evaluate.py`, and `dvc.yaml` match the structure above.

