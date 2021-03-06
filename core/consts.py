# -*- coding: utf-8 -*-

"""
定数
"""
#RESPONSIBLE_TARGET_LIST_NAME = u'担当ターゲット'


"""
CHOICES
"""
"""
味わい評価
"""
EVALUATION_CHOICES = (
                (1,u'1:とてもよくない/強くない'),
                (2,u'2:あまりよくない/強くない'),
                (3,u'3:どっちつかず'),
                (4,u'4:良い/強い'),
                (5,u'5:とても良い/強い')
                )

"""
検索用味わい評価
"""
EVALUATION_CHOICES_STRONGNESS = (
                (0,u'選択しない'),
                (1,u'1:とても弱い'),
                (2,u'2:弱い'),
                (3,u'3:どっちつかず'),
                (4,u'4:強い'),
                (5,u'5:とても強い')
                )

"""
検索用味わい評価
"""
EVALUATION_CHOICES_GOODNESS = (
                (0,u'選択しない'),
                (1,u'1:よくない'),
                (2,u'2:あまりよくない'),
                (3,u'3:どっちつかず'),
                (4,u'4:よい'),
                (5,u'5:とてもよい')
                )

"""
検索用味わい評価
"""
EVALUATION_CHOICES_EXISTNESS = (
                (0,u'選択しない'),
                (1,u'1:ない'),
                (2,u'2:あまりない'),
                (3,u'3:どっちつかず'),
                (4,u'4:ある'),
                (5,u'5:とてもある')
                )
"""
登録用用味わい評価
"""
EVALUATION_ADD_CHOICES_STRONGNESS = (
                (0,u'---------'),
                (1,u'1:とても弱い'),
                (2,u'2:弱い'),
                (3,u'3:どっちつかず'),
                (4,u'4:強い'),
                (5,u'5:とても強い')
                )

"""
検索用味わい評価
"""
EVALUATION_ADD_CHOICES_GOODNESS = (
                (0,u'---------'),
                (1,u'1:よくない'),
                (2,u'2:あまりよくない'),
                (3,u'3:どっちつかず'),
                (4,u'4:よい'),
                (5,u'5:とてもよい')
                )

"""
検索用味わい評価
"""
EVALUATION_ADD_CHOICES_EXISTNESS = (
                (0,u'---------'),
                (1,u'1:ない'),
                (2,u'2:あまりない'),
                (3,u'3:どっちつかず'),
                (4,u'4:ある'),
                (5,u'5:とてもある')
                )

"""
性別スタイル
"""
GENDER_STYLE_CHOICES = (
                ('MALE',u'男性'),
                ('FEMALE',u'女性'),
                ('NEUTRAL',u'中性'),
                ('NONE',u'選択しない')
                )

"""
ユーザランク
"""
USER_RANK_CHOICES = (
                (1,u'1:初心者。これからたくさん飲もう！'),
                (2,u'2:レベル２。なかなかビールのことわかってきている。'),
                (3,u'3:中級レベルに突入。ビール初心者にビールのことを教えてあげよう！'),
                (4,u'4:ビールの知識が安定してきた。周りに自慢できるレベル。'),
                (5,u'5:まさに中堅クラス。店員さんとおしゃべりで負けない。'),
                (6,u'6:そろそろ上級者。ビール仲間の中でも尊敬されるレベルの知識量。'),
                (7,u'7:安定した上級者。ビール専門店でもドヤれるレベル。'),
                (8,u'8:マニアック。ブルワーへの転職をおすすめします。'),
                (9,u'9:理解の範疇を超える。自給自足でビール醸造してるんじゃないですか？'),
                (10,u'10:神様')
                )

"""
wish listのアイテムカテゴリチョイス
カテゴリ名はテーブル名と対応させる
"""
WISH_ITEM_CATEGORY_CHOICES = (
                (1,'Beer'),
                (2,'Brewery'),
                (3,'Venue'),
                (4,'Comment')
)

