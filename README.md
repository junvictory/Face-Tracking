# Face-Tracking
실시간으로 Face를 검출하여 검출된 Face를 트랙킹하여 Arduino 와 Serial 통신을 이용해 Arduino를 컨트롤 한다

<br>

## 목표
Face를 정확히 검출하고 트랙킹이 정상적으로 이루어 지며 Serial 통신을 통하여 Arduino를 정확히 컨트롤 하자

<br>

## 구현
- **Face Detection**
  - Haar Cascade
- **Face Tracking**
  - KCF (Kernelized Correlation Filters)
- **Serial**

<br> 

## 구현 방법
- **Face Detection**
  - haarcascade_frontalface_alt를 이용하여 얼굴을 먼저 검출
- **Face Tracking**
  - haar를 이용하여 검출된 ROI(Region of Interest)를 KCF(Kernelized Correlation Filters)를 이용하여 실시간으로 Tracking 시킨다
- **Serial**
  - Serial 라이브러리를 이용하여 Port를 지정하여 통신
<br>

## 기술 스택
- Python 3.7.3
- OpenCV 4.0

