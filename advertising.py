from urllib.parse import urljoin


class Advertising:
    def __init__(self):
        self.ad = None
        self.ads = []

    def set_ad(self, ad):
        self.ad = ad

    @staticmethod
    def get_ads(source_code):
        return source_code.find_all("div", class_='post-card-item-af972')

    def get_ad_url(self):
        a_tag = self.ad.find('a')
        if a_tag:
            return urljoin("https://divar.ir", a_tag.get("href"))

    def get_ad_title(self):
        return self.ad.find('h2', class_='kt-post-card__title').text

    def get_ad_img(self):
        img = self.ad.find('img')
        if img:
            return img.attrs['data-src']
        return 'https://clipground.com/images/no-image-png-5.jpg'

    def find_all_ads(self, source_code):
        ads = self.get_ads(source_code)
        new_ads = []
        for ad in ads:
            self.set_ad(ad)
            ad_url = self.get_ad_url()
            if ad_url is None or ad_url in self.ads:
                continue

            new_ad = {
                'url': self.get_ad_url(),
                'title': self.get_ad_title(),
                'image': self.get_ad_img()
            }

            new_ads.append(new_ad)
            self.ads.append(ad_url)
        return new_ads
