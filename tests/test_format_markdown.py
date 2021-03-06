# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from format_markdown import format
from unittest import TestCase

with open("./tests/fixtures/dotnet.md", "r", encoding="utf-8") as fh:
    dotnet = fh.read()

class FormatMarkdownTests(TestCase):
    def test_converts_dotnet_format_to_standard_format(self):
        fmd = format(dotnet)
        assert '* feat: add BigQuery Storage Write API v1' in fmd
