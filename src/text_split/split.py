import argparse
import os

parser = argparse.ArgumentParser(description="a simple parser")

parser.add_argument("filename", type=str)
parser.add_argument("lineno", nargs="+", type=int)
parser.add_argument("--same_length", action=argparse.BooleanOptionalAction)


def main():
    args = parser.parse_args()
    filename = args.filename
    linenos = args.lineno
    same_length = args.same_length
    linenos = list(map(lambda x: x - 1, linenos))
    linenos.sort()
    results = []
    with open(filename, "r", encoding="utf-8") as f:
        content = f.readlines()
        if not same_length:
            start = 0

            for lineno in linenos:
                results.append("".join(content[start:lineno]))
                start = lineno
            results.append("".join(content[start:]))

        else:
            lineno = linenos[0] + 1 if linenos[0] else 100000
            start = 0
            while start < len(content):
                results.append("".join(content[start: start + lineno]))
                start += lineno

        name, ext = os.path.splitext(filename)

        for i, result in enumerate(results):
            with open(f"{name}-{i + 1:02}{ext}", "w", encoding="utf-8") as f:
                f.write(result)
