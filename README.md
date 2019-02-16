# Computer_Vision_Motion_Detection

----- TO DETECT MOTION IN A VIDEO, WE WILL USE THE DIFFERENCE OF TWO VIDEO FRAMES ----- 

1. The video is segmented into frames, (conider each frame as an image)
2. Consider 2 images / frames (A & B) that were taken back-to-back.
3. Convert the image A & B into gray scale. 
4. Compute a difference between these two gray scale images, and assign it to image C.
5. If, significant differece is detected between these two frames, we can conclude that some motion has occoured. 
6. An loop function will thus produce an new C image every time there is a frame change in the video. 

