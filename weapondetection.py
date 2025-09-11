import cv2
from ultralytics import YOLO

def main():
    # Load YOLO model (replace with your trained model)
    # Example: model = YOLO("weapon_best.pt")cd C:\Users\hasin\Documents
py "weapon dectection.py"

    model = YOLO("yolov8n.pt")

    # Open webcam (0 = default camera)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Starting weapon detection... Press 'q' to exit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to grab frame.")
            break

        # Run YOLO detection
        results = model(frame)

        # Draw bounding boxes
        annotated_frame = results[0].plot()

        # Show output
        cv2.imshow("Weapon Detection", annotated_frame)

        # Exit on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
