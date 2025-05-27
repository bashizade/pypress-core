from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Post, Comment

@receiver(post_save, sender=Comment)
def update_post_comment_count(sender, instance, created, **kwargs):
    """
    Update the comment count of a post when a comment is added or removed
    """
    post = instance.post
    post.comment_count = Comment.objects.filter(post=post, is_approved=True).count()
    post.save(update_fields=['comment_count'])

@receiver(post_delete, sender=Comment)
def update_post_comment_count_on_delete(sender, instance, **kwargs):
    """
    Update the comment count of a post when a comment is deleted
    """
    post = instance.post
    post.comment_count = Comment.objects.filter(post=post, is_approved=True).count()
    post.save(update_fields=['comment_count']) 