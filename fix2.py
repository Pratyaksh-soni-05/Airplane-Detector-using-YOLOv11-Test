from pathlib import Path

label_dir = Path(r"C:\OIDv4_ToolKit\OID\Dataset\labels\train")

for file in label_dir.glob("*.txt"):
    try:
        lines = file.read_text().strip().splitlines()
        if not lines or all(line.strip() == "" for line in lines):
            print(f"🗑 Deleting empty label file: {file.name}")
            file.unlink()
    except Exception as e:
        print(f"⚠️ Error reading {file.name}: {e}")
