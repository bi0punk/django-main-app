from django.views.generic import ListView

from .models import Sismo


class PostListView(ListView):
    model = Sismo
    paginate_by = 3

    def get_queryset(self):
        try:
            """ category_id = int(self.request.GET.get('category')) """
            sismo_id = int(self.request.GET.get('sismo_id'))
        except Exception as e:
            category_id = None
        if category_id:
            object_list = self.model.objects.filter(categories__in=[category_id])
        else:
            object_list = self.model.objects.all()
        return object_list


class CategoryListView(ListView):
    model = Sismo
