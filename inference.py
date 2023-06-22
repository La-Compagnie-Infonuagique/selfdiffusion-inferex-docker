#!/usr/bin/env python
import runpod
import os
import time
import torch
from diffusers import StableDiffusionPipeline

device = "cuda" if torch.cuda.is_available() else "cpu"
pipe = StableDiffusionPipeline.from_pretrained("/models/stable-diffusion-v1-5")
pipe.to(device)


def handler(event):

    prompt = event["input"]["prompt"]
    img = pipe(prompt).images[0]

    return "ok"


runpod.serverless.start({
    "handler": handler
})