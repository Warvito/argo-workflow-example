import torch
from torchvision import models


def infer_image():
    img = torch.load("/tmp/image.pt")
    model = models.squeezenet1_1(pretrained=True)
    with torch.no_grad():
        output = model(img)
    print(f"Predicted class: {output.argmax()}")


if __name__ == '__main__':
    infer_image()
