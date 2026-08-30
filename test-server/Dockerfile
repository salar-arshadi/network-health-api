FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y \
        openssh-server \
        sudo && \
    mkdir /var/run/sshd

RUN useradd -m monitor && \
    echo "monitor:monitor123" | chpasswd && \
    adduser monitor sudo

RUN mkdir /home/monitor/.ssh && \
    chown -R monitor:monitor /home/monitor/.ssh

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
