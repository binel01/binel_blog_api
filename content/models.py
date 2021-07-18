from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.reverse_related import ManyToOneRel
from django.utils.translation import gettext as _
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    """
    Model used to store categories of posts
    """
    name = models.CharField(_("Name"), max_length=150)
    description = models.CharField(_("Description"), max_length=150)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"pk": self.pk})


class Post(models.Model):
    """
    This model is used to store Users' posts inside the database
    """
    title = models.CharField(_("Title"), max_length=150)
    content = models.TextField(_("Content"))
    cover_image = models.ImageField(_("Image"), upload_to="uploads")
    category = models.ForeignKey(Category, verbose_name=_("Category"), on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=_("Author"), on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)

    class Meta:
        verbose_name = _("post")
        verbose_name_plural = _("posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    """
    Model used to store posts' comments
    """
    content = models.CharField(_("Content"), max_length=150)
    post = models.ForeignKey(Post, verbose_name=_("Post"), on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)

    class Meta:
        verbose_name = _("comment")
        verbose_name_plural = _("comments")

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse("comment_detail", kwargs={"pk": self.pk})

