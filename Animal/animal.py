class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100


    def Walk(self):
        print 'Walking'
        self.health -= 1
        return self

    def Run(self):
        print 'Running'
        self.health -= 5
        return self

    def Display_health(self):
        print 'My name is: ' + str(self.name)
        print 'My current health is: '+ str(self.health)

animal = Animal('Cat')
animal.Walk()
animal.Walk()
animal.Walk()
animal.Run()
animal.Run()
animal.Display_health()

# or

animal = Animal('Dog')
animal.Walk().Walk().Walk().Run().Run().Display_health()

class Dog(Animal):
    def __init__(self, name):
        super(Dog,self).__init__(name)
        self.health = 150

    def pet(self):
        print 'Get pets'
        self.health += 5
        return self

dog = Dog('Sophie')
dog.Walk().Walk().Walk().Run().Run().pet().Display_health()


class Dragon(Animal):
    def __init__(self, name):
        super(Dragon,self).__init__(name)
        self.health = 170

    def fly(self):
        print 'Flying and seeking prey'
        self.health -= 10
        return self

    def Display_health(self):
        print "I am THE Dragon you fear"
        super(Dragon, self).Display_health()

dragon = Dragon('Nightfury')
dragon.fly().Display_health()

class Horse(Animal):
    def __init__(self, name):
        super(Horse,self).__init__(name)
        self.health = 125

horse = Horse('Carl')
horse.Display_health()
