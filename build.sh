#!/usr/bin/env bash
# exit on error
set -o errexit

# প্রয়োজনীয় প্যাকেজ ইনস্টল এবং স্ট্যাটিক ফাইল কালেকশন
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
export DJANGO_SETTINGS_MODULE="myapp.settings"
# 🎯 এই কোডটুকু অটোমেটিক অনলাইনে আপনার এডমিন অ্যাকাউন্ট বানিয়ে দেবে
python -c "
import django
django.setup()
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'Ratul@2026')
    print('Superuser created successfully!')
else:
    print('Superuser already exists.')
"
