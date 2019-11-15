FROM gitpod/workspace-full-vnc:latest

# install custom tools, runtime, etc.

USER root
# Install custom tools, runtime, etc.
#RUN apt-get update && apt-get install -y firefox net-tools \
#    && apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*

RUN pip3 install https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-18.04/wxPython-4.0.7-cp37-cp37m-linux_x86_64.whl
RUN pip3 install opencv-python
RUN chown -R gitpod:gitpod /home/gitpod/.cache/pip

USER gitpod
# Apply user-specific settings
#ENV ...

# Give back control
USER root
