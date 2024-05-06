# DeepLX API Load Balancer

[中文](./README-zh.md)

This project is a load balancer built using the Flask framework, designed to provide stable and efficient translation services through multiple free DeepLX translation API endpoints. By dynamically detecting and selecting endpoints with the lowest latency, this project optimizes the speed and reliability of translation requests.

## Features

- **Dynamic Endpoint Detection**: Automatically detects and selects translation endpoints with the lowest latency.
- **Load Balancing**: Distributes translation requests evenly across endpoints using a cyclic iterator, ensuring balanced load on each service endpoint.
- **Fault Tolerance**: Handles failures of service endpoints to ensure high availability of the service.
- **CORS Support**: Supports cross-origin requests, facilitating integration with various frontend applications.

## Technology Stack

- **Python**: Developed using the Python programming language.
- **Flask**: Utilizes the Flask framework to create a lightweight web server.
- **Docker**: Supports Docker containerization to simplify deployment and operational tasks.

## Quick Start

### Building and Running the Docker Container

1. Clone the repository to your local machine:
   ```bash
   git clone https://your-repository-url.git
   cd your-repository-directory
   ```

2. Build the Docker image:
   ```bash
   docker build --no-cache -t deeplx .
   ```

3. Run the Docker container:
   ```bash
   docker run -dit -p 1188:1188 --name deeplx deeplx:latest
   ```

### Using the API

Send a POST request to the `/translate` endpoint with the following JSON data:

```json
{
    "text": "Hello, world!",
    "source_lang": "EN",
    "target_lang": "ZH"
}
```

### Results

A successful response will return the translated text.

## Development and Maintenance

### Dependencies

Ensure that `requirements.txt` includes all necessary Python packages. Key dependencies include:

- `flask`
- `requests`

### Contributing

Contributions via Pull Requests or Issues for code improvements and feature suggestions are welcome.

## License

This project is licensed under the MIT License. For more details, please refer to the `LICENSE` file.

---

By using this project, you can easily integrate and utilize multiple DeepLX translation APIs, enjoying the efficiency and stability provided by load balancing.