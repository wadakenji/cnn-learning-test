import numpy as np
import _pickle,random

# ファイルを読み込む
# cf. https://qiita.com/lumbermill/items/010920d264806b903e5f
def unpickle(file):
    fo = open(file, 'rb')
    dict = _pickle.load(fo, encoding='latin-1')
    fo.close()
    return dict

# 長さ1024の配列の配列
# ↓
# 長さ(32,32,3)の3次元配列の配列
def vectors_to_images(vector_arr):
    image_data_arr = []

    for index, vector in enumerate(vector_arr):
        if index % 3 != 0 : continue
        r = vector_arr[index]
        g = vector_arr[index+1]
        b = vector_arr[index+2]
        data = np.array([r,g,b]).T.reshape(32,32,3)
        image_data_arr.append(data)

    return image_data_arr

# データセットのファイルを画像データとラベルにフォーマット
def get_images_and_labels(filename):
    file_data = unpickle(filename)
    labels = file_data['labels']
    vectors = file_data['data']
    images = vectors_to_images(vectors)
    return [images, labels]

images_1, labels_1 = get_images_and_labels('src/data/cucumber-9-python/data_batch_1')
images_2, labels_2 = get_images_and_labels('src/data/cucumber-9-python/data_batch_2')
images_3, labels_3 = get_images_and_labels('src/data/cucumber-9-python/data_batch_3')
images_4, labels_4 = get_images_and_labels('src/data/cucumber-9-python/data_batch_4')
images_5, labels_5 = get_images_and_labels('src/data/cucumber-9-python/data_batch_5')
images_train = np.array(images_1 + images_2 + images_3 + images_4 + images_5)
labels_train = np.array(labels_1 + labels_2 + labels_3 + labels_4 + labels_5)

images_test, labels_test = get_images_and_labels('src/data/cucumber-9-python/data_batch_5')
images_test = np.array(images_test)
labels_test = np.array(labels_test)