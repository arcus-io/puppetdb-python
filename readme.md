# puppetdb-python
Python interface to [PuppetDB](http://docs.puppetlabs.com/puppetdb/1.1/index.html)

Note: this currently only supports PuppetDB API version 2

# Usage
* `pip install puppetdb` or `python setup.py install` (from this source)

```
>>> from puppetdb import PuppetDBClient
>>> c = PuppetDBClient()
>>> c.get_nodes()
>>> [{'deactivated': None, 'facts_timestamp': '2013-02-09T21:05:15.082Z', 'name': 'sandbox.local', 'report_timestamp': None, 'catalog_timestamp': '2013-02-09T21:05:15.663Z'}, {'deactivated': None, 'facts_timestamp': '2013-02-27T14:08:53.992Z', 'name': 'util.local', 'report_timestamp': '2013-02-27T14:09:58.000Z', 'catalog_timestamp': '2013-02-27T14:08:55.463Z'}]

>>> c.get_node('sandbox.local')
>>> {'deactivated': None, 'facts_timestamp': '2013-02-09T21:05:15.082Z', 'name': 'sandbox.local', 'report_timestamp': None, 'catalog_timestamp': '2013-02-09T21:05:15.663Z'}

>>> c.get_node_facts('sandbox.local')
>>> [{'certname': 'sandbox.local', 'name': 'architecture', 'value': 'amd64'}, {'certname': 'sandbox.local', 'name': 'augeasversion', 'value': '0.10.0'}, {'certname': 'sandbox.local', 'name': 'boardmanufacturer', 'value': 'Oracle Corporation'}, {'certname': 'sandbox.local', 'name': 'boardproductname', 'value': 'VirtualBox'}, {'certname': 'sandbox.local', 'name': 'boardserialnumber', 'value': '0'}, {'certname': 'sandbox.local', 'name': 'clientcert', 'value': 'sandbox.local'}, {'certname': 'sandbox.local', 'name': 'clientversion', 'value': '3.1.0'}, {'certname': 'sandbox.local', 'name': 'domain', 'value': 'local'}, {'certname': 'sandbox.local', 'name': 'facterversion', 'value': '1.6.17'}, {'certname': 'sandbox.local', 'name': 'fqdn', 'value': 'sandbox.local'}, {'certname': 'sandbox.local', 'name': 'hardwareisa', 'value': 'x86_64'}, {'certname': 'sandbox.local', 'name': 'hardwaremodel', 'value': 'x86_64'}, {'certname': 'sandbox.local', 'name': 'hostname', 'value': 'sandbox'}, {'certname': 'sandbox.local', 'name': 'id', 'value': 'root'}, {'certname': 'sandbox.local', 'name': 'interfaces', 'value': 'eth0,eth1,lo'}, {'certname': 'sandbox.local', 'name': 'ipaddress', 'value': '10.0.2...
...


```

# Contributing
* `pip install -r requirements.txt`
* `./test.sh -v` (optional)
* Fork, Edit, Issue Pull Request
