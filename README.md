# docker-gnormplus
Docker for Gnormplus Gene Normalisation

## How to run
1. Run docker, mount the host drive containing the GnormData input, output & dictionary.
> docker run -i -t lanax/gnormplus -v /mnt/biocreative/gnormplus:/gnormdata

2. Run GNormPlus
> java -Xmx10G -Xms10G -jar /GNormPlusJava/GNormPlus.jar /gnormdata/input /gnormdata/output /gnormdata/setup.txt
