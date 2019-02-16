import cv2

# Read the video file / source
cap = cv2.VideoCapture(0)

# Capture the 1st & 2nd frames and store them in resp. variables:
ret1, frame1 = cap.read()
ret2, frame2 = cap.read()

# Loop the capture of frames:
while True:
    # Convert the frame1 & frame2 into gray scale to calculate differences:
    frame1_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    frame2_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    # Apply the Gaussian blur onto the gray scale frames
    # Kernel size is 21*21 which applies a stronger level of blurring:
    frame1_blur = cv2.GaussianBlur(frame1_gray, (21, 21), 0)
    frame2_blur = cv2.GaussianBlur(frame2_gray, (21, 21), 0)

    # Calculate the difference between the two frames:
    frames_diff = cv2.absdiff(frame1_blur, frame2_blur)

    # Display the difference in an open window:
    cv2.imshow("Motion Captured:", frames_diff)

    # Repeat the same for the upcoming frames in the video:
    frame1 = frame2
    ret, frame2 = cap.read()

    if not ret:
        break
    k = cv2.waitKey(10)
    if k == ord('q'):
        break

cv2.destroyAllWindows()
