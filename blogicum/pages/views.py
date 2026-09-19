from django.shortcuts import render


def about(request):

    template_name = 'pages/about.html'

    title = 'Главная страница Blogicum'

    context = {
        'title': title,
    }

    return render(request, template_name, context)


def rules(request):

    template_name = 'pages/rules.html'

    title = 'Главная страница Blogicum'

    context = {
        'title': title,
    }

    return render(request, template_name, context)
