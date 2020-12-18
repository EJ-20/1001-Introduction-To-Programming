class Song:
    def __init__(self, name, minutes, seconds):
        self.__name = name
        self.__mins = int(minutes)
        self.__secs = int(seconds)

    def setTime(self, name, time):
        mins = int(time[:2])
        secs = int(time[3:])
        self.__name = name
        self.__mins = mins
        self.__secs = secs

    def getMins(self):
        return self.__mins
    def getSecs(self):
        return self.__secs
    def getName(self):
        return self.__name

class Album(Song):
    def __init__(self, title, artist, date, name, minutes, seconds):
        super().__init__(name, minutes, seconds)
        self.__title = title
        self.__artist = artist
        self.__date = date
        self.__songs = []

    def setAlbum(self, title, artist, date):
        self.__title = title
        self.__artist = artist
        self.__date = date

    def getTitle(self):
        return self.__title 
    def getArtist(self):
        return self.__artist
    def getDate(self):
        return self.__date

    def addSong(self, song):
        self.__songs.append(song)

    def calcLength(self):
        
        
def main():
    song = Song("EJ", "20", "30")
    mins = song.getMins()
    secs = song.getSecs()
    name = song.getName()
    print(name, mins, secs)
    song.setTime("DJ", "30:20")
    mins1 = song.getMins()
    secs1 = song.getSecs()
    name1 = song.getName()
    print(name1, mins1, secs1)
main()
