from setuptools import setup

setup(
    name="electrum-server",
    version="0.9",
    scripts=['run_electrum_server','electrum-server','configure','electrum.conf.sample'],
    install_requires=['plyvel','jsonrpclib', 'irc'],
    package_dir={'electrum_server':'src'},
    py_modules=[
        'electrum_server.__init__',
        'electrum_server.utils',
        'electrum_server.storage',
        'electrum_server.deserialize',
        'electrum_server.networks',
        'electrum_server.blockchain_processor',
        'electrum_server.server_processor',
        'electrum_server.processor',
        'electrum_server.version',
        'electrum_server.ircthread',
        'electrum_server.stratum_tcp',
        'electrum_server.stratum_http'
    ],
    description="OKCash Electrum Server",
    author="Thomas Voegtlin, OKtoshi",
    author_email="thomasv1@gmx.de",
    license="GNU Affero GPLv3",
    url="https://github.com/oktoshi/electrum-server/",
    long_description="""Server for the Electrum Lightweight OKCash Wallet"""
)


