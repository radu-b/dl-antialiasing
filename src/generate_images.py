#%%
from PIL import Image, ImageDraw, ImageFont
import string
import random

#%%

fonts = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
    "/usr/share/fonts/truetype/freefont/FreeMono.ttf",
    "/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf",
    "/usr/share/fonts/truetype/freefont/FreeMonoBoldOblique.ttf",
    "/usr/share/fonts/truetype/freefont/FreeMonoOblique.ttf",
    "/usr/share/fonts/truetype/freefont/FreeSans.ttf",
    "/usr/share/fonts/truetype/freefont/FreeSansBold.ttf",
    "/usr/share/fonts/truetype/freefont/FreeSansBoldOblique.ttf",
    "/usr/share/fonts/truetype/freefont/FreeSansOblique.ttf",
    "/usr/share/fonts/truetype/freefont/FreeSerif.ttf",
    "/usr/share/fonts/truetype/freefont/FreeSerifBold.ttf",
    "/usr/share/fonts/truetype/freefont/FreeSerifBoldItalic.ttf",
    "/usr/share/fonts/truetype/freefont/FreeSerifItalic.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationMono-BoldItalic.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationMono-Italic.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-BoldItalic.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSansNarrow-Bold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSansNarrow-BoldItalic.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSansNarrow-Italic.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSansNarrow-Regular.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSerif-BoldItalic.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf",
    "/usr/share/fonts/truetype/liberation2/LiberationMono-Bold.ttf",
    "/usr/share/fonts/truetype/liberation2/LiberationMono-BoldItalic.ttf",
    "/usr/share/fonts/truetype/liberation2/LiberationMono-Italic.ttf",
    "/usr/share/fonts/truetype/liberation2/LiberationMono-Regular.ttf",
    "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf",
    "/usr/share/fonts/truetype/liberation2/LiberationSans-BoldItalic.ttf",
    "/usr/share/fonts/truetype/liberation2/LiberationSans-Italic.ttf",
    "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    "/usr/share/fonts/truetype/liberation2/LiberationSerif-Bold.ttf",
    "/usr/share/fonts/truetype/liberation2/LiberationSerif-BoldItalic.ttf",
    "/usr/share/fonts/truetype/liberation2/LiberationSerif-Italic.ttf",
    "/usr/share/fonts/truetype/liberation2/LiberationSerif-Regular.ttf",
]


def random_text():
    letters = "       " + string.digits + string.ascii_letters + string.punctuation
    return "\n".join(
        "".join(random.choice(letters) for i in range(20)) for l in range(0, 20)
    )


def random_text_image():
    font_size = random.randint(20, 80)
    font = ImageFont.truetype(random.choice(fonts), font_size)
    image = Image.new("L", (200, 200), color=(255))
    draw = ImageDraw.Draw(image)

    x = random.randint(-font_size, font_size)
    y = random.randint(-font_size, font_size)
    draw.text((x, y), random_text(), font=font, fill=(0))

    return image


def random_figure():
    image = Image.new("L", (800, 800), color=(255))
    draw = ImageDraw.Draw(image)

    for i in range(4):
        coords = [random.randint(0, 800) for c in range(4)]
        draw.line(coords, fill=(0), width=random.randint(4, 50))

    return image.resize((200, 200), resample=Image.BICUBIC)


#%%

random.seed(4)

for index in range(5000):
    if index % 100 == 0:
        print(100 * index / 5000)

    image = random_text_image()
    image.save(f"data/train/y/{index}.png")
    image.convert("1", dither=0).save(f"data/train/x/{index}.png")


# %%

for index in range(5000, 10000):
    if index % 100 == 0:
        print(100 * index / 10000)

    image = random_figure()
    image.save(f"data/train/y/{index}.png")
    image.convert("1", dither=0).save(f"data/train/x/{index}.png")

# %%
