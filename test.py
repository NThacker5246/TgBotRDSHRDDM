#importing libs


import math as Math

class LinkedArr(object):
	"""docstring for LinkedArr"""
	def __init__(self, key, value):
		super(LinkedArr, self).__init__()
		self.elem = None
		self.head = True
		self.tali = True
		self.key = key
		self.value = value

	def insert(self, key, value):
		if self.elem != None:
			self.elem.insert(keyValue)
		else:
			self.elem = LinkedArr(key, value)
			self.elem.head = False
			self.tail = False

	def find(self, key):
		if self.key != key:
			return self.elem.find(key)
		else:
			return self

	def edit(self, key, NewValue, NewKey):
		if self.key != key:
			if self.elem != None:
				self.elem.edit(key, NewValue, NewKey)
			else:
				return None
		else:
			self.key = NewKey
			self.value = NewValue

	def delete(self, key):
		if self.key != key:
			if self.elem != None:
				self.elem.delete(key)
			else:
				return None
		else:
			if self.elem != None:
				self.key = self.elem.key
				self.value = self.elem.value
				self.elem = self.elem.elem
				self.tail = self.elem.tail
				return None
			else:
				self = None

	def getAllKeysVals(self, stack):
		stack.append([self.key, self.value])
		if self.elem == None:
			return stack
		return self.elem.getAllKeysVals(stack)

class HT(object):
	"""docstring for HT"""
	lengths = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
	def __init__(self, length):
		super(HT, self).__init__()
		self.array = []
		i = 0
		while i < length:
			self.array.append(None)
			i += 1

	def getHash(self, key):
		if isinstance(key, int):
			return key
		elif isinstance(key, str):
			i = 0
			num = 0
			while i < len(key):
				num = (num << 5) - num + ord(key[i])
				i += 1
			return num

	def getIndex(self, hash1):
		return (hash1 % len(self.array))


	def check(self):
		lon = len(self.array)
		has = 0
		for item in self.array:
			if self != None:
				has += 1
		percent = 0.75
		full = lon * percent
		n = 0
		for leng in self.lengths:
			if (lon + leng)*percent > has:
				n = leng
				break
		#print(lon, has, full, n)
		if has >= full:
			self.expand(n)


	def insert(self, key, value):
		self.check()
		ArrayKey = self.getIndex(self.getHash(key))
		if self.array[ArrayKey] == None:
			self.array[ArrayKey] = LinkedArr(key, value)
		else:
			self.array[ArrayKey].insert(key, value)

	def find(self, key):
		ArrayKey = self.getIndex(self.getHash(key))
		if self.array[ArrayKey] != None:
			return self.array[ArrayKey].find(key).value
		else:
			return None

	def delete(self, key):
		ArrayKey = self.getIndex(self.getHash(key))
		self.array[ArrayKey].delete(key)

	def expand(self, length):
		oldLong = len(self.array)
		arr = []
		for item in self.array:
			stack = []
			if item != None:
				item.getAllKeysVals(stack)
				for it in stack:
					arr.append(it)
			else:
				pass

		NewLong = oldLong + length
		self.array = []
		i = 0
		while i < NewLong:
			self.array.append(None)
			i += 1

		for item in arr:
			self.insert(item[0], item[1])


	def getFirstNode(self):
		return self.array[0].value

	def save(self):
		arr = []
		for item in self.array:
			stack = []
			if item != None:
				item.getAllKeysVals(stack)
				for it in stack:
					arr.append(it)
			else:
				pass
		saveString = ""
		for item in arr:
			key  = item[0]
			value = item[1]
			if value.__class__.__name__ == "Student":
				cookie = value
				value = f"(Student&{cookie.name}&{cookie.age}&{cookie.counts}&{cookie.pwd}&)"
			keyValue = f"{key}={value}"
			saveString += keyValue
			if item != arr[-1]:
				saveString += "$"

		file = open("HT.txt", "w")
		file.write(saveString)
		file.close()

	def load(self):
		file = open("HT.txt")
		string = file.read()
		li = string.split("$")
		for item in li:
			keyValue = item.split("=")
			key = keyValue[0]
			value = keyValue[1]
			val = value.split("&")
			if val[0] == "(Student":
				name = val[1]
				age = val[2]
				counts = val[3]
				pwd = val[4]
				value = Student(name, age, counts, pwd)
			self.insert(key, value)
	
	def getData(self):
		arr = []
		for item in self.array:
			stack = []
			if item != None:
				item.getAllKeysVals(stack)
				for it in stack:
					arr.append(it)
			else:
				pass
		return arr		

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

class Student(object):
	def __init__(self, name, age, counts, pwd, isAdmin):
		self.name = name
		self.age = age
		self.counts = counts
		self.pwd = pwd
		self.isAdmin = isAdmin

	def score(self, counts):
		self.counts += counts

studs = HT(31)
studs.insert("NThacker", Student(name="NThacker", age=14, counts=0, pwd="1234", isAdmin=True))

def LOGIN(cmd, **kwargs):
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


def profile1(cmd, **kwargs):
	glob = globals()
	cookie = glob["current"]
	name = cookie.name
	age = cookie.age
	counts = cookie.counts
	string = f"Your Name: {name},\nYour Age: {age},\nYour Score: {counts}\n------------------\n"
	return string


def LOGOUT(cmd, **kwargs):
	glob = globals()
	cookie = glob["current"]
	studs.delete(cookie.name)
	studs.insert(cookie.name, cookie)
	studs.save()
	glob["current"] = None
	return "You sucsefully terminated your login. All data saved!"

def register(cmd, **kwargs):
	cm = []
	for item in cmd:
		if item != cmd[0]:
			cm.append(item)

	name = cm[0]
	age = cm[1]
	pwd = cm[2]
	studs.insert(name, Student(name=name, age=age, pwd=pwd, counts=0, isAdmin=False))
	return "Registed"

def bubbleSort(arr):
	n = len(arr)
	swapped = False
	for i in range(n-1):
		for j in range(0, n-i-1):
			if arr[j] > arr[j + 1]:
				swapped = True
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
		
		if not swapped:
			return

@dp.callback_query_handler(text="TopStud")
async def test(callback: types.CallbackQuery):
	data = studs.getData()
	scores = []
	for item in data:
		scores.append(item.counts)
	bubbleSort(scores)
	st1 = scores[-1]
	nd2 = scores[-2]
	rd3 = scores[-3]
	st1x = getByScore(st1)
	nd2x = getByScore(nd2)
	rd3x = getByScore(rd3)
	result = f"1: {st1x.name}: {st1},\n2: {nd2x.name}: {nd2},\n3: {rd3x.name}: {rd3}\n----------------------\n"
	await callback.answer(result)

async def admin(cmd, message: Message):
	glob = globals()
	if glob["current"].isAdmin == True:
		keyboard = InlineKeyboardMarkup()
		keyboard.add(InlineKeyboardButton(text="Смотреть топ", callback_data="TopStud"))
		await message.answer(text="Функции админ-панели", reply_markup=keyboard)
		return "Добро пожаловать в админ-панель"
	else:
		return "У вас нет прав."

def START(cmd, message: Message, **kwargs):
	result = f"Добро пожаловать {message.from_user.first_name},\nЯ бот Taskman от РДДМ Самара 166,\nЯ присылаю список заданий, новостей, квестов. У нас есть реферальная система с очками, которые можно обменять на всякие плюшки)\nСкорее регистрируйся, у нас много интересно) :D"
	return result

coms = {
	"/start": START,
	"/login": LOGIN,
	"/profile": profile1,
	"/exit": LOGOUT,
	"/register": register,
	"/menu": admin
}

class Task(object):
	"""docstring for Task"""
	def __init__(self, docstring, score):
		super(Task, self).__init__()
		self.docstring = docstring
		self.score = score

cur_task = []

def create(docstring, score):
	task = Task(docstring, score)
	cur_task.append(task)

def getById(ids):
	trust_id = ids - 1
	return trust_id

def getByScore(score):
	result = []
	for item in cur_task:
		if item.score == score:
			result.append(item)
	return result

def getByName(name):
	result = []
	for item in cur_task:
		if name in item.name:
			result.append(item)
	return result

def complete(id4):
	trust_id = id4 - 1
	cur_task[trust_id].isCompleted = True
	score = cur_task[trust_id].score
	glob = globals()
	glob["current"].counts += score

#create("Зарегистрироваться на РДШ.рф", 50)
#create("Перейти по ссылке http://рдш.рф/competions/5356", 50)
#create("Написать @triger777 и отправить скриншот прохождения", 50)

def saveTasks(array):
	saveString = ""
	for item in array:
		value = item
		if value.__class__.__name__ == "Task":
			cookie = value
			value = f"(Task&{cookie.docstring}&{cookie.score}&)"
		saveString += value
		if item != array[-1]:
			saveString += "$"

	file = open("Array.txt", "w")
	file.write(saveString)
	file.close()

def loadTask(array):
	file = open("Array.txt")
	string = file.read()
	li = string.split("$")
	for item in li:
		value = item
		val = value.split("&")
		if val[0] == "(Task":
			docstring = val[1]
			score = val[2]
			value = Task(docstring=docstring, score=int(score))
		array.append(value)

loadTask(cur_task)

def seeTsk():
	listing = ""
	i = 0
	while i < len(cur_task):
		value = cur_task[i]
		string = str(i + 1) + ". " + value.docstring + ": " + str(value.score) + " очков\n"
		listing += string
		i += 1
	listing += "---------------------------------------------------------------------------------------------\n"
	return listing

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
		complete(int(action))
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
		await message.reply(coms[cmd[0]](cmd, message=message))
	except Exception as e:
		await message.reply("Такой комманды не существует")
	


asyncio.run(
	dp.start_polling()
)
