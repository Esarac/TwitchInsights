# MusicInsights

Data Engineering project to analyse users music taste 😎

## Instructions

1. Download docker desktop.
2. Download [offset explorer](https://kafkatool.com/download.html) (GUI Kafka tool).
3. Run docker-compose command.

    ```sh
    docker-compose up -d
    ```

4. Open Offset Explorer &rarr; Add new connection &rarr; Add with the following parameters

| Parameter | Value |
|---|---|
| Cluster Name | MusicInsightCluster |
| Bootstrap Server | localhost:29092 |
