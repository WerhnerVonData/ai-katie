import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import Sequential, Model
from tensorflow.keras.layers import Dense, Dropout

import importlib


def _translate_name_to_layer(name):
    return {
        "input": getattr(importlib.import_module("tensorflow.keras.layers"), "Input"),
        "dense": getattr(importlib.import_module("tensorflow.keras.layers"), "Dense"),
        "dropout": getattr(importlib.import_module("tensorflow.keras.layers"), "Dropout")
    }.get(name, None)


class ConfigurableDense:
    def __init__(self, model_structure):
        self.model = Model
        yield

    @staticmethod
    def _construct_model(model_structure):
        yield

