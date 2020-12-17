import pygame
import tensorflow as tf
from tensorflow.keras.layers import Dense, Flatten
from PIL import Image
from tensorflow.keras.models import load_model
import numpy as np
import os.path


def create_and_train_new_model(model_file_name):
    mnist = tf.keras.datasets.mnist
    (X_train, y_train), (X_test, y_test) = mnist.load_data()

    # Нормализация данных (делаем length = 1)
    X_train = tf.keras.utils.normalize(X_train, axis=1)
    X_test = tf.keras.utils.normalize(X_test, axis=1)

    # Создание модели нейронной сети
    model = tf.keras.models.Sequential()
    model.add(Flatten())
    model.add(Dense(units=128, activation=tf.nn.relu))
    model.add(Dense(units=128, activation=tf.nn.relu))
    model.add(Dense(units=10, activation=tf.nn.softmax))

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # Тренировка модели
    model.fit(X_train, y_train, epochs=3)

    # Оценка модели
    val_loss, val_acc = model.evaluate(X_test, y_test)
    print(val_loss)
    print(val_acc)

    # Сохранение модели
    model.save(model_file_name)
    return model


def predict_digit(image):
    # Подготовка изображения
    image = image.resize((28, 28))
    image = image.convert('L')
    image = np.array(image)
    image = image.reshape(1, 28, 28, 1)
    image = image / 255.0
    # Распознавание
    res = model.predict([image])[0]
    print("Это цифра {} с вероятностью {}%".format(np.argmax(res), max(res)*100))


def start_user_interface():
    circle_radius = 10
    pygame.init()
    white = pygame.color.Color('White')
    black = pygame.color.Color('Black')
    screen = pygame.display.set_mode((250, 250))
    screen.fill(black)
    is_mouse_button_down = False
    play = True
    pygame.display.update()
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
            # Нажатие на Enter распознает цифру и выводит результаты в консоль
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                pygame.image.save(screen, './image.png')
                image = Image.open('./image.png')
                predict_digit(image)

            # Нажатие на Backspace очищает поле для рисования цифры
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                screen.fill(black)
                pygame.display.update()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                is_mouse_button_down = True
                pos = pygame.mouse.get_pos()
                pygame.draw.circle(screen, white, pos, circle_radius)
                pygame.display.update()

            elif event.type == pygame.MOUSEMOTION and is_mouse_button_down:
                pygame.draw.circle(screen, white, event.pos, circle_radius)
                pygame.display.update()

            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                is_mouse_button_down = False


model_file_name = 'digits.h5'
if os.path.isfile(model_file_name):
    model = load_model(model_file_name)
else:
    model = create_and_train_new_model(model_file_name)
start_user_interface()
