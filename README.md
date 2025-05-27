# PyPress Core - Modern Python CMS

PyPress Core is a high-performance, secure, and SEO-optimized Content Management System built with Python, Django, and Django REST Framework. It provides a robust foundation for building modern web applications with pre-built templates and extensive customization options.

## 🌟 Key Features

- **High Performance**
  - Redis caching integration
  - Optimized database queries
  - Efficient resource management
  - CDN-ready static file serving

- **Enhanced Security**
  - Two-factor authentication (2FA)
  - JWT-based API authentication
  - CSRF, XSS, and SQL injection protection
  - Rate limiting and CORS policies
  - Secure password hashing

- **SEO Optimization**
  - Clean URL structures
  - Automated sitemap generation
  - Meta tags management
  - Open Graph and Twitter Card support
  - Mobile-responsive design
  - Image optimization

- **Core Modules**
  - User Management System
  - Blog Platform
  - E-commerce Store
  - Notification System
  - Analytics Dashboard
  - Site Settings

- **Developer-Friendly**
  - RESTful API with comprehensive documentation
  - Pre-built Tailwind CSS templates
  - WebSocket support for real-time features
  - Multilingual support (English & Persian)
  - Extensive test coverage

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- PostgreSQL 13 or higher
- Redis 6 or higher
- Node.js 16 or higher (for Tailwind CSS)

### Installation

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

4. Create environment file:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` with your configuration.

5. Initialize the database:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

Visit http://localhost:8000/admin to access the admin panel.

## 📚 Documentation

### API Endpoints

#### Authentication
- `POST /api/v1/auth/register/` - User registration
- `POST /api/v1/auth/login/` - User login
- `POST /api/v1/auth/logout/` - User logout
- `POST /api/v1/auth/token/refresh/` - Refresh JWT token

#### Users
- `GET /api/v1/users/me/` - Get current user profile
- `PUT /api/v1/users/me/` - Update user profile
- `POST /api/v1/users/me/change-password/` - Change password

#### Blog
- `GET /api/v1/blog/posts/` - List blog posts
- `POST /api/v1/blog/posts/` - Create blog post
- `GET /api/v1/blog/posts/{id}/` - Get blog post
- `PUT /api/v1/blog/posts/{id}/` - Update blog post
- `DELETE /api/v1/blog/posts/{id}/` - Delete blog post

#### Store
- `GET /api/v1/store/products/` - List products
- `GET /api/v1/store/products/{id}/` - Get product details
- `POST /api/v1/store/orders/` - Create order
- `GET /api/v1/store/orders/` - List user orders

For complete API documentation, visit `/api/docs/` after starting the server.

### Template Customization

Templates are built with Tailwind CSS and can be customized in the `templates` directory:

```
templates/
├── base.html
├── blog/
│   ├── list.html
│   └── detail.html
├── store/
│   ├── products.html
│   └── checkout.html
└── users/
    ├── profile.html
    └── settings.html
```

## 🔒 Security Features

- HTTPS enforcement
- Secure session handling
- CSRF protection
- XSS prevention
- SQL injection protection
- Rate limiting
- 2FA support
- Password strength validation
- CORS policies

## 🔧 Configuration

Key settings can be configured through environment variables:

```env
DEBUG=False
SECRET_KEY=your-secret-key
DATABASE_URL=postgres://user:password@localhost:5432/dbname
REDIS_URL=redis://localhost:6379/0
EMAIL_HOST=smtp.yourprovider.com
EMAIL_PORT=587
EMAIL_HOST_USER=your@email.com
EMAIL_HOST_PASSWORD=your-password
```

## 📈 Performance Optimization

- Redis caching for frequently accessed data
- Database query optimization
- Static file compression and caching
- Image optimization and lazy loading
- CDN support for static files

## 🌐 Deployment

Recommended deployment stack:
- Gunicorn as WSGI server
- Nginx as reverse proxy
- PostgreSQL for database
- Redis for caching
- Celery for background tasks

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Django and Django REST Framework communities
- Tailwind CSS team
- All contributors and users of PyPress Core 