from pathlib import Path
from datetime import datetime, timedelta
from keras.preprocessing.image import load_img, img_to_array
import numpy as np
from keras.models import load_model
import shutil
from config import checked_image_dir, gourmet_dir
import argparse
from args import get_args


def filtered_path_list(days, checked_image_dir):
    today = datetime.today()
    today_str = today.strftime("%Y/%m/%d %H:%M:%S")
    print(f"Executed at {today_str}.")
    p = Path(f"{checked_image_dir}/{today.year}")
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


def load_images(path_list, height, width):
    images = []
    for path in path_list:
        img = load_img(path, target_size=(height, width))
        img_array = img_to_array(img)
        images.append(img_array / 255)
    return np.array(images)


def get_prediction(images, threshold, model_dir, model_name):
    model_path = f"{model_dir}/{model_name}"
    model = load_model(model_path)
    pred = model.predict(images)[:, 1]
    return np.where(pred >= threshold, 1, 0)


def move_files(pred, path_list, gourmet_dir):
    for i in range(len(path_list)):
        if pred[i] == 1:
            shutil.move(str(path_list[i]),
                        f"{gourmet_dir}/{path_list[i].name}")
    print(f"{sum(pred==1)} files are classified as gourmet image and moved.")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    get_args(parser)
    args = parser.parse_args()

    path_list = filtered_path_list(
        days=args.days, checked_image_dir=checked_image_dir)
    images = load_images(path_list, height=args.height, width=args.width)
    if len(images) == 0:
        raise Exception("No images to be classified!")
    pred = get_prediction(images, threshold=args.threshold,
                          model_dir=args.model_dir, model_name=args.model_name)

    move_files(pred, path_list, gourmet_dir=gourmet_dir)
