from django.conf.urls import url, include

from .views import (
    LogInView, ResendActivationCodeView, RemindUsernameView, SignUpView, ActivateView, LogOutView,
    ChangeEmailView, ChangeEmailActivateView, ChangeProfileView, ChangePasswordView,
    RestorePasswordView, RestorePasswordDoneView, RestorePasswordConfirmView,
)

app_name = 'accounts'

urlpatterns = [
    url(r'^log-in/', LogInView.as_view(), name='log_in'),
    url(r'^log-out/', LogOutView.as_view(), name='log_out'),

    url(r'^resend/activation-code/', ResendActivationCodeView.as_view(), name='resend_activation_code'),

    url(r'^sign-up/', SignUpView.as_view(), name='sign_up'),
    url(r'^activate/<code>/', ActivateView.as_view(), name='activate'),

    url(r'^restore/password/', RestorePasswordView.as_view(), name='restore_password'),
    url(r'^restore/password/done/', RestorePasswordDoneView.as_view(), name='restore_password_done'),
    url(r'^restore/<uidb64>/<token>/', RestorePasswordConfirmView.as_view(), name='restore_password_confirm'),

    url(r'^remind/username/', RemindUsernameView.as_view(), name='remind_username'),

    url(r'^change/profile/', ChangeProfileView.as_view(), name='change_profile'),
    url(r'^change/password/', ChangePasswordView.as_view(), name='change_password'),
    url(r'^change/email/', ChangeEmailView.as_view(), name='change_email'),
    url(r'^change/email/<code>/', ChangeEmailActivateView.as_view(), name='change_email_activation'),
]