"""
国
"""
COUNTRY_CHOICES = (
                ('Afghanistan',u'アフガニスタン'),
                ('Albania',u'アルバニア'),
                ('Algeria',u'アルジェリア'),
                ('Andorra',u'アンドラ'),
                ('Angola',u'アンゴラ'),
                ('Antigua and Barbuda',u'アンティグア・バーブーダ'),
                ('Argentina',u'アルゼンチン'),
                ('Armenia',u'アルメニア'),
                ('Australia',u'オーストラリア'),
                ('Austria',u'オーストリア'),
                ('Azerbaijan',u'アゼルバイジャン'),
                ('Bahamas',u'バハマ'),
                ('Bahrain',u'バーレーン'),
                ('Bangladesh',u'バングラデシュ'),
                ('Barbados',u'バルバドス'),
                ('Belarus',u'ベラルーシ'),
                ('Belgium',u'ベルギー'),
                ('Belize',u'ベリーズ'),
                ('Benin',u'ベニン'),
                ('Bhutan',u'ブータン'),
                ('Bolivia',u'ボリビア'),
                ('Bosnia and Herzegovina',u'ボスニア・ヘルツェゴビナ'),
                ('Botswana',u'ボツワナ'),
                ('Brazil',u'ブラジル'),
                ('Brunei Darussalam',u'ブルネイ'),
                ('Bulgaria',u'ブルガリア'),
                ('Burkina Faso',u'ブルキナファソ'),
                ('Burundi',u'ブルンジ'),
                ('Cabo Verde',u'カーボベルデ'),
                ('Cambodia',u'カンボジア'),
                ('Cameroon',u'カメルーン'),
                ('Canada',u'カナダ'),
                ('Central African Republic',u'中央アフリカ共和国'),
                ('Chad',u'チャド'),
                ('Chile',u'チリ'),
                ('China',u'中国'),
                ('Colombia',u'コロンビア'),
                ('Comoros',u'コモロ'),
                ('Congo (Republic of the)',u'コンゴ'),
                ('Costa Rica',u'コスタリカ'),
                ('Cote dIvoire',u'コートジボアール'),
                ('Croatia',u'クロアチア'),
                ('Cuba',u'キューバ'),
                ('Cyprus',u'キプロス'),
                ('Czech Republic',u'チェコ'),
                ('Democratic Peoples Republic of Korea',u'朝鮮民主主義人民共和国'),
                ('Democratic Republic of the Congo',u'コンゴ民主共和国'),
                ('Denmark',u'デンマーク'),
                ('Djibouti',u'ジブチ'),
                ('Dominica',u'ドミニカ'),
                ('Dominican Republic',u'ドミニカ共和国'),
                ('Ecuador',u'エクアドル'),
                ('Egypt',u'エジプト'),
                ('El Salvador',u'エルサルバドル'),
                ('Equatorial Guinea',u'赤道ギニア'),
                ('Eritrea',u'エリトリア'),
                ('Estonia',u'エストニア'),
                ('Eswatini',u'エスワティニ'),
                ('Ethiopia',u'エチオピア'),
                ('Fiji',u'フィジ－'),
                ('Finland',u'フィンランド'),
                ('France',u'フランス'),
                ('Gabon',u'ガボン'),
                ('Gambia',u'ガンビア'),
                ('Georgia',u'ジョージア'),
                ('Germany',u'ドイツ'),
                ('Ghana',u'ガーナ'),
                ('Greece',u'ギリシャ'),
                ('Grenada',u'グレナダ'),
                ('Guatemala',u'グアテマラ'),
                ('Guinea',u'ギニア'),
                ('Guinea-Bissau',u'ギニアビサウ'),
                ('Guyana',u'ガイアナ'),
                ('Haiti',u'ハイチ'),
                ('Honduras',u'ホンジュラス'),
                ('Hungary',u'ハンガリ'),
                ('Iceland',u'アイスランド'),
                ('India',u'インド'),
                ('Indonesia',u'インドネシア'),
                ('Iran',u'イラン'),
                ('Iraq',u'イラク'),
                ('Ireland',u'アイルランド'),
                ('Israel',u'イスラエル'),
                ('Italy',u'イタリア'),
                ('Jamaica',u'ジャマイカ'),
                ('Japan',u'日本'),
                ('Jordan',u'ヨルダン'),
                ('Kazakhstan',u'カザフスタン'),
                ('Kenya',u'ケニア'),
                ('Kiribati',u'キリバス'),
                ('Kuwait',u'クウェート'),
                ('Kyrgyzstan',u'キルギスタン'),
                ('Lao Peoples Democratic Republic',u'ラオス人民民主共和国'),
                ('Latvia',u'ラトビア'),
                ('Lebanon',u'レバノン'),
                ('Lesotho',u'レソト'),
                ('Liberia',u'リベリア'),
                ('Libya',u'リビア'),
                ('Liechtenstein',u'リヒテンシュタイン'),
                ('Lithuania',u'リトアニア'),
                ('Luxembourg',u'ルクセンブルク'),
                ('Madagascar',u'マダガスカル'),
                ('Malawi',u'マラウィ'),
                ('Malaysia',u'マレーシア'),
                ('Maldives',u'モルディブ'),
                ('Mali',u'マリ'),
                ('Malta',u'マルタ'),
                ('Marshall Islands',u'マーシャル諸島'),
                ('Mauritania',u'モーリタニア'),
                ('Mauritius',u'モーリシャス'),
                ('Mexico',u'メキシコ'),
                ('Micronesia (Federated States of)',u'ミクロネシア連邦'),
                ('Monaco',u'モナコ'),
                ('Mongolia',u'モンゴル'),
                ('Montenegro',u'モンテネグロ'),
                ('Morocco',u'モロッコ'),
                ('Mozambique',u'モザンビーク'),
                ('Myanmar',u'ミャンマー'),
                ('Namibia',u'ナミビア'),
                ('Nauru',u'ナウル'),
                ('Nepal',u'ネパール'),
                ('Netherlands',u'オランダ'),
                ('New Zealand',u'ニュージーランド'),
                ('Nicaragua',u'ニカラグア'),
                ('Niger',u'ニジェール'),
                ('Nigeria',u'ナイジェリア'),
                ('North Macedonia',u'北マケドニア'),
                ('Norway',u'ノルウェー'),
                ('Oman',u'オマーン'),
                ('Pakistan',u'パキスタン'),
                ('Palau',u'パラオ'),
                ('Panama',u'パナマ'),
                ('Papua New Guinea',u'パプア・ニューギニア'),
                ('Paraguay',u'パラグアイ'),
                ('Peru',u'ペルー'),
                ('Philippines',u'フィリピン'),
                ('Poland',u'ポーランド'),
                ('Portugal',u'ポルトガル'),
                ('Qatar',u'カタール'),
                ('Republic of Korea',u'韓国'),
                ('Republic of Moldova',u'モルドバ'),
                ('Romania',u'ルーマニア'),
                ('Russian Federation',u'ロシア連邦'),
                ('Rwanda',u'ルワンダ'),
                ('Saint Kitts and Nevis',u'セントクリストファー・ネイビス'),
                ('Saint Lucia',u'セントルシア'),
                ('Saint Vincent and the Grenadines',u'セントビンセントおよびグレナディーン諸島'),
                ('Samoa',u'サモア'),
                ('San Marino',u'サンマリノ'),
                ('Sao Tome and Principe',u'サントメ・プリンシペ'),
                ('Saudi Arabia',u'サウジアラビア'),
                ('Senegal',u'セネガル'),
                ('Serbia',u'セルビア'),
                ('Seychelles',u'セイシェル'),
                ('Sierra Leone',u'シエラレオネ'),
                ('Singapore',u'シンガポール'),
                ('Slovakia',u'スロバキア'),
                ('Slovenia',u'スロベニア'),
                ('Solomon Islands',u'ソロモン諸島'),
                ('Somalia',u'ソマリア'),
                ('South Africa',u'南アフリカ'),
                ('South Sudan',u'南スーダン'),
                ('Spain',u'スペイン'),
                ('Sri Lanka',u'スリランカ'),
                ('Sudan',u'スーダン'),
                ('Suriname',u'スリナム'),
                ('Sweden',u'スウェーデン'),
                ('Switzerland',u'スイス'),
                ('Syria',u'シリア'),
                ('Tajikistan',u'タジキスタン'),
                ('Thailand',u'タイ'),
                ('Timor-Leste',u'東ティモール'),
                ('Togo',u'トーゴ'),
                ('Tonga',u'トンガ'),
                ('Trinidad and Tobago',u'トリニダード・トバゴ'),
                ('Tunisia',u'チュニジア'),
                ('Turkey',u'トルコ'),
                ('Turkmenistan',u'トルクメニスタン'),
                ('Tuvalu',u'ツバル'),
                ('Uganda',u'ウガンダ'),
                ('Ukraine',u'ウクライナ'),
                ('United Arab Emirates',u'アラブ首長国連邦'),
                ('United Kingdom',u'英国'),
                ('United Republic of Tanzania',u'タンザニア'),
                ('United States of America',u'米国'),
                ('Uruguay',u'ウルグアイ'),
                ('Uzbekistan',u'ウズベキスタン'),
                ('Vanuatu',u'バヌアツ'),
                ('Venezuela',u'ベネズエラ'),
                ('Viet Nam',u'ベトナム'),
                ('Yemen',u'イエメン'),
                ('Zambia',u'ザンビア'),
                ('Zimbabwe',u'ジンバブエ')
                )
