from django.contrib import admin


from forms import models

admin.site.register([
    models.RiskAllowance,
])
