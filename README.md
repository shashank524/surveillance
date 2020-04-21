# Getting Started
install the requirements by running the following command
```
pip install -r requirements.txt
```

# Running the abnormal event detection algorithm

go to the Abnormal_Event_Detection folder and run the following commands

* To run inference on a video
```
python video_inference.py video-name
```
example
```
python video_inference.py Abuse.mp4
```

* To run inference on a live stream
```
python start_live_feed.py
```


# Running the object detection algorithm

To run the object detection algorithm, first set the path variable. To do so run the following command 
first make sure that you are in the research folder. 
```
cd OBJECT_DETECTION\research\
```
Then run...

* if you are on mac/linux then run the following command(in the research folder)
```
export PYTHONPATH=$PYTHONPATH:pwd:pwd/slim
```
* if you are on windows run the following commands(in the research folder)
```
set PYTHONPATH=%cd%;%cd%\slim

set PATH=%PATH%;PYTHONPATH
```

Now to run inference first go to the 'object_detection' folder and run the following commands
```
cd OBJECT_DETECTION\research\object_detection
```
To use the SSD model (RECOMMENDED)

* on the test video
```
python object_detection_video.py
```

* on live feed
```
python object_detection_webcam.py
```

* on an image
```
python object_detection_image.py
```
IT IS RECOMMENDED TO RUN THIS FILE USING IDLE OR ANOTHER IDE

To use the RCNN model

* on the test video
```
python object_detection_video_rcnn.py
```

* on live feed
```
python object_detection_webcam_rcnn.py
```

* on an image
```
python object_detection_image_rcnn.py
```
IT IS RECOMMENDED TO RUN THIS FILE USING IDLE OR ANOTHER IDE

