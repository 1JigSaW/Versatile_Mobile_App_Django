"""
WSGI config for pizzaproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pizzaproject.settings')

application = get_wsgi_application()

<VirtualHost *:80>
  ServerName localhost
  ServerAdmin webmaster@localhost
Alias /static /var/www/venv/BookProject/pizzaproject/static
<Directory /var/www/venv/BookProject/pizzaproject/static>
   Require all granted
</Directory>
Alias /media /var/www/venv/BookProject/pizzaproject/media
<Directory /var/www/venv/BookProject/pizzaproject/media>
   Require all granted
</Directory>
<Directory /var/www/venv/BookProject/pizzaproject/pizzaproject>
    <Files wsgi.py>
        Require all granted
    </Files>
</Directory>
WSGIDaemonProcess home python-path=/var/www/venv/BookProject/
pizzaproject/:/var/www/venv/lib/python3.6/site-packages
WSGIProcessGroup home
WSGIScriptAlias / /var/www/venv/BookProject/pizzaproject/
pizzaproject/wsgi.py
ErrorLog ${APACHE_LOG_DIR}/error.log
CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>