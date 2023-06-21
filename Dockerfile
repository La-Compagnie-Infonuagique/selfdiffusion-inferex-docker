FROM runpod/pytorch:3.10-2.0.1-118-runtime

ARG FILE_NAME=inference.py

RUN pip install --upgrade pip
RUN pip install transformers diffusers accelerate boto3 runpod
RUN pip install click 

ADD $FILE_NAME /

RUN chmod +x /$FILE_NAME

# Download baked in models
COPY download /download
WORKDIR /download

RUN ./download_and_save.py save -m "prompthero/openjourney" -m "SG161222/Realistic_Vision_V1.4" --destination "/models"

CMD ["/$FILE_NAME"]