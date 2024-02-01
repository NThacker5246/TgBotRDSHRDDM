import os

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

create("Зарегистрироваться на РДШ.рф", 50)
create("Перейти по ссылке http://рдш.рф/competions/5356", 50)
create("Написать @triger777 и отправить скриншот прохождения", 50)

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

test = HT(5)
class Student(object):
	def __init__(self, name, age, counts, pwd):
		self.name = name
		self.age = age
		self.counts = counts
		self.pwd = pwd

	def score(self, counts):
		self.counts += counts

# Python program for implementation of Bubble Sort

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


# Driver code to test above
arr = [64, 34, 25, 12, 54, 22, 11, 90]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
	print("% d" % arr[i], end=" ")
