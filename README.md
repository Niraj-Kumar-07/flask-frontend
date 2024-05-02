# Coin Flip Flask App

This is a simple Flask application that simulates flipping a coin. It is dockerized and utilizes Gunicorn as the WSGI server and Nginx as a load balancer.

## Usage

1. Clone the repository:

2. Navigate to the project directory:

3. Build and run the Docker containers:
   docker-compose up --build

4. Open a web browser and go to `http://localhost` to view the application.

## Architecture

- **Flask App**: The core application is built with Flask, a lightweight WSGI web application framework.
- **Gunicorn**: Gunicorn is used as the WSGI server to handle incoming HTTP requests efficiently.
- **Nginx Load Balancer**: Nginx acts as a load balancer to distribute incoming traffic across multiple Gunicorn worker processes, improving the application's scalability and reliability.
- **Docker Compose**: Docker Compose is used to define and run multi-container Docker applications. It simplifies the process of managing and orchestrating the different components of the application.

## Configuration

The Nginx configuration is provided in the `nginx.conf` file. Adjustments can be made to this file to customize Nginx's behavior according to your specific requirements.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

[MIT License](LICENSE)
```

This README provides a brief overview of the application's architecture, usage instructions, and configuration details. You can further expand it with specific details about the Flask app or any additional features. Let me know if you need more assistance!
