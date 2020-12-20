from brewtils import command, parameter, system, Plugin

from .__version__ import __version__


@system
class Client:
    pass


def main():
    plugin = Plugin(
        name="{{ cookiecutter.plugin_name }}",
        version=__version__,
        description="{{ cookiecutter.description }}",
    )
    plugin.client = Client()
    plugin.run()


if __name__ == "__main__":
    main()
