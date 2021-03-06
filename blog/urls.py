from django.conf.urls import url, patterns
from django.contrib.auth.decorators import login_required
from blog.views import PostListView, PostCreateView, PostUpdateView, PostDeleteView,PostDetailView , CommentNewView, StockDetailView, StockListView

urlpatterns = patterns('blog.views',
    # url(r'^$', 'index', name='index'),
    url(r'^$', PostListView.as_view(), name='index'),
    # url(r'^(?P<pk>\d+)/$', 'post_detail', name='post_detail'),
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name='post_detail'),

    # url(r'^search/$', 'search_name', name='search_name'),
    # url(r'^$', StockListView.as_view(), name='stock_list'),

    url(r'^search/$', StockDetailView.as_view(), name='search_name'),
    url(r'^search2/$', 'search_titles', name='search_titles'),
    # url(r'^search/(?P<pk>\d+)/$', StockDetailView2.as_view(), name='search_name2'),
    # url(r'^enemy/(?P<tag>\d+)', 'EnemyAbility'),





    url(r'^timeline/$', StockListView.as_view(), name='timeline'),
    # url(r'^test/$', TimelineDetailView.as_view() , name='post_test'),

    url(r'^new/$', login_required(PostCreateView.as_view()), name='post_create'),
    url(r'^(?P<pk>\d+)/edit/$', PostUpdateView.as_view(), name='post_update'),
    url(r'^(?P<pk>\d+)/delete/$', PostDeleteView.as_view(), name='post_delete'),

    # url(r'^(?P<pk>\d+)/comments/new/$', 'comment_new', name='comment_new'), #새 댓글생성
    url(r'^(?P<pk>\d+)/comments/new/$', CommentNewView.as_view(), name='comment_new'), #새 댓글생성
    url(r'^(?P<post_pk>\d+)/comments/(?P<pk>\d+)/edit/$', 'comment_edit', name='comment_edit'), #댓글 수정
    url(r'^(?P<post_pk>\d+)/comments/(?P<pk>\d+)/delete/$', 'comment_delete', name='comment_delete'), #댓글 삭제





    )


# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
