import argparse
import os


def setup_parser():
    description = "This program inject font into your Dek-D's Writer HTML file."
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument(
        "-V", "--version", help="show program version", action="store_true"
    )
    parser.add_argument("-i", "--input", help="specify input file", default="in.html")
    parser.add_argument(
        "-o", "--output", help="specify output file", default="out.html"
    )
    parser.add_argument(
        "-c", "--change", help="specify old font name", default="Cordia New"
    )
    parser.add_argument(
        "-t", "--to", help="specify target font name", default="Sarabun"
    )
    return parser


def inject(name_in, name_out, font_in, font_out):
    buffer = ""
    with open(name_in, "r") as f:
        buffer = f.read()

    # Add @import to the top of the file.
    buffer = (
        '<style>\n\t@import url("https://fonts.googleapis.com/css?family='
        + font_in.replace(" ", "+")
        + '&display=swap");\n</style>\n'
        + buffer
    )

    # Remove extra face argument
    key = buffer.find(font_in + ",") + len(font_in)
    key_end = buffer.find('">', key)
    while True:
        buffer = buffer[:key] + buffer[key_end:]
        key = buffer.find(font_in + ",", key_end) + len(font_in)
        if key < key_end:
            break
        key_end = buffer.find('">', key)

    # Clean up HTML
    buffer = buffer.replace('style=""', "")

    with open(name_out, "w") as g:
        g.write(buffer.replace('face="' + font_in, 'face="' + font_out))


def main():
    parser = setup_parser()
    args = parser.parse_args()
    if not os.path.exists(args.input):
        print("Error: Input file (" + args.input + ") does not exit.")
    else:
        with open(args.input, "r") as f:
            print(
                "There are "
                + str(f.read().count(args.change))
                + " to be replaced. Continue? [Y/n] : ",
                end="",
            )
        if input().lower() == "n":
            exit()
        inject(args.input, args.output, args.change, args.to)
        print("Done")


if __name__ == "__main__":
    main()
