poetry run `
    python3 ./delabels.py `
    -f "./1d_barcode_extended/labels/JPEGImages.yolo.json" `
    -f "./1d_barcode_extended_plain/labels/Original.yolo.json" `
    -f "./BarcodeDatasets/labels/Dataset1.yolo.json" `
    -f "./BarcodeDatasets/labels/Dataset2.yolo.json" `
    -f "./extends/labels/imagenet_2012_n07248320.yolo.json" `
    -f "./pictures/labels/20210316_2.yolo.json" `
    -f "./pictures/labels/20210317_2.yolo.json" `
    -f "./WWU_Muenster_Barcode_Database/labels/nokia-N95-Imgs.yolo.json"
