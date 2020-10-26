import pytest

from ..ConfigurableDense import _translate_name_to_layer
from tensorflow.keras.layers import Input, Dense, Dropout

_type_conversion_data = [("input", Input),
                         ("dense", Dense),
                         ("dropout", Dropout)]


@pytest.mark.parametrize("layer_type, expected_result", _type_conversion_data)
def test_of_input_conversion(layer_type, expected_result):
    input_type = type(_translate_name_to_layer(layer_type))
    assert type(
        expected_result) == input_type, f"Should be of type tensorflow.keras.layers.{expected_result}, but is: {input_type}"
