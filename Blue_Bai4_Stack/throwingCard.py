class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue) 


while True:
    n = int(input())
    if n == 0:
      break
    
    cards = Queue()
    cards.queue = [i for i in range(1,n+1)]
    discard = []
    
    while cards.size() > 1:
      discard.append(cards.dequeue())
      cards.enqueue(cards.dequeue())
    print('Discarded cards:',end="")
    for i in range (len(discard)):
      if i == len(discard)-1:
        print(discard[-1])
      else:
        print(discard[i],end=", ")
    print('Remaining card:',cards.dequeue())

