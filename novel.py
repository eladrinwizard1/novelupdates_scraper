from typing import List

from chapter import Chapter


class Novel:
    """
    Represents a novel.
    """

    def __init__(self, link: str) -> None:
        """
        Initializes a new Novel.
        :param link: Link to the novelupdates source page for the Novel.
        :return None.
        """
        # TODO: put metadata here
        self.chapters: List[Chapter] = []
        raise NotImplementedError

    def __getitem__(self, key: int) -> Chapter:
        """
        Returns the chapter specified by the index.
        :param key: The index of the chapter to return.
        :return: The indicated chapter.
        """
        return self.chapters[key]

    def _scrape_chapters(self) -> None:
        """
        Downloads the chapter data for the novel.
        :return: None.
        """
        raise NotImplementedError

    def _build_novel(self, path: str) -> None:
        """
        Builds an ebook for the given novel and returns a path to the novel.
        :param path: The directory in which to create the ebook.
        :return: None.
        """
        raise NotImplementedError