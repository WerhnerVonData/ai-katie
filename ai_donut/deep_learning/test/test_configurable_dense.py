from ..ConfigurableDense import _translate_name_to_layer
from tensorflow.keras.layers import Input


def test_of_input_conversion():
    input_type = type(_translate_name_to_layer("input"))
    assert type(Input) == input_type, f"Should be of type tensorflow.keras.layers.Input, but is: {input_type}"
