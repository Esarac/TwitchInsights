# Twitch Insight Studio 🎥

Data Engineering project to analyse my streams 💪

## Instructions (Out of date)

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

## Notes

- [How to connect sql server container](https://stackoverflow.com/questions/47984603/using-sql-server-management-studio-to-remote-connect-to-docker-container)
- Check container for MySql
- Migrate database from local to container
- Connect to PySpark ✅
- Containarize python scripts (Consumers, Producers and Pipeline).
- Connect with BI Tool
- Update README.md
- Think of which graphs we want (To know what data do we need):
  - Viewers vs/and chatters per stream (Linechart)
  - Viewers who are the most active (Barchar)
  - Subscribers vs Followers vs Just Watching (Piechart)
  - Top most used words (Barchar?)
  - Hour with more views (Barchar,Line)
  - More relevant topic (?)
