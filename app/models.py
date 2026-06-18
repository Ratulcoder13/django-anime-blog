from django.db import models
from django.utils.text import slugify
 

class BlogApp(models.Model):
    
    STATUS_CHOICES = (
        ('Draft', 'Draft'),
        ('Published', 'Published'),
    )
    
    CATEGORY_CHOICES = (
    ('Anime','Anime'),
    ('Movies','Movies'),
    ('Top_Anime_Series','Top_Anime_Series'),
    ('Top_Movies','Top_Movies'),
    )
    
    
    title = models.CharField(max_length=200)
    
    slug = models.SlugField(max_length=150,unique=True,blank=True,null=True)
    category = models.CharField(max_length=40,choices=CATEGORY_CHOICES,default="Anime")
    author = models.CharField(max_length=30)
    image = models.ImageField(upload_to='blog_images/',blank=True,null=True)
    content = models.TextField()
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="Draft")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
# auto make slug 

def save(self,*args,**kwargs):
    if not self.slug:
        self.slug = slugify(self.title)
    super().save(*args,**kwargs)
    
# for top anime ranking model

class TopAnime(models.Model):
    rank = models.IntegerField(unique=True) # for 1,2,3,4
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='top_anime/')
    rating = models.FloatField()
    description = models.TextField()
    
    class Meta:
        ordering =['rank']  # admin panel ar website aa ata serial akaray thakbo
        
    def __str__(self):
        return f"#{self.rank}-{self.title}"
        
    
# for top movies
class TopMovies(models.Model):
    rank = models.IntegerField(unique=True) # for 1,2,3,4
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='top_movies/')
    rating = models.FloatField()
    description = models.TextField()
    
    class Meta:
        ordering =['rank']  # admin panel ar website aa ata serial akaray thakbo
        
    def __str__(self):
        return f"#{self.rank}-{self.title}"
        
    

class UserFormModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name