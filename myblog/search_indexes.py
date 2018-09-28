from haystack import  indexes
from myblog.models import Blog

class BlogIndex(indexes.SearchIndex,indexes.Indexable):
    text=indexes.CharField(document=True,use_template=True)
    # title = indexes.CharField(model_attr='title')
    # create_time=indexes.DateTimeField(model_attr='create_time')
    # click_nums=indexes.IntegerField(model_attr='click_nums')

    def get_model(self):
        return Blog

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

