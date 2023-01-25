from typing import Union
from rich.text import Text
from rich.style import StyleType

TextParts = Union[str, Text, tuple[str, StyleType]]
