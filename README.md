# Twitch Insight Studio 🎥

Data Engineering project to analyse my streams 💪

## Instructions

1. Download docker desktop.
2. Create the .env file with the following variables:

    - CLIENT_ID
    - CLIENT_SECRET
    - ESARAC_TOKEN

3. Run docker-compose command.

    ```sh
    docker-compose up -d
    ```

4. Run producer.py and consumer.py in different consoles.

    ```sh
    # To run the producer
    py producer.py
    ```

    ```sh
    # To run the consumer
    py consumer.py
    ```
