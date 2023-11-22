# Assenment

Note: REQUIREMENTS( also specified in requirements.txt),

REQUIREMENTS:

Python 3
MySQL
Django (install by PIP 'pip install django' and install 'pip install djangorestframework')
MySQL db (install by PIP 'pip install mysqlclient' and create database name'vendor_management_db' or configure the database)

Steps to run application:
first, run the commands 'python manage.py makemigrations' and 'python manage.py migrate' to create the tables
Create admin by using 'python manage.py createsuperuser' to reference and to run the server 'python manage.py runserver'
first create the records for vendors follow the urls as specefied 
http://127.0.0.1:8000/vendors/              To create and get the vendor
http://127.0.0.1:8000/vendors/id               To get-details,update,delete vendor

and to create the Purchase Order records
http://127.0.0.1:8000/purchase_orders/?vendor=id              To get purchase orders by vendor id and to create purchase orders
http://127.0.0.1:8000/purchase_orders/id                To get,update, or to delete the purchase order
http://127.0.0.1:8000/vendors/vendor_id/performance             To get performance of vendor
http://127.0.0.1:8000/purchase_orders/id/acknowledge                To update the acknowledgement

By using these URL's you can perform needed operations.

