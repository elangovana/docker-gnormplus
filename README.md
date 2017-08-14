
# docker-gnormplus
Docker for Gnormplus for gene named entity recognition & gene normalisation

## How to run
1. Start docker and map your local host path (e.g /mnt/biocreative/gnormplus) to the container path /gnormdata
> docker run -i -t lanax/gnormplus -v /mnt/biocreative/gnormplus:/gnormdata

2. Inside the docker container, run GNormPlus with input files in mounted directory /gnormdata/input.
> java -Xmx10G -Xms10G -jar /GNormPlusJava/GNormPlus.jar /gnormdata/input /gnormdata/output /gnormdata/setup.txt

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
## Additional Information
GNormplus - https://www.ncbi.nlm.nih.gov/research/bionlp/Tools/gnormplus/

