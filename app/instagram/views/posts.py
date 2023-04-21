from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.http import urlencode
from django.views.generic import ListView, CreateView, TemplateView, DetailView

from instagram.models import Posts, Comments

from instagram.forms import PostsForm, CommentsForm

from accounts.models import Account


class PostsListView(ListView):
    template_name = 'posts_list.html'
    model = Posts
    context_object_name = 'posts'
    ordering = ('created_at')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['user'] = self.request.user
        context['posts'] = Posts.objects.all()
        return context


class PostAddView(LoginRequiredMixin, CreateView):
    template_name = 'post_create.html'
    model = Posts
    form_class = PostsForm

    def get_success_url(self):
        return reverse('posts_list')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            request.user.number_of_publications += 1
            user = self.request.user
            description = form.cleaned_data.get('description')
            img = form.cleaned_data.get('img')
            Posts.objects.create(user=user, description=description, img=img)
            return redirect(reverse('account_list', kwargs={'pk': self.request.user.pk}))
        return render(request, 'post_create.html',
                      context={'form': form, 'user': self.request.user})


class LikePostView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        account = request.user
        if Posts.objects.get(id=self.kwargs['pk']) in account.liked_posts.all():
            account.liked_posts.remove(Posts.objects.get(id=self.kwargs['pk']))
            post = Posts.objects.get(id=self.kwargs['pk'])
            post.likes -= 1
            post.save()
            account.save()
        else:
            account.liked_posts.add(Posts.objects.get(id=self.kwargs['pk']))
            post = Posts.objects.get(id=self.kwargs['pk'])
            post.likes += 1
            post.save()
            account.save()
        return redirect('posts_list')


class PostDetailView(DetailView):
    template_name = 'post_detail.html'
    model = Posts
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comments.objects.filter(post=Posts.objects.get(pk=self.kwargs['pk']))
        return context


class CommentAddView(LoginRequiredMixin, CreateView):
    template_name = 'comment_create.html'
    model = Comments
    form_class = CommentsForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_pk'] = self.kwargs['pk']
        return context

    def get_success_url(self):
        return reverse('post_detail', kwargs=self.kwargs['pk'])

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            post = Posts.objects.get(id=self.kwargs['pk'])
            post.comments += 1
            post.save()
            user = self.request.user
            description = form.cleaned_data.get('description')
            Comments.objects.create(user=user, description=description, post=post)
            return redirect(reverse('post_detail', kwargs={'pk': self.kwargs['pk']}))
        return render(request, 'comment_create.html',
                      context={'form': form, 'user': self.request.user})
