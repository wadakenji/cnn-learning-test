from data.get_data import images_test, labels_test
from PIL import Image

if __name__ == "__main__":
    for index, array in enumerate(images_test):
        pil_image = Image.fromarray(array)
        pil_image.save(f'src/data/cucumber-9-python/images/{index}-{labels_test[index]}.png')
