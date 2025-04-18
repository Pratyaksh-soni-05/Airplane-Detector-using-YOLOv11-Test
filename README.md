# ✈️ Airplane Detector using YOLOv11

This project builds a custom object detector using [YOLOv11 (Ultralytics)](https://github.com/ultralytics/ultralytics) to detect airplanes in aerial imagery. The dataset is custom-labeled, and label files are auto-normalized and cleaned before training.

---

## 📁 Project Structure

Airplane-Detector-using-YOLOv11-Test/ ├── config.yaml # Dataset configuration for YOLO ├── main.py # Combined script to fix labels and train ├── requirements.txt # Python dependencies ├── README.md # Project documentation └── Dataset/ ├── images/ │ └── train/ # Training images └── labels/ └── train/ # YOLO format label files

2. Create and Activate a Virtual Environment
   python -m venv venv
venv\Scripts\activate         # On Windows
# source venv/bin/activate   # On Linux/macOS

3. Install Dependencies
pip install -r requirements.txt


🛠️ Dataset Configuration (config.yaml)
path: C:/OIDv4_ToolKit/OID/Dataset  # Root directory of your dataset
train: images/train/                # Relative path to training images
val: images/train/                  # Relative path to validation images
names:
  0: airplane                       # Label for the class (airplane)

📦 Dependencies (requirements.txt)
ultralytics
pillow

Install the dependencies with:
pip install -r requirements.txt

🏃‍♂️ Running the Script
The train.py script will:

Normalize and clean all YOLO label files

Start training the model using YOLOv11n on your custom dataset

✍️ Author
Pratyaksh Soni
GitHub: @Pratyaksh-soni-05

📄 License
Licensed under the MIT License.

---

This version of the `README.md` is properly structured and formatted for GitHub. It includes the necessary instructions, dataset configuration, and example code for running the project.

