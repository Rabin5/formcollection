import logging

from django.apps import AppConfig
from django.db import connection

logger = logging.getLogger(__name__)


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        check = connection.introspection.table_names()
        if 'django_content_type' in check:
            from django.contrib.contenttypes.models import ContentType
            from .models import GlobalPermission
            from django.contrib.auth.models import Group

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
                    'name': 'Collection Six Form Permission',
                    'content_type': content_type,
                    'codename': 'perm_collection_six_form',
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
                    'name': '(Approve) Collection Six Form Permission',
                    'content_type': content_type,
                    'codename': 'collection_six_form_approve',
                },
                {
                    'name': 'Master Data Permission',
                    'content_type': content_type,
                    'codename': 'perm_master_data',
                },
                {
                    'name': 'User Management Permission',
                    'content_type': content_type,
                    'codename': 'perm_user_management',
                },

            ]

            for param in params:
                if 'Approve' in param['name']:
                    grp_name = param['name'].replace('Permission', '')
                else:
                    grp_name = param['name'].replace('Permission', 'Operator')
                new_group, created = Group.objects.get_or_create(name=grp_name)
                admin_grp, is_created = Group.objects.get_or_create(
                    name='ADMIN')
                if not created:
                    new_group.save()
                if not is_created:
                    admin_grp.save()
                try:
                    perm = GlobalPermission.objects.get(
                        codename=param['codename'])
                    new_group.permissions.add(perm)
                    admin_grp.permissions.add(perm)
                except:
                    new_perm = GlobalPermission.objects.create(**param)
                    logger.info(f"Creating permission: { new_perm }")
                    new_perm.save()
                    new_group.permissions.add(new_perm)
                    admin_grp.permissions.add(new_perm)
