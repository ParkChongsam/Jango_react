from django.views.generic import ListView
from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

post_list = ListView.as_view(model=Post)

# class PostListView(ListView):
#     model = Post
# post_list = PostListView.as_view()


# def post_list(request):
#     qs = Post.objects.all()
#     q = request.GET.get('q', '')  # q라는 이름의 인자가 있으면 q를 반환, 없으면 None를 반환하기

#     if q:  # q라는 이름의 인자가 있으면
#         # print(q)
#         qs = qs.filter(message__icontains=q)
#     # instagram/templates/instagram/post_list.html
#     return render(request, 'instagram/post_list.html', {
#         'post_list': qs,
#         'q': q,
#     })

def post_detail(request, pk):
    # return render(request, 'instagram/post_list.html')
    response = HttpResponse()
    response.write("Hello world!")
    return response


def archives_year(request, year):  # UrlConf에서 받은 인자(year)를 반드시 넣어준다.
    return HttpResponse(f"{year}년 archives")
