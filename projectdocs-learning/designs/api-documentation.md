# API Documentation

## Endpoints

### Products
- **GET /api/products**: Retrieve a list of all products.
- **GET /api/products/:id**: Retrieve details of a specific product.
- **POST /api/products**: Create a new product.
- **PUT /api/products/:id**: Update an existing product.
- **DELETE /api/products/:id**: Delete a product.

### Stock
- **GET /api/stock**: Retrieve stock levels for all products.
- **PUT /api/stock/:id**: Update stock level for a specific product.

### Users
- **GET /api/users**: Retrieve a list of all users.
- **GET /api/users/:id**: Retrieve details of a specific user.
- **POST /api/users**: Create a new user.
- **PUT /api/users/:id**: Update an existing user.
- **DELETE /api/users/:id**: Delete a user.

## Authentication
- **POST /api/auth/login**: Authenticate a user and generate a token.
- **POST /api/auth/register**: Register a new user.

## Error Handling
- All endpoints return appropriate HTTP status codes.
- Error responses include a message field with details about the error.
