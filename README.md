# Swin-msi


We provide the mosquito taxonomy index [Unknown_mosquito_identification.py](Unknown_mosquito_identification.py) in this work. Please change to your classification method if you need to use it.

# Overview all architecture of Swin-msi
![MSI](figures/MSI.png)

# Set up
Install swin transformer environment:[Swin-Transformer](https://github.com/microsoft/Swin-Transformer.git)

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
