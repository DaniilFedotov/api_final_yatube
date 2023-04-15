from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from posts.models import Comment, Post, Group, Follow, User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(read_only=True)
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(read_only=True,
                            slug_field='username',
                            default=serializers.CurrentUserDefault())
    following = SlugRelatedField(slug_field='username',
                                 queryset=User.objects.all(),)

    def validate(self, data):
        user = self.context['request'].user
        following = data['following']
        is_not_unique = Follow.objects.filter(
            user=user, following=following).exists()
        if user == following:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя')
        if is_not_unique:
            raise serializers.ValidationError(
                'Вы уже подписаны на этого автора')
        return data

    class Meta:
        fields = '__all__'
        model = Follow
