import os
import re
import shlex

from compressor.exceptions import FilterError
from compressor.filters.base import CompilerFilter


class VueCompiler(CompilerFilter):
    def __init__(self, content, attrs, **kwargs):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        node_path = os.path.join(base_dir, 'npm_prefix', 'node_modules')
        rollup_bin = os.path.join(node_path, 'rollup', 'dist', 'bin', 'rollup')
        rollup_config = os.path.join(base_dir, 'rollup.config.js')
        command = (
            ' '.join((
                'NODE_PATH='+shlex.quote(node_path),
                shlex.quote(rollup_bin),
                '-c',
                shlex.quote(rollup_config))
            ) +
            ' --input {infile} -n {export_name} --file {outfile}'
        )
        super().__init__(content, command=command, **kwargs)

    def input(self, **kwargs):
        if self.filename is None:
            raise FilterError('VueCompiler can only compile files, not inline code.')
        self.options += (('export_name', re.sub(
            r'^([a-z])|[^a-z0-9A-Z]+([a-zA-Z0-9])?',
            lambda s: s.group(0)[-1].upper(),
            os.path.basename(self.filename).split('.')[0]
        )),)
        return super().input(**kwargs)
