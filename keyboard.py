from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup  
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

number = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
number.add(KeyboardButton('Отправить контакт', request_contact=True))

markups = InlineKeyboardMarkup(row_width=2)
markups.add(
    InlineKeyboardButton(text='Калькулятор', callback_data='calc'),
    InlineKeyboardButton(text='Таблицы продуктов', callback_data='product'),
)
tables = InlineKeyboardMarkup(row_width=1)

tables.add(
    InlineKeyboardButton(text='Хлеб, мука, крупы, бобовые', callback_data='table_0'),
    InlineKeyboardButton(text='Молочные продукты', callback_data='table_1'),
    InlineKeyboardButton(text='Мясные продукты, птица', callback_data='table_2'),
    InlineKeyboardButton(text='Колбасные изделия, мясные консервы', callback_data='table_3'),
    InlineKeyboardButton(text='Рыба и морепродукты', callback_data='table_4'),
    InlineKeyboardButton(text='Яйцепродукты', callback_data='table_5'),
    InlineKeyboardButton(text='Масла, жиры', callback_data='table_6'),
    InlineKeyboardButton(text='Овощи, картофель, зелень, грибы', callback_data='table_7'),
    InlineKeyboardButton(text='Фрукты, ягоды, бахчевые', callback_data='table_8'),
    InlineKeyboardButton(text='Орехи, семена, сухофрукты', callback_data='table_9'),
    InlineKeyboardButton(text='Сахар, сладкое и кондитерские изделия', callback_data='table_10'),
    InlineKeyboardButton(text='Напитки безалкогольные', callback_data='table_11'),
    InlineKeyboardButton(text='Напитки алкогольные', callback_data='table_12'),
    )

motivation = InlineKeyboardMarkup(row_width=3)
motivation.add(
    InlineKeyboardButton(text='Похудеть', callback_data='motivation_1'),
    InlineKeyboardButton(text='Сохранить вес', callback_data='motivation_2'),
    InlineKeyboardButton(text='Набрать', callback_data='motivation_3'),
)

gends = InlineKeyboardMarkup(row_width=2)
gends.add(
    InlineKeyboardButton(text='👨‍🦱', callback_data='m'),
    InlineKeyboardButton(text='👱‍♀️', callback_data='f'),
)

coeffs = InlineKeyboardMarkup(row_width=1)
coeffs.add(
    InlineKeyboardButton(text='Редко выхожу из дома, почти весь день сижу', callback_data='coef_1'),
    InlineKeyboardButton(text='Хожу в магазин или недолго прогуливаюсь', callback_data='coef_2'),
    InlineKeyboardButton(text='Ежедневно гуляю не меньше часа', callback_data='coef_3'),
    InlineKeyboardButton(text='Занимаюсь активными видами спорта/досуга', callback_data='coef_4'),
    InlineKeyboardButton(text='Регулярно занимаюсь спортом', callback_data='coef_5'),
)