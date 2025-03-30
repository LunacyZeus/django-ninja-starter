# AUTH_USER_MODEL = 'system.Users'
# USERNAME_FIELD = 'username'
ALL_MODELS_OBJECTS = []  # 所有app models 对象

DEMO = False  # 开启demo模式
# 接口白名单，不需要授权直接访问
WHITE_LIST = []

NOT_AUTH_LIST = []

# token 有效时间 时 分 秒
TOKEN_LIFETIME = 15 * 24 * 60 * 60
# TOKEN_LIFETIME = 50

# 初始化需要执行的列表，用来初始化后执行
INITIALIZE_RESET_LIST = []
