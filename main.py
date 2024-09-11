from model.LLM import LLM
from model.yolo import Yolo
import cv2
import matplotlib.pyplot as plt
from api import flaskapp

flaskapp.run()

# llm = LLM()

# llm.generate("testuser", "hey there!")

# yolo = Yolo()
# image = cv2.imread('test/img1.jpg')
# preds = yolo.predict()


# for i in range(len(preds)):
#     pred = preds[i]
#     image, x1, y1, x2, y2, label, confidence = pred['image'], pred['x1'], pred['y1'], pred['x2'], pred['y2'], pred['label'], pred['confidence']
#     cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
#     cv2.putText(image, f"{label} {confidence:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# plt.imshow(image)
# plt.show()

# while (True):
#     inp = str(input("> "))
#     out = llm.generate("testuser", inp)
#     print(out)
    
