from setuptools import setup

setup(
    name="electrum-ok-server",
    version="0.9",
    scripts=['run_electrum_ok_server','electrum-ok-server'],
    install_requires=['plyvel','jsonrpclib', 'irc>=11'],
    package_dir={
        'electrumokserver':'src'
        },
    py_modules=[
        'electrumokserver.__init__',
        'electrumokserver.utils',
        'electrumokserver.storage',
        'electrumokserver.deserialize',
        'electrumokserver.networks',
        'electrumokserver.blockchain_processor',
        'electrumokserver.server_processor',
        'electrumokserver.processor',
        'electrumokserver.version',
        'electrumokserver.ircthread',
        'electrumokserver.stratum_tcp',
        'electrumokserver.stratum_http'
    ],
    description="OKCash Electrum Server",
    author="Thomas V, OKtoshi",
    author_email="thomasv1@gmx.de",
    license="GNU Affero GPLv3",
    url="https://github.com/okcashpro/electrum-ok-server/",
    long_description="""Server for the Electrum Lightweight OKCash Wallet"""
)


