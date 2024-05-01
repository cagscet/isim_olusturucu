
import random
def isimolusturucu():
    ilk_isim = ["çağlar", "çetin", "ali", "veli", "mert", "hasan", "atakan", "görkem"]
    ikinci_isim = ["çetin", "aydın", "yılmaz", "yıldırım", "candan", "tunç"]

    return "{} {}".format(random.choice(ilk_isim),random.choice(ikinci_isim))
for i in range(11):
    print(isimolusturucu())