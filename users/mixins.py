from django.shortcuts import redirect


class SubscriptionRequiredMixin:
    """Verify that the current user has an active subscription."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.subscription.is_active:
            return redirect('users:subscribe')
        return super().dispatch(request, *args, **kwargs)
