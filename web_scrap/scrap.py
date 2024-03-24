import os
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile


class Scrapper:
    main_tag            = "a"
    main_class          = "internal-link"
    main_string         = "Anexo"
    main_file_extension = ".pdf"

    def __init__(self, link, target_filename, folder=""):
        self.link      = link
        self.target    = target_filename
        self.filtered  = list()
        self.folder    = folder

        if self.folder.endswith("/"):
            raise KeyError("Folder name must not end with '/'")

        if self.folder != "":
            try:
                os.mkdir(self.folder)
            except OSError as error:
                print(f"Folder {self.folder} already created")


    def parsed_page(self, link):
        """
        Get a link to a webpage and returns
        the html already parsed.

        link: main link to page to be scrapped
        """
        page = requests.get(link)
        parser_page = BeautifulSoup(page.text, "html.parser")

        return parser_page


    def find_by_tag_class(self, parser_page):
        """
        Filter all the tags returning
        a list of all anchors in page

        parser_page: html already parsed
        """
        special_tags = parser_page.find_all(self.main_tag, class_=self.main_class)

        return special_tags


    def filter_by_string_and_href(self, tag):
        """
        Auxiliary function
        """
        return self.main_string in tag.string and tag.get("href").endswith(self.main_file_extension)


    def filtered_result(self, tag_list):
        """
        Filter wrong links and anchors
        given a list of special links

        tag_list: list of already filtered tags (anchors)
        """
        list_result = list(filter(self.filter_by_string_and_href, tag_list))

        if len(list_result) != 2:
            raise KeyError("Number of links different from expected")

        self.filtered = list_result


    def download_files(self):
        """
        Download the files in 'href' given
        a set of anchors
        """
        right_path = f"{self.folder}/" if self.folder != "" else ""

        for anchor in self.filtered:
            link_to_file = anchor.get("href")

            chunk_size = 2000
            requested_file = requests.get(link_to_file, stream=True)
            filename = os.path.basename(link_to_file)

            print(f"Getting file: {filename}")
            try:
                with open(f"{right_path}{filename}", "wb") as file:
                    for chunk in requested_file.iter_content(chunk_size):
                        file.write(chunk)
            except OSError as error:
                raise KeyError(f"Error while get file: {filename}\n\nError: {error}")



    def zip_files(self):
        right_path = f"{self.folder}/" if self.folder != "" else ""
        
        try:
            with ZipFile(self.target, mode="w") as archive:
                for file in self.filtered:
                    link_to_file = file.get("href")
                    filename = os.path.basename(link_to_file)

                    archive.write(f"{right_path}{filename}")
        except OSError as error:
            raise KeyError(f"Error while zipping file: {right_path}{filename}\n\nError: {error}")


    def get_files(self):
        parsed = self.parsed_page(self.link)
        special_tags = self.find_by_tag_class(parsed)
        self.filtered_result(special_tags)
        self.download_files()
        self.zip_files()
