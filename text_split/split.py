import argparse
import os

parser = argparse.ArgumentParser(description="a simple parser")

parser.add_argument("filename", type=str)
parser.add_argument("lineno", nargs="+", type=int)


def main():
    args = parser.parse_args()
    filename = args.filename
    linenos = args.lineno
    linenos = list(map(lambda x: x - 1, linenos))
    linenos.sort()
    results = []

    with open(filename, "r", encoding="utf-8") as f:
        content = f.readlines()

    start = 0

    for lineno in linenos:
        results.append("".join(content[start:lineno]))
        start = lineno
    results.append("".join(content[start:]))

    name, ext = os.path.splitext(filename)

    for i, result in enumerate(results):
        with open(f"{name}-{i + 1:02}{ext}", "w", encoding="utf-8") as f:
            f.write(result)
