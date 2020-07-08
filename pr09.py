#Facade
class EventManager():

    def __init__(self):
        print("Checking...")

    def arrange(self):

        self.presenter = Presenter()
        self.presenter.setPresentation()

        self.theaterGroup = TheaterGroup()
        self.theaterGroup.setTheater()

        self.services = Services()
        self.services.setServices()

        self.lecturer = Lecturer()
        self.lecturer.setLecture()

        self.musicGroup = MusicGroup()
        self.musicGroup.setMusic()


#Subsystems
class Presenter():

    def __init__(self):
        print("what day is your celebration ?")

    def setPresentation(self):
        print("Wednesday!")

class TheaterGroup():

    def __init__(self):
        print("Be serious or be fun ?")

    def setTheater(self):
        print("Fun!")

class Services():

    def __init__(self):
        print("What should the reception look like ?")

    def setServices(self):
        print("Sweets, orange juice!")


class Lecturer():

    def __init__(self):
        print("What is the topic of the lecture?")

    def setLecture(self):
        print("What is the difference between university and high school ?")

class MusicGroup():

    def __init__(self):
        print("How many songs to play ?")

    def setMusic(self):
        print("Two, Traditional")

#Client

class You:

    def __init__(self):
        print("There are manye things to do to celerate!")

    def askEventManager(self):
        print("I leave everything to the Scientific Association.")
        em = EventManager()
        em.arrange()

    def __del__(self):
        print("Thank you for doing everything!")


you = You()
you.askEventManager()
