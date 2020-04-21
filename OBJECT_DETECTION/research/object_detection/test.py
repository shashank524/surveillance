import object_detection_api
import os
from PIL import Image

# If you want to test the code with your images, just add path to the images to the TEST_IMAGE_PATHS.
PATH_TO_TEST_IMAGES_DIR = 'C:/tensorflow1/models/research/object_detection/test_images' #cwh
TEST_IMAGE_PATHS = [ os.path.join(PATH_TO_TEST_IMAGES_DIR, 'image{}.jpg'.format(i)) for i in range(1, 3) ]

# for image_path in TEST_IMAGE_PATHS:
#     image = Image.open(image_path)
#     response = object_detection_api.get_objects(image)
#     print("returned JSON: \n%s" % response)

image = Image.open('C:/tensorflow1/models/research/object_detection/test_images/image.jpg')
response = object_detection_api.get_objects(image)
print("returned JSON: \n%s" % response)
