Usage
-----

Adjust paths in ``getfile.php`` and ``findlines.py``

**index.htm will be written in working directory**

    findlines.sh | addlinks.py
    
Move ``getfile.php`` and ``index.htm`` to a web server that can execute PHP. Browse ``index.htm``.

    cd <logdirectory>
    grep -rinH haha | (cd /tmp/pidgin-log-searcher; ./addlinks.py)
    cd /tmp/pidgin-log-searcher
    ln -fvs $PWD/getfile.php $PWD/index.htm /var/www/temp
