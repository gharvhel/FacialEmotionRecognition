import cv2
import numpy as np


class Image:
    def __init__(self, pixels):
        self.image = np.fromstring(pixels, dtype=np.uint8, sep=' ').reshape((48, 48, 1))

    def __str__(self):
        return ' '.join(map(str, self.image.flatten().tolist()))

    def show(self):
        cv2.imshow('image', self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
