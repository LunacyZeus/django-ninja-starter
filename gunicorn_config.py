import multiprocessing

"""gunicorn+uvicorn 的配置文件"""

# 代码热更新
reload = True

# 预加载资源
preload_app = True

# 使用 Unix Socket 绑定
bind = "unix:/opt/run/demo.sock"  # "0.0.0.0:10000"

# 进程数: CPU数量 * 2 + 1
workers = multiprocessing.cpu_count() + 1

# 线程数: CPU数量 * 2
threads = multiprocessing.cpu_count()

# 等待队列最大长度, 超过这个长度的连接将被拒绝
backlog = 8192

# 工作模式
worker_class = "uvicorn.workers.UvicornWorker"

# 最大客户端并发数量
worker_connections = 8192

# 进程名称
proc_name = "demo"

# 进程 PID 记录文件
pidfile = "/opt/run/demo.pid"

# 日志等级
loglevel = "debug"

# 日志文件名
# logfile = '/opt/log/ec-debug.log'

# 错误信息日志
# errorlog = '/opt/log/ec-error.log'

# 如果你不需要访问日志，可以保持注释状态
# accesslog = '/opt/log/ec-access.log'
# 访问记录格式
# access_log_format = '%(h)s %(t)s %(U)s %(q)s'

# 设置 Socket 文件的权限（可选）
umask = 0o002

max_requests = 20000
# 随机增加偏移量range(1, max_requests_jitter)，与max_requests配合，防止多个worker同时重启
max_requests_jitter = 1000
# 设置超时时间120s，默认为30s。按自己的需求进行设置timeout = 120
timeout = 120
# 超时重启
graceful_timeout = 300
# 在keep-alive连接上等待请求的秒数，默认情况下值为2。一般设定在1~5秒之间。
keepalive = 5
# HTTP请求行的最大大小，此参数用于限制HTTP请求行的允许大小，默认情况下，这个值为4094。
# 值是0~8190的数字。此参数可以防止任何DDOS攻击
limit_request_line = 5120
# 限制HTTP请求中请求头字段的数量。
#  此字段用于限制请求头字段的数量以防止DDOS攻击，与limit-request-field-size一起使用可以提高安全性。
# 默认情况下，这个值为100，这个值不能超过32768
limit_request_fields = 101
# 限制HTTP请求中请求头的大小，默认情况下这个值为8190。
# 值是一个整数或者0，当该值为0时，表示将对请求头大小不做限制
limit_request_field_size = 0
