#%%

import fastai.vision as fv
import warnings
import torchvision.transforms as transforms

warnings.filterwarnings("ignore")

#%%

path_x = "data/train/x"
path_y = "data/train/y"

#%%

bs, size = 40, 200
arch = fv.models.resnet18

src = fv.ImageImageList.from_folder(path_x).split_by_rand_pct(0.1, seed=42)

#%%


def get_data(bs, size):
    data = (
        src.label_from_func(lambda x: f"{path_y}/{x.name}")
        .transform(
            fv.get_transforms(
                flip_vert=True, max_rotate=False, max_zoom=False, max_lighting=False
            ),
            size=size,
            tfm_y=True,
        )
        .databunch(bs=bs)
        # .normalize(imagenet_stats, do_y=True)
    )

    data.c = 3
    return data


#%%

data = get_data(bs, size)
data.show_batch(ds_type=fv.DatasetType.Valid, rows=2, figsize=(9, 9))

# %%

base_loss = fv.F.l1_loss


def custom_loss(input, target):
    mask = (target > 0) * (target < 1)
    return base_loss(input, target) + base_loss(input[mask], target[mask]) * 100


wd = 1e-3
learn = fv.unet_learner(
    data,
    arch,
    wd=wd,
    loss_func=custom_loss,
    blur=False,
    norm_type=fv.NormType.Weight,
    pretrained=False,
)

fv.gc.collect()

# %%

# learn.lr_find()
# learn.recorder.plot()

#%%

lr = 1e-3

learn.unfreeze()
learn.fit_one_cycle(4, slice(1e-5, lr), pct_start=0.9)
learn.save("first")

#%%

learn.fit_one_cycle(4, slice(1e-5, lr), pct_start=0.9)
learn.save("second")

#%%


learn.fit_one_cycle(5, slice(1e-5, lr), pct_start=0.9)
learn.save("third-d")

# %%
learn.show_results(rows=1, imgsize=5)

# %%

learn.load("first")

# %%

for test_file in fv.get_image_files("data/test/x"):
    img = fv.open_image(test_file)
    predicted = learn.predict(img)[1]

    predicted = predicted.mean(0)
    predicted[predicted < 0] = 0
    predicted[predicted > 1] = 1

    transforms.ToPILImage()(predicted).save(f"data/test/y_hat/{test_file.name}")


# %%
