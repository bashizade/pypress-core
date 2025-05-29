# PyPress Core

A Django-based content management system with user management, blog, and site settings.

## Features

- User Management
  - Custom user model with additional fields
  - Role-based access control
  - User authentication and authorization
  - RESTful API endpoints

- Blog System
  - Post management with rich text editor
  - Category and tag support
  - SEO-friendly URLs and meta tags
  - Custom meta fields support
  - RESTful API endpoints

- Site Settings
  - Basic site information
  - Contact information
  - Social media links
  - SEO settings
  - RESTful API endpoints

## Requirements

- Python 3.8+
- Django 5.0+
- Redis (for caching)
- Other dependencies listed in requirements.txt

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/pypress-core.git
cd pypress-core
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## API Endpoints

### Users
- `GET /api/users/` - List users
- `POST /api/users/` - Create user
- `GET /api/users/{id}/` - Retrieve user
- `PUT /api/users/{id}/` - Update user
- `DELETE /api/users/{id}/` - Delete user
- `GET /api/users/me/` - Get current user

### Blog
- `GET /api/blog/posts/` - List posts
- `POST /api/blog/posts/` - Create post
- `GET /api/blog/posts/{id}/` - Retrieve post
- `PUT /api/blog/posts/{id}/` - Update post
- `DELETE /api/blog/posts/{id}/` - Delete post
- `GET /api/blog/categories/` - List categories
- `POST /api/blog/categories/` - Create category
- `GET /api/blog/categories/{id}/` - Retrieve category
- `PUT /api/blog/categories/{id}/` - Update category
- `DELETE /api/blog/categories/{id}/` - Delete category

### Settings
- `GET /api/settings/settings/` - Get site settings
- `PUT /api/settings/settings/{id}/` - Update site settings

## Security Features

- Password hashing
- CSRF protection
- XSS protection
- SQL injection protection
- Role-based access control
- Secure file uploads
- Input validation

## Performance Features

- Redis caching
- Database query optimization
- Pagination
- Efficient file handling
- Lazy loading

## SEO Features

- Meta tags support
- SEO-friendly URLs
- Schema.org markup
- Open Graph tags
- Twitter Cards support

## License

This project is licensed under the MIT License - see the LICENSE file for details. 