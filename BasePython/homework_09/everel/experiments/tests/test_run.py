from random import random

from django.test import TestCase

from experiments.models import Hypothesis, Run


class RunTest(TestCase):

    def setUp(self):
        hypothesis = Hypothesis.objects.create(name="Hypothesis")
        Run.objects.create(
            name="Run1",
            hypothesis=hypothesis,
            scalars={
                "x": [random() for _ in range(10)],
                "y": [random() for _ in range(10)]
            }
        )

    def test_tags(self):
        run = Run.objects.get(name="Run1")
        self.assertListEqual(sorted(run.get_tags()), ["x", "y"])

    def test_naming(self):
        run = Run.objects.get(name="Run1")
        self.assertTrue(str(run).startswith("run_"))

    def tearDown(self):
        Run.objects.all().delete()
        Hypothesis.objects.all().delete()