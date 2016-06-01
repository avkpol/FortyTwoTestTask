
from django import template
from django.core import urlresolvers
from django.contrib.contenttypes.models import ContentType

register = template.Library()

@register.simple_tag
def get_admin_url(obj):
    content_type = ContentType.objects.get_for_model(obj.__class__)
    return urlresolvers.reverse("admin:%s_%s_change"
                                %(content_type.app_label,
                                  content_type.model),
                                args=(obj.id,)
                                )

