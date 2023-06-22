FROM runpod/pytorch:3.10-2.0.1-118-runtime

RUN pip install --upgrade pip
RUN pip install transformers diffusers accelerate boto3 runpod
RUN pip install click 

ADD inference.py /

RUN chmod +x /inference.py

# Download baked in models
COPY models /models

CMD ["/inference.py"]