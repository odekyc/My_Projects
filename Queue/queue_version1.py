class Element:
	def __init__(self,value):
		self.value=value



class Queue:
    def __init__(self):
    	self.head=None
    	self.tail=None
    	self.current=None
    	self.previous=None
    	self.next=None
    	self.length=0
    def enqueue(self, element):
    	if (self.head==None):
    		self.head=element
    		self.current=element
    		self.tail=element
    		self.length+=1
    	elif (self.head!=None and self.previous==None):
    		self.head=element
    		self.previous=self.current
    		self.current=element
    		self.tail=self.previous
    		self.length+=1
    	elif (self.head!=None and self.previous!=None):
    		
    		self.head=element
    		self.previous=self.current
    		self.current=element
    		self.length+=1

    def dequeue(self):
    	if (self.head==None):
    		return "the queue is empty"
    	elif (self.head!=None and self.previous==None):
    		self.head=None
    		self.tail=None
    		self.current=None
    	elif (self.head!=None and self.previous!=None):
    		self.tail=self.previous
    		self.current=self.previous

    def len(self):
    	return self.length

    def is_empty(self):
    	if (self.head==None):
    		return True
    	else :
    		return False

    def get_front(self):
    	if (self.head==None):
    		return "the queue is empty"
    	else :
    		return self.head.value
    def get_end(self):
    	if (self.tail==None):
    		return "the queue is empty"
    	else:
    		return self.tail.value

   # def print_queue(self):


playlist1=Element("Playlist1")
playlist2=Element("Playlist2")
playlist3=Element("Playlist3")

playlist4=Element("Playlist4")
playlist5=Element("Playlist5")
playlist6=Element("Playlist6")
queue1=Queue()
queue1.enqueue(playlist6)
queue1.enqueue(playlist5)
queue1.enqueue(playlist4)
queue1.enqueue(playlist3)
queue1.enqueue(playlist2)
queue1.enqueue(playlist1)

print (queue1.is_empty())
print (queue1.get_front())
print (queue1.get_end())
print (queue1.len())