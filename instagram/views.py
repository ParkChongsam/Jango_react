from django.views.generic import DetailView, ListView
from django.shortcuts import render, get_list_or_404
from .models import Post
from django.http import HttpResponse, Http404, HttpRequest

post_list = ListView.as_view(model=Post, paginate_by=2)

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
# def post_detail(request, pk):
#     post = get_list_or_404(Post, pk =pk)
#     return render(request, 'instagram/post_detail.html', {
#         'post':post,
#     })

class PostDetailView(DetailView):
    model = Post

    def get_queryset(self):
        qs = super().get_queryset  # super 부모클래스의 함수 상속
        # 그러니까 DetailView 클래스의 get_queryset 함수를 상속 받는다.
        if not self.request.user.is_authenticated:  # 로그인 안한경우 공개된 문서만 보게하기
            qs = qs.filter(is_public=True)
        return qs


post_detail = DetailView.as_view(model=Post)


def archives_year(request, year):  # UrlConf에서 받은 인자(year)를 반드시 넣어준다.
    return HttpResponse(f"{year}년 archives")
