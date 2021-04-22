#! /usr/bin/env bash

function update{
  git pull --ff-only > /dev/null
   if [[ $? -eq 0 ]]; then
        echo "更新完成。"
    else
        echo "更新失败，请手动执行 git pull 更新。"
   fi
}

fetch_head=".git/FETCH_HEAD"
if [[ ! -e ${fetch_head} ]]; then
    echo "未检测到更新记录，自动更新程序中..."
    update
else
    last_pull=$(stat -c %Y .git/FETCH_HEAD)
    now=$(date +%s)
    interval=$(expr ${now} - ${last_pull})

    # 一小时一次
    if [[ ${interval} -ge 3600 ]]; then
        echo "上次更新时间 $(date -d @${last_pull})，自动更新程序中..."
        update
    fi
fi