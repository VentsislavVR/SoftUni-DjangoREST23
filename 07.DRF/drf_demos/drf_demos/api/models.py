from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(
        max_length=30
    )
    last_name = models.CharField(
        max_length=30
    )

    followers_count = models.IntegerField(

    )

    def increment_followers(self):
        self.followers_count += 1
        self.save()




# Create
# a = Author(first_name="John", last_name="Doe")
# # Update
# a.first_name = "Jane"
# # Delete
# a.delete()
# # Read
# a
# # Action
# a.increment_followers()