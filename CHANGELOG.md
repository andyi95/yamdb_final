# CHANGELOG

## 2021-07-09

Now let's test Workflow on test branch
#### Fixed:
 - Fixed general code issues
 - Finished and corrected [README in English](/README-en.md)
 
#### Added:
 - Copy base files on deploy
 - Demo servers in Readme
 - Moved deployment script to a separate file
 
## 2021-07-06
#### Added:
 - GitHub Workflow deployment
 - Updated [README.md](README.md)

## 2021-07-05
 - Moved to [yamdb_final](https://github.com/andyi95/yamdb_final) repository

## 2021-07-04
From [infra_sp2](https://github.com/andyi95/infra_sp2) repository
#### Added:

 - moved Django migration files to the repo
 - Nginx configuration templates with env variables support
 - MIT license


#### Fixed:

 - Nginx security improvements
 - Dockerfile and docker-compose config optimisation, image size decreased from ~600 to 120 Mb, build time decrease in 1,75 times - from 95 to 53 seconds (measured with standart `time` utility  on Ubuntu 20.04 with 2Gb RAM, HDD drive)
 - Excess comments removed, code has been brought in line with PEP8

 
#### TODO:

 - Finish English translation of README.md
