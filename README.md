# colorImgScale

## eval model

```bash
$ python eval_model.py ../vecs/aozora_week210625.kv.bin # print output to both stdout and log file
loading model:  ../vecs/aozora_week210625.kv.bin
[1]Word2Vec.load
=> failed: could not find MARK
  model = Word2Vec.load(mname).wv
            model = super(Word2Vec, cls).load(*args, **kwargs)
        obj = unpickle(fname)
        return _pickle.load(f, encoding='latin1')  # needed because loading from S3 doesn't support readline()

[2]KeyedVectors.load2vec_format(binary=False)
=> failed: could not convert string to float: '>\x08Y>x'
  model = KeyedVectors.load_word2vec_format(mname, binary=False, unicode_errors='ignore')
        return _load_word2vec_format(
            _word2vec_read_text(fin, kv, counts, vocab_size, vector_size, datatype, unicode_errors, encoding)
        word, weights = _word2vec_line_to_vector(line, datatype, unicode_errors, encoding)
    word, weights = parts[0], [datatype(x) for x in parts[1:]]
    word, weights = parts[0], [datatype(x) for x in parts[1:]]

[3]KeyedVectors.load2vec_format(binary=True)
model: <gensim.models.keyedvectors.KeyedVectors object at 0x7f529146a0a0>
vocab size: 175131
140/178
78.65168539325843 %
exists:     {('進歩的', '進歩的な'), ('楽しい', '楽しい'), ('強烈', '強烈な'), ('派手', '派手な'), ('大人しい', '大人しい'), ('洗練', '洗練された'), ('嬉しい', '嬉しい'), ('ロマンチック', 'ロマンチックな'), ('上品', '上品な'), ('豪華', '豪華な'), ('初々しい', '初々しい'), ('艶っぽい', '艶っぽい'), ('のんびり', 'のんびりした'), ('奥ゆかしい', '奥ゆかしい'), ('革新的', '革新的な'), ('生き生き', '生き生きした'), ('優美', '優美な'), ('陽気', '陽気な'), ('本格的', '本格的な'), ('自然', '自然な'), ('豊か', '豊かな'), ('賑やか', '賑やかな'), ('セクシー', 'セクシーな'), ('華麗', '華麗な'), ('華やか', '華やかな'), ('神聖', '神聖な'), ('精密', '精密な'), ('清々しい', '清々しい'), ('快適', '快適な'), ('伸び伸び', '伸び伸びした'), ('若々しい', '若々しい'), ('朗らか', '朗らかな'), ('文化的', '文化的な'), ('エネルギッシュ', 'エネルギッシュな'), ('スポーティ', 'スポーティな'), ('女性的', '女性的な'), ('安らか', '安らかな'), ('淡白', '淡白な'), ('理知的', '理知的な'), ('贅沢', '贅沢な'), ('甘美', '甘美な'), ('豊潤', '豊潤な'), ('爽やか', '爽やかな'), ('開放的', '開放的な'), ('慎ましい', '慎ましい'), ('男性的', '男性的な'), ('柔和', '柔和な'), ('凛々しい', '凛々しい'), ('真面目', '真面目な'), ('大胆', '大胆な'), ('クリア', 'クリアな'), ('シャープ', 'シャープな'), ('平和', '平和な'), ('元気', '元気な'), ('装飾的', '装飾的な'), ('丈夫', '丈夫な'), ('ダンディ', 'ダンディな'), ('厳粛', '厳粛な'), ('風流', '風流な'), ('質素', '質素な'), ('長閑', '長閑な'), ('地味', '地味な'), ('刺激的', '刺激的な'), ('清らか', '清らかな'), ('清潔', '清潔な'), ('繊細', '繊細な'), ('スピーディ', 'スピーディな'), ('古風', '古風な'), ('あどけない', 'あどけない'), ('たくましい', '逞しい'), ('エレガント', 'エレガントな'), ('麗しい', '麗しい'), ('高雅', '高雅な'), ('伝統的', '伝統的な'), ('新鮮', '新鮮な'), ('軽快', '軽快な'), ('メカニック', 'メカニックな'), ('荘厳', '荘厳な'), ('ダイナミック', 'ダイナミックな'), ('気高い', '気高い'), ('素朴', '素朴な'), ('閑静', '閑静な'), ('どっしり', 'どっしりした'), ('溌剌', '溌剌とした'), ('淡い', '淡い'), ('控えめ', '控えめな'), ('懐かしい', '懐かしい'), ('子供らしい', '子供らしい'), ('スマート', 'スマートな'), ('純真', '純真な'), ('堅実', '堅実な'), ('活動的', '活動的な'), ('メルヘン', 'メルヘンの'), ('叙情的', '叙情的な'), ('微妙', '微妙な'), ('快活', '快活な'), ('がっしり', 'がっしりした'), ('丹念', '丹念な'), ('激しい', '激しい'), ('しなやか', 'しなやかな'), ('瑞々しい', '瑞々しい'), ('高尚', '高尚な'), ('青春', '青春の'), ('力強い', '力強い'), ('人工的', '人工的な'), ('静か', '静かな'), ('合理的', '合理的な'), ('健康', '健康な'), ('優しい', '優しい'), ('ワイルド', 'ワイルドな'), ('冷静', '冷静な'), ('渋い', '渋い'), ('鮮やか', '鮮やかな'), ('クラシック', 'クラシックな'), ('家庭的', '家庭的な'), ('シック', 'シックな'), ('マイルド', 'マイルドな'), ('ユーモラス', 'ユーモラスな'), ('気軽', '気軽な'), ('情熱的', '情熱的な'), ('可憐', '可憐な'), ('重厚', '重厚な'), ('知的', '知的な'), ('モダン', 'モダンな'), ('和やか', '和やかな'), ('素直', '素直な'), ('淑やか', '淑やかな'), ('愉快', '愉快な'), ('充実', '充実した'), ('円熟', '円熟した'), ('温雅', '温雅な'), ('味わい深い', '味わい深い'), ('すっきり', 'すっきりした'), ('安全', '安全な'), ('清楚', '清楚な'), ('タフ', 'タフな'), ('温和', '温和な'), ('機敏', '機敏な'), ('気楽', '気楽な'), ('簡素', '簡素な')}
not exists: {('鄙びた', '鄙びた'), ('気品のある', '気品のある'), ('優雅な', '優雅な'), ('スカッと', 'スカッとした'), ('男っぽい', '男っぽい'), ('田園的', '田園的な'), ('躍動的', '躍動的な'), ('きりりとした', 'きりりとした'), ('洒落た', '洒落た'), ('フェミニン', 'フェミニンな'), ('力動的', '力動的な'), ('艶やか', '艶やかな'), ('アクティブ', 'アクティブな'), ('枯れた', '枯れた'), ('アンティーク', 'アンティークな'), ('情緒的', '情緒的な'), ('肌ざわりのよい', '肌ざわりのよい'), ('紳士的', '紳士的な'), ('寛いだ', '寛いだ'), ('きめ細かい', 'きめ細かい'), ('キュート', 'キュートな'), ('魅惑的', '魅惑的な'), ('行動的', '行動的な'), ('大らか', '大らかな'), ('さっぱりした', 'さっぱりした'), ('フォーマル', 'フォーマルな'), ('格調のある', '格調のある'), ('風格のある', '風格のある'), ('さりげない', 'さりげない'), ('馴染みやすい', '馴染みやすい'), ('活気のある', '活気のある'), ('都会的', '都会的な'), ('親しみやすい', '親しみやすい'), ('こってりした', 'こってりした'), ('ドレッシー', 'ドレッシーな'), ('カジュアル', 'カジュアルな'), ('飾り気のない', '飾り気のない'), ('居心地のよい', '居心地のよい')}
```

