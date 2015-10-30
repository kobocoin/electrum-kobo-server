![Electrum-OK](i.imgur.com/rOeEycy.png)
electrum-ok-server
=========================================
  * Language: Python
  * Authors: ThomasV (original ltc fork) oktoshi (okcash fork)

Features
--------

  * The server indexes UTXOs by address, in a Patricia tree structure
    described by Alan Reiner (see the 'ultimate blockchain
    compression' thread in the Bitcointalk forum)

  * The server requires okcashd, leveldb and plyvel

  * The server code is open source. Anyone can run a server, removing
    single points of failure concerns.

  * The server knows which set of OKCash addresses belong to the same
    wallet, which might raise concerns about anonymity. However, it
    should be possible to write clients capable of using several
    servers. An i2p electrum server, as well as tor based electrum server 
    will be worked for if requested by the community.

Installation
------------

  1. To install and run a server, see INSTALL. For greater
     detail on the installation process, see HOWTO.md.

  2. To start and stop the server, use the 'electrum-ok-server' script



License
-------

electrum-ok-server is made available under the terms of the [GNU Affero General
Public License](http://www.gnu.org/licenses/agpl.html), version 3. See the 
included `LICENSE` for more details.

[![Visit our IRC Chat!](https://kiwiirc.com/buttons/irc.freenode.net/okcash.png)](https://kiwiirc.com/client/irc.freenode.net/?nick=ok|?&theme=cli#okcash)
