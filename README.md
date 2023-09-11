# Video-Anomoly-Detection
Identifying anomalies through video frames. Done by using a convolutional neural network.

The goal of this task was to implement an autoencoder for anomaly detection (aka outlier detection). Anomaly detection is the identification of rare items, events or observations which deviate significantly from the majority of the data and do not conform to a well defined notion of normal behaviour. Anomaly detection have applications in many domains including cyber security, medicine, machine vision, statistics, neuroscience, law enforcement and financial fraud.

We use a short video to detect frames where something unusual happens. The video is from the Anomalous Behavior Data Set, compiled by Andrei Zaharescu and Richard P. Wildes at the Vision Lab at York University.

The individual video frames are extracted from the video and stored as JPEG images. Then, the images can be loaded into a Numpy array and used to train the model.
