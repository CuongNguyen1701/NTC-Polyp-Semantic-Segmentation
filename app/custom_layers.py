import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras.layers import Conv2D, Dropout, BatchNormalization, Conv2DTranspose, Concatenate, LeakyReLU, ReLU
#some blocks of layers for the network
class ConvBlock(layers.Layer):
        def __init__(self, filters, kernel_size, strides=1, padding='same', drop_out_rate=0.1, pool=False):
            super().__init__()
            
            self.conv = Conv2D(filters=filters, kernel_size=kernel_size, strides=strides, padding=padding, kernel_initializer='he_normal')
            self.dropout = Dropout(drop_out_rate)
            self.norm = BatchNormalization()
            self.relu = LeakyReLU(0.1)

        def call(self, x):
            x = self.conv(x)
            x = self.norm(x)
            x = self.relu(x)
            x = self.dropout(x)
            return x
        

class UpConvBlock(layers.Layer):
    def __init__(self, filters, kernel_size, strides=2, padding='same', drop_out_rate=0.1):
            super().__init__()
#             self.concat_layer = concat_layer
            self.tconv = Conv2DTranspose(filters=filters, kernel_size=kernel_size, strides=strides, padding=padding)
            self.dropout = Dropout(drop_out_rate)
            self.norm = BatchNormalization()
            self.relu = ReLU()
            self.concat = Concatenate(axis=3)
    def call(self, x, y=None):
            x = self.tconv(x)
            if y != None:
                x = self.concat([x, y])
            x = self.norm(x)
            x = self.relu(x)
            x = self.dropout(x)
            return x  