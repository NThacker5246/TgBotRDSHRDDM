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

def complete(id4, user):
	trust_id = id4 - 1
	cur_task[trust_id].isCompleted = True
	score = cur_task[trust_id].score
	#glob = globals()
	#glob["current"].counts += score
	user.counts += score

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