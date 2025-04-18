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
2. Create and Activate a Virtual Environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate         # On Windows
# source venv/bin/activate   # On Linux/macOS
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
🛠️ Dataset Configuration (config.yaml)
The config.yaml file should contain the following dataset configuration for YOLO:

yaml
Copy
Edit
path: C:/OIDv4_ToolKit/OID/Dataset  # Root directory of your dataset
train: images/train/                # Relative path to training images
val: images/train/                  # Relative path to validation images
names:
  0: airplane                       # Label for the class (airplane)
📦 Dependencies (requirements.txt)
nginx
Copy
Edit
ultralytics
pillow
Install the dependencies with:

bash
Copy
Edit
pip install -r requirements.txt
🏃‍♂️ Running the Script
The main.py script will:
Normalize and clean all YOLO label files

Start training the model using YOLOv11n on your custom dataset

Run the script with:

bash
Copy
Edit
python main.py
Example Training Code in main.py:
python
Copy
Edit
from ultralytics import YOLO

# Load a pretrained YOLOv11n model
model = YOLO("yolo11n.pt")

# Train the model on the custom dataset for 100 epochs
train_results = model.train(
    data="config.yaml",  # Path to dataset configuration file
    epochs=1,            # Number of training epochs
)
🔄 Git Commands for Pushing to GitHub
If you'd like to push the changes to GitHub, follow these steps:

1. Initialize the Local Git Repository
bash
Copy
Edit
git init
2. Add the Remote Repository
bash
Copy
Edit
git remote add origin https://github.com/Pratyaksh-soni-05/Airplane-Detector-using-YOLOv11-Test.git
3. Add All Files to the Staging Area
bash
Copy
Edit
git add .
4. Commit Your Changes
bash
Copy
Edit
git commit -m "Initial commit"
5. Pull the Latest Changes from GitHub (if there are any)
bash
Copy
Edit
git pull origin main --rebase
6. Push Your Changes to the Remote Repository
bash
Copy
Edit
git push -u origin main
✍️ Author
Pratyaksh Soni
GitHub: @Pratyaksh-soni-05

📄 License
Licensed under the MIT License.

yaml
Copy
Edit

---

This version of the `README.md` is formatted properly for clarity and ease of use. It explains all the steps needed t
