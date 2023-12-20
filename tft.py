from dataclasses import dataclass
from typing import ClassVar


@dataclass
class TFT:
    title: str
    description: str
    contact: str
    source: str
    separator: ClassVar[str] = f"\n\0\n"

    def __str__(self):
        return (f"## Título: {self.title}\n"
                f"Descripción: {self.description}\n"
                f"Contacto: {self.contact}\n"
                f"\n"
                f"[Enlace]({self.source})\n"
                f"\n")

    def contains_query(self, query: str):
        return query in (self.title + self.description + self.contact).casefold()
