## Install Python-Opencv

### Prerequisites
- numpy
- matplotlib

### About OpenCV

OpenCV (Open Source Computer Vision Library) is an open source computer vision and machine learning software library. OpenCV was built to provide a common infrastructure for computer vision applications and to accelerate the use of machine perception in the commercial products. Being a BSD-licensed product, OpenCV makes it easy for businesses to utilize and modify the code.
(https://opencv.org/about)

### For Windows
```
python -m pip install --upgrade pip
pip install matplotlib
pip install opencv-python
```

### For Linux

```
sudo apt update
sudo apt install python3-opencv
```
#### Check
```
python3
```
Output
```
Python 3.6.9 (default, Nov  7 2019, 10:44:02) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```
Input again
```
>>> import cv2
>>> cv2.__version__
```

Output
```
'3.2.0'
```
*note : example version of opencv

### For Mac


### Example Image

![idn1](https://user-images.githubusercontent.com/49097125/71385188-c3ba7b80-25dd-11ea-8378-7af40400a8c7.png)

### Resources
- Homepage: http://opencv.org
- Docs: http://docs.opencv.org/master/
- Q&A forum: http://answers.opencv.org
- Issue tracking: https://github.com/opencv/opencv/issues
