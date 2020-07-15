from inspect import cleandoc

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
