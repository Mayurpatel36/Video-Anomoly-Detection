import numpy as np
import cv2
from tensorflow.keras.models import load_model
import os
from PIL import Image


def predict(frame):
    images = []
    im = Image.open(frame)
    # resize the image to im_width and im_height.
    im_array = np.array(im.resize((60, 44)))
    # Convert uint8 to decimal and normalize to 0 - 1.
    images.append(im_array.astype(np.float32) / 255.)
    # Close the PIL image once converted and stored.
    im.close()
    # Flatten the images to a single vector
    X = np.array(images).reshape(-1, np.prod(images[0].shape))
    frame_reshaped = np.array(images)

    # Make a prediction using the autoencoder
    reconstructed_frame = model.predict(frame_reshaped)

    # Calculate the prediction loss for the frame
    prediction_loss = np.mean(
        np.abs(reconstructed_frame - frame_reshaped), axis=(1, 2, 3))

    # Set a threshold
    threshold = 0.032

    if prediction_loss > threshold:
        anomaly = True
    elif prediction_loss < threshold:
        anomaly = False
    # Return True if the frame is anomalous (prediction loss exceeds the threshold), False otherwise
    print(anomaly)
    return anomaly


### For instructor ###
# Change this to local directory where the model as well as the py file is stored
os.chdir('/Users/mayurpatel/Desktop/MMAI5500')

model = load_model('A3_model')

# Replace the frame with the one to test
frame = 'frame0789.jpg'
predict(frame)
