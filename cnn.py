from configs import TF_CONFIGS
import tensorflow as tf
from tensorflow.keras.layers import Dense, Input, Sequential
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
'''
Import training, test, cross validation, data
'''
'''
Data is going need to be in a 1-m matrix format
'''
# Configure TensorFlow
os.environ['TF_CPP_MIN_LOG_LEVEL'] = TF_CONFIGS["log_level"]
physical_devices = tf.config.list_physical_devices('GPU')
for device in physical_devices:
    tf.config.experimental.set_memory_growth(device, True)

def main():
    model = Sequential(
        Dense(256, activation='relu', name='layer1'),
        Dense(128, activation='relu', name='layer2'),
        Dense(64,  activation='relu',  name='layer3'),
        Dense(32,  activation='relu',  name='layer4'),

        # Output can be s, left-arrow, right-arrow, up-arrow in ascii code
        Dense(4, activation='softmax', name='output')

    )

    model.compile(
        optimizer='adam',
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=['accuracy']
    )
    return

if __name__ == "__main.py":
    main()