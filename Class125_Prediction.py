
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import  accuracy_score
from PIL import Image
import PIL.ImageOps 


X,y = fetch_openml("mnist_784",version=1,return_X_y=True)
X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=9, train_size=7500,test_size=2500)
X_train_scaled= X_train/255.0
X_test_scaled = X_test/255.0

clf = LogisticRegression(solver='saga',multi_class='multinomial').fit(X_train_scaled,y_train)


def get_prediction(img):
    im_pil = Image.open(img)
    img_bw = im_pil.convert("L")
    img_bw_resized = img_bw.resize((28,28),Image.ANTIALIAS)
    pixel_filter = 20
    min_pixel = np.percentile(img_bw_resized,pixel_filter)
    img_bw_resized_inverted = PIL.ImageOps.invert(img_bw_resized)
    img_bw_resized_inverted_scaled = np.clip(img_bw_resized-min_pixel,0,255)
    max_pixel = np.max(img_bw_resized)
    img_bw_resized_inverted_scale= np.asarray(img_bw_resized_inverted_scaled)/max_pixel
    test_sample = np.array(img_bw_resized_inverted_scaled).reshape(1,784)
    test_pred = clf.predict(test_sample)
    return test_pred[0]

print("Completed")



