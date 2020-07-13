from django.shortcuts import render

from .models import Post


def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q', '')  # q라는 이름의 인자가 있으면 q를 반환, 없으면 None를 반환하기

    if q:  # q라는 이름의 인자가 있으면
        # print(q)
        qs = qs.filter(message__icontains=q)
    # instagram/templates/instagram/post_list.html
    return render(request, 'instagram/post_list.html', {
        'post_list': qs,
        'q': q,
    })
