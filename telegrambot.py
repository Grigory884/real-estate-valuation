import numpy as np
import pandas as pd
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from flask import Flask, request, jsonify

# Инициализация токена бота
TOKEN = '6374538466:AAEdhZ7gnNfBoPPjIffDk9QD7QqAGt7253c'

# Инициализация бота
bot = telegram.Bot(token=TOKEN)

# Функция для обработки команды /start
def start(update, context):
    update.message.reply_text('Здравствуйте! Я бот для оценки стоимости недвижимости. Отправь мне данные об общей площади, количестве комнат, районе и площади кухни, и я предскажу стоимость недвижимости.')

# Функция для обработки текстовых сообщений
def echo(update, context):
    try:
        text = update.message.text
        if 'площадь' in text and 'комнат' in text and 'район' in text  and 'площадь кухни' in text:
          total_area = float(text.split('площадь')[1].split('комнат')[0])
          num_room = int(text.split('комнат')[1].split('район')[0])
          sub_area = float(text.split('район')[1])
          kitch_sq = int(text.split('район')[1].split('площадь кухни')[0])
          predicted_price = predict_house_price(total_area, num_room, sub_area, kitch_sq)
          update.message.reply_text(f'Предполагаемая стоимость недвижимости: {predicted_price}')
        else:
            update.message.reply_text('Пожалуйста, отправьте данные об общей площади, количестве комнат, районе и площади кухни.')
    except Exception as e:
        update.message.reply_text('Произошла ошибка при обработке вашего запроса.')

# Загрузка данных
data = pd.read_csv('train.csv')
data = pd.read_csv('macro.csv')

# Подготовка данных
X = data[['площадь', 'количество_комнат', 'район', 'площадь_кухни']]
y = data['стоимость']

# Разделение данных на обучающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Создание и обучение модели
model = LinearRegression()
model.fit(X_train, y_train)

# Предсказание стоимости недвижимости
y_pred = model.predict(X_test)

# Оценка качества модели
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Функция для оценки стоимости недвижимости
def predict_house_price(total_area, num_room, sub_area, kitch_sq):
    input_data = np.array([total_area, num_room, sub_area, kitch_sq]).reshape(1, -1)
    predicted_price = model.predict(input_data)
    return predicted_price[0]

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Создание и запуск бота
updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
updater.start_polling()
updater.idle()