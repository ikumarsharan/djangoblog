from rest_framework import serializers
from .models import Post

class PostsSerializer(serializers.ModelSerializer):
    # postscategories = serializers.CharField(source='postscategories.name')
    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(PostsSerializer, self).to_representation(instance)
        rep['postscategories'] = instance.postscategories.catname
        return rep