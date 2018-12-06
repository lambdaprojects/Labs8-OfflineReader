from rest_framework import serializers, viewsets
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'


class ArticleViewSet(viewsets.ModelViewSet):
    serializers_class = ArticleSerializer
    # open access
    #queryset = Article.objects.all()

    # access granted when logged in
    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return Article.objects.none()
        else:
            return Article.objects.filter(user=user)
