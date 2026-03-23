from ultralytics import YOLO

# model = YOLO("yolo11n.pt") # or "yolov8n.pt"
# results = model.train(
# data="/home/ritz/Documents/object_detection/dataset/data.yaml",
# epochs=1,
# imgsz=640,
# batch=16
# )

model = YOLO("yolov8m.pt") # or "yolov8m.pt"

results = model.train(
    data="/home/ritz/Documents/object_detection/dataset/data.yaml",
    epochs=1,
    imgsz=640)