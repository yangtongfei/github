# FROM centos:7 
# MAINTAINER yang<yang@126.com>
# 
# ENV MYPATH /usr/local
# WORKDIR $MYPATH
# 
# RUN yum -y install vim  #安装vim
# RUN yum -y install net-tools  #安装网络服务
# 
# #安装java8以及lib库
# RUN yum -y install glibc.i686
# RUN mkdir /usr/local/java
# 
# ADD jdk-8u171-linux-x64.tar.gz /usr/local/java/
# 
# ENV JAVA_HOME /usr/local/java/jdk1.8.0_171
# ENV JRE_HOME $JAVA_HOME/jre
# ENV CLASSPATH $JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JRE_HOME/lib:$CLASSPATH
# ENV PATH $JAVA_HOME/bin:$PATH
# 
# EXPOSE 80 #端口号
# 
# CMD echo $MYPATH
# CMD echo "success-----------ok"
# CMD /bin/bash


FROM ubuntu
MAINTAINER yang<yang@123.com>

WORKDIR /usr/local

RUN apt-get update
RUN apt-get -y install net-tools
RUN apt-get -y install vim 

EXPOSE 80

CMD echo "安装完成.....ok"

