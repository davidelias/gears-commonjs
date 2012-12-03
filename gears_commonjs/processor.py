import re

from gears.processors.base import BaseProcessor


MODULE = u"require.define({'%(name)s': function(exports, require, module){%(source)s}});"


class CommonJSProcessor(BaseProcessor):

    module_search = None

    def __init__(self, module_search=None):
        if module_search:
            self.module_search = re.compile(module_search)

    def __call__(self, asset):
        name = self.get_module_name(asset.attributes.path_without_suffix)
        if name:
            asset.processed_source = MODULE % {
                'name': name,
                'source': asset.processed_source
            }

    def get_module_name(self, path):
        if not self.module_search:
            return path

        match = self.module_search.match(path)
        if match:
            for m in match.groups():
                path = path.replace(m, '')
            return path.lstrip('/')
