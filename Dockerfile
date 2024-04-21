FROM python:3.11
RUN mkdir -p /neatqueue-chatbot
COPY . /neatqueue-chatbot
WORKDIR neatqueue-chatbot
RUN pip3 install -r requirements.txt
CMD python3 main.py
