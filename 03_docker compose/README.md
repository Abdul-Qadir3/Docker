### Create and start containers.
```bash
docker-compose up
docker-compose up -d           # Run containers in the background (detached mode)
docker-compose up --build      # Build images before starting containers

```
### Stop and remove containers, networks, images, and volumes.

```bash
docker-compose down
docker-compose down --volumes          # Remove named volumes declared in the `volumes` section of the Compose file and anonymous volumes attached to containers
docker-compose down --remove-orphans   # Remove containers for services not defined in the Compose file
```
### Start existing containers

```bash
docker-compose start
```

### Stop running containers.

```bash
docker-compose stop
```

### Restart containers.

```bash
docker-compose restart
```
### Pause running containers. 

```bash
docker-compose pause
```

### Unpause paused containers.

```bash
docker-compose unpause
```

### List containers.

```bash
docker-compose ps
```

### View output from containers.

```bash
docker-compose logs
docker-compose logs -f          # Follow log output
docker-compose logs --tail=50   # Show only the last 50 lines of logs
```
### Build or rebuild services

```bash
docker-compose build
docker-compose build --no-cache  # Do not use cache when building the image
docker-compose build --pull      # Always attempt to pull a newer version of the image
```

### Validate and view the Compose file.

```bash
docker-compose config
docker-compose config --services  # Print the service names
docker-compose config --volumes   # Print the volume names
docker-compose config --profiles  # Print the profile names
```

### Remove stopped containers.

```bash
docker-compose rm
docker-compose rm -f       # Don't ask to confirm removal
docker-compose rm -s       # Stop the containers, if required, before removing
docker-compose rm -v       # Remove any anonymous volumes attached to containers
```

### Force stop service containers.

```bash
docker-compose kill
docker-compose kill -s SIGNAL  # SIGNAL to send to the container (default is SIGKILL)
```