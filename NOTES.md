# NOTES and REFERENCES

 - [Possible to commit files after workflow runs?](https://github.community/t5/GitHub-Actions/Possible-to-commit-files-after-workflow-runs/td-p/49755#)
 - [Can GitHub actions directly edit files in a repository?](https://github.community/t5/GitHub-Actions/Can-GitHub-actions-directly-edit-files-in-a-repository/td-p/50551#)
 - [github action to copy a file from one repo to another](https://stackoverflow.com/questions/59408320/github-action-to-copy-a-file-from-one-repo-to-another)
 - [github push action (by @ad-m)](https://github.com/ad-m/github-push-action)
 - [run Github Actions locally](https://github.com/nektos/act)
 - [manually trigger Github Actions](https://dev.to/s_abderemane/manual-trigger-with-github-actions-279e)
 - [how-to-run-jupiter-keras-tensorflow-pandas-sklearn-and-matplotlib-in-docker-container](https://medium.com/@andreimaksimov/how-to-run-jupiter-keras-tensorflow-pandas-sklearn-and-matplotlib-in-docker-container-35a49fd4b175)
 
 # run locally (windows)
 install chocolatey
 install act cli via chocolatey 
 install docker-desktop (win10), or docker-toolkit (win < 10, which I have) via chocolatey  https://www.smarthomebeginner.com/install-docker-on-windows-7-8-10/
 
 
 # docker container
 mkdir ubuntu-node-pandas
 create Dockerfile
 cd
 docker build -t azrafe7/ubuntu-node-pandas:12.6-buster-slim .
 
 