======
Pyping
======

A pure python ping implementation using raw sockets.

Note that ICMP messages can only be sent from processes running as root
(in Windows, you must run this script as 'Administrator').

Original Version from Matthew Dixon Cowles.
  
* Copyleft 1989-2011 by the python-ping team, see `AUTHORS <https://raw.github.com/toxinu/pyping/master/AUTHORS>`_ for more details.
* License: GNU GPL v2, see `LICENCE <https://raw.github.com/toxinu/pyping/master/LICENSE>`_ for more details.

Usage
-----
Use as a cli tool::

    $ sudo pyping example.com

    PYTHON-PING example.com (92.243.5.143): 55 data bytes
    241 bytes from example.com (92.243.5.143): icmp_seq=0 ttl=55 time=64.5 ms
    241 bytes from example.com (92.243.5.143): icmp_seq=1 ttl=55 time=67.7 ms
    241 bytes from example.com (92.243.5.143): icmp_seq=2 ttl=55 time=66.6 ms

    ----example.com PYTHON PING Statistics----
    3 packets transmitted, 3 packets received, 0.0% packet loss
    round-trip (ms)  min/avg/max = 64.457/66.244/67.677

    $ pyping --help

Use as a Python lib::

    >>> import pyping
    >>> r = pyping.ping('example.com')                # Need to be root or
    >>> r = pyping.ping('example.com', udp = True)    # But it's udp, not real icmp
    >>> r.ret_code
    0
    >>> r.destination
    'example.com'
    >>> r.max_rtt
    '69.374'
    >>> r.avg_rtt
    '68.572'
    >>> r.min_rtt
    '67.681'
    >>> r.destination_ip
    '92.243.5.143'

Todo
----

- Docs
- Refactor core.py
- Tests

Contribute
----------

`Fork <http://help.github.com/fork-a-repo/>`_ this repo on `GitHub <https://github.com/toxinu/pyping>`_ and `send <http://help.github.com/send-pull-requests>`_ pull requests. Thank you.

Links
-----

 - Sourcecode at GitHub: https://github.com/toxinu/pyping
 - Python Package Index: http://pypi.python.org/pypi/pyping/
