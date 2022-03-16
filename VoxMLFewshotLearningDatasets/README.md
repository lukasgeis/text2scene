# VoxML Fewshot-Learning Datasets

Create your own Fewshot-Learning-Dataset for VoxML-Attributes. Run 
```
python3 GenerateFewShotData.py <VoxML-Attribute>
    --voxml <VoxML-Directory>
    --train <train.dat>
    --test <test.dat>
    --output <outpath>
    --way <way>
    --shot <shot>
```

The following rules apply:
* VoxML-Attribute should include the full 'path' (for example Type/Concavity)
* VoxML-Directory is a directory of VoxML files
* train.dat and test.dat should be ModelNet40 datasets (see [Point-BERT](https://github.com/lulutang0608/Point-BERT))

