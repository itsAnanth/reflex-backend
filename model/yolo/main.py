from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt


class Yolo:
    
    def __init__(self):
        self.confidenceThreshold = 0.5
        self.model = YOLO('yolov8n.pt')
        
        
    def predict(self, image):
        results = self.model.predict(source=image, show=False, save=False)
        confidence_threshold = 0.5  # Set your desired confidence threshold
        # Draw bounding boxes and labels on the image
        predictions = []
        for result in results:
            for box in result.boxes:
                confidence = box.conf[0].item()  # Confidence score
                if confidence < confidence_threshold:
                    continue  # Skip detections with low confidence

                # Get bounding box coordinates
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                class_id = int(box.cls[0].item())  # Class ID

                # Load label
                label = self.model.names[class_id]

                predictions.append({
                    'label': label,
                    'confidence': confidence,
                    'x1': x1,
                    'y1': y1,
                    'x2': x2,
                    'y2': y2
                })
        # print(predictions)
        
        return predictions



# # Load a pretrained ResNet model
# model = YOLO("yolov8l.pt")




# # Convert image from BGR (OpenCV format) to RGB (matplotlib format)
# # image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# # Perform object detection
# image = cv2.imread('objectClassification\\test\\elephant.jpg')

# results = model.predict(source=image, show=False, save=False)

# # Confidence threshold
# confidence_threshold = 0.5  # Set your desired confidence threshold
# predictions = []
# # Draw bounding boxes and labels on the image
# for result in results:
#     for box in result.boxes:
#         confidence = box.conf[0].item()  # Confidence score
#         if confidence < confidence_threshold:
#             continue  # Skip detections with low confidence

#         # Get bounding box coordinates
#         x1, y1, x2, y2 = map(int, box.xyxy[0])
#         class_id = int(box.cls[0].item())  # Class ID

#         # Load label
#         label = model.names[class_id]

#         predictions.append({
#             'label': label,
#             'confidence': confidence
#         })
#         # Draw bounding box and label on the image
#         cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
#         cv2.putText(image, f"{label} {confidence:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# # Display the image using matplotlib
# plt.imshow(image)
# print(predictions)
# plt.axis('off')  # Turn off axis numbers and ticks
# plt.show()