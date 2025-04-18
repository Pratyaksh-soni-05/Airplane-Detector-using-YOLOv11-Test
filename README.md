# ✈️ Airplane Detector using YOLOv11

This project builds a custom object detector using [YOLOv11 (Ultralytics)](https://github.com/ultralytics/ultralytics) to detect airplanes in aerial imagery. The dataset is custom-labeled, and label files are auto-normalized and cleaned before training.

---

## 📁 Project Structure

Airplane-Detector-using-YOLOv11-Test/ ├── config.yaml # Dataset configuration for YOLO ├── main.py # Combined script to fix labels and train ├── requirements.txt # Python dependencies ├── README.md # Project documentation └── Dataset/ ├── images/ │ └── train/ # Training images └── labels/ └── train/ # YOLO format label files

yaml
Copy
Edit


---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Pratyaksh-soni-05/Airplane-Detector-using-YOLOv11-Test.git
cd Airplane-Detector-using-YOLOv11-Test

🔧 Dataset Configuration (config.yaml)
path: C:/OIDv4_ToolKit/OID/Dataset  # root dir
train: images/train/                # relative to 'path'
val: images/train/                  # relative to 'path'
names:
  0: airplane



