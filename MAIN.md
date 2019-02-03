# Django Billd by Texmith Technologies

Simple Django Billing and Invoice App with Django.

## Architecture

### Overview

Billd uses a client/server Model Approach to the architechture.

1. Defining Scope
   1. Multi Tenant
   2. Flatpages
   3. Sitemaps
   4. LocMemCache
   5. Responsive
   6. Invoice Autogenerate
   7. Custom Invoice Templates(Samples provided)
   8. Tenant Subscription
   9. Billing Management
   10. Product Mangement
       1.  Product Type CRUD.
       2.  Product Variant CRUD.
       3.  Stock CRUD
   11. History
   12. Payment Gateway
   13. App Instance - Heroku
   14. Static Storages - Heroku(Whitenoise)
   15. Advertisement Management for SuperAdmin
   16. Analytics

### Expected Result

Simple Django based Billing & Invoice on the Cloud with Multi Tenancy to enable Texmith to sell subscriptions or add organizations.

### Components

1. PostgreSQL 11.1+
2. Django 2.1.5+
3. Jinja 2+
4. NgninX
5. uWSGI
6. Django Debug Toolbar
7. Django Compressor
8. Django Rest Framework
9. Django Extensions
10. Django Environ
11. Django Multi Tenants
