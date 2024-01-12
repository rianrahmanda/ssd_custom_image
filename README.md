# ssd_custom_image
SSD Implementation

Tahapan deployment

1. Install anaconda
2. buka anaconda prompt, buat folder yang disini kita sebut 'tflite1' di direktori yang diingikan.
contoh:
```
mkdir D:\tflite1
cd D:\tflite1
```
3. buat virtual environment Python 3.9 menggunakan script berikut ini:
```
conda create --name tflite1-env python=3.9
```

setelah virtual environment dibuat, jalankan kode berikut ini:

```
conda activate tflite1-env
pip install tensorflow opencv-python protobuf==3.20.*
```

4. copy file custom_model_lite.zip yang sudah dilatih sebelumnya ke dalam folder 'tflite1', kemudian ekstraksi file zip nya.

5. jalankan perintah berikut ini untuk mendownload script deployment
```
curl https://raw.githubusercontent.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi/master/TFLite_detection_webcam.py --output TFLite_detection_webcam.py
```

6. Jalankan perintah ```python TFLite_detection_webcam.py --modeldir=custom_model_lite``` untuk menjalankan kode yang dibuat
