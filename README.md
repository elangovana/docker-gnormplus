
# docker-gnormplus
Docker for Gnormplus for gene named entity recognition & gene normalisation

## How to run
1. Start docker and map your local host path (e.g /mnt/biocreative/gnormplus) to the container path /gnormdata
    ```bash
    docker run -it  -v /mnt/biocreative/gnormplus:/gnormdata lanax/gnormplus /bin/bash

    ```


3. To update the set up file.. Copy the contents to  

    ```bash
    cp /gnormdata/setup.txt /GNormPlusJava/setup.txt
    ```
    ##### Sample setup.txt
    ```
    #===Annotation
    #Attribution setting:
    #FocusSpecies = Taxonomy ID
    #	All: All species
    #	9606: Human
    #	4932: yeast
    #	7227: Fly
    #	10090: Mouse
    #	10116: Rat
    #	7955: Zebrafish
    #	3702: Arabidopsis thaliana
    #open: True
    #close: False
    
    [Focus Species]
        FocusSpecies = All
    [Dictionary & Model]
        DictionaryFolder = /GNormPlusJava/Dictionary
        GNRModel = /GNormPlusJava/Dictionary/GNR.Model
        SCModel = /GNormPlusJava/Dictionary/SimConcept.Model
        GeneIDMatch = True
        Normalization2Protein = False
        DeleteTmp = True
    ```

2. Inside the docker container, run GNormPlus with input files in mounted directory /gnormdata/input.
    ```bash
        java -Xmx10G -Xms10G -jar /GNormPlusJava/GNormPlus.jar /gnormdata/input /gnormdata/output setup.txt
    ```

## Running on aws batch
For aws batch, see [aws_batch/Readme.md](aws_batch/Readme.md)
    
For download and update results from S3.
    
    ```bash
    docker run -i -v /data/full_pubmed/:/gnormdata lanax/gnormplus /bin/bash aws_batch_wrapper.sh s3://aegovan-data/pubmed_json_parts/part_0/pubmed19n0219.json.txt /gnormdata/input s3://aegovan-data/test_dumm/  /gnormdata/output 10G 20G 
    ```

## Additional Information
GNormplus - https://www.ncbi.nlm.nih.gov/research/bionlp/Tools/gnormplus/



