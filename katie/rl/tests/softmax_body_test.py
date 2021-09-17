import torch
from katie.rl.softmax_body import SoftmaxBody


def test_softmax_body_creation():
    sb = SoftmaxBody()
    assert (1.0 == sb.temperature)


def test_softmax_body_call():
    sb = SoftmaxBody()
    outputs = torch.tensor([[50, 20, 30, 40]])
    sb_output = sb(outputs=outputs)
    assert (torch.is_tensor(sb_output))
    assert ((1, 1) == sb_output.shape)
    assert ((1, 3) == sb(outputs=outputs, num_samples=3).shape)


def test_softmax_body_call_with_bigger_number_of_samples():
    sb = SoftmaxBody()
    outputs = torch.tensor([[50, 20, 30, 40]])
    sb_output = sb(outputs=outputs, num_samples=10)
    assert (torch.is_tensor(sb_output))
    print(sb_output.shape)
    assert ((1, 4) == sb_output.shape)
