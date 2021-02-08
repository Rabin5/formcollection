import logging

from django.apps import AppConfig
from django.db import connection


logger = logging.getLogger(__name__)

class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        check = connection.introspection.table_names()
        if 'django_content_type' in  check:
            from django.contrib.contenttypes.models import ContentType
            from .models import GlobalPermission

            content_type, created = ContentType.objects.get_or_create(
                    model="global permission", app_label="users",
                )

            params = [
                {
                    'name': 'COVID Hospital Form Permission',
                    'content_type': content_type,
                    'codename': 'perm_cov_hos_form',
                },
                {
                    'name': 'Province Form Permission',
                    'content_type': content_type,
                    'codename': 'perm_province_form',
                },
                {
                    'name': 'Internal Affairs Form Permission',
                    'content_type': content_type,
                    'codename': 'perm_internal_affairs_form',
                },
                {
                    'name': 'Chief Minister Form Permission',
                    'content_type': content_type,
                    'codename': 'perm_chief_minister_form',
                },
                {
                    'name': 'Local Level Form Permission',
                    'content_type': content_type,
                    'codename': 'perm_local_level_form',
                },
                {
                    'name': '(Approve) COVID Hospital Form Permission',
                    'content_type': content_type,
                    'codename': 'perm_cov_hos_form_approve',
                },
                {
                    'name': '(Approve) Province Form Permission',
                    'content_type': content_type,
                    'codename': 'perm_province_form_approve',
                },
                {
                    'name': '(Approve) Internal Affairs Form Permission',
                    'content_type': content_type,
                    'codename': 'perm_internal_affairs_form_approve',
                },
                {
                    'name': '(Approve) Chief Minister Form Permission',
                    'content_type': content_type,
                    'codename': 'perm_chief_minister_form_approve',
                },
                {
                    'name': '(Approve) Local Level Form Permission',
                    'content_type': content_type,
                    'codename': 'perm_local_level_form_approve',
                },
                {
                    'name': 'Master Data Permission',
                    'content_type': content_type,
                    'codename': 'perm_master_data',
                },
            ]
            
            for param in params:
                try:
                    gp = GlobalPermission.objects.get(codename=param['codename'])
                except:
                    new_gp = GlobalPermission.objects.create(**param)
                    logger.info(f"Creating permission: { new_gp }")
                    new_gp.save()
