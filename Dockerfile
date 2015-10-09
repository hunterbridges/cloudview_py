FROM codenvy/python27

RUN sudo pip install --upgrade pip
RUN sudo pip install requests
RUN sudo pip install livestreamer

COPY . /src

CMD sh /src/run.sh
