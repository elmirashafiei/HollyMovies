from pyexpat.errors import messages

from django.db.models import Model , CharField , ForeignKey ,IntegerField , DateField , TextField , DateTimeField , DO_NOTHING , CASCADE

class Genre(Model):
    name = CharField(max_length=128)

    def __str__(self):
        return self.name

class Movie(Model):
  title = CharField(max_length=128)
  genre = ForeignKey(Genre, on_delete=CASCADE)
  rating = IntegerField()
  released = DateField()
  description = TextField()
  created = DateTimeField(auto_now_add=True)
  def __str__(self):
    #messages.success(self.request, "Movie added succesfully")
    return f"{self.title}, {self.released}: {self.genre}"