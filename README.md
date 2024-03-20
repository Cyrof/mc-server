# Minecraft Server with Docker and Backup Script
This repository hosts a Minecraft server setup utilizing Docker and Docker Compose, providing flexibility for deployment with or without port forwarding. Additionally, It includes a backup script to automate the process of backing up Minecraft server data.

## Docker Setup
### Docker Compose Files
- **docker-compose-ngrok.yaml**: This file sets up the Minecraft server along with an Ngrok container, allowing for for easy access to the server without the need for port forwarding. The Minecraft container is connected to the same Ngrok container, ensuring seamless integration. <br>
**IMPORTANT** Change the `<ngrok authtoken>` to your own ngrok token
``` yaml
environment:
      - NGROK_AUTHTOKEN=<ngrok authtoken>
```

- **docker-compose-pf.yaml**: This file sets up the Minecraft server without Ngrok. Users are required to port forward the default Minecraft port (25565) on their router for external access.

### Usage
To start the server, simply run: 
``` bash
$ docker-compose -f <docker-compose-file> up -d
```
If you preder using Docker directly for port forwarding, you can use the following command:
```bash
$ docker run -d -p 25565:25565 -e EULA=TRUE -v <server_path>:/data itzg/minecraft-server
```
**IMPORTANT** change the <server_path> to the path of your minecraft server to link to docker container. Please ensure that you have port 25565 forwarded on your router for external access to the server.

### Backup Script
The '**mc-backup-script**' folder contains a Python script '**backup.py**', designed to automate the backup process for your Minecraft server data.

### Setup 
1. Navigate into the folder:
    ```bash
    $ cd mc-backup-script
    ```
2. Create a virtual environment:
    ```bash
    $ python3 -m venv <name_of_venv>
    ``` 
3. Activate the virtual environment:
    ```bash
    $ source <name_of_venv>/bin/activate
    ```
4. Install the required packgages:
    ```bash 
    $ pip install -r requirements.txt
    ```
5. Create a '**.env**' file in the '**mc-backup-script**' folder.
6. Add the following variables to the '**.env**' file:
   ```plaintext
   SRC=<path-to-mc-server-folder>
   DST=<path-to-backup-folder>
   ```
   Replace '**<path-to-mc-server-folder>**' with the full path to your Minecraft server folder containing the data you want to back up, and '**<path-to-backup-folder>**' with the full path where you want to store your backups.

### Usage
Set up cronjob with 5 min interval to run this python script.

## Contributing 
Feel free to contribute to this project by forking this repository and creating a pull request with your changes.

## Issues
If you encounter any issues or have suggestions for improvements, please open an issue in the repository.

## License 
This project is licensed under the [**Apache 2.0 License**](https://github.com/Cyrof/mc-server/blob/main/LICENSE)