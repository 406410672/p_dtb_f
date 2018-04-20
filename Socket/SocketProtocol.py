#TypeKey
## msg type, could be REGISTER, UNREGISTER and HEARTBEAT
MSG_TYPE	= 'request_type'

#typeValue
## 请求任务
APPLICATION_TASKS = 'application_tasks'
## 注册爬虫机
REGISTER 	= 'register'
## send heart beat to server with id
HEARTBEAT	= 'heartbeat'
## 上传任务
UPLOAD_TASKS = 'upload_tasks'


# server status key word
SERVER_STATUS	= 'server_status'
# server status value
## server status values
SERVER_RUNNING	= 'server_running'
SERVER_PAUSED 	= 'server_paused'
SERVER_SHUTDOWN	= 'server_shutdown'



# error key
ERROR = 'error'

# errorValue
## 爬虫端失去连接
ERROR_CONNECTION_LOST	= 'error_connection_lost'
## client id not found, then it needs to register itself
ERR_NOT_FOUND	= 'error_not_found'
## 上传任务失败
ERR_UPLOAD_TASK	= 'error_upload_task'
