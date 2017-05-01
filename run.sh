#!/bin/sh
# pretrain generator with lower conv2_2 layer
python3 enhance.py --train "../dataset/**/*.jpg" --loss-save-file=train.latefusion.log --device=cuda \
--model latefusion --epochs=50 --batch-shape=256 \
--generator-blocks=8 --generator-filters=128 --generator-residual=0 \
--perceptual-layer=conv2_2 --smoothness-weight=1e7 --adversary-weight=0.0 \
--batch-size=15 --frame-expanse=1 --learning-rate=1E-5
--train-noise=1.0

# train together with discriminator
python3 enhance.py --train "../dataset/**/*.jpg" --loss-save-file=train.latefusion.log --device=cuda \
--model latefusion --epochs=2667 --perceptual-layer=conv5_2 \
--smoothness-weight=5e3 --adversary-weight=5e1 --batch-shape=256 \
--generator-start=10 --discriminator-start=0 --adversarial-start=10 --discriminator-size=64 \
--batch-size=15 --frame-expanse=1 --learning-rate=1E-6
