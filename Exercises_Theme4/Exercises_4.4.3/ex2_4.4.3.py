# Visualize the loaded data
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

digits = load_digits()
# There are 1797 images, each one has a dimension 8x8=64
print("Shape of image data: {}".format(digits.data.shape))
# Inform the total labeled data using int from 0 to 9
print("Shape of labeled data: {}".format(digits.target.shape))

plt.figure(figsize=(14,4))
for index, (image, label) in enumerate(zip(digits.data[0:5], digits.target[0:5])):
    plt.subplot(1, 5, index+1)
    plt.imshow(np.reshape(image, (8,8)),cmap=plt.cm.gray)
    plt.title('Training: {}\n'.format(label, fontsize=15))
