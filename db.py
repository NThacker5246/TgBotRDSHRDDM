from tasks import *
from users import Student
import math as Math

class LinkedArr(object):
	"""docstring for LinkedArr"""
	def __init__(self, key, value):
		super(LinkedArr, self).__init__()
		self.elem = None
		self.head = True
		self.tail = True
		self.key = key
		self.value = value

	def insert(self, key, value):
		if self.elem != None:
			self.elem.insert(key, value)
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
				self.tail = self.elem.tail
				self.elem = self.elem.elem
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
				value = f"(Student&{cookie.name}&{cookie.age}&{cookie.counts}&{cookie.pwd}&{cookie.isAdmin})"
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
				counts = int(val[3])
				pwd = val[4]
				isAdmin = val[5]
				value = Student(name, age, counts, pwd, isAdmin=isAdmin)
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


test = HT(5)
test.insert(5, "er")
test.save()

text = HT(5)
text.load()
print(text.getData())