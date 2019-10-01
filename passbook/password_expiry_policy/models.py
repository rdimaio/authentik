"""passbook password_expiry_policy Models"""
from datetime import timedelta

from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext as _
from structlog import get_logger

from passbook.core.models import Policy, PolicyResult, User

LOGGER = get_logger(__name__)


class PasswordExpiryPolicy(Policy):
    """If password change date is more than x days in the past, call set_unusable_password
    and show a notice"""

    deny_only = models.BooleanField(default=False)
    days = models.IntegerField()

    form = 'passbook.password_expiry_policy.forms.PasswordExpiryPolicyForm'

    def passes(self, user: User) -> PolicyResult:
        """If password change date is more than x days in the past, call set_unusable_password
        and show a notice"""
        actual_days = (now() - user.password_change_date).days
        days_since_expiry = (now() - (user.password_change_date + timedelta(days=self.days))).days
        if actual_days >= self.days:
            if not self.deny_only:
                user.set_unusable_password()
                user.save()
                message = _(('Password expired %(days)d days ago. '
                             'Please update your password.') % {
                                 'days': days_since_expiry
                             })
                return PolicyResult(False, message)
            return PolicyResult(False, _('Password has expired.'))
        return PolicyResult(True)

    class Meta:

        verbose_name = _('Password Expiry Policy')
        verbose_name_plural = _('Password Expiry Policies')
