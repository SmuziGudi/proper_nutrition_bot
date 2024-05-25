from aiogram.utils import executor
from aiogram import types, Dispatcher
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import keyboard, table, calc
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
TOKEN="your_token"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)

class Form(StatesGroup):
    age = State()
    height = State()
    weight = State() 
    gend = State()
    motivation = State()
    coef = State() 

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Поделитесь с нами вашим номером, для дальнейшего взаимодействия', reply_markup=keyboard.number)

@dp.message_handler(content_types=['contact'])
async def contact(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!\nВыбирай действие", reply_markup=keyboard.markups)
    await bot.send_message(chat_id=692604698, text=f'Чат ID: {message.chat.id}\nИмя: {message.from_user.full_name}\nНомер: {message.contact.phone_number}\n')


async def tables(call: types.CallbackQuery):
    await call.message.edit_text("Какой категории продукт интересует?", reply_markup=keyboard.tables)

async def get_table(call: types.CallbackQuery):
    number = call.data.replace('table_','')
    table_def = await table.search_product(int(number))
    messages = []
    for i in table_def:
        message = f"<b>{i['name']}</b>\nБелки: {i['belki']}\nЖиры: {i['jir']}\nУглеводы: {i['ugl']}\nКаллории: {i['calories']}\n"
        messages.append(message)
    try:
        await call.message.answer('\n'.join(messages), parse_mode='html')
    except:
        half = int(len(messages)/2)
        await call.message.answer('\n'.join(messages[:half]), parse_mode='html')
        await call.message.answer('\n'.join(messages[half:]), parse_mode='html')

async def calculate(call: types.CallbackQuery):
    await Form.coef.set()
    await call.message.edit_text(f"Отлично, начнем с того, какой у тебя уровень активности?", reply_markup=keyboard.coeffs)

async def age(call: types.CallbackQuery, state: FSMContext):
    await Form.age.set()
    await call.message.delete()
    async with state.proxy() as data:
        data['coef'] = call.data.replace('coef_','')
    await call.message.answer("Теперь введи свой возраст")

async def height(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text
    await Form.next()
    await message.answer("Теперь введи свой рост")

async def weight(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['height'] = message.text
    await Form.next()
    await message.answer("Теперь введи вес в киллограмах")

async def gend(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['weight'] = message.text
    await Form.next()
    await message.answer("Ты мужчина или женщина?", reply_markup=keyboard.gends)

async def motivation(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['gend'] = call.data
    await Form.next()
    await call.message.delete()
    await call.message.answer("Ваша цель?", reply_markup=keyboard.motivation)

async def calc_data(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['motivation'] = call.data.replace('motivation_','')
        print(data)
    
    call_answer = calc.calc(int(data['age']), int(data['height']), int(data['weight']), data['gend'], data['coef'])
    await call.message.delete()

    if data['motivation'] == '1':
        call_answer = call_answer - 428
        await call.message.answer(
        f"Отлично, твой результат: <b>{int(call_answer)}</b> ккал в день для того чтобы похудеть", 
        parse_mode='html')
    if data['motivation'] == '2':
        await call.message.answer(
        f"Отлично, твой результат: <b>{int(call_answer)}</b> ккал в день для того чтобы поддерживать форму", 
        parse_mode='html')
    if data['motivation'] == '3':
        call_answer = call_answer + 428
        await call.message.answer(
        f"Отлично, твой результат: <b>{int(call_answer)}</b> ккал в день для того чтобы набрать вес", 
        parse_mode='html')
    await state.finish()

def register_handlers(dp : Dispatcher):
    dp.register_message_handler(height, state=Form.age)  
    dp.register_message_handler(weight, state=Form.height)
    dp.register_message_handler(gend, state=Form.weight)



def register_callback_client(dp : Dispatcher):
    dp.register_callback_query_handler(tables, text='product')
    dp.register_callback_query_handler(get_table, text_startswith='table')
    
    dp.register_callback_query_handler(calculate, text='calc')
    dp.register_callback_query_handler(age, text_startswith='coef', state=Form.coef)
    dp.register_callback_query_handler(motivation, state=Form.gend)
    dp.register_callback_query_handler(calc_data, text_startswith='motivation',state=Form.motivation)


register_handlers(dp)
register_callback_client(dp)
if __name__ == '__main__':
    executor.start_polling(dp)
