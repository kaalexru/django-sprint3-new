from django.shortcuts import get_object_or_404, render

from .models import Category, Post

POSTS_LIMIT = 5


def index(request):
    post_list = Post.objects.published().with_related()[:POSTS_LIMIT]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(
        Post.objects.published().with_related(),
        pk=post_id,
    )
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    post_list = Post.objects.published().with_related().filter(
        category=category,
    )
    context = {
        'category': category,
        'post_list': post_list,
    }
    return render(request, 'blog/category.html', context)
