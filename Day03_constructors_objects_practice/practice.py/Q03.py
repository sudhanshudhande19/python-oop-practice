# Create a Movie class with:

# title
# director
# rating

# Create a method:

# display_movie()

# Create three movie objects and display their information.
#----------------------------------------------------------------------

class movie :
    def __init__(self,title,director,rating):
        self.title = title
        self.dierctor = director
        self.rating = rating

    def display_movie(self):
        print(f'Titile ={self.title}\nDierctor = {self.dierctor}\nRating = {self.rating}\n')
        print('---------------------------------------')

obj = movie('The Shawshank Redemption','Frank Darabont',9.3)
obj2 = movie('The Dark Knight','Christopher Nolan',9.1)
obj3 = movie('Inception','Christopher Nolan',8.8)

obj.display_movie()
obj2.display_movie()
obj3.display_movie()