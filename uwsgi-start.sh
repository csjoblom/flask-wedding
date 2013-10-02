sudo uwsgi -s /tmp/uwsgi-rsvp.sock --file /home/csjoblom/code/flask-rsvp/rsvp/rsvp.py --callable app -H /home/csjoblom/code/rsvpenv --chmod-socket=666 --daemonize=/var/log/uwsgi/rsvp.log
