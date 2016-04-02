from setuptools import setup

setup(
    name="electrum-kobo-server",
    version="1.1",
    scripts=['run_electrum_kobo_server','electrum-kobo-server'],
    install_requires=['plyvel','jsonrpclib', 'irc>=11'],
    package_dir={
        'electrumkoboserver':'src'
        },
    py_modules=[
        'electrumkoboserver.__init__',
        'electrumkoboserver.utils',
        'electrumkoboserver.storage',
        'electrumkoboserver.deserialize',
        'electrumkoboserver.networks',
        'electrumkoboserver.blockchain_processor',
        'electrumkoboserver.server_processor',
        'electrumkoboserver.processor',
        'electrumkoboserver.version',
        'electrumkoboserver.ircthread',
        'electrumkoboserver.stratum_tcp',
        'electrumkoboserver.stratum_http'
    ],
    description="Kobocoin Electrum Server",
    author="Felix Ugoji",
    author_email="dev@kobocoin.com",
    license="GNU Affero GPLv3",
    url="https://github.com/kobocoin/electrum-kobo-server/",
    long_description="""Server for the Electrum Lightweight Kobocoin Wallet"""
)


