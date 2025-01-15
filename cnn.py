from configs import TF_CONFIGS
import tensorflow as tf
from tensorflow.keras.layers import Dense, Input
import numpy as np
'''
Import training, test, cross validation, data
'''

# Configure TensorFlow
os.environ['TF_CPP_MIN_LOG_LEVEL'] = TF_CONFIGS["log_level"]
physical_devices = tf.config.list_physical_devices('GPU')
for device in physical_devices:
    tf.config.experimental.set_memory_growth(device, True)

def main():
    return

if __name__ == "__main.py":
    main()