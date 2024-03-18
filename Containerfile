FROM python:3.12

COPY . /home/barcode_dataset

WORKDIR /home/barcode_dataset

RUN yes | apt-get update \
    &&  yes | apt-get install pipx \
    && pipx install poetry \
    && pipx ensurepath

RUN /root/.local/bin/poetry install \
    && /root/.local/bin/poetry \
        run python3 \
        ./labels.py \
            -p "./1d_barcode_extended/labels/JPEGImages" \
            -p "./1d_barcode_extended_plain/labels/Original" \
            -p "./BarcodeDatasets/labels/Dataset1" \
            -p "./BarcodeDatasets/labels/Dataset2" \
            -p "./extends/labels/imagenet_2012_n07248320" \
            -p "./pictures/labels/20210316_2" \
            -p "./pictures/labels/20210317_2" \
            -p "./WWU_Muenster_Barcode_Database/labels/nokia-N95-Imgs"

