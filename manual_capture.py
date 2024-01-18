import cv2
import os
import time
import uuid

IMAGES_PATH = 'collectedimages'

# Membuat direktori 'collectedimages' jika belum ada
if not os.path.exists(IMAGES_PATH):
    os.mkdir(IMAGES_PATH)

labels = ['hello', 'thanks', 'yes', 'no', 'iloveyou']
number_imgs = 15
label_index = 0

# Inisialisasi penghitung gambar
img_counter = {label: 0 for label in labels}

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)

    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break
    elif key & 0xFF == ord('s'):
        if not os.path.exists(os.path.join(IMAGES_PATH, labels[label_index])):
            os.mkdir(os.path.join(IMAGES_PATH, labels[label_index]))
        imgname = os.path.join(IMAGES_PATH, labels[label_index], labels[label_index]+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imgname, frame)
        img_counter[labels[label_index]] += 1
        print('Image captured for label {}. Total images for this label: {}'.format(labels[label_index], img_counter[labels[label_index]]))
    elif key & 0xFF == ord('l'):
        label_index += 1
        if label_index >= len(labels):
            print('All labels have been captured. Press \'q\' to quit.')
        else:
            print('Switched to next label: {}'.format(labels[label_index]))
        time.sleep(2)

cap.release()
cv2.destroyAllWindows()
