#!/bin/sh

# Pre-train the model using perceptual loss from paper [1] below.
# python3 enhance.py --train "../dataset/**/*.jpg" --device=gpu0 --model 3DConv --train-scales=1 --epochs=50 \
#     --perceptual-layer=conv2_2 --smoothness-weight=1e7 --adversary-weight=0.0


python3 enhance.py --train "../dataset/**/*.jpg" --loss-save-file=train.3DConv.log --device=gpu0 \
--model 3DConv --train-scales=1 --epochs=2667 --perceptual-layer=conv5_2 --smoothness-weight=2e4 \
--adversary-weight=1e3 --generator-start=5 --discriminator-start=0 --adversarial-start=5 --discriminator-size=64
