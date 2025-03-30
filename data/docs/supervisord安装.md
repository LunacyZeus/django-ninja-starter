
#直接安装在系统当中，整个环境中都有  
sudo apt-get install supervisor  
#可以在虚拟环境中通过pip安装  
pip3 install supervisor

生成配置文件  
echo_supervisord_conf > /etc/supervisord.conf  

mkdir /etc/supervisord.d/


cp /usr/local/src/demo/data/conf/supervisord/demo.ini /etc/supervisord.d/demo.ini
cp /usr/local/src/demo/data/conf/supervisord/celery.ini /etc/supervisord.d/celery.ini



supervisord -c /etc/supervisord.conf

ps -ef | grep supervisord

supervisorctl reload demo
supervisorctl restart demo

supervisorctl restart ec_beat
supervisorctl restart ec_worker

supervisorctl stop demo
supervisorctl remove demo
supervisorctl demo
supervisorctl add demo



https://juejin.cn/post/7078831374840365070