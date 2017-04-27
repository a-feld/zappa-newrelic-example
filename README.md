Introduction
============

This repository is meant to showcase an example Zappa application with New Relic instrumentation.
New Relic does not officially support Zappa; however, this repository showcases a Zappa application which reports to New Relic.

Usage
======

1. Add a New Relic license key to `newrelic.ini`
```
export NEW_RELIC_LICENSE_KEY=<<<YOUR LICENSE KEY HERE>>>
echo "license_key=$NEW_RELIC_LICENSE_KEY" >> newrelic.ini
```

2. `pip install -r requirements.txt`

3. Configure your `zappa_settings.json`

4. `zappa deploy`
