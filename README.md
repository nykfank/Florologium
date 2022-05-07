# Florologium
Linnaeus Flower Clock timelapse scripts

# Servers
- Florbox: This is the Raspberry Pi4 in the box at the Botanical Gardens controlling the Nikon D7500 though USB. Connected to the internet by a GSM modem, it creates a reverse SSH tunnel (using ssh_tunnel.service) to the Katzidien server.
- Katzidien (katz): Run the lighttpd webserver and is the entrance to the tunnel to Florbox (flortun).
- Flor: Asus server for storing the images, computing timelapse movies and image analysis. The nikon directory is mounted to the Katzidien server by sshfs to allow it to add new images there.
