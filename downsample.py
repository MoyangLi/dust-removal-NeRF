import numpy as np
import os
import imageio

imgdir = './imgs/wall/images'
savedir = './imgs/wall/images_1'

if not os.path.exists(savedir):
    os.makedirs(savedir)

to8b = lambda x : x.astype(np.uint8)

imgfiles = [os.path.join(imgdir, f) for f in sorted(os.listdir(imgdir)) if
            f.endswith('JPG') or f.endswith('jpg') or f.endswith('png') or f.endswith('bmp')]

# 降采样比例系数
factor = 1

def imread(f):
    return imageio.v3.imread(f)

imgs = [imread(f)[..., :3] for f in imgfiles]
imgs = np.stack(imgs, 0)
sh = imgs.shape
sh = np.array(sh)
sh[1:3] = sh[1:3]/factor
# imgs = np.stack(imgs, -1)
x_array = np.arange(0, sh[2]*factor, factor).tolist()
y_array = np.arange(0, sh[1]*factor, factor).tolist()
new_imgs = np.zeros(sh)
new_imgs = imgs[:, y_array, :, :][:, :, x_array, :]

for i in range(sh[0]):
    if savedir is not None:
        rgb8 = to8b(new_imgs[i])
        filename = os.path.join(savedir, '{:03d}.png'.format(i))
        imageio.imwrite(filename, rgb8)
