from finder import ad_finder

example_url = 'https://divar.ir/s/tehran/rent-residential'
example_url_2 = 'https://divar.ir/s/tehran/rent-apartment?credit=100000000-500000000'
example_url_3 = (
    'https://divar.ir/s/tehran/car/peugeot/504?brand_model=Peugeot%20Pars%20ELX%20XUM%2CPeugeot%20Pars'
    '%20ELX-TU5%2CPeugeot%20Pars%20XU7P%2CPeugeot%20Pars%20XU7P-ELX%2CPeugeot%20Pars%20basic%2CPeugeot'
    '%20Pars%20latest&body_status=intact'
)

ads = ad_finder(url=example_url_3, crawling_time=0.5)
print(ads)
