from pathlib import Path
from datetime import datetime, timedelta
from keras.preprocessing.image import load_img, img_to_array
import numpy as np
from keras.models import load_model
import shutil
from config import checked_image_dir, gourmet_dir, slack_token
import argparse
from args import get_args
import glob
from slack import WebClient


def filtered_path_list(days, checked_image_dir):
    """実行した日の前日からdays日間に撮影されたimage fileのpathを取得する."""
    today = datetime.today()
    result = []
    for i in range(1, days + 1):
        d = today - timedelta(days=i)
        date_limited_path_list = get_path_list(
            d.year, d.month, d.day, checked_image_dir)
        filtered_with_suffix = filter_with_suffix(date_limited_path_list)
        result = result + filtered_with_suffix
    return result


def get_path_list(year, month, day, checked_img_dir):
    """指定した日付の画像のpathのリストを返す."""
    p = checked_img_dir / f"{year}/{month:02d}/{day:02d}"
    return list(p.glob("*/*"))


def filter_with_suffix(path_list):
    """該当する拡張子以外のファイルへのpathをリストから除外する."""
    result = []
    for path in path_list:
        if path.suffix.lower() in [".jpg", ".png"]:
            result.append(path)
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


def move_files(path_list, gourmet_dir):
    for p in path_list:
        shutil.move(p, gourmet_dir / p.name)


def get_gourmet_path_list(pred, path_list_to_classify):
    path_list = []
    for i in range(len(path_list_to_classify)):
        if pred[i] == 1:
            path_list.append(path_list_to_classify[i])
    return path_list


def post_to_slack(message, path_list, slack_token, gourmet_dir):
    client = WebClient(slack_token)
    client.chat_postMessage(channel="classified_gourmet",
                            text=message, username="gourmet_classifier")

    for p in path_list:
        client.files_upload(
            channels="classified_gourmet",
            file=str(gourmet_dir / p.name)
        )


def main(args):
    message_to_post = ""
    path_list_to_classify = filtered_path_list(
        days=args.days, checked_image_dir=Path(checked_image_dir))
    date = datetime.now()
    message_to_post += f"[{date.year}/{date.month:02d}/{date.day:02d} {date.hour:02d}:{date.minute:02d}]\n"

    images = load_images(path_list_to_classify,
                         height=args.height, width=args.width)
    if len(images) == 0:
        message_to_post += "No images to be classified!"
        post_to_slack(message_to_post, [], slack_token)
        return
    else:
        message_to_post += f"{len(path_list_to_classify)} files are found.\n"
    pred = get_prediction(images, threshold=args.threshold,
                          model_dir=args.model_dir, model_name=args.model_name)

    message_to_post += f"{sum(pred==1)} files are classified as gourmet image and moved.\n"
    path_list = get_gourmet_path_list(
        pred, path_list_to_classify)
    move_files(path_list, gourmet_dir)
    images_num = len(glob.glob(f"{gourmet_dir}/*"))
    message_to_post += f"{images_num} files are in {gourmet_dir} now."
    post_to_slack(message_to_post, path_list, slack_token, gourmet_dir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    get_args(parser)
    args = parser.parse_args()
    main(args)
