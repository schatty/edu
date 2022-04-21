from django.test import TestCase

from experiments.models import Hypothesis, Run


class AddRunTest(TestCase):

    def test_add_run(self):
        # Create hypothesis
        gauss_noise_hyp = Hypothesis.objects.create(name="Gaussian Noise")

        # Create experiments
        system_data = {"CPU": "Intel i5", "RAM": "2GB"}
        mu_s = [0, -1, 1]
        sigma_s = [1, 0.5, 2]
        for mu, sigma in zip(mu_s, sigma_s):
            scalar_data = {"x": [1, 2, 3], "y": [1, 2, 3]}
            Run.objects.create(
                name=f"mu_{mu}_sigma_{sigma}",
                hypothesis=gauss_noise_hyp,
                scalars=scalar_data,
                system=system_data,
            )