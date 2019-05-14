from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Categories"


    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

class Location(models.Model):
    name=models.CharField(max_length=30)


    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

class Image(models.Model):
    image=models.ImageField(upload_to ='images/')
    name=models.CharField(max_length =30)
    description=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    location=models.ForeignKey(Location,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()
    def delete_image(self):
        self.delete()

    @classmethod
    def get_photos(cls):

        photos=cls.objects.all()
        return photos

    @classmethod
    def get_image_by_id(cls,image_id):
        image=cls.objects.get(id=image_id)
        return image


    @classmethod
    def search_by_category(cls,search_term):
        photos=cls.objects.filter(category__name__icontains=search_term)
        return photos

    @classmethod
    def filter_by_location(cls,location_id):
        photos=cls.objects.filter(id=location_id)
        return photos

    # @classmethod
    # def filter_by_category(cls,category_id):
    #     photos=cls.objects.filter(id=category_id)
    #     return photos