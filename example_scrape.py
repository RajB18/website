"""Minimal example of using Scrapling to fetch and parse a page."""

from scrapling.fetchers import Fetcher


def main() -> None:
    page = Fetcher.get("https://example.com/")
    print(page.css("h1::text").get())


if __name__ == "__main__":
    main()
