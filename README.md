# Minecraft Server
This is a minecraft server using minecraft docker image, docker compose, and ngrok for tcp connection without port forwarding

## Instructions
1. Update `NGROK_AUTHTOKEN` to your own ngrok authentication token
2. Navigate to the current directory  
3. Run `sudo docker compose up -d`
4. Check if ngrok is up using `sudo docker ps`. If container not up open a github issue. 
5. Navigate to localhost:4040 on a browser to get the tcp address.
6. Copy the tcp address without the `tcp://`
7. In minecraft connect to server using the address copied.