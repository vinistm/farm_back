from django.contrib.gis.db import models
from django.utils.translation import gettext as _


class Farm(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=255,
                            null=False, blank=True)

    geometry = models.GeometryField(verbose_name=_("Geometry"),
                                    null=True, blank=True)

    area = models.FloatField(verbose_name=_("Area"),
                             blank=True, null=True)

    centroid = models.PointField(verbose_name=_("Centroid"),
                                 blank=True, null=False)
    municipality = models.CharField(verbose_name=_("Municipality"), max_length=120,
                                 blank=True, null=False)
    state = models.CharField(verbose_name=_("State"), max_length=50,
                                 blank=True, null=True)

    creation_date = models.DateTimeField(verbose_name=_("Creation date"),
                                         auto_now_add=True, editable=False)

    last_modification_date = models.DateTimeField(
        verbose_name=_("Last modification date"), auto_now=True)

    is_active = models.BooleanField(verbose_name=_("Is Active"), default=True)
    
    owner = models.ForeignKey('farm_base.Owner', on_delete = models.CASCADE, related_name = 'Farm', null=False)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['id']
        verbose_name = _('Farm')
        verbose_name_plural = _('Farms')
