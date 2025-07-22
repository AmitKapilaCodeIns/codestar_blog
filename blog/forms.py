from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Form class for users to submit comments on blog posts.
    """
    class Meta:
        """
        Meta class to specify the model and fields for the comment form.
        """
        model = Comment
        fields = ('body',)