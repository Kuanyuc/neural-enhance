#!/bin/sh
python3 enhance.py --train "../dataset/**/*.jpg" --loss-save-file=train.earlyfusion.log --device=gpu0 \
--model earlyfusion --train-scales=2 --epochs=1200 --perceptual-layer=conv5_2 --smoothness-weight=2e5 \
--adversary-weight=1e3 --generator-start=5 --discriminator-start=0 --adversarial-start=5 --discriminator-size=64
