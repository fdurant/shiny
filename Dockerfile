FROM shiny
MAINTAINER Frederik Durant "Frederik.Durant@pandora.be"
USER dkr
COPY /myapp/* /srv/shiny-server/
WORKDIR ~/
