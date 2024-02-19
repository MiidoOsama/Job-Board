import django_filters
from .models import Job

class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    content = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Job
        fields = '__all__'  # all fields (you can specify only desired fields)
        exclude = ['owner','published_at' , 'image' , 'salary' , 'Vacancy' , 'slug']