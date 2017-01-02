FROM rocker/shiny
MAINTAINER Frederik Durant "Frederik.Durant@pandora.be"
EXPOSE 80 3838 7474
COPY /myapp/* /srv/shiny-server/
WORKDIR ~/
