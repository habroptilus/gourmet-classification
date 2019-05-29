from pathlib import Path
from datetime import datetime, timedelta
from keras.preprocessing.image import load_img, img_to_array
import numpy as np
from keras.models import load_model
import shutil


def filtered_path_list(days=7):
    today = datetime.today()
    p = Path(
        f"/Users/hikaru/picture/google_drive_smart/Google フォト/{today.year}")
    all_path_list = list(p.glob("*"))
    print(f"{len(all_path_list)} files are found.")
    result = []
    for path in p.glob("*"):
        ct = path.stat().st_birthtime
        dt = datetime.fromtimestamp(ct)
        from_dt = today - timedelta(days=days)
        if from_dt <= dt:
            result.append(path)
    print(f"{len(result)} files have remained after filtering.")
    return result


def load_images(path_list, height=224, width=224):
    images = []
    for path in path_list:
        img = load_img(path, target_size=(height, width))
        img_array = img_to_array(img)
        images.append(img_array / 255)
    return np.array(images)


def get_prediction(images, threshold=0.5, model_path="./models/model_v1.h5"):
    model = load_model(model_path)
    pred = model.predict(images)[:, 1]
    return np.where(pred >= threshold, 1, 0)


def move_files(pred, path_list, gourmet_dir="/Users/hikaru/picture/google_drive_smart/gourmet"):
    for i in range(len(path_list)):
        if pred[i] == 1:
            shutil.move(str(path_list[i]),
                        f"{gourmet_dir}/{path_list[i].name}")


days = 5
path_list = filtered_path_list(days)
images = load_images(path_list)
print(images.shape)

pred = get_prediction(images)
print(pred)

move_files(pred, path_list, gourmet_dir="./images")
