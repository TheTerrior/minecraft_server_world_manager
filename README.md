# minecraft_server_world_manager
To use, run 
```
python worldmanager.py [action] [world_name]
```
where action is either 'save' or 'retrieve' and world_name is the world you're targetting.

Saving deletes the existing world of the given name, and saves the current world under that name.

Retrieving first saves the current world into the backups folder. It then deletes the current world and overwrites it with the stored world of the given name. The backup is there in case you wish to roleback this action. Please note these backups can pile up quickly, to make sure to manage this on your own if you wish.
