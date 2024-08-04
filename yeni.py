import pandas as pd
import io


csv_data = """snackss_product,snackss_product_url,snackss_product_price,competitor1_product,competitor1_product_url,competitor_product_price
"Haselnusskerne, geröstet",https://snackss.de/products/haselnusskerne-gerostet?variant=51018759045469,16.50,Macadamia nuts,https://www.korodrogerie.de/en/macadamia-nuts-wholes-and-halves-500g,16.50
"Pistazien, geröstet & gesalzen",https://snackss.de/products/pistazien-gerostet-gesalzen?variant=51018860659037,24.26,Pistazienkerne mit Haut 1 kg,https://www.korodrogerie.de/pistazienkerne-mit-haut-1-kg,33.00
"Mandeln, geröstet & gesalzen",https://snackss.de/collections/sale/products/mandeln-gerostet-gesalzen?variant=51018794959197,13.46,Geröstete und gesalzene Mandeln 1 kg,https://www.korodrogerie.de/geroestete-und-gesalzene-mandeln-1-kg,15.50
"Mango, getrocknet & gesüBt",https://snackss.de/collections/sale/products/mango-getrocknet-gesusst?variant=51018822254941,19.76,Bio Mangostreifen Brooks 1 kg,https://www.korodrogerie.de/bio-mangostreifen-brooks-1-kg,21.00
"Maiskörner, geröstet mit BBQ-Gewürz",https://snackss.de/collections/alle-produkte/products/maiskorner-gerostet-bbq-gewurz?variant=51018776609117,10.49,Geröstete Maiskörner mit BBQ-Gewürz 1 kg,https://www.korodrogerie.de/geroestete-maiskoerner-mit-bbq-gewuerz-1-kg,12.00
"Medjool Datteln, naturbelassen",https://snackss.de/collections/alle-produkte/products/medjool-datteln-naturbelassen?variant=51018844078429,13.46,"Medjool Datteln Premium Large mit Stein, Medjool Plus 1 kg",https://www.korodrogerie.de/medjool-datteln-premium-large-mit-stein-medjool-plus-1-kg,16.00
"Feigen, getrocknet",https://snackss.de/products/feigen-getrocknet?variant=51018754556253,14.36,Feigen aus der Türkei 1 kg,https://www.korodrogerie.de/feigen-aus-der-tuerkei-1-kg,15.50
"Erdnüsse, geröstet & gesalzen",https://snackss.de/products/erdnusse-gerostet-gesalzen?variant=51018752262493,9.59,Geröstete Erdnusskerne mit Salz und Öl 1 kg,https://www.korodrogerie.de/geroestete-erdnusskerne-mit-salz-und-oel-1-kg,6.50
"Cashewkerne, geröstet & gesalzen",https://snackss.de/collections/alle-produkte/products/cashewkerne-gerostet-gesalzen?variant=51018745086301,14.36,Geröstete und gesalzene Cashewkerne 1 kg,https://www.korodrogerie.de/geroestete-und-gesalzene-cashewkerne-1-kg,15.50
"Kichererbsen, gesalzen",https://snackss.de/products/kichererbsen-gesalzen?variant=51018766713181,7.61,Geröstete und gesalzene Kichererbsen 1 kg,https://www.korodrogerie.de/geroestete-und-gesalzene-kichererbsen-1-kg,10.00
"Weinbeeren, getrocknet & kernlos",https://snackss.de/products/schwarze-rosinen-kernlos?variant=51018993074525,8.00,Jumbo Weinbeeren 1 kg,https://www.korodrogerie.de/jumbo-weinbeeren-1-kg,8.50
"Pflaumen, getrocknet",https://snackss.de/products/pflaumen-getrocknet?variant=51018850337117,17.96,Getrocknete und entsteinte Pflaumen 1 kg,https://www.korodrogerie.de/getrocknete-und-entsteinte-pflaumen-1-kg,14.50
"Birnen, getrocknet",https://snackss.de/products/birnen-getrocknet?variant=51018743021917,19.76,Getrocknete Bio Birnen 1 kg,https://www.korodrogerie.de/getrocknete-bio-birnen-1-kg,21.50
"Erdbeeren, getrocknet",https://snackss.de/products/erdbeeren-getrocknet?variant=51018751017309,47.66,Getrocknete Erdbeeren,https://www.korodrogerie.de/getrocknete-erdbeeren-500-g,51.00
"Aprikosen, getrocknet",https://snackss.de/collections/alle-produkte/products/aprikosen-getrocknet?variant=51018736861533,16.16,Getrocknete wilde Aprikosen 1 kg,https://www.korodrogerie.de/getrocknete-wilde-aprikosen-1-kg,14.50"""

df = pd.read_csv(io.StringIO(csv_data))

def compare_prices(row):
    snackss_price = float(row['snackss_product_price'])
    competitor_price = float(row['competitor_product_price'])
    difference = snackss_price - competitor_price
    return snackss_price, competitor_price, difference

df[['snackss_product_price', 'competitor_product_price', 'price_difference']] = df.apply(compare_prices, axis=1, result_type='expand')

print(df[['snackss_product', 'snackss_product_price', 'competitor1_product', 'competitor_product_price', 'price_difference']])