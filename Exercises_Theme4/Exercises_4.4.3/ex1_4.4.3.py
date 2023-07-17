# Load data of "load_digits" base and inform the amount of data
from sklearn.datasets import load_digits

digits = load_digits()
# There are 1797 images, each one has a dimension 8x8=64
print("Shape of image data: {}".format(digits.data.shape))
# Inform the total labeled data using int from 0 to 9
print("Shape of labeled data: {}".format(digits.target.shape))
