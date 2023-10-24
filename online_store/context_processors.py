from category.models import Category


def get_all_categories(request):
    return {'get_categories': Category.objects.all()}