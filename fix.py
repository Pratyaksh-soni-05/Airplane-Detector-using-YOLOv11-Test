from pathlib import Path
from PIL import Image

# Paths
label_dir = Path(r"C:\OIDv4_ToolKit\OID\Dataset\labels\train")
image_dir = Path(r"C:\OIDv4_ToolKit\OID\Dataset\images\train")

# Map class names to numeric IDs
class_map = {
    "Airplane": 0,
    "airplane": 0
}

for label_file in label_dir.glob("*.txt"):
    image_file = image_dir / (label_file.stem + ".jpg")
    if not image_file.exists():
        print(f"❌ Image missing for {label_file}")
        continue

    try:
        with Image.open(image_file) as img:
            w, h = img.size
    except Exception as e:
        print(f"❌ Could not open image {image_file}: {e}")
        continue

    new_lines = []

    with open(label_file, "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) < 5:
                continue  # Skip empty or invalid lines

            try:
                class_raw = parts[0]
                cls = class_map.get(class_raw, int(class_raw))

                coords = list(map(float, parts[1:]))

                if len(coords) % 4 != 0:
                    print(f"⚠️ Skipping malformed line in {label_file}: {line}")
                    continue

                for i in range(0, len(coords), 4):
                    x1, y1, x2, y2 = coords[i:i+4]

                    x_center = (x1 + x2) / 2 / w
                    y_center = (y1 + y2) / 2 / h
                    bw = (x2 - x1) / w
                    bh = (y2 - y1) / h

                    if not all(0 <= v <= 1 for v in [x_center, y_center, bw, bh]):
                        print(f"⚠️ Out-of-bounds box in {label_file}: {[x1, y1, x2, y2]}")
                        continue

                    new_line = f"{cls} {x_center:.6f} {y_center:.6f} {bw:.6f} {bh:.6f}"
                    new_lines.append(new_line)

            except Exception as e:
                print(f"❌ Error parsing {label_file}: {e}")

    # Save corrected label
    with open(label_file, "w") as f:
        for line in new_lines:
            f.write(line + "\n")

    if not new_lines:
        print(f"⚠️ All labels removed from {label_file}, possibly invalid.")
