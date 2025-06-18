import argparse
def sort_lines(lines, reverse=False):
    return sorted(lines, reverse=reverse)
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--reverse", action="store_true")
    parser.add_argument("-o", "--output", required=True)
    parser.add_argument("input_file")
    args = parser.parse_args()

    with open(args.input_file, "r", encoding="utf-8-sig") as infile:
        lines = [line.rstrip('\n') for line in infile.readlines()]

    sorted_lines = sorted(lines, reverse=args.reverse)

    with open(args.output, "w", encoding="utf-8") as outfile:
        for line in sorted_lines:
            outfile.write(line+'\n')  

    print(f"sorted '{args.input_file}' saved to '{args.output}'" + ("(in reverse ordrr)." if args.reverse else "."))
if __name__ == "__main__":
    main()