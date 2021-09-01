# Chaos Game Representation

A Python script to generate the chaos game representation of a DNA sequence (https://towardsdatascience.com/chaos-game-representation-of-a-genetic-sequence-4681f1a67e14).

Here an example with a SARS-CoV-2 sequence.

![NC_045512 22](https://user-images.githubusercontent.com/62892813/120557509-529c0c00-c3fe-11eb-87c4-f2c402cacaac.png)

## Further modifications

The `.fasta` sequences are not handled in a smart way. The output of this script is a `matplotlib` plot. In future I want the program to produce images with arbitrary resolution in which the actual matplotlib points will be substituted with the pixels, in order to train neural networks with images containing sequences features. Probably I will do it with `SeqIO` from `Bio` and `OpenCV`, in Python.
