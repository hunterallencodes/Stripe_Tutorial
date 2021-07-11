from django.shortcuts import redirect, render, reverse
from django.views.generic import (
    CreateView,
    ListView,
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from .forms import UserRegisterForm
from .mixins import SubscriptionRequiredMixin
from .serializers import UserSerializer
from members.models import Post


User = get_user_model()


class UserAPIView(ListAPIView):
    permission_classes = [AllowAny,]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class MembersAreaView(SubscriptionRequiredMixin, ListView):
    template_name = 'users/members_area.html'
    context_object_name = 'posts'

    def get_queryset(self):
        qs = Post.objects.all()
        return qs


def inactive_subscription(request):
    return render(request, 'users/subscription.html')


class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'

    def get_success_url(self):
        return reverse('users:login')


def landing_page(request):
    if request.user.is_authenticated:
        return redirect('users:profile')
    return render(request, 'landing_page.html')


@login_required
def profile(request):
    context = {
        'user': User.objects.get(username=request.user.username),
    }
    return render(request, 'users/profile.html', context)
