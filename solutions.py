import os
from dotenv import load_dotenv

from web_scrap.scrap import Scrapper

load_dotenv()

def solution_one():
	LINK = os.getenv("LINK")
	src = Scrapper(LINK, "files.zip", "data")
	src.get_files()


def solution_two():
	LINK = os.getenv("LINK")
	src = Scrapper(LINK, "files.zip", "data")
	src.download_files()


def main():
	if __name__ == "__main__":
		solution_one()


main()