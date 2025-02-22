# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022-2024)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pathlib

import streamlit as st
from tests.delta_generator_test_case import DeltaGeneratorTestCase


class StHtmlAPITest(DeltaGeneratorTestCase):
    """Test st.html API."""

    def test_st_html(self):
        """Test st.html."""
        st.html("<i> This is a i tag </i>")

        el = self.get_delta_from_queue().new_element
        self.assertEqual(el.html.body, "<i> This is a i tag </i>")

    def test_st_html_with_file(self):
        """Test st.html with file."""
        st.html("./tests/streamlit/elements/test_html.js")

        el = self.get_delta_from_queue().new_element
        self.assertEqual(el.html.body, "<button>Corgi</button>")

    def test_st_html_with_path(self):
        """Test st.html with path."""
        st.html(pathlib.Path("./tests/streamlit/elements/test_html.js"))

        el = self.get_delta_from_queue().new_element
        self.assertEqual(el.html.body, "<button>Corgi</button>")
