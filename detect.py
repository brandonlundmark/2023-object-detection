import cv2
from ultralytics import YOLO

# Load the YOLO model
model = YOLO('data/YOLOv5sNORO.pt')

# Open video capture
cap = cv2.VideoCapture(0)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv5 tracking on the frame, persisting tracks between frames
        results = model.track(frame, persist=True)

        # Display the annotated frame
        cv2.imshow("YOLO Tracking", results[0].plot())

        ## Object geometry can be accessed like this
        #print(results[0].boxes.xywh.data)

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()