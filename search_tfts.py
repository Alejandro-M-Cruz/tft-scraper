from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

from tft import TFT
from tft_searcher import TFTSearcher


def main(query: str | None, file_path: str):
    with open(".tfts", "r") as f:
        tfts = [eval(tft_string) for tft_string in f.read().split(TFT.separator)]
    if query:
        tfts = TFTSearcher(tfts, query).search()
    if len(tfts) == 0:
        print("No results found")
        return
    with open(file_path, "w") as f:
        f.write("\n".join([str(tft) for tft in tfts]))
    print(f"Stored {len(tfts) if query else 'all'} results in {file_path}")


if __name__ == "__main__":
    parser = ArgumentParser(
        description="Scrape and search TFTs and save them to a text file",
        formatter_class=ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("-q", "--query", help="the query to match the TFTs against")
    parser.add_argument("-f", "--file", help="the file to save the results to", default="tfts.md")
    args = vars(parser.parse_args())
    main(args["query"], args["file"])
