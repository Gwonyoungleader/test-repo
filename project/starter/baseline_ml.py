import argparse
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
from sklearn.model_selection import train_test_split


def run_classification(data_path: str, seed: int = 42):
    d = np.load(data_path)
    X = d["X"]
    y = d["y"]

    X = X.reshape((X.shape[0], -1))

    X_train, X_temp, y_train, y_temp = train_test_split(
        X, y, test_size=0.3, random_state=seed, stratify=y
    )
    X_valid, X_test, y_valid, y_test = train_test_split(
        X_temp, y_temp, test_size=0.5, random_state=seed, stratify=y_temp
    )

    clf = LogisticRegression(max_iter=300)
    clf.fit(X_train, y_train)

    for split_name, X_split, y_split in [
        ("valid", X_valid, y_valid),
        ("test", X_test, y_test),
    ]:
        pred = clf.predict(X_split)
        acc = accuracy_score(y_split, pred)
        f1 = f1_score(y_split, pred)
        cm = confusion_matrix(y_split, pred)
        print(f"[{split_name}] acc={acc:.4f}, f1={f1:.4f}")
        print(cm)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", choices=["classify"], default="classify")
    parser.add_argument("--data", type=str, default="project/starter/data_classify.npz")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    if args.task == "classify":
        run_classification(args.data, args.seed)


if __name__ == "__main__":
    main()
