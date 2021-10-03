import cv2 as cv


class Image:
    def __init__(self, path):
        self.path = path
        self.img = cv.imread(path, cv.IMREAD_UNCHANGED)

    @property
    def __image_format(self):
        return self.path.split('.')[-1]

    def change_image_size(self, width, height):
        resized_image = cv.resize(self.img, (width, height), interpolation=cv.INTER_AREA)
        new_image_path = self.path.replace(f".{self.__image_format}",
                                           f"_{width}_{height}.{self.__image_format}")
        cv.imwrite(new_image_path, resized_image)
        print(f"The image has been saved in the {new_image_path} directory.")
