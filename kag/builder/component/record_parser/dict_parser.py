# -*- coding: utf-8 -*-
# Copyright 2023 OpenSPG Authors
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied.

from typing import Dict, List
from kag.interface import RecordParserABC
from knext.common.base.runnable import Output, Input
from kag.builder.model.chunk import Chunk


@RecordParserABC.register("dict")
class DictParser(RecordParserABC):
    """
    A class for parsing dictionaries into Chunk objects.

    This class inherits from RecordParserABC and provides the functionality to convert dictionary inputs
    into a list of Chunk objects.

    Attributes:
        id_col (str): The key in the input dictionary that corresponds to the chunk's ID.
        name_col (str): The key in the input dictionary that corresponds to the chunk's name.
        content_col (str): The key in the input dictionary that corresponds to the chunk's content.
    """

    def __init__(
        self, id_col: str = "id", name_col: str = "name", content_col: str = "content"
    ):
        """
        Initializes the DictParser with the specified column names.

        Args:
            id_col (str): The key in the input dictionary that corresponds to the chunk's ID. Defaults to "id".
            name_col (str): The key in the input dictionary that corresponds to the chunk's name. Defaults to "name".
            content_col (str): The key in the input dictionary that corresponds to the chunk's content. Defaults to "content".
        """
        self.id_col = id_col
        self.name_col = name_col
        self.content_col = content_col

    @property
    def input_types(self) -> Input:
        return Dict

    def invoke(self, input: Input, **kwargs) -> List[Output]:
        """
        Converts the input dictionary into a list of Chunk objects.

        Args:
            input (Input): The input dictionary containing the data to be parsed.
            **kwargs: Additional keyword arguments, currently unused but kept for potential future expansion.

        Returns:
            List[Output]: A list containing a single Chunk object created from the input dictionary.
        """
        chunk_id = input.pop(self.id_col)
        chunk_name = input.pop(self.name_col)
        chunk_content = input.pop(self.content_col)
        return [Chunk(id=chunk_id, name=chunk_name, content=chunk_content, **input)]