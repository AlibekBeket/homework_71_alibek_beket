from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, ListView, DetailView

from accounts.forms import LoginForm, CustomUserCreationForm

from instagram.models import Posts

from accounts.models import Account



# Create your views here.


class LoginView(TemplateView):
    template_name = 'login.html'
    form = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form()
        context = {'form': form}
        return self.render_to_response(context=context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            return redirect('login')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if not user:
            return redirect('login')
        login(request, user)
        next = request.GET.get('next')
        if next:
            return redirect(next)
        return redirect('posts_list')


def logout_view(request):
    logout(request)
    return redirect('posts_list')


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(self.success_url)
        context = {'form': form}
        return self.render_to_response(context)


class AccountView(DetailView):
    template_name = 'user_detail.html'
    model = Account
    context_object_name = 'user'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['posts'] = Posts.objects.filter(user=Account.objects.get(id=self.kwargs['pk']))
        context['not_my_page'] = False
        context['sub'] = False
        if self.kwargs['pk'] != self.request.user.pk:
            context['not_my_page'] = True
        if self.request.user == Account.objects.get(id=self.kwargs['pk']):
            context['sub'] = True
        return context


class AccountsListView(ListView):
    template_name = 'accounts_list_page.html'
    model = Account
    context_object_name = 'accounts'


class AccountsSubView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        account = request.user
        if account in Account.object.get(pk=self.kwargs['pk']).subscriptions.all():
            Account.object.get(pk=self.kwargs['pk']).subscriptions.remove(account)
            account_sub = Account.objects.get(id=self.kwargs['pk'])
            account_sub.number_of_subscriptions -= 1
            account_sub.save()
            account.number_of_subscribers -= 1
            account.save()
        else:
            Account.object.get(pk=self.kwargs['pk']).subscriptions.add(account)
            account_sub = Account.objects.get(id=self.kwargs['pk'])
            account_sub.number_of_subscriptions += 1
            account_sub.save()
            account.number_of_subscribers += 1
            account.save()
        return redirect(reverse('account_list', kwargs={'pk': self.kwargs['pk']}))
