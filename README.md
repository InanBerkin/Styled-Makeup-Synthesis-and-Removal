# Styled-Makeup-Synthesis-and-Removal
CS484-555 Project - Styled Makeup Synthesis and Removal Using Generative Adversarial Networks

MT-Dataset: Dataset can be found here. [https://drive.google.com/file/d/18UlvYDL6UGZ2rs0yaDsSzoUlw8KI5ABY/view]

To re-train the ResNet-50 with transfer learning run `Makeup_Clustering.ipynb`. If you prefer using the pretrained model, you can download from [Drive](https://drive.google.com/file/d/1I4adydGnVLGZz3WmxYNl4rBgkVwVmEgX/view?usp=sharing).

The re-trained model can be saved by `torch.save(model_ft, "/content/drive/MyDrive/fine_tune_makeup")`, where path is where the model will be saved.

The re-trained ResNet-50 is used in `Makeup_Clustering.ipynb` in `resnet_model = torch.load("/content/drive/MyDrive/fine_tune_makeup")`

DCGAN can be trained by running `Makeup_Clustering.ipynb`, although the training will not give meaningful results.
