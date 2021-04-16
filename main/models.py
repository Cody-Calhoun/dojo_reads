from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors['name'] = "Name must be at least 2 characters"
        if len(postData['alias']) < 2:
            errors['alias'] = "Alias must be at least 2 characters"
        if not EMAIL_REGEX.match(postData['email']):   
            errors['email'] = "Invalid email address!"
        users_with_email = User.objects.filter(email = postData['email'])
        if len(users_with_email) >= 1:
            errors['duplicate'] = "Email already exists."
        if len(postData['password']) < 5:
            errors['password'] = "Password must be at least 5 characters"
        if postData['password'] != postData['confirm_password']:
            errors['pw_match'] = "Password must match!"
        return errors

class BookManager(models.Manager):
    def book_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Title must be at least 2 characters"
        return errors

class AuthorManager(models.Manager):
    def author_validator(self, postData):
        errors = {}
        if len(postData['author_name']) < 2:
            errors['author_name'] = "Name must be at least 2 characters"
        author_in_db = Author.objects.filter(name=postData['author_name'])
        if len(author_in_db) >= 1:
            errors['duplicate'] = "Author already exists."
        return errors

class ReviewManager(models.Manager):
    def review_validator(self, postData):
        errors = {}
        if len(postData['content']) < 10:
            errors['content'] = "Please leave review of at least 10 characters"
        return errors

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    alias = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    #user_reviews = []

class Book(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()
    # author = []
    # book_reviews = []

class Author(models.Model):
    name = models.CharField(max_length=75)
    books = models.ManyToManyField(Book, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AuthorManager()

class Review(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    user_review = models.ForeignKey(User, related_name="user_reviews", on_delete=models.CASCADE)
    book_reviewed = models.ForeignKey(Book, related_name="book_reviews", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()