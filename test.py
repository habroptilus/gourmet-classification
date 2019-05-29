from pathlib import Path
from datetime import datetime, timedelta


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


for path in filtered_path_list(10):
    print(datetime.fromtimestamp(path.stat().st_birthtime))