```bash
$ python eval_model.py ../vecs/hottoSNS-w2v_20190301/w2v_all_vector200_win5_sgns0.vec
loading model:  ../vecs/hottoSNS-w2v_20190301/w2v_all_vector200_win5_sgns0.vec
[1]Word2Vec.load
=> failed: unpickling stack underflow
  model = Word2Vec.load(mname).wv
            model = super(Word2Vec, cls).load(*args, **kwargs)
        obj = unpickle(fname)
        return _pickle.load(f, encoding='latin1')  # needed because loading from S3 doesn't support readline()

[2]KeyedVectors.load2vec_format(binary=False)
model: <gensim.models.keyedvectors.KeyedVectors object at 0x7f8034e11250>
vocab size: 2067629
156/178
87.64044943820225 %
exists:     {('軽快', '軽快な'), ('艶っぽい', '艶っぽい'), ('さりげない', 'さりげない'), ('楽しい', '楽しい'), ('丹念', '丹念な'), ('しなやか', 'しなやかな'), ('家庭的', '家庭的な'), ('安らか', '安らかな'), ('ダンディ', 'ダンディな'), ('合理的', '合理的な'), ('静か', '静かな'), ('エレガント', 'エレガントな'), ('控えめ', '控えめな'), ('シック', 'シックな'), ('簡素', '簡素な'), ('大胆', '大胆な'), ('純真', '純真な'), ('伸び伸び', '伸び伸びした'), ('進歩的', '進歩的な'), ('精密', '精密な'), ('気楽', '気楽な'), ('快活', '快活な'), ('地味', '地味な'), ('平和', '平和な'), ('冷静', '冷静な'), ('溌剌', '溌剌とした'), ('麗しい', '麗しい'), ('若々しい', '若々しい'), ('華麗', '華麗な'), ('スピーディ', 'スピーディな'), ('贅沢', '贅沢な'), ('豊潤', '豊潤な'), ('ロマンチック', 'ロマンチックな'), ('メカニック', 'メカニックな'), ('淡白', '淡白な'), ('鮮やか', '鮮やかな'), ('きめ細かい', 'きめ細かい'), ('清らか', '清らかな'), ('ダイナミック', 'ダイナミックな'), ('清潔', '清潔な'), ('刺激的', '刺激的な'), ('愉快', '愉快な'), ('クリア', 'クリアな'), ('長閑', '長閑な'), ('柔和', '柔和な'), ('優雅な', '優雅な'), ('厳粛', '厳粛な'), ('朗らか', '朗らかな'), ('気軽', '気軽な'), ('奥ゆかしい', '奥ゆかしい'), ('がっしり', 'がっしりした'), ('スカッと', 'スカッとした'), ('凛々しい', '凛々しい'), ('あどけない', 'あどけない'), ('質素', '質素な'), ('文化的', '文化的な'), ('閑静', '閑静な'), ('真面目', '真面目な'), ('温和', '温和な'), ('開放的', '開放的な'), ('フェミニン', 'フェミニンな'), ('清楚', '清楚な'), ('装飾的', '装飾的な'), ('懐かしい', '懐かしい'), ('機敏', '機敏な'), ('アクティブ', 'アクティブな'), ('革新的', '革新的な'), ('古風', '古風な'), ('嬉しい', '嬉しい'), ('甘美', '甘美な'), ('和やか', '和やかな'), ('上品', '上品な'), ('派手', '派手な'), ('タフ', 'タフな'), ('元気', '元気な'), ('繊細', '繊細な'), ('洒落た', '洒落た'), ('活動的', '活動的な'), ('フォーマル', 'フォーマルな'), ('優しい', '優しい'), ('温雅', '温雅な'), ('味わい深い', '味わい深い'), ('セクシー', 'セクシーな'), ('豊か', '豊かな'), ('伝統的', '伝統的な'), ('アンティーク', 'アンティークな'), ('高尚', '高尚な'), ('気高い', '気高い'), ('情熱的', '情熱的な'), ('淡い', '淡い'), ('カジュアル', 'カジュアルな'), ('本格的', '本格的な'), ('素朴', '素朴な'), ('キュート', 'キュートな'), ('豪華', '豪華な'), ('のんびり', 'のんびりした'), ('知的', '知的な'), ('渋い', '渋い'), ('神聖', '神聖な'), ('力強い', '力強い'), ('陽気', '陽気な'), ('青春', '青春の'), ('大人しい', '大人しい'), ('シャープ', 'シャープな'), ('快適', '快適な'), ('女性的', '女性的な'), ('可憐', '可憐な'), ('新鮮', '新鮮な'), ('高雅', '高雅な'), ('清々しい', '清々しい'), ('健康', '健康な'), ('堅実', '堅実な'), ('充実', '充実した'), ('素直', '素直な'), ('爽やか', '爽やかな'), ('メルヘン', 'メルヘンの'), ('安全', '安全な'), ('マイルド', 'マイルドな'), ('重厚', '重厚な'), ('賑やか', '賑やかな'), ('エネルギッシュ', 'エネルギッシュな'), ('どっしり', 'どっしりした'), ('激しい', '激しい'), ('理知的', '理知的な'), ('慎ましい', '慎ましい'), ('スポーティ', 'スポーティな'), ('艶やか', '艶やかな'), ('ワイルド', 'ワイルドな'), ('モダン', 'モダンな'), ('男性的', '男性的な'), ('枯れた', '枯れた'), ('ユーモラス', 'ユーモラスな'), ('都会的', '都会的な'), ('自然', '自然な'), ('荘厳', '荘厳な'), ('生き生き', '生き生きした'), ('クラシック', 'クラシックな'), ('丈夫', '丈夫な'), ('たくましい', '逞しい'), ('風流', '風流な'), ('人工的', '人工的な'), ('紳士的', '紳士的な'), ('優美', '優美な'), ('スマート', 'スマートな'), ('ドレッシー', 'ドレッシーな'), ('強烈', '強烈な'), ('初々しい', '初々しい'), ('華やか', '華やかな'), ('淑やか', '淑やかな'), ('微妙', '微妙な'), ('大らか', '大らかな'), ('すっきり', 'すっきりした'), ('子供らしい', '子供らしい'), ('洗練', '洗練された'), ('瑞々しい', '瑞々しい'), ('円熟', '円熟した')}
not exists: {('こってりした', 'こってりした'), ('飾り気のない', '飾り気のない'), ('きりりとした', 'きりりとした'), ('叙情的', '叙情的な'), ('肌ざわりのよい', '肌ざわりのよい'), ('格調のある', '格調のある'), ('情緒的', '情緒的な'), ('男っぽい', '男っぽい'), ('さっぱりした', 'さっぱりした'), ('風格のある', '風格のある'), ('鄙びた', '鄙びた'), ('田園的', '田園的な'), ('躍動的', '躍動的な'), ('行動的', '行動的な'), ('馴染みやすい', '馴染みやすい'), ('寛いだ', '寛いだ'), ('親しみやすい', '親しみやすい'), ('気品のある', '気品のある'), ('活気のある', '活気のある'), ('居心地のよい', '居心地のよい'), ('魅惑的', '魅惑的な'), ('力動的', '力動的な')}
```
