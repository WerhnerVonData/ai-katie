from torch.nn.functional import softmax

"""
"""
class SoftmaxBody:
    """

    """
    def __init__(self, temperature):
        """

        :param temperature:
        """
        self.temperature = temperature

    def __call__(self, outputs):
        """

        :param outputs:
        :return:
        """
        probabilities = softmax(outputs * self.temperature, dim=len(outputs))
        actions = probabilities.multinomial(num_samples=1)
        return actions
