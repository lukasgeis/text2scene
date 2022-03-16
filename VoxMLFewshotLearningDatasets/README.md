# VoxML Fewshot-Learning Datasets

Create your own Fewshot-Learning-Dataset for VoxML-Attributes. Run 
```
python3 GenerateFewShotData.py <VoxML-Attribute>
    --voxml <VoxML-Directory>
    --dataset <3D-Pointclouds>
    --output <outpath>
```

The following rules apply:
* VoxML-Attribute should include the full 'path' (for example Type/Concavity)
* VoxML-Directory is a directory of VoxML files
* 3D-Pointclouds follow the structure of ModelNet40:
```
│dataset/
├──obj/
│   ├──train/
|       ├── ...           
│   ├──test/
|       ├── ...
├──.......
```

The generation is heavily based and made for [Point-BERT](https://github.com/lulutang0608/Point-BERT).

## Credits

All Pointcloud-Data was taken from the [ModelNet40-Dataset](https://modelnet.cs.princeton.edu/).