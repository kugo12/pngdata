from inspect import cleandoc
from typing import Optional, Union, BinaryIO, Tuple
from os import path 

from .abc import PluginABC


class DataToImage:
    plugins = {}

    @classmethod
    def register_plugin(cls):
        def wrap(plugin):
            if issubclass(plugin, PluginABC):
                name = plugin.__name__
                if plugin.__doc__:
                    plugin.__doc__ = cleandoc(plugin.__doc__)
                cls.plugins[name] = plugin
            else:
                raise ValueError(f'{ repr(plugin) } must inherit DataToImage.abc.PluginABC')

            return plugin
        return wrap

    @classmethod
    def help(cls, name: str) -> Optional[str]:
        if name in cls.plugins:
            return cls.plugins[name].__doc__

    @classmethod
    def encode(cls, name: str, data: str,
               save_path: Optional[str] = None) -> Union[str, Tuple[BinaryIO, str]]:
        if name in cls.plugins:
            plugin = cls.plugins[name]

            encoded = plugin.encode(data)  # (BinaryIO, extension)
            if save_path:
                p = path.dirname(save_path)
                fn = path.splitext(path.basename(save_path))[0]
                if not fn:  # if there is no filename
                    fn = 'encoded'
                p = path.join(p, fn + encoded[1])  # path + filename + extension

                with open(p, 'wb') as f:
                    f.write(encoded[0].read())

                return path.abspath(p)
            else:
                return encoded

    @classmethod
    def decode(cls, name: str, p: str) -> Optional[str]:
        if name in cls.plugins:
            plugin = cls.plugins[name]

            if path.exists(p):
                with open(p, 'rb') as f:
                    decoded = plugin.decode(f)

                return decoded
