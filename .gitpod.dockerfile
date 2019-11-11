FROM gitpod/workspace-full-vnc:latest

# install custom tools, runtime, etc.

USER root
# Install custom tools, runtime, etc.
RUN apt-get update && apt-get install -y firefox net-tools \
    && apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*

RUN python3 -m pip install wxpython
RUN python3 -m pip install opencv-python

USER gitpod
# Apply user-specific settings
#ENV ...

# Give back control
USER root
