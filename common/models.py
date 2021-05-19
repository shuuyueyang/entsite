#from __future__ import unicode_literals
from django.db import models
#from future.builtins import str
#from future.utils import with_metaclass

from json import loads
try:
    from urllib.request import urlopen
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlopen, urlencode

from django.apps import apps
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.db.models.base import ModelBase
from django.template.defaultfilters import truncatewords_html
#from django.utils.encoding import python_2_unicode_compatible
from django.utils.html import strip_tags
from django.utils.timesince import timesince
from django.utils.timezone import now
from django.utils.translation import ugettext, ugettext_lazy as _

class MetaData(models.Model):
    """
    Abstract model that provides meta data for content.
    """

    # _meta_title = models.CharField(_("HTML Page Title"), null=True, blank=True,
        # max_length=500,
        # help_text=_("Optional title to be used in the HTML title tag. "
                    # "If left blank, the main title field will be used."))
    _meta_description = models.TextField(_("HTML Page Description"), blank=True)
    # gen_description = models.BooleanField(_("Generate description"),
        # help_text=_("If checked, the description will be automatically "
                    # "generated from content. Uncheck if you want to manually "
                    # "set a custom description."), default=True)
    _meta_keywords = models.CharField(_("HTML Page Keywords"), null=True, blank=True,
        max_length=500,
        help_text=_("Optional keywords to be used in the HTML title tag. "
                    "If left blank, the main keywords field will be used."))

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """
        Set the description field on save.
        """
        #if self.gen_description:
        #    self.description = strip_tags(self.description_from_content())
        super(MetaData, self).save(*args, **kwargs)

    def meta_title(self):
        """
        Accessor for the optional ``_meta_title`` field, which returns
        the string version of the instance if not provided.
        """
        return self._meta_title or getattr(self, "title", str(self))

    def description_from_content(self):
        """
        Returns the first block or sentence of the first content-like
        field.
        """
        description = ""
        # Use the first RichTextField, or TextField if none found.
        for field_type in (RichTextField, models.TextField):
            if not description:
                for field in self._meta.get_fields():
                    if (isinstance(field, field_type) and
                            field.name != "description"):
                        description = getattr(self, field.name)
                        if description:
                            from mezzanine.core.templatetags.mezzanine_tags \
                                                    import richtext_filters
                            description = richtext_filters(description)
                            break
        # Fall back to the title if description couldn't be determined.
        if not description:
            description = str(self)
        # Strip everything after the first block or sentence.
        ends = ("</p>", "<br />", "<br/>", "<br>", "</ul>",
                "\n", ". ", "! ", "? ")
        for end in ends:
            pos = description.lower().find(end)
            if pos > -1:
                description = TagCloser(description[:pos]).html
                break
        else:
            description = truncatewords_html(description, 100)
        try:
            description = unicode(description)
        except NameError:
            pass  # Python 3.
        return description

# Create your models here.
class TimeStamped(models.Model):
    """
    Provides created and updated timestamps on models.
    """

    class Meta:
        abstract = True

    _created_date = models.DateTimeField(null=True, editable=False)
    _updated_date = models.DateTimeField(null=True, editable=False)

    def save(self, *args, **kwargs):
        _now = now()
        self._updated_date = _now
        if not self.id:
            self._created_date = _now
        super(TimeStamped, self).save(*args, **kwargs)