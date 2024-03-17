# barcode_detection_dataset

1. Dataset format is yolo.

2. All codes based on MIT

3. Any uncode part are based on CC-BY-SA-4.0(or any later version).

DO NOT TO BE DONE: Auto Download and unzip shell script.
+ you should download and put the pictures to its own subfolder.

DONE: Use Json to store data labels, produce them by script after download repo.
+ [x] convert the labels to a `filename.yolo.json` file
+ [x] convert the `filename.yolo.json` file to a yolo format folder

ps: the json file after tgz is smaller than the original folder.

## toolchain

+ scoop install python3
+ scoop install poetry
+ poetry install

[![MIT](https://img.shields.io/badge/License-MIT-orange)][MIT]

[![CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-orange)][cc_by_sa_4_0]

[![CC BY-SA 4.0][cc_by_sa_4_0_image]][cc_by_sa_4_0]

[MIT]: https://opensource.org/licenses/MIT

[cc_by_sa_4_0]: https://creativecommons.org/licenses/by-sa/4.0/

[cc_by_sa_4_0_image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
