import jingo
import jinja2

from addons.helpers import new_context


@jingo.register.inclusion_tag('versions/version.html')
@jinja2.contextfunction
def version_detail(context, addon, version, src,
                   show_versions_link=True, itemclass='article'):
    return new_context(**locals())


@jingo.register.inclusion_tag('versions/mobile/version.html')
def mobile_version_detail(addon, version, src):
    return locals()
