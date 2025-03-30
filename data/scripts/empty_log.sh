#!/bin/bash

# 清空日志脚本
# 描述: 清空 /opt/log 目录下所有 .log 文件的内容

# 设置日志目录
LOG_DIR="/opt/log"

# 检查脚本是否以root用户运行（根据需要调整）
if [ "$(id -u)" -ne 0 ]; then
    echo "请使用root权限运行此脚本。" >&2
    exit 1
fi

# 检查日志目录是否存在
if [ ! -d "$LOG_DIR" ]; then
    echo "目录 $LOG_DIR 不存在。" >&2
    exit 1
fi

# 查找所有 .log 文件并清空内容
find "$LOG_DIR" -type f -name "*.log" | while IFS= read -r file; do
    if [ -f "$file" ]; then
        # 使用 cat /dev/null 清空文件内容
        cat /dev/null > "$file"
        echo "已清空: $file"
    fi
done

# 或者，使用更高效的循环方式（适用于大量文件）
# find "$LOG_DIR" -type f -name "*.log" -exec sh -c '> "$0"' {} \;

# 记录清空操作日志（可选）
echo "$(date '+%Y-%m-%d %H:%M:%S') - 已清空 $LOG_DIR 目录下所有 .log 文件的内容。" >> /var/log/cleanup.log

echo "所有 .log 文件已清空完成。"