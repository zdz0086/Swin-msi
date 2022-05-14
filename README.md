# Swin-msi
This project is based on the detection of novel mosquito species based on swin transformer

Before using it, you should get the swin transformer on the [Swin-Transformer](https://github.com/microsoft/Swin-Transformer.git), then follow the usage of the swin transformer, replace the [main.py](main.py) in the swin transformer, and add [Unknown_mosquito_identification.py](Unknown_mosquito_identification.py) to the path of the swin transformer。

We provide the mosquito taxonomy index [Unknown_mosquito_identification.py](Unknown_mosquito_identification.py) in this work. Please change to your classification method if you need to use it.

# Overview Architecture for swin msi
![teaser]()

# set up
Install swin transformer environment

# Run the code
0. To train a `Swin msi` on ImageNet format dataset,run:

```bash
  python -m torch.distributed.launch --nproc_per_node <num-of-gpus-to-use> --master_port 12345  main.py --cfg <config-file> --data-path <imagenet-path
```
  
1. To evaluate a `Swin msi` on ImageNet format dataset,run:
```bash
  python -m torch.distributed.launch --nproc_per_node <num-of-gpus-to-use> --master_port 12345 main.py --eval --cfg <config-file> --resume <checkpoint> --data-path <imagenet-path> 
```


# Acknowledgement
Part of the code is based on the following repositories:
[Swin-Transformer](https://github.com/microsoft/Swin-Transformer.git)
