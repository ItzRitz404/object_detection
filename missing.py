from pathlib import Path

base = Path("/home/ritz/Documents/object_detection/dataset")

for split in ["train", "val"]:
    imgs = {p.stem for p in (base / "images" / split).iterdir() if p.is_file()}
    lbls = {p.stem for p in (base / "labels" / split).iterdir() if p.is_file()}

    print(f"\n{split.upper()}")
    print("images:", len(imgs))
    print("labels:", len(lbls))
    print("images without labels:", len(imgs - lbls))
    print("labels without images:", len(lbls - imgs))
    print("sample missing labels:", list(sorted(imgs - lbls))[:10])
    print("sample missing images:", list(sorted(lbls - imgs))[:10])