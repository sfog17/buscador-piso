# buscador-piso

## Objective

- [ ] Scrape flats ads from Idealista according to specific criteria
- [ ] Extract additional information (e.g. energy efficiency, year of construction), not available in the filter of the website
- [ ] Store interesting flats
- [ ] Automate search & storage daily
- [ ] Send alerts

Note: This is only designed for personal use and limited calls, not
to scrape hundreds of adverts, do large-scale analysis or serve it 
to another service

## Requirements

Tested with:

- Ubuntu 20.04.6 LT
- Python 3.8.10

Dependencies are listed in [requirements.txt](requirements.txt).

Can be run with

```bash
$ python3 -m venv myenv
$ source myenv/bin/activate
$ pip install -r requirements.tx
```