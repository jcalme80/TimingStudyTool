class Environment:
    def __init__(self):
        #self.events is a dictionary containing the events of the time study. Keys are the event names, values are the
        #event objects.
        self.events={}
        #self.starts contains information on when untriggered events (such as the first event in a sequence) should
        #start. It is a dictionary with the event name as key, and the start time as value.
        self.starts={}
        self.time=0

    def update(self):
        for event in self.events:
            self.events[event].update()
            self.time += .1

    def addEvent(self, name, duration):
        self.events[name] = Event(name=name, parent=self, duration=duration)

    def addStart(self, name, time):
        self.starts[name] = time

    def status(self):
        print(self.events)
        for event in self.events:
            self.events[event].status()


class Event:
    def __init__(self, name, parent, duration):
        self.name = name
        self.parent = parent
        self.isActive = 0
        self.start = None
        self.progress = 0
        self.duration = duration
        self.end = None
        self.triggers = []

    def update(self):
        if self.isActive:
            self.time += .1


        if self.time >= self.duration:
            self.time = 0
            self.isActive = 0
            for trigger in self.triggers:
                self.parent.events[trigger].setActive = 1

    def status(self):
        print(self.name)
        print(self.time)
        print(self.isActive)
        print(self.duration)
        print(self.triggers)



