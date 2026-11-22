from pathlib import Path
import numpy as np
import torch
import torchvision.datasets as datasets
from torch.utils.data import random_split
from torchvision.transforms import transforms


def get_mnist():
    mnist_trainset = datasets.MNIST(root='../data', train=True, download=True)
    mnist_testset = datasets.MNIST(root='../data', train=False, download=True)

    # Split the 60k MNIST Trainset into 50k Training Samples and 10k Validation Samples with Random Seed 42
    random_seed = torch.Generator().manual_seed(42)
    train, validation = random_split(mnist_trainset, [50000, 10000], generator=random_seed)

    train_images = []
    train_targets = []
    for index in train.indices:
        image, target = mnist_trainset[index]
        train_images.append(image)
        train_targets.append(target)

    val_images = []
    val_targets = []
    for index in validation.indices:
        image, target = mnist_trainset[index]
        val_images.append(image)
        val_targets.append(target)

    test_images = []
    test_targets = []
    for image, target in mnist_testset:
        test_images.append(image)
        test_targets.append(target)


    train_images = np.array(train_images)
    train_targets = np.array(train_targets)
    val_images = np.array(val_images)
    val_targets = np.array(val_targets)
    test_images = np.array(test_images)
    test_targets = np.array(test_targets)


    print("Train distribution:", np.bincount(train_targets))
    print("Validation distribution:", np.bincount(val_targets))
    print("Test distribution:", np.bincount(test_targets))
    print("Train images:", train_images.shape, "    min:", train_images.min(), "    max:", train_images.max())
    print("Val images:", val_images.shape, "    min:", val_images.min(), "    max:", val_images.max())
    print("Test images:", test_images.shape, "    min:", test_images.min(), "    max:", test_images.max())


    save_dir = Path("../data/MNIST/processed_v2")
    save_dir.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(save_dir / "train.npz", images=train_images, labels=train_targets)
    np.savez_compressed(save_dir / "validation.npz", images=val_images, labels=val_targets)
    np.savez_compressed(save_dir / "test.npz", images=test_images, labels=test_targets)

    print("Saved processed datasets successfully.")

if __name__ == '__main__':
    get_mnist()