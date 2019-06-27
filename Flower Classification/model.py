import csv
import ntpath
import os
import shutil
import numpy as np
from keras import models
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator



def load_model(src):
    model = models.load_model(src)
    return model


def copy_file(src, des):
    src_files = os.listdir(src)
    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, des)
        elif file_name != 'tmp_test' and os.path.isdir(full_file_name):
            copy_file(full_file_name, des)


def save_to_csv(predictions_list, destination):
    size = len(predictions_list)
    with open(destination + '/flower predictions.csv', 'w+', newline='') as csv_file:
        file_writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_ALL)
        for i in range(0, size):
            file_writer.writerow([predictions_list[i][0], predictions_list[i][1]])


def predict_image(train_model, src):
    model_class = {0: 'daisy', 1: 'dandelion', 2: 'rose', 3: 'sunflower', 4: 'tulip'}
    if os.path.isdir(src+'/tmp_test'):
        shutil.rmtree(src+'/tmp_test')
    os.makedirs(src+'/tmp_test/flowers')
    copy_file(src, src+'/tmp_test/flowers')
    img_size = 128
    batch_size = 20
    test_data_gen = ImageDataGenerator(rescale=1. / 255)
    test_generator = test_data_gen.flow_from_directory(
        directory=src+'/tmp_test',
        target_size=(img_size, img_size),
        color_mode='rgb',
        batch_size=batch_size,
        class_mode=None,
        shuffle=False
    )
    file_names = test_generator.filepaths
    size = len(file_names)
    predicted = train_model.predict_generator(test_generator, verbose=1, steps=size / batch_size)
    predicted_class_indices = np.argmax(predicted, axis=1)
    predictions = [model_class[k] for k in predicted_class_indices]
    predictions_list = []
    for i in range(0, size):
        predictions_list.append([ntpath.basename(file_names[i]), predictions[i]])
    try:
        if os.path.isdir(src+'/tmp_test'):
            shutil.rmtree(src+'/tmp_test')
    except:
        print('bug')
    return predictions_list
