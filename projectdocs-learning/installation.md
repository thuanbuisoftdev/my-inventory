# Installation

## Prerequisites
- Node.js (v14 or higher)
- npm (v6 or higher)
- Git

## Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/inventory-management.git
    ```
2. Navigate to the project directory:
    ```bash
    cd inventory-management
    ```
3. Install dependencies:
    ```bash
    npm install
    ```
4. Set up environment variables:
    ```bash
    cp .env.example .env
    ```
    Edit the `.env` file to configure your database and other settings.

5. Run database migrations:
    ```bash
    npm run migrate
    ```

6. Start the application:
    ```bash
    npm start
    ```

## Running Tests
To run the test suite, use the following command:
```bash
npm test
```
