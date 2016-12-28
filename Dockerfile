FROM rocker/shiny
MAINTAINER Frederik Durant "Frederik.Durant@pandora.be"
EXPOSE 80
USER dkr
COPY /myapp/* /srv/shiny-server/
WORKDIR ~/
