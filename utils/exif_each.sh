#!/bin/bash
set -eoux pipefail
###
 # @Github: https://github.com/Certseeds/barcode_detection_dataset
 # @Organization: SUSTech
 # @Author: nanoseeds
 # @Date: 2021-03-17 22:27:04
 # @LastEditors: nanoseeds
 # @LastEditTime: 2021-03-17 22:43:21
### 
#!/bin/bash
set -eoux pipefail
pre_path="../barcode_detection_dataset/"
clear_path(){
    origin_path=$(pwd)
    for i in "$@"; do
        pic_path=${pre_path}${i}
        cd ${pic_path}
        for file in ./* ;do
            if [[ -f ${file}  ]] ; then
                echo "${file} 是文件"
                exiftool -all= ${file}
            fi
        done
        cd ${origin_path}
    done
}
main(){
    path_array[0]="BarcodeDatasets/images/Dataset1"
    path_array[1]="BarcodeDatasets/images/Dataset2"
    path_array[2]="1d_barcode_extended_plain/images/Original"
    path_array[3]="1d_barcode_extended/images/JPEGImages"
    path_array[4]="pictures/images/20210316_2"
    path_array[5]="pictures/images/20210317_2"
    for i in ${path_array[@]}; do
        echo ${pre_path}${i}
    done
    clear_path ${path_array}
}
main $@
# clear_path