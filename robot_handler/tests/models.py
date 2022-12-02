from django.db import models

class TestSuite(models.Model):
    name = models.CharField(max_length=200)
    documentation = models.TextField()
    metadata = models.CharField(max_length=200)
    suite_setup = models.CharField('suite setup', max_length=200)
    suite_teardown = models.CharField('suite teardown', max_length=200)
    force_tags = models.CharField('force tags', max_length=200)
    test_setup = models.CharField('test setup', max_length=200)
    test_teardown = models.CharField('test teardown', max_length=200)
    test_timeout = models.CharField('test timeout', max_length=200)
    library = models.CharField(max_length=200)
    path = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class TestCase(models.Model):
    suite = models.ForeignKey(TestSuite, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    documentation = models.TextField()
    tags = models.CharField(max_length=200)
    setup = models.CharField(max_length=200)
    teardown = models.CharField(max_length=200)
    template = models.CharField(max_length=200)
    timeout = models.CharField(max_length=200)
    arguments = models.CharField(max_length=200)
    body = models.TextField()
    path = models.CharField(max_length=200)

    def __str__(self):
        return self.name
