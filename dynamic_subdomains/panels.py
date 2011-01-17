from debug_toolbar.panels import DebugPanel

from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

class SubdomainPanel(DebugPanel):
    """
    Panel that allows you to alter the subdomain you are viewing the site
    without /etc/hosts hacks.
    """

    name = 'Subdomain'
    has_content = True

    def nav_title(self):
        return _("Subdomain")

    def nav_subtitle(self):
        return self.domain

    def url(self):
        return ''

    def title(self):
        return _("Subdomain navigation")

    def content(self):
        return render_to_string('subdomains/panel.html', self.context)

    def process_request(self, request):
        self.domain = request.COOKIES.get('_domain')

        request.META.pop('HTTP_HOST', '')
        if self.domain:
            request.META['HTTP_HOST'] = self.domain