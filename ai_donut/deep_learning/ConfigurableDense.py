import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import Sequential, Model
from tensorflow.keras.layers import Dense, Dropout

import importlib


def _translate_name_to_layer(name):
    return {
        "input": getattr(importlib.import_module("tensorflow.keras.layers"), "Input")
    }.get(name, None)


class ConfigurableDense:
    def __init__(self):
        yield

    # def _construct_model(self, model_structure):

