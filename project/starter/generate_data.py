import argparse
from pathlib import Path
import numpy as np


def make_line_image(size=32, slope=0.2, intercept=16, noise_hits=20):
    img = np.zeros((size, size), dtype=np.float32)
    xs = np.arange(size)
    ys = slope * xs + intercept
    for x, y in zip(xs, ys):
        yi = int(np.clip(round(y), 0, size - 1))
        img[yi, x] = 1.0

    for _ in range(noise_hits):
        ry = np.random.randint(0, size)
        rx = np.random.randint(0, size)
        img[ry, rx] = 1.0
    return img


def make_curve_image(size=32, curve=0.01, slope=0.0, intercept=8, noise_hits=20):
    img = np.zeros((size, size), dtype=np.float32)
    xs = np.arange(size)
    ys = curve * (xs - size / 2) ** 2 + slope * xs + intercept
    for x, y in zip(xs, ys):
        yi = int(np.clip(round(y), 0, size - 1))
        img[yi, x] = 1.0

    for _ in range(noise_hits):
        ry = np.random.randint(0, size)
        rx = np.random.randint(0, size)
        img[ry, rx] = 1.0
    return img


def generate_classification(n_samples=2000, size=32, seed=42):
    rng = np.random.default_rng(seed)
    X = np.zeros((n_samples, size, size), dtype=np.float32)
    y = np.zeros(n_samples, dtype=np.int64)

    for i in range(n_samples):
        noise_hits = int(rng.integers(5, 30))
        if i % 2 == 0:
            slope = float(rng.uniform(-0.5, 0.5))
            intercept = float(rng.uniform(4, size - 4))
            X[i] = make_line_image(size=size, slope=slope, intercept=intercept, noise_hits=noise_hits)
            y[i] = 0
        else:
            curve = float(rng.uniform(0.005, 0.03))
            slope = float(rng.uniform(-0.3, 0.3))
            intercept = float(rng.uniform(0, size / 3))
            X[i] = make_curve_image(size=size, curve=curve, slope=slope, intercept=intercept, noise_hits=noise_hits)
            y[i] = 1

    return X, y


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", choices=["classify"], default="classify")
    parser.add_argument("--n_samples", type=int, default=2000)
    parser.add_argument("--size", type=int, default=32)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--out", type=str, default="project/starter/data_classify.npz")
    args = parser.parse_args()

    if args.task == "classify":
        X, y = generate_classification(args.n_samples, args.size, args.seed)
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        np.savez(out_path, X=X, y=y)
        print(f"Saved: {out_path} | X={X.shape}, y={y.shape}")


if __name__ == "__main__":
    main()
