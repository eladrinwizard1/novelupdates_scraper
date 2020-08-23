from typing import List, Optional

from chapter import Chapter

import pypub


class Novel:
    """
    Represents a novel.
    """

    def __init__(self, link: str) -> None:
        """
        Initializes a new novel.
        :param link: Link to the novelupdates source page for the novel.
        :return None.
        """
        self.link: str = link

        self._scrape_metadata()
        self._init_chapters()

    def _scrape_metadata(self) -> None:
        """
        Scrapes the metadata from the novel homepage.
        :return: None.
        """
        self.title: str = ""
        raise NotImplementedError

    def _init_chapters(self) -> None:
        """
        Initializes the chapter list.
        :return: None.
        """
        self.chapters: List[Chapter] = []
        raise NotImplementedError

    def scrape(self, path: str, translator: Optional[str] = None,
               no_cache: bool = False) -> None:
        """
        Scrapes a novel to a given output directory.
        :param path: The output directory.
        :param translator: The translator to prefer, or None.
        :param no_cache: Whether to force rescraping of cached chapters.
        :return: None.
        """
        # TODO: pass in metadata here
        epub = pypub.Epub(self.title)
        chapter_data = [c.scrape(translator, no_cache) for c in self.chapters]
        for c in chapter_data:
            epub.add_chapter(c)
        epub.create_epub(path)
