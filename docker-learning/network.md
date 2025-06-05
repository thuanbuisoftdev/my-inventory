# Docker Network Overview

Docker networking enables communication between containers, services, and external systems. It provides multiple network drivers to suit different use cases.

## Docker Network Drivers

### 1. **Bridge Network** (Default for Standalone Containers)

- Containers can communicate with each other on the same bridge network.
- Uses a virtual Ethernet bridge (docker0) to route packets.
- Containers get an internal IP and can be accessed via container name.
- Example:

  ```sh
  docker network create my_bridge
  docker run --network=my_bridge my_container
  ```

### 2. **Host Network**

- Removes network isolation between the container and the host.
- The container shares the host's network stack.
- No port mapping is required.
- Example:

  ```sh
  docker run --network=host my_container
  ```

### 3. **Overlay Network** (For Swarm Mode)

- Enables communication between containers across multiple Docker hosts.
- Used in Docker Swarm for service-to-service communication.
- Requires Swarm mode to be enabled.
- Example:

  ```sh
  docker network create --driver=overlay my_overlay
  ```

### 4. **Macvlan Network**

- Assigns a unique MAC address to containers, making them appear as physical devices.
- Useful for direct network access without NAT.
- Example:

  ```sh
  docker network create -d macvlan --subnet=192.168.1.0/24 my_macvlan
  ```

### 5. **None Network**

- Completely disables networking for a container.
- The container has no external connectivity.
- Example:

  ```sh
  docker run --network=none my_container
  ```

## Listing and Inspecting Networks

- **List networks**: `docker network ls`
- **Inspect a network**: `docker network inspect <network_name>`
- **Remove a network**: `docker network rm <network_name>`

## Connecting and Disconnecting Containers

- **Connect a container to a network**: `docker network connect <network_name> <container_name>`
- **Disconnect a container from a network**: `docker network disconnect <network_name> <container_name>`

## Conclusion

Docker networking provides flexibility to create isolated or connected environments. Choosing the right network driver depends on the architecture and communication needs of your containers.
