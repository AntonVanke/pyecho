#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import django


if __name__ == '__main__':
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Pyecho.settings')
    django.setup()

    from Admin import models

    # 测试mysql
    print(models.Users.objects.filter(username="ser").__len__() == 0)

