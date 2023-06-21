#!/usr/bin/env python3

import click
from diffusers import StableDiffusionPipeline

import pathlib

@click.group()
def main():
    pass

@main.command()
@click.option('--model-ids', '-m', multiple=True, required=True, type=str)
@click.option('--destination', '-d', required=True, type=str)
def save(model_ids, destination):
    """ Save model to destination """

    for model_id in model_ids:

        # download the model from the hub
        pipeline = StableDiffusionPipeline.from_pretrained(model_id)

        # extract a name for the model from the model id
        model_name = model_id.split('/')[-1]

        # make sure the directory exists
        dest_path = pathlib.Path(destination) /model_name
        dest_path.mkdir(parents=True, exist_ok=True) 

        # save the model
        pipeline.save_pretrained(dest_path)

    return

if __name__ == '__main__':
    main()

    