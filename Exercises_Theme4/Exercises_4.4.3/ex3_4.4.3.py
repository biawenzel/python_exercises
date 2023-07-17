# Use a logistic regression model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
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

x_training, x_test, y_training, y_test = train_test_split(digits.data, digits.target, test_size=0.25, random_state=0)
pipe = make_pipeline(StandardScaler(), LogisticRegression())
pipe.fit(x_training, y_training)
