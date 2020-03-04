from a2ml.api.auger.train import AugerTrain
from a2ml.api.auger.deploy import AugerDeploy
from a2ml.api.auger.predict import AugerPredict
from a2ml.api.auger.evaluate import AugerEvaluate
from a2ml.api.auger.import_data import AugerImport


class AugerA2ML(object):
    """Auger A2ML implementation."""

    def __init__(self, ctx):
        super(AugerA2ML, self).__init__()
        self.ctx = ctx

    def import_data(self):
        return AugerImport(self.ctx).import_data()

    def train(self):
        return AugerTrain(self.ctx).train()

    def evaluate(self):
        return AugerEvaluate(self.ctx).evaluate()

    def deploy(self, model_id, locally=False):
        return AugerDeploy(self.ctx).deploy(model_id, locally)

    def predict(self, filename, model_id, threshold=None, locally=False):
        return AugerPredict(self.ctx).predict(filename, model_id, threshold, locally)

    def review(self):
        pass
