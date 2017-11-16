SimpleUpload
===========

安装::

    pip install SimpleUpload


服务端需要安装Flask和gunicorn::

    pip install Flask gunicorn

使用环境变量指定配置文件的位置::

    export SIMPLE_UPLOAD_SETTINGS="{path}/simple_upload.cfg"

启动::

    gunicorn -b :8000 http_upload.server:app


上传方式(以HTTPie为例)::

    http -f POST yldev.lankaifa.com:8000 r={your random string} path={local path} f@{local_path}
