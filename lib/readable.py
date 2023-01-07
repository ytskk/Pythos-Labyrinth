from typing import Any


class Readable:
    DEFAULT_ROUND_DIGITS: int = 5
    __round_digits: int | None = None

    def readable(
        self,
        *,
        round_digits: int | None = None,
    ) -> str:
        """
        Outputs all attributes in format: {attribute_name}={attribute_value}.
        Ignores methods.
        """
        self.__round_digits = round_digits or Readable.DEFAULT_ROUND_DIGITS
        return f"{self.__class__.__name__}({self.__props_to_string()})"

    def readable_detailed(
        self,
        include_private_methods: bool = True,
        *,
        round_digits: int | None = None,
    ) -> str:
        """
        Outputs all attributes in format: {attribute_name}={attribute_value}.
        Ignores methods.
        """
        self.__include_private_methods = include_private_methods
        self.__round_digits = round_digits or Readable.DEFAULT_ROUND_DIGITS
        return f"{self.__class__.__name__}({self.__props_to_detailed_string()})"

    def __props_to_detailed_string(self) -> str:
        """
        Converts attributes to string.

        If the attribute is a Readable object, it will be converted to readable_detailed.
        """
        return ", ".join(
            f"{self.__trim_private_classname(name)}={self.__convert_value_to_readable_detailed(getattr(self, name))}"
            for name in self.props()
        )

    def __props_to_string(self) -> str:
        """
        Converts attributes to string.

        If the attribute is a Readable object, it will be converted to readable.
        """
        return ", ".join(
            f"{self.__convert_value_to_readable(getattr(self, name))}"
            for name in self.props()
        )

    def __trim_private_classname(self, name: str) -> str:
        """
        Removes private class name from attribute name.

        Example:
            _Attributes__strength -> __strength
        """
        return (
            name.replace(f"_{self.__class__.__name__}", "")
            if name.startswith("_")
            else name
        )

    def __round_number(self, number: Any) -> str:
        """
        Round value if it is a number. Otherwise, return as is.

        Example:
            1.234223312 -> 1.234
            1.2 -> 1.2
            1 -> 1
            'value' -> 'value'
        """
        return (
            str(round(number, self.__round_digits))
            if isinstance(number, float) and self.__round_digits is not None
            else str(number)
        )

    def __attribute_names(self) -> list[Any]:
        """
        Returns all attribute names of the object, except methods and private attributes and methods.
        """
        return [attr for attr in self.dir() if not callable(getattr(self, attr))]

    def __attribute_values(self) -> list[Any]:
        """
        Returns all attribute values of the object, except methods and private attributes and methods.
        """
        return [getattr(self, attr) for attr in self.__attribute_names()]

    def __convert_value_to_readable_detailed(self, value: Any) -> str:
        """
        If value is a Readable object, it will be converted to readable_detailed. Otherwise, it will be returned as is.
        """
        return (
            value.readable_detailed(
                include_private_methods=self.__include_private_methods
            )
            if isinstance(value, Readable)
            else self.__convert_value_to_readable(value)
        )

    def __convert_value_to_readable(self, value: Any) -> str:
        """
        Beautifies value.
        - If value is a number, it will be rounded to round_digits decimal places.
        """
        converted_value = self.__round_number(value)

        return converted_value

    def props(self) -> list[Any]:
        """
        Returns all attributes of the object, except methods and private attributes and methods.
        """
        return self.__attribute_names()

    def dir(self) -> list[str]:
        """
        Returns all object's attributes and methods names.

        Ignores private attributes.

        You can customize this method to exclude additional attributes.
        """
        return [
            attr
            for attr in dir(self)
            if Readable.__dir_not_is_private(attr)
            and Readable.__dir_not_is_upper(attr)
            and Readable.__dir_not_is_private_classname(attr)
            and self.__dir_shows_private_methods(attr)
        ]

    @staticmethod
    def __dir_not_is_private(name: str) -> bool:
        """
        Skip magic methods and private attributes.

        Example:
            __init__ -> True
            __str__ -> True
            ...
        """
        return not name.startswith("__")

    @staticmethod
    def __dir_not_is_upper(name: str) -> bool:
        """
        Skip static attributes or class constants.

        Example:
            MAX_VALUE -> True
        """
        return not name.isupper()

    @staticmethod
    def __dir_not_is_private_classname(name: str) -> bool:
        """
        Skip Readable private attributes.

        Example:
            _Readable__include_private_methods -> True
        """
        return not name.startswith("_Readable")

    def __dir_shows_private_methods(self, name: str) -> bool:
        """
        Skip private attributes for child classes.

        Example:
            _Attributes__strength -> True
        """
        return self.__include_private_methods or not name.startswith("_")

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        """
        Returns all attributes as string.
        """
        return self.readable()
