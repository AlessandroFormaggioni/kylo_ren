# How to link the terminal with a github folder
1. Make a new folder and initalize it `git init`.
2. Configure your account `git config --local user.name “charlesdarwin”` and `git config --local user.email “charlesdarwin@ontheoriginofspecies.org”`
3. Create a ssh key, follow (https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent). The command is `ssh-keygen -t ed25519 -C "your_email@example.com"`
4. Copy the key in the file .pub in. Go in Github -> Settings -> SSH and GPG keys -> Add a new SH key and paste the string of the .pub file
5. Put the file you want to download in the folder on the terminal. 
6. Upload the file on github: `git add massextinction.sh` then `git commit -m "something"` use the flag -m to avoid the message; then `git push`.
7. To upload from github to terminal `git pull origin main`
