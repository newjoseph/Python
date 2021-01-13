# CECS 174
# Professor Gina Song
# Project 2
# Team 5: Jennifer Gensler, Angela Barandino, Minhyuk Kim, Adrian Rodriguez, Noah Avina

# Media is a superclass of Book class and Video class
class Media:

    # initializing data
    def __init__(self, title, author, publisher):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.checkedOutBy = '' # initialize this variable so we can save who checked out what media later
        self.checkedOut = False #flag if the media has been checked out

    def checkOut(self, member_name):
        self.checkedOut = True #flag if the media has been checked out
        self.checkedOutBy = member_name # save who checked out the media

    def checkIn(self):
        self.checkedOut = False #switch flag

    def isAvailable(self):
        return not self.checkedOut #return the flag variable to call during checkOut in Member class #negate the flag to make the logic work

# Book is a subclass of Media
class Book(Media):
    # tracks number of books and number of books checked out
    count_of_books = 0
    count_of_books_checked_out = 0


    def __init__(self, title, author, publisher, numOfPages):
        super().__init__(title, author, publisher) #call init from Media class to inherit
        self.numOfPages = numOfPages # initialize numOfPages
        Book.count_of_books += 1 #increases count for the amount of books

    def checkOut(self, member_name):
        super().checkOut(member_name) #call checkOut from Media class
        Book.count_of_books_checked_out += 1 # increases count for the amount of books checked out

    def checkIn(self):
        super().checkIn() #call CheckIn from Media class to change the flag
        Book.count_of_books_checked_out -= 1 #decreases count for amount of books checked out

    # format how messages for books are printed
    def __repr__(self):
        return 'Book --> {} written by {}'.format(self.title, self.author)

    @classmethod
    def get_count_of_books(cls): # returns the amount of books
        return cls.count_of_books

    @classmethod
    def get_count_of_books_checked_out(cls): #returns the amount of books checked out
        return cls.count_of_books_checked_out

# Video is a subclass of Media
class Video(Media):
    # tracks number of videos and number of videos checked out
    count_of_videos = 0
    count_of_videos_checked_out = 0

    def __init__(self, title, author, publisher, runningTime):
        super().__init__(title, author, publisher) #call init from Media class to inherit
        self.runningTime = runningTime #initialize runningTime
        Video.count_of_videos += 1 #increases count for the amount of videos

    def checkOut(self, member_name):
        super().checkOut(member_name) #call checkOut from Media class
        Video.count_of_videos_checked_out += 1 #increases count for the amount of videos checked out

    def checkIn(self):
        super().checkIn() #call checkIn from Media class to change the flag
        Video.count_of_videos_checked_out -= 1 #decreases count for amount of videos checked out

    # format how messages for videos are printed
    def __repr__(self):
        return 'Video --> {} video {} created by {}, {}'.format(self.runningTime, self.title, self.author, self.publisher)

    @classmethod
    def get_count_of_videos(cls): #returns amount of videos
        return cls.count_of_videos

    @classmethod
    def get_count_of_videos_checked_out(cls): #returns amount of videos checked out
        return cls.count_of_videos_checked_out

