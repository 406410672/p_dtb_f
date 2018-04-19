# msg type, could be REGISTER, UNREGISTER and HEARTBEAT
MSG_TYPE	= 'request_type'

# send register
REGISTER 	= 'register'

# unregister client with id assigned by master
UNREGISTER 	= 'unregister'

# send heart beat to server with id
HEARTBEAT	= 'heartbeat'

# notify master paused with id
PAUSED 		= 'pause'

# notify master resumed with id
RESUMED		= 'resumed'

# notify master SHUTDOWN with id
SHUTDOWN		= 'shutdown'

# client id key word
CLIENT_ID 	= 'client_id'

# client name key word
CLIENT_NAME 	= 'client_name'

# server status key word
ACTION_REQUIRED	= 'action_required'

# server require pause
PAUSE_REQUIRED	= 'pause_required'

# server require pause
RESUME_REQUIRED	= 'resume_required'

# server require shutdown
SHUTDOWN_REQUIRED	= 'shutdown_required'

# server status key word
SERVER_STATUS	= 'server_status'

# server status values
SERVER_RUNNING	= 'server_running'

SERVER_PAUSED 	= 'server_paused'

SERVER_SHUTDOWN	= 'server_shutdown'

SERVER_CONNECTION_LOST	= 'client_connection_lost'

ERROR = 'error'

# client id not found, then it needs to register itself
ERR_NOT_FOUND	= 'error_not_found'



