# Development Guide

## Code Structure
- **src/**: Contains the source code of the application.
- **tests/**: Contains the test cases for the application.
- **config/**: Contains configuration files.

## Branching Strategy
- **main**: The main branch contains the stable version of the code.
- **develop**: The develop branch contains the latest development changes.
- **feature/**: Feature branches are created from develop for new features.
- **bugfix/**: Bugfix branches are created from develop for bug fixes.

## Code Style
- Follow the [Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript).
- Use ESLint to enforce code quality.

## Commit Messages
- Use meaningful commit messages.
- Follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification.

## Pull Requests
- Ensure all tests pass before creating a pull request.
- Provide a clear description of the changes in the pull request.
- Request reviews from at least two team members.

## Testing
- Write unit tests for all new features and bug fixes.
- Use Jest as the testing framework.
- Run tests using the following command:
    ```bash
    npm test
    ```

## Deployment
- Use Docker for containerization.
- Create a Docker image using the following command:
    ```bash
    docker build -t inventory-management .
    ```
- Run the Docker container using the following command:
    ```bash
    docker run -p 3000:3000 inventory-management
    ```
