![Electrum-OK](http://kobocoin.com/kobocoin.png)
Electrum Kobocoin Server
=========================================
  * Language: Python
  * Authors: ThomasV (orig.btc), oktoshi (mod.ok), TheTribesman (dev.kobo)

Features
--------

  * The server indexes UTXOs by address, in a Patricia tree structure
    described by Alan Reiner (see the 'ultimate blockchain
    compression' thread in the Bitcointalk forum)

  * The server requires Kobocoind, leveldb and plyvel

  * The server code is open source. Anyone can run a server, removing
    single points of failure concerns.

  * The server knows which set of Kobocoin addresses belong to the same
    wallet, which might raise concerns about anonymity. However, it
    should be possible to write clients capable of using several
    servers. An i2p electrum server, as well as tor based electrum server 
    will be worked for if requested by the community.

Installation
------------

  1. To install and run a server, see INSTALL. For greater
     detail on the installation process, see HOWTO.md.

  2. To start and stop the server, use the 'electrum-kobo-server' script



License
-------

electrum-kobo-server is made available under the terms of the [GNU Affero General
Public License](http://www.gnu.org/licenses/agpl.html), version 3. See the 
included `LICENSE` for more details.
