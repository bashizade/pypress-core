# PyPress Core

A Django-based content management system with user management, blog, shop, and site settings.

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
  - Comment system with moderation
  - RESTful API endpoints

- Shop System
  - Product management with variants
  - Category and attribute support
  - Order management
  - Payment integration
  - Shipping management
  - Customer management
  - Virtual product support with course content
  - Chapter and lesson management
  - User progress tracking
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
- Pillow (for image processing)
- django-taggit (for tag management)
- django-ckeditor (for rich text editing)
- drf-nested-routers (for nested API endpoints)
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
- `GET /api/blog/comments/` - List comments
- `POST /api/blog/comments/` - Create comment
- `GET /api/blog/comments/{id}/` - Retrieve comment
- `PUT /api/blog/comments/{id}/` - Update comment
- `DELETE /api/blog/comments/{id}/` - Delete comment

### Shop
- `GET /api/shop/products/` - List products
- `POST /api/shop/products/` - Create product
- `GET /api/shop/products/{id}/` - Retrieve product
- `PUT /api/shop/products/{id}/` - Update product
- `DELETE /api/shop/products/{id}/` - Delete product
- `GET /api/shop/categories/` - List categories
- `POST /api/shop/categories/` - Create category
- `GET /api/shop/categories/{id}/` - Retrieve category
- `PUT /api/shop/categories/{id}/` - Update category
- `DELETE /api/shop/categories/{id}/` - Delete category
- `GET /api/shop/orders/` - List orders
- `POST /api/shop/orders/` - Create order
- `GET /api/shop/orders/{id}/` - Retrieve order
- `PUT /api/shop/orders/{id}/` - Update order
- `DELETE /api/shop/orders/{id}/` - Delete order
- `GET /api/shop/attributes/` - List attributes
- `POST /api/shop/attributes/` - Create attribute
- `GET /api/shop/attributes/{id}/` - Retrieve attribute
- `PUT /api/shop/attributes/{id}/` - Update attribute
- `DELETE /api/shop/attributes/{id}/` - Delete attribute

### Course Content (Virtual Products)
- `GET /api/shop/products/{id}/chapters/` - List chapters
- `POST /api/shop/products/{id}/chapters/` - Create chapter
- `GET /api/shop/products/{id}/chapters/{chapter_id}/` - Retrieve chapter
- `PUT /api/shop/products/{id}/chapters/{chapter_id}/` - Update chapter
- `DELETE /api/shop/products/{id}/chapters/{chapter_id}/` - Delete chapter
- `GET /api/shop/products/{id}/chapters/{chapter_id}/lessons/` - List lessons
- `POST /api/shop/products/{id}/chapters/{chapter_id}/lessons/` - Create lesson
- `GET /api/shop/products/{id}/chapters/{chapter_id}/lessons/{lesson_id}/` - Retrieve lesson
- `PUT /api/shop/products/{id}/chapters/{chapter_id}/lessons/{lesson_id}/` - Update lesson
- `DELETE /api/shop/products/{id}/chapters/{chapter_id}/lessons/{lesson_id}/` - Delete lesson
- `GET /api/shop/progress/` - List user progress
- `POST /api/shop/progress/` - Create progress record
- `GET /api/shop/progress/{id}/` - Retrieve progress
- `PUT /api/shop/progress/{id}/` - Update progress
- `DELETE /api/shop/progress/{id}/` - Delete progress

### Settings
- `GET /api/settings/settings/` - Get site settings
- `PUT /api/settings/settings/{id}/` - Update site settings

## Admin Interface

The project includes a comprehensive admin interface for managing all aspects of the system:

- User Management
  - User creation and editing
  - Role assignment
  - Permission management

- Blog Management
  - Post creation and editing with rich text editor
  - Category management
  - Tag management
  - Comment moderation
  - SEO settings

- Shop Management
  - Product management with variants
  - Category management
  - Attribute management
  - Order management
  - Payment settings
  - Shipping settings
  - Virtual product management
  - Chapter and lesson management
  - User progress tracking

- Site Settings
  - Basic information
  - Contact details
  - Social media links
  - SEO configuration

## Security Features

- Password hashing
- CSRF protection
- XSS protection
- SQL injection protection
- Role-based access control
- Secure file uploads
- Input validation
- API authentication
- Rate limiting

## Performance Features

- Redis caching
- Database query optimization
- Pagination
- Efficient file handling
- Lazy loading
- Image optimization
- API response caching

## SEO Features

- Meta tags support
- SEO-friendly URLs
- Schema.org markup
- Open Graph tags
- Twitter Cards support
- XML sitemap
- Robots.txt configuration

## Development

### Code Style
- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Write docstrings for all functions and classes
- Keep functions small and focused

### Testing
- Write unit tests for all new features
- Use pytest for testing
- Maintain good test coverage
- Run tests before committing

### Git Workflow
- Use feature branches
- Write meaningful commit messages
- Keep commits focused and atomic
- Review code before merging

## License

This project is licensed under the MIT License - see the LICENSE file for details. 