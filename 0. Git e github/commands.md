## Git Commands Notes 


### Git add:
It is used to add all or one archive to git stage:
* **git add .** -> add every modified file on stage
* **git add archive.md** -> add that specific file on stage

### Git status:
Used to show the file and path status inside repo.

### Git commit:
The command git commit will send the modifications to the local repo. So, after putting the file on stage, we commit it using:
* **git commit -m "your message"** 


### Git push:
The command **git push** is used to send the modifications commited to gitHub (remote repo).

If the message "has no upstream branch" appears: Upstream is the remote origin of branch from github. We need to connect that branch with local repo. So we need to **git push --set-upstream origin master** . 


### Git pull:
the command **git pull** is used to send modifications from remote repo to local repo. It is usefull when we are working as a team, so we can update others work before making modifications on code.

### Git checkout / working with branches:
Create a New branch and swit to it:
* **git checkout -b Name_of_new_branch**

Swit to a branch already created on Github:
* **git checkout name_of_existing_branch**

Lists existing branchs:
* **git branch**

### merge:
the comand git merge is used to join two existing branches. 
We can view the available branches through git status.
In the branch you wants to join with, run:
* **git merge name_of_other_branch**

#
## Some usefull links about git:
#### [ In Portuguese ]

* [Artigo] Guia rápido e Comandos básicos para iniciantes

https://dev.to/womakerscode/git-e-github-guia-rapido-e-comandos-basicos-para-iniciantes-4ile

* [Tutorial] git commit -am: Atualizando arquivo modificado no Git

https://dev.to/womakerscode/tutorial-git-adicionando-um-arquivo-modificado-no-git-116c

* [Tutorial] git commit: Enviando arquivos para o repositório Git:

https://dev.to/womakerscode/tutorial-git-enviando-arquivos-para-o-repositorio-git-1k91

* [Tutorial] git add: Adicionando arquivos no Git:

https://dev.to/womakerscode/tutorial-git-adicionando-arquivos-no-git-3a0o

* [Tutorial] Enviando um projeto para o repositório remoto no GitHub:

https://dev.to/womakerscode/tutorial-git-enviando-um-projeto-para-o-repositorio-remoto-no-github-2p36

* [Tutorial] Puxando commits remotos:

https://dev.to/womakerscode/tutorial-git-puxando-commits-remotos-44an

* [Tutorial] gitignore: Ignorando arquivos no Git:

https://dev.to/womakerscode/tutorial-git-ignorando-arquivos-no-git-32m9

* [Tutorial] O que são branches (ramos) no Git?:

https://dev.to/womakerscode/tutorial-git-o-que-sao-branches-ramos-no-git-57pn



