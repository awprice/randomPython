import xmlrpclib

# Create an object to represent our server.
server_url = "http://username:password@server.address.com/path";
server = xmlrpclib.Server(server_url);

# Get torrents in the seeding view
torrents = server.download_list("", "seeding")

# For each torrent in the seeding view
for torrent in torrents:

        #print server.d.get_name(torrent)

        #print server.d.get_directory(torrent)

        # Erase the torrent from the server
        server.d.erase(torrent)
