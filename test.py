#importing libs

from db import *
from tasks import *
from users import *

import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import filters
from aiogram.types.inline_keyboard import InlineKeyboardButton
from aiogram.types.inline_keyboard import InlineKeyboardMarkup


bot = Bot(token="5947987351:AAGnAgt00HcM7usENY3GC7B1IZtze9_Zp0o")
dp = Dispatcher(bot=bot)
studs = HT(31)
#studs.insert("NThacker", Student(name="NThacker", age=14, counts=0, pwd="1234", isAdmin=True))
studs.load()

@dp.callback_query_handler(text="TopStud")
async def test(callback: types.CallbackQuery):
	data = studs.getData()
	scores = []
	for item in data:
		scores.append(item[1].counts)
	bubbleSort(scores)
	if len(scores) > 2:
		st1 = scores[-1]
		nd2 = scores[-2]
		rd3 = scores[-3]
		st1x = getByScore(st1)
		nd2x = getByScore(nd2)
		rd3x = getByScore(rd3)
		result = f"1: {st1x[0]}: {st1},\n2: {nd2x[0]}: {nd2},\n3: {rd3x[0]}: {rd3}\n----------------------\n"
	else:
		st1 = scores[-1]
		st1x = getByScore(st1)
		result = f"1: {st1x}: {st1}\n----------------------\n"
	await callback.answer(result)



def START(cmd, message: Message, **kwargs):
	result = f"Добро пожаловать {message.from_user.first_name},\nЯ бот Taskman от РДДМ Самара 166,\nЯ присылаю список заданий, новостей, квестов. У нас есть реферальная система с очками, которые можно обменять на всякие плюшки)\nСкорее регистрируйся, у нас много интересно) :D"
	return result

def LOGIN(cmd, user, **kwargs):
	cm = []
	for item in cmd:
		if item != cmd[0]:
			cm.append(item)

	name = cm[0]
	pwd = cm[1]
	tr = studs.find(name)
	if tr.pwd == pwd:
		glob = globals()
		glob["current"] = tr
		return "Sucsefully"
	else:
		return "Incorrect password"


def LOGOUT(cmd, **kwargs):
	glob = globals()
	cookie = glob["current"]
	studs.delete(cookie.name)
	studs.insert(cookie.name, cookie)
	studs.save()
	glob["current"] = None
	return f"You sucsefully terminated your login. All data saved! {cookie.counts}"

current = ""

coms = {
	"/start": START,
	"/login": LOGIN,
	"/profile": profile1,
	"/exit": LOGOUT,
	"/register": register
}

loadTask(cur_task)


user_data = {}

print(seeTsk())
'''
@dp.message_handler(filters.Text(contains="/tasks", ignore_case=True))
async def test(message: Message):
	inline_btn_1 = InlineKeyboardButton('ShowTasks', callback_data=seeTsk)
	inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)
	await message.reply("Нажмите, чтобы посмотреть задания", reply_markup=inline_kb1)
'''
@dp.message_handler(commands="tasks")
async def cmd_random(message: types.Message):
	user_data[message.from_user.id] = 0
	keyboard = types.InlineKeyboardMarkup()
	keyboard.add(types.InlineKeyboardButton(text="Задания", callback_data="task"))
	await message.answer("Нажмите на кнопку, чтобы получить список заданий", reply_markup=keyboard)

@dp.message_handler(commands="menu")
async def cmd_random(message: types.Message):
	user_data[message.from_user.id] = 0
	#keyboard = types.InlineKeyboardMarkup()
	#keyboard.add(types.InlineKeyboardButton(text="Задания", callback_data="task"))
	#await message.answer("Нажмите на кнопку, чтобы получить список заданий", reply_markup=keyboard)
	glob = globals()
	if glob["current"].isAdmin == True:
		keyboard = InlineKeyboardMarkup()
		keyboard.add(InlineKeyboardButton(text="Смотреть топ", callback_data="TopStud"))
		await message.answer("Добро пожаловать в админ-панель")
		await message.answer(text="Функции админ-панели", reply_markup=keyboard)
	else:
		await message.answer("У вас нет прав.")

@dp.callback_query_handler(text="task")
async def tasks(call: types.CallbackQuery):
	keyboard = types.InlineKeyboardMarkup()
	i = 0
	while i < len(cur_task):
		keyboard.add(types.InlineKeyboardButton(text=f"{i + 1}", callback_data=f"complete_{i + 1}"))
		i += 1
	stri = seeTsk()
	await call.message.answer(stri, reply_markup=keyboard)
	await call.message.answer(text="Выбери номер для завершения")

@dp.callback_query_handler()
async def callbacks(callback: types.CallbackQuery):
	if callback.data.split("_")[0] == "complete":
		user_value = user_data.get(callback.from_user.id, 0)
		action = callback.data.split("_")[1]
		result = ""
		complete(int(action), globals()["current"])
		result = f"Dev, {action}, {user_value}"
		await callback.answer(result)
	else:
		await callback.answer(callback.data)

'''
@dp.callback_query_handler(func=lambda c: c.data == 'tasks')
async def process_callback_button1(callback_query: types.CallbackQuery):
	
	#await bot.answer_callback_query(callback_query.id)
	await bot.send_message(callback_query.from_user.id, seeTsk())
'''
@dp.message_handler(filters.Text(contains="/", ignore_case=True))
async def test(message: Message):
	try:
		cmd = message.text.strip().split()
		glob = globals()
		user = glob["current"]
		await message.reply(coms[cmd[0]](cmd, message=message, user=user))
	except Exception as e:
		await message.reply(f"Такой комманды не существует\n{e}")
		raise e
	
studs.load()

try:
	asyncio.run(
		dp.start_polling()
	)
except e as Exception:
	studs.save()
	raise SyntaxError 