# Member is a separate class from Media
class Member:
    MAX_NUMBER_OF_MEDIA = 2 #max number of media per member; a constant number
    numberOfMembers = 0 #keeps track of the total number of members
    total_media_checked_out = [] #list for all of the media that is checked out by all members

    #initializing data
    def __init__(self, name):
        self.name = name #store member name
        self.numOfMedia = 0 #initialize how much media each member has checked out
        self.mediaCheckedOut = [] #list for all media that is checked out by an individual
        Member.numberOfMembers += 1 #adds a member to total number of members

    # function to print out what media a particular member has checked out
    def printCheckedOut(self):
        print('Items checked out by {}:'.format(self.name)) #format for the printed message
        for obj in self.mediaCheckedOut: #goes through list and prints each item
            print(obj)

    def checkOut(self, media_to_be_checked_out):
        # method to check out media
        if self.numOfMedia < Member.MAX_NUMBER_OF_MEDIA: #make sure they haven't surpassed that max number of media they can check out
            if media_to_be_checked_out.isAvailable(): #make sure the media wasn't checked out already by checking the flag
                self.mediaCheckedOut.append(media_to_be_checked_out) # add to member's checked out list
                Member.total_media_checked_out.append(media_to_be_checked_out) # add to list of total media checked out
                self.numOfMedia += 1 # increment counter for amount of media the member has checked out
                media_to_be_checked_out.checkOut(self.name) # save who checked out the media and increase Video/Book checked out count
                print('{} has checked out: {}'.format(self.name, media_to_be_checked_out)) #print a confirmation message saying they sucessfully checked out the media
            else:
                #tell them they can't check it out because it has already been checked out and who checked it out
                print('Sorry', self.name + ',', media_to_be_checked_out.title, 'is not available. It has been checked out by', media_to_be_checked_out.checkedOutBy)
        else:
            #tell them they have checked out the max number of media
            print('{} reached the maximum number ({}) of borrowed items, so can not check out: {}'.format(self.name, Member.MAX_NUMBER_OF_MEDIA, media_to_be_checked_out))

    def checkIn(self, media_to_be_checked_in):
        # method to check in media
        if media_to_be_checked_in in self.mediaCheckedOut: #check if they were the ones who checked it out/it has been checked out
            self.mediaCheckedOut.remove(media_to_be_checked_in) #remove from their individual checked out list
            Member.total_media_checked_out.remove(media_to_be_checked_in) #remove from total checked out list
            self.numOfMedia -= 1 #reduce number of media the person has checked out
            media_to_be_checked_in.checkIn() #call the checkIn method in Video/Book to decrease number of Video/Book checked out
            print('{} has checked in: {}'.format(self.name, media_to_be_checked_in)) #print a confirmation messag saying they sucessfully checked in the media
        else:
            #tell them they can't return something they haven't checked out
            print('You have not checked out', media_to_be_checked_in)

    @classmethod
    def get_number_of_members(cls): #returns amount of members
        return Member.numberOfMembers

    @classmethod
    def printMediaCheckedOut(cls):
        for obj in cls.total_media_checked_out:  # this will print all the media that has been checked out
            print(obj)

def displayStats(): #displays stats by calling @classmethod functions
    print('*'*100) #border
    print('Record of library:')
    print('Total number of books =', Book.get_count_of_books())
    print('Number of books checked out =', Book.get_count_of_books_checked_out())
    print('Total number of videos = ', Video.get_count_of_videos())
    print('Total number of videos checked out =', Video.get_count_of_videos_checked_out())
    print('Total number of members = ', Member.get_number_of_members())
    print('The following items are checked out of the library:')
    Member.printMediaCheckedOut()
    print('*' * 100) #border


### TEST CASES ###
Amy = Member('Amy Santiago')
Jake = Member('Jake Peralta')
Charles = Member('Charles Boyle')
book1 = Book('Harry Potter', 'JK Rowling', 'Publisher1', '120')
book2 = Book('How To Kill A Mockingbird', 'Harper Lee', 'Publisher3', '300')
book3 = Book('Pride and Prejudice', 'Jane Austen', 'Publisher2', '400')
video1 = Video('How The Grinch Stole Christmas', 'Ron Howard', 'Universal', '2 hrs')
video2 = Video('Love Actually', 'Richard Curtis', 'Universal', '2 hrs 10 mins')

Amy.checkOut(book3)
Jake.checkOut(book2)
Charles.checkOut(book3)
Charles.checkOut(book1)
Amy.checkOut(book1)
Charles.checkOut(video1)
Charles.checkOut(video2)
Charles.checkIn(book1)
Charles.checkOut(video2)
Amy.checkOut(book1)
Jake.checkIn(book2)
Jake.checkOut(video1)
Charles.checkIn(video1)
Jake.checkOut(video1)
displayStats()
Amy.printCheckedOut()
Jake.printCheckedOut()
Charles.printCheckedOut()
### TEST CASES ###