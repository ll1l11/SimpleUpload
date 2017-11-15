HTTPUpload
===========

安装::

    pip install HTTPUpload


服务端需要安装Flask和gunicorn::

    pip install Flask gunicorn

启动::

    gunicorn -b 0.0.0.0:8000 http_upload.server:app