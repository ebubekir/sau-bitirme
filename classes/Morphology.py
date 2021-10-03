import numpy as np
import cv2 as cv


class Morphology:
    kernel = np.ones((5, 5), np.uint8)

    @classmethod
    def erosion(cls, image):
        return cv.erode(image, cls.kernel, iterations=1)

    @classmethod
    def dilation(cls, image):
        return cv.dilate(image, cls.kernel, iterations=1)

    @classmethod
    def opening(cls, image):
        return cv.morphologyEx(image, cv.MORPH_OPEN, cls.kernel)

    @classmethod
    def closing(cls, image):
        return cv.morphologyEx(image, cv.MORPH_CLOSE, cls.kernel)

    @classmethod
    def top_hat(cls, image):
        return cv.morphologyEx(image, cv.MORPH_TOPHAT, cls.kernel)

    @classmethod
    def black_hat(cls, image):
        return cv.morphologyEx(image, cv.MORPH_BLACKHAT, cls.kernel)

