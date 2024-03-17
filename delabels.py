#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import json
import os
import time
from typing import List, Dict, Set, Any

now: int = int(time.time())


def filter_unexist_files(files: List[str]) -> List[str]:
    [print(f'{file} do not exist') for file in files if (not os.path.exists(file) or (not os.path.isfile(file)))]
    files = [file for file in files if file.endswith(".yolo.json")]
    return [file for file in files if os.path.exists(file)]


def check_json_format(files: List[str]) -> List[str]:
    format_correct: List[str] = []
    for file in files:
        with open(file, encoding="utf-8") as f:
            content = f.read()
            obj: Dict[str, Any] = json.loads(content)
            assert (obj["name"] != "")
            assert (obj["labels"] != {})
            assert (obj["files"] != {})
        for k, v in obj["labels"].items():
            assert (isinstance(k, str))
            assert (isinstance(v, int))
        for file_labels in obj["files"]:
            assert (file_labels["filename"] != "")
            for labels in file_labels["labels"]:
                assert (isinstance(labels["type"], str))
                assert (labels["type"] != "")
                assert (labels["type"] in obj["labels"])
                assert (labels["values"] != [])
                for value in labels["values"]:
                    assert (isinstance(value, float))
                    assert (value >= 0)
                    assert (value <= 1)
        format_correct.append(file)
    return format_correct


def convert_folder_from_a_json(path: str) -> None:
    with open(path, encoding="utf-8") as yolojson:
        content = yolojson.read()
        obj: Dict[str, Any] = json.loads(content)
        name: str = obj["name"]
        label_map: Dict[str, int] = obj["labels"]
        files: List[Dict[str, Any]] = obj["files"]
        path: str = os.path.dirname(path)
    # create folder if not exist
    if not os.path.exists(f'{path}/{name}'):
        os.mkdir(f'{path}/{name}')
    # create files one by one
    for file in files:
        filename: str = file["filename"]
        labels: List[Dict[str, Any]] = file["labels"]
        with open(f"{path}/{name}/{filename}", encoding="utf-8", mode="w") as f:
            for label in labels:
                typestr: str = label["type"]
                values: List[float] = label["values"]
                f.write(f"{label_map[typestr]} {' '.join([str(value) for value in values])}\n")
    print(f"convert {path} to {name}")


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="delabels.py",
        description="this file deserialize the labels of pictures from json to txt files",
        epilog="Text at the bottom of help",
    )

    parser.add_argument(
        "-f",
        "--files",
        action="append",
        help="files of the filename.yolo.json of pictures",
        required=True,
    )
    args = vars(parser.parse_args())
    files: List[str] = args["files"]
    files: List[str] = filter_unexist_files(files)
    # files: List[str] = filter_unexist_folder(files)
    files: List[str] = check_json_format(files)
    # files: List[str] = check_folder_format(files)
    for file in files:
        convert_folder_from_a_json(file)
    print("hello-world")


if __name__ == "__main__":
    main()

# parse command line args
