from abc import ABCMeta, abstractmethod

#Product
class Section(metaclass = ABCMeta):

    @abstractmethod
    def describe(self):
        pass

class PersonalSection(Section):

    def describe(self):
        print("PersonalSection")

class AlbumSection(Section):

    def describe(self):
        print("AlbumSection")

class PatentSection(Section):

    def describe(self):
        print("PatentSection")

class PublicationSection(Section):

    def describe(self):
        print("PatentSection")

#Creator
class Profile(metaclass = ABCMeta):

    def __init__(self):
        self.sections = []
        self.createprofile()

    @abstractmethod
    def createprofile(self):
        pass

    def getSections(self):
        return self.sections

    def addSections(self, section):
        self.sections.append(section)


class linkedin(Profile):

    def createprofile(self):
        self.addSections(PersonalSection())
        self.addSections(PatentSection())
        self.addSections(PublicationSection())

class facebook(Profile):

    def createprofile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())


# Client

if __name__ == "__main__":
    profile_input = input("what's your profile ? ")
    profile = eval(profile_input.lower())()
    print("Done! Profile is :", type(profile).__name__)
    print("Sections are : ", profile.getSections())
