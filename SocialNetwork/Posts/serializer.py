from rest_framework import serializers
from Posts.models import SNPost
from django import forms
 
class SNPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SNPost
        fields = '__all__'
 
class SNPostValidator(forms.Form) :
    username = forms.CharField()
    post_text = forms.CharField()

class CommentValidator(forms.Form):
    username = forms.CharField()
    reply_text = forms.CharField()