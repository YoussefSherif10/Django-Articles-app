from myarts.models import Article
from myarts.owner import OwnerListView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView, OwnerDetailView

# Create your views here.
class ArticleListView(OwnerListView):
    model = Article

class ArticleDetailView(OwnerDetailView):
    model = Article

class ArticleCreateView(OwnerCreateView):
    model = Article
    fields = ['title', 'text']

class ArticleUpdateView(OwnerUpdateView):
    model = Article
    fields = ['title', 'text']

class ArticleDeleteView(OwnerDeleteView):
    model = Article

