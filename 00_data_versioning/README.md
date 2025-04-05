# 📦 00_data_versioning

This module demonstrates how to perform **data versioning** with DVC. It includes steps to fetch a raw dataset, process it, and store it with full reproducibility using DVC.

---

## 🧩 Steps Overview

1. **Download raw XML file**
2. **Transform XML to CSV**
3. **Track `data.csv` with DVC**
4. **Configure and push to remote (Google Drive)**

---

## 🪄 Step-by-Step

### 1. 📥 Download `data.xml`

```bash
dvc get https://github.com/iterative/dataset-registry get-started/data.xml -o data/data.xml
```

### 2. 🧹 Transform to CSV

```bash
python src/prepare.py
```

### 3. ➕ Track with DVC

```bash
dvc add data/data.csv
git add data/data.csv.dvc data/.gitignore
git commit -m "Track processed data.csv with DVC"
```

### 4. ☁️ Setup and Push to Google Drive

#### Add remote:
```bash
dvc remote add -d myremote gdrive://<your-folder-id>
```

#### Configure service account:
```bash
dvc remote modify myremote gdrive_use_service_account true
dvc remote modify myremote gdrive_service_account_json_file_path .secrets/gdrive_service_account.json
```

#### Push to remote:
```bash
dvc push
```

---

## 🧾 logs.txt (Command Log)

```bash
# Step 1: Download XML
$ dvc get https://github.com/iterative/dataset-registry get-started/data.xml -o data/data.xml

# Step 2: Convert to CSV
$ python src/prepare.py

# Step 3: Track CSV
$ dvc add data/data.csv
$ git add data/data.csv.dvc data/.gitignore
$ git commit -m "Track processed data.csv with DVC"

# Step 4: Set Remote and Push
$ dvc remote add -d myremote gdrive://1JI4acT5z9AFodYdXCrcAvyFpEtGucwoC
$ dvc remote modify myremote gdrive_use_service_account true
$ dvc remote modify myremote gdrive_service_account_json_file_path .secrets/gdrive_service_account.json
$ dvc push
```

---

✅ Done! You're now tracking your dataset like a pro 💪

