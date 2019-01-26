from PIL import Image
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data


mnist = input_data.read_data_sets("./data/", one_hot=True)
temp = mnist.train.images[0]
temp = np.reshape(temp, (28, 28))
temp = temp*255
im = Image.fromarray(temp).convert('L')
im.show()
