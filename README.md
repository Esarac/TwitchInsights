# Twitch Insight Studio 🎥

Data Engineering project to analyse my streams 💪

## Instructions

1. Download docker desktop.
2. Download Sql Server and configure server (users, logins, schemas).
3. Run DLL script on your database. **(Probably better idea to create a container for the DB)**
4. Create the .env file with the following variables:

    - CLIENT_ID
    - CLIENT_SECRET
    - ESARAC_TOKEN

    - DB_SERVER
    - DB_DATABASE
    - DB_USERNAME
    - DB_PASSWORD

5. Run docker-compose command.

    ```sh
    docker-compose up -d
    ```

6. Run producer_chat.py and consumer_chat.py in different consoles.

    ```sh
    # To run the producer
    py producer_chat.py
    ```

    ```sh
    # To run the consumer
    py consumer_chat.py
    ```
