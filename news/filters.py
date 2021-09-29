from django_filters import FilterSet, \
    DateFromToRangeFilter  # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import Post


class PostFilter(FilterSet):
    dateCreation = DateFromToRangeFilter()

    class Meta:
        model = Post
        fields = ('dateCreation', 'title', 'author',
                  )  # поля, которые мы будем фильтровать (т. е. отбирать по каким-то критериям, имена берутся из моделей)

