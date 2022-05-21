Follow below steps to add a wrapper around docker. It can be used in a shared environment. It forces users o run docker
with --runby argument which is user name of user running commands.

for e.g.
docker --runby dshah run -it ubuntu

Steps
=======
1. get location of docker. If it is a symbolic link, you need to make changes to original location in next steps. Not the link. In my case
it is not a symbolic link.

