import weka.core.converters as converters
from weka.classifiers import Classifier
from weka.classifiers import Evaluation
from weka.core.classes import Random
import weka.core.jvm as jvm
jvm.start()


# Veri kümesini yükle (CSV formatı)
data_file = "datasets/final.csv"  # Veri kümesinin yolunu doğru bir şekilde belirtiniz
loader = converters.Loader("weka.core.converters.CSVLoader")
data = loader.load_file(data_file)

# Sınıflandırıcı oluştur (J48)
classifier = Classifier(classname="weka.classifiers.trees.J48")

# Veri kümesini sınıflandırıcıya eğitim için ata
classifier.build_classifier(data)

# Sınıflandırma doğruluğunu değerlendir
print("---J48---")
evaluator = Evaluation(data)
evaluator.crossvalidate_model(classifier, data, 10, Random(1))
print(evaluator.summary())
