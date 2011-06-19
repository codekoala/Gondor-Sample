from django.db import models

pif = lambda *args: models.PositiveIntegerField(*args)

class FitTest(models.Model):
    switch_kicks = pif()
    power_jacks = pif()
    power_knees = pif()
    power_jumps = pif()
    globe_jumps = pif()
    suicide_jumps = pif()
    push_up_jacks = pif()
    low_plank_oblique = pif()

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('date_created',)
