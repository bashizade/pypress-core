# PyPress Core

A Django-based content management system with user management, blog, shop, and site settings.

## Features

- User Management
  - Custom user model with additional fields (mobile, national code, birth date, etc.)
  - Role-based access control
  - User authentication and authorization
  - RESTful API endpoints
  - User profile management

- Blog System
  - Post management with rich text editor (CKEditor)
  - Category and tag support
  - SEO-friendly URLs and meta tags
  - Custom meta fields support
  - Comment system with moderation
  - RESTful API endpoints
  - Nested routing for comments

- Shop System
  - Product management with variants
  - Category and attribute support
  - Order management
  - Payment integration
  - Shipping management with zones
  - Customer management
  - Virtual product support with course content
  - Chapter and lesson management
  - User progress tracking
  - Discount code system
  - RESTful API endpoints
  - Nested routing for product resources

- Site Settings
  - Basic site information
  - Contact information
  - Social media links
  - SEO settings
  - RESTful API endpoints

## Project Structure

```
pypress-core/
├── api/                 # API configuration
├── blog/               # Blog application
├── core/               # Core project settings
├── settings/           # Site settings application
├── shop/               # Shop application
├── users/              # User management application
├── manage.py           # Django management script
├── requirements.txt    # Project dependencies
└── README.md          # Project documentation
```

## Requirements

- Python 3.8+
- Django 5.0+
- Django REST Framework 3.15+
- Pillow 10.0+ (for image processing)
- django-taggit 5.0+ (for tag management)
- django-ckeditor 6.7+ (for rich text editing)
- drf-nested-routers 0.94+ (for nested API endpoints)
- django-allauth 0.61+ (for authentication)
- django-redis 5.4+ (for caching)
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

### Users API (`/api/users/`)
- `GET /` - List users
- `POST /` - Create user
- `GET /{id}/` - Retrieve user
- `PUT /{id}/` - Update user
- `DELETE /{id}/` - Delete user
- `GET /profile/` - Get/Update user profile

### Blog API (`/api/blog/`)
- `GET /categories/` - List categories
- `POST /categories/` - Create category
- `GET /categories/{id}/` - Retrieve category
- `PUT /categories/{id}/` - Update category
- `DELETE /categories/{id}/` - Delete category
- `GET /posts/` - List posts
- `POST /posts/` - Create post
- `GET /posts/{id}/` - Retrieve post
- `PUT /posts/{id}/` - Update post
- `DELETE /posts/{id}/` - Delete post
- `GET /posts/{post_id}/comments/` - List comments
- `POST /posts/{post_id}/comments/` - Create comment
- `GET /posts/{post_id}/comments/{id}/` - Retrieve comment
- `PUT /posts/{post_id}/comments/{id}/` - Update comment
- `DELETE /posts/{post_id}/comments/{id}/` - Delete comment

### Shop API (`/api/shop/`)
- `GET /categories/` - List categories
- `POST /categories/` - Create category
- `GET /categories/{id}/` - Retrieve category
- `PUT /categories/{id}/` - Update category
- `DELETE /categories/{id}/` - Delete category
- `GET /products/` - List products
- `POST /products/` - Create product
- `GET /products/{id}/` - Retrieve product
- `PUT /products/{id}/` - Update product
- `DELETE /products/{id}/` - Delete product
- `GET /products/{product_id}/variants/` - List variants
- `POST /products/{product_id}/variants/` - Create variant
- `GET /products/{product_id}/chapters/` - List chapters
- `POST /products/{product_id}/chapters/` - Create chapter
- `GET /products/{product_id}/chapters/{chapter_id}/lessons/` - List lessons
- `POST /products/{product_id}/chapters/{chapter_id}/lessons/` - Create lesson
- `GET /products/{product_id}/reviews/` - List reviews
- `POST /products/{product_id}/reviews/` - Create review
- `GET /users/{user_id}/orders/` - List user orders
- `POST /users/{user_id}/orders/` - Create order
- `GET /users/{user_id}/cart/` - Get user cart
- `POST /users/{user_id}/cart/items/` - Add item to cart
- `POST /validate-discount-code/` - Validate discount code

### Settings API (`/api/settings/`)
- `GET /settings/` - Get site settings
- `PUT /settings/{id}/` - Update site settings

## Admin Interface

The project includes a comprehensive admin interface for managing all aspects of the system:

- User Management
  - User creation and editing
  - Role assignment
  - Permission management
  - Profile management

- Blog Management
  - Post creation and editing with CKEditor
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
  - Shipping settings with zones
  - Discount code management
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
- Secure password reset
- Session management

## Performance Features

- Redis caching
- Database query optimization
- Pagination
- Efficient file handling
- Lazy loading
- Image optimization
- API response caching
- Nested resource optimization

## SEO Features

- Meta tags support
- SEO-friendly URLs
- Schema.org markup
- Open Graph tags
- Twitter Cards support
- XML sitemap
- Robots.txt configuration
- Custom meta fields

## Development

### Code Style
- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Write docstrings for all functions and classes
- Keep functions small and focused
- Use type hints where appropriate

### Testing
- Write unit tests for all new features
- Use pytest for testing
- Maintain good test coverage
- Run tests before committing
- Include integration tests

### Git Workflow
- Use feature branches
- Write meaningful commit messages
- Keep commits focused and atomic
- Review code before merging
- Follow semantic versioning

## License

This project is licensed under the MIT License - see the LICENSE file for details. 