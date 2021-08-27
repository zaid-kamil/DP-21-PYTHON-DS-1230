class Movie:

    def __init__(self,title,director,year,cast=[],genre=[]):
        self.title = title
        self.director = director
        self.year = year
        self.cast = cast
        self.genre = genre
    
    def show(self):
        """
        function that shows the detail of movie
        """
        print("Movie Detail")
        print("Title:",self.title)
        print("Director:",self.director)
        print("Year:",self.year)
        print("Cast:", ",".join(self.cast))
        print("Genre:", ",".join(self.genre))

if __name__ == "__main__":
    movie = Movie("Avengers","Joss Whedon",2012,["Action","Adventure","Sci-Fi"])
    movie2 = Movie("Avengers: Infinity War","Anthony Russo",2019);
    
    movie.show()
    movie2.show()
    movie2.cast = ["Robert Downey Jr.","Chris Evans","Mark Ruffalo"]
    movie2.genre = ["Action","Adventure","Sci-Fi","Fantasy"]
    print("-"*30)
    movie2.show()
        
    









