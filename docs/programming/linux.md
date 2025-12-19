```
apt install mosh

sudo apt-get update && sudo apt-get install locales
sudo locale-gen en_US.UTF-8
sudo locale-gen C.UTF-8

sudo update-locale LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8


ssh-copy-id -i .ssh/id.1 ubuntu@93.115.203.225
rm /etc/ssh/sshd_config.d/50-cloud-init.conf

sudo apt install zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

```

https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository

```
echo '%wheel ALL=(ALL) ALL' > /etc/sudoers.d/wheel
setfont /usr/share/consolefonts/CyrSlav-Terminus32x16.psf.gz
```
