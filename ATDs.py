#/usr/bin/python
#Joseph Daviesn 2020
#https://github.com/Joseph-Davies/vce-algroithmics-adts

class queue:
	def __init__(self):
		self._container = list()
		
	def enqueue(self, element):
		self._container.append(element)
	
	def dequeue(self):
		element = self._container[0]
		self._container.pop(0)
		return element
		
	def front(self):
		return self._container[0]
	
	def back(self):
		return self._container[-1]
	
	def length(self):
		return len(self._container)
	
	def __len__(self):
		return len(self._container)
	
	def __str__(self):
		output = "queue {"
		output += str(self._container[0])
		for element in self._container[1:]:
			output += ", " + str(element)
		output += "}"
		return output
	
	def __repr(self):
		output = "queue {"
		output += str(self._container[0])
		for element in self._container[1:]:
			output += ", " + str(element)
		output += "}"
		return output
