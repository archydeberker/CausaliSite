https://blog.tutum.co/2014/04/10/creating-a-docker-image-from-your-code/

Dockerfile:
FROM tutum/buildstep
EXPOSE 8000
CMD ["/start", "web"]

Build the image by typing this while in the main folder
docker build -t zapscience/app .

Start it with 
docker run -d -p 8000 zapscience/app

And see IP (but can't connect for some reason)
docker-machine ls
docker ps -a
