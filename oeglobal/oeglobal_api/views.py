from rest_framework import viewsets
from rest_framework import filters

from oeglobal_api.serializers import ArticleSerializer, TopicSerializer, TopicURLSerializer, PodcastSerializer, RecentPodcastSerializer
from oeglobal_api.models import Article, Topic, TopicURL, Podcast, RecentPodcast


class ArticleViewSet(viewsets.ModelViewSet):
   queryset = Article.objects.all()
   serializer_class = ArticleSerializer
   filter_backends = [filters.SearchFilter, filters.OrderingFilter]
   filterset_fields = ['ArticleID', 'Title', 'Articleurl', 'Replies', 'Views', 'Date']
   search_fields = ['ArticleID', 'Title', 'Articleurl', 'Replies', 'Views', 'Date']
   ordering_fields = '__all__'


class TopicViewSet(viewsets.ModelViewSet):
   queryset = Topic.objects.all()
   serializer_class = TopicSerializer
   filter_backends = [filters.SearchFilter, filters.OrderingFilter]
   filterset_fields = ['TopicID', 'Topic', 'ArticleID']
   search_fields = ['TopicID', 'Topic', 'ArticleID']
   ordering_fields = '__all__'

class TopicURLViewSet(viewsets.ModelViewSet):
   queryset = TopicURL.objects.all()
   serializer_class = TopicURLSerializer
   filter_backends = [filters.SearchFilter, filters.OrderingFilter]
   filterset_fields = ['TopicUrlID', 'TopicUrl', 'TopicID']
   search_fields = ['TopicUrlID', 'TopicUrl', 'TopicID']
   ordering_fields = '__all__'

class PodcastViewSet(viewsets.ModelViewSet):
   queryset = Podcast.objects.all()
   serializer_class = PodcastSerializer
   filter_backends = [filters.SearchFilter, filters.OrderingFilter]
   filterset_fields = ['Title', 'Podcasturl', 'Comments', 'Description', 'Date']
   search_fields = ['Title', 'Podcasturl', 'Comments', 'Description', 'Date']
   ordering_fields = '__all__'


class RecentPodcastViewSet(viewsets.ModelViewSet):
   queryset = RecentPodcast.objects.all()
   serializer_class = RecentPodcastSerializer
   filter_backends = [filters.SearchFilter, filters.OrderingFilter]
   filterset_fields =  ['Title', 'RecentPodcasturl', 'Date']
   search_fields = ['Title', 'RecentPodcasturl', 'Date']
   ordering_fields = '__all__'