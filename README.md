# Django URL Shortener Project + DRF API Integration

## Project Description

This project is a **URL Shortener** application that allows users to shorten long URLs. Built with Django, it stores long URLs along with their corresponding short codes in the database. When a user accesses the short URL, the system automatically redirects to the original long URL.

The project is extended with an API developed using **Django Rest Framework (DRF)**, enabling interaction with URL data through HTTP requests.

---

## Features

- Accepts a long URL and generates a random short code to save in the database.
- Redirects to the original long URL when the short version is visited.
- Allows viewing all saved URL records through the admin panel.
- Simple and functional user interface.
- DRF API integration includes:
  - Creating a new short URL record (POST)
  - Listing all stored URLs (GET)
  - Deleting a specific URL record (DELETE)
  - Querying a short URL to retrieve its long version
