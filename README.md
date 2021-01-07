# Styled-Makeup-Synthesis-and-Removal
CS484-555 Project - Styled Makeup Synthesis and Removal Using Generative Adversarial Networks

To re-train the ResNet-50 with transfer learning run `Makeup_Clustering.ipynb`. 

The re-trained model can be saved by `torch.save(model_ft, "/content/drive/MyDrive/fine_tune_makeup")`, where path is where the model will be saved.

The re-trained ResNet-50 is used in `Makeup_Clustering.ipynb` in `resnet_model = torch.load("/content/drive/MyDrive/fine_tune_makeup")`

DCGAN can be trained by running `Makeup_Clustering.ipynb`, although the training will not give meaningful results.
