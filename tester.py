from ultralytics import YOLO

model = YOLO("best.pt") # or "yolov8n.pt"

results = model.predict("/home/ritz/Documents/object_detection/dataset/images/train/K6Jgf01G1Tk9hULexw4iWw.jpg")

print(results)

