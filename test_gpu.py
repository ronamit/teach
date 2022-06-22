# from tensorflow.python.client import device_lib
# print(device_lib.list_local_devices())
import tensorflow as tf
import os

print(3333)
print('LD_LIBRARY_PATH == ', os.environ.get("LD_LIBRARY_PATH"))

print(tf.config.list_physical_devices('GPU'))