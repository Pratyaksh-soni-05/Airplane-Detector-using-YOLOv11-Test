import os

# Function to normalize the bounding boxes and fix the label format
def fix_labels(image_dir, label_dir):
    # Iterate over all label files in the label directory
    for label_file in os.listdir(label_dir):
        label_path = os.path.join(label_dir, label_file)

        if label_file.endswith('.txt'):
            with open(label_path, 'r') as f:
                lines = f.readlines()

            # Read the associated image to get its width and height
            image_path = os.path.join(image_dir, label_file.replace('.txt', '.jpg'))
            if not os.path.exists(image_path):
                continue  # Skip if corresponding image is not found

            from PIL import Image
            img = Image.open(image_path)
            img_width, img_height = img.size  # Image dimensions (width, height)

            new_lines = []
            for line in lines:
                parts = line.strip().split()

                # If there are incorrect parts, skip this line
                if len(parts) != 5:
                    print(f"Skipping invalid line in {label_file}: {line}")
                    continue

                # Extract original values
                class_id = int(parts[0])
                min_x = float(parts[1])
                min_y = float(parts[2])
                max_x = float(parts[3])
                max_y = float(parts[4])

                # Normalize the bounding box coordinates
                x_center = (min_x + max_x) / 2 / img_width
                y_center = (min_y + max_y) / 2 / img_height
                width = (max_x - min_x) / img_width
                height = (max_y - min_y) / img_height

                # Ensure the values are within bounds (0-1)
                x_center = max(0, min(x_center, 1))
                y_center = max(0, min(y_center, 1))
                width = max(0, min(width, 1))
                height = max(0, min(height, 1))

                # Write the fixed line
                new_lines.append(f"{class_id} {x_center} {y_center} {width} {height}\n")

            # Save the fixed labels back to the label file
            with open(label_path, 'w') as f:
                f.writelines(new_lines)
            print(f"Fixed labels for {label_file}")

# Specify your image and label directories
image_dir = "C:/OIDv4_ToolKit/OID/Dataset/images/train"  # Path to image directory
label_dir = "C:/OIDv4_ToolKit/OID/Dataset/labels/train"  # Path to label directory

# Run the fix function
fix_labels(image_dir, label_dir)
