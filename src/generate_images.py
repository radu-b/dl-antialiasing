#%%

from PIL import Image
from torchvision import transforms
from torch.utils.data import *
import torch
import matplotlib.pyplot as plt

#%%

preprocess = transforms.Compose([transforms.Grayscale(), transforms.ToTensor()])

image = preprocess(Image.open("data/image-aa.png"))

#%%

to_image = transforms.ToPILImage()
*rest, rows, cols = image.shape
part_size = 200

for index in range(3000):
    r = torch.randint(rows - part_size, (1,))[0].item()
    c = torch.randint(cols - part_size, (1,))[0].item()

    part_y = image[:, r : r + part_size, c : c + part_size]
    part_x = part_y.clone()
    part_x[part_x < 0.5] = 0
    part_x[part_y >= 0.5] = 1

    part_x_image = to_image(part_x)
    part_x_image.save(f"data/images-x/{index}.png")

    part_y_image = to_image(part_y)
    part_y_image.save(f"data/images-y/{index}.png")


# %%
