from django.core.management.base import BaseCommand

from experiments.models import Project, Hypothesis, Run, RLRun


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # Create project
        Project.objects.get_or_create(name="RandomNoise", description="Comparison of random noises. Test case.")

        # Create hypothesis
        gauss_noise_hyp, _ = Hypothesis.objects.get_or_create(name="Gaussian Noise")

        # Create experiments
        system_data = {"CPU": "Intel i5", "RAM": "2GB"}
        mu_s = [0, -1, 1]
        sigma_s = [1, 0.5, 2]
        for mu, sigma in zip(mu_s, sigma_s):
            scalar_data = {"x": [1, 2, 3], "y": [1, 2, 3]}
            Run.objects.get_or_create(
                name=f"mu_{mu}_sigma_{sigma}",
                hypothesis=gauss_noise_hyp,
                scalars=scalar_data,
                system=system_data,
            )