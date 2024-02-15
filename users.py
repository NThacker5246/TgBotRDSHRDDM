class Student(object):
	def __init__(self, name, age, counts, pwd, isAdmin):
		self.name = name
		self.age = age
		self.counts = counts
		self.pwd = pwd
		self.isAdmin = isAdmin

	def score(self, counts):
		self.counts += counts

def profile1(cmd, user, **kwargs):
	glob = globals()
	cookie = user
	name = cookie.name
	age = cookie.age
	counts = cookie.counts
	string = f"Your Name: {name},\nYour Age: {age},\nYour Score: {counts}\n------------------\n"
	return string

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