# geoadmingeocoder readme
2011-07-05
Bill Morris

# Purpose
provides a geocoder for the "Add Feature" function in a modified version of the geodjango geographic administrator application

# Project Components
## Django Geocoder Service Requests
A stripped-down django backend for calling to geocoding services, including
- __init__.py
- urls.py
- views.py

## Web Interface
A simple address dialog built on top of the geographic_admin (http://code.google.com/p/geodjango-basic-apps/wiki/GeographicAdminQuickStart) map when adding a new feature to any existing layers

# Dependencies
- Geodjango
- GDAL
- Internet connectivity
