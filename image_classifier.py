from imageai.Classification import ImageClassification

prediction = ImageClassification()
prediction.setModelTypeAsResNet50()
prediction.setModelPath("A:/coding priojects/Image Classifier/resnet50_imagenet_tf.2.0.h5")
prediction.loadModel()
predictions, percentage_probabilities = prediction.classifyImage("A:/coding priojects/Image Classifier/a.png", result_count=5)
for index in range(len(predictions)):
  print(predictions[index] , " : " , percentage_probabilities[index])

