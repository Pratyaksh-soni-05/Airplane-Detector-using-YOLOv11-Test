from ultralytics import YOLO
import multiprocessing
from multiprocessing import freeze_support

# Function for training
def main():
    # Load a pretrained YOLO11n model
    model = YOLO("yolo11n.pt")

    # Train the model on the dataset
    train_results = model.train(
        data="config.yaml",  # Path to dataset configuration file
        epochs=1,  # Number of training epochs
    )

# Entry point for the script
if __name__ == '__main__':
    # Ensure the proper start method for multiprocessing on Windows
    multiprocessing.set_start_method('spawn')

    # Freeze support is required for multiprocessing on Windows when using PyInstaller (even if you're not freezing)
    freeze_support()  # Add this line for safety

    # Call the main function that does the training
    main()
