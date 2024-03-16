#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import json
import os
from typing import List, Dict, Set

LABELS_FILE_NAME: str = "labels.txt"


def filter_unexist_folder(paths: List[str]) -> List[str]:
    [print(f'{path} do not exist') for path in paths if (not os.path.exists(path) or (not os.path.isdir(path)))]
    paths =  [path.removesuffix("/") for path in paths]
    paths =  [path.removesuffix("\\") for path in paths]
    return [path for path in paths if os.path.exists(path)]


def check_folder_format(paths: List[str]) -> List[str]:
    format_correct: List[str] = []
    for path in paths:
        files: List[str] = os.listdir(path)
        files: List[str] = [file for file in files if file.endswith(".txt")]
        # remove the file ends with "/" 's /
        files: Set[str] = set(files)
        # using stream to filter the files do not endswith ".txt"
        if (LABELS_FILE_NAME not in files) or (os.path.isfile(f"{path}/{LABELS_FILE_NAME}") is False):
            print(f'{path} do not have labels.txt')
            continue
        with open(f"{path}/{LABELS_FILE_NAME}", encoding="utf-8") as labels:
            lines: List[str] = labels.readlines()
            types: List[str] = [line.strip() for line in lines]
            map: Dict[int, str] = {index: value for index, value in enumerate(types)}
        files.remove(LABELS_FILE_NAME)
        for file in files:
            file: str = f"{path}/{file}"
            assert (os.path.isfile(file))
            with open(file, encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    assert (len(line.split()) == 5)
                    for i in range(0, 4, 1):
                        assert (float(line.split()[i]) >= 0)
                    assert (int(line.split()[0]) in map)
        format_correct.append(path)
    return format_correct


def convert_folder_to_a_json(path: str) -> None:
    with open(f"{path}/{LABELS_FILE_NAME}", encoding="utf-8") as labels:
        lines: List[str] = labels.readlines()
        types: List[str] = [line.strip() for line in lines]
        map: Dict[int, str] = {index: value for index, value in enumerate(types)}
    files: List[str] = os.listdir(path)
    files: List[str] = [file for file in files if file.endswith(".txt")]
    files: Set[str] = set(files)
    files.remove(LABELS_FILE_NAME)
    files_json = []
    for file in files:
        filename: str = file
        file: str = f"{path}/{file}"
        with open(file, encoding="utf-8") as f:
            lines: List[str] = f.readlines()
            lines: List[str] = [line.strip() for line in lines]
            labels: List[Dict[str, object]] = []
            for line in lines:
                typestr: str = map[int(line.split()[0])]
                values: List[float] = [float(value) for value in line.split()[1:]]
                labels.append({
                    "type": typestr,
                    "values": values
                })
        files_json.append({
            "filename": filename,
            "labels": labels
        })
    path_latest: str = path.split("/")[-1]
    map_reverse: Dict[str, int] = {value: index for index, value in map.items()}
    json_object: Dict[str, object] = {
        "name": path_latest,
        "labels": map_reverse,
        "files": files_json
    }
    with open(f"{path}.yolo.json", encoding="utf-8", mode="w") as f:
        f.write(json.dumps(json_object, indent=4))
    print(json_object)


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="labels.py",
        description="this folder package the labels of pictures to a json",
        epilog="Text at the bottom of help",
    )

    parser.add_argument(
        "-p",
        "--path",
        action="append",
        help="fodler of the labels of pictures",
        required=True,
    )
    args = vars(parser.parse_args())
    folders: List[str] = args["path"]
    folders: List[str] = filter_unexist_folder(folders)
    fodlers: List[str] = check_folder_format(folders)
    for folder in folders:
        convert_folder_to_a_json(folder)
    print("hello-world")


if __name__ == "__main__":
    main()

# parse command line args
