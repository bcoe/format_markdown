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
import markdown
import re
import xmltodict

re_replace_leading_colon = re.compile(r"^:\W?")

def is_dotnet(parsed_md):
    # Dotnet format CHANGELOG has heading: "Changes in this release":
    if parsed_md['xml'].get('p', None):
        if re.match(r"Changes in this release", parsed_md['xml'].get('p')):
            return True
    return False

# Format: https://github.com/googleapis/google-cloud-dotnet/releases/tag/Google.Cloud.BigQuery.Storage.V1-2.5.0
def format_dotnet(parsed_md):
    md = "### Updates\n\n"
    # There do not appear to be any updates for this release,
    # consumer should throw out this entry:
    if not parsed_md['xml'].get('ul', {}).get('li', None):
        return None
    
    # Dotnet format changelog should consist of list of updates:
    # - feat: foo
    # - docs: bar
    if not type(parsed_md['xml']['ul']['li']) is list:
        return None

    for li in parsed_md['xml']['ul']['li']:
        # If a single commit includes multiple changes, the changes will
        # be nested as standalone strings under top level li:
        #  - [Commit beebb6a](https://github.com/googleapis/google-cloud-dotnet/commit/beebb6a):
        #    - docs: Align session length with public documentation
        #    - feat: Expose estimated bytes that a session will scan.
        if type(li) == str:
            md += f"* {li}\n"
        # If there are not multiple commits, format is as follows:
        # - [Commit c896df1](https://.../c896df1): feat: add BigQuery Storage Write API v1
        elif li.get('#text', None):
            line = re_replace_leading_colon.sub("", li['#text'])
            if line:
                md += f"* {line}\n"
    return md

def format(text):
    parsed_md = xmltodict.parse(
        f"<xml>{markdown.markdown(text)}</xml>"
    )
    if is_dotnet(parsed_md):
        return format_dotnet(parsed_md)
    else:
        # Node.js, Python, and Java do not require any reformatting.
        # Format: https://github.com/googleapis/nodejs-secret-manager/releases/tag/v3.8.0
        return text
