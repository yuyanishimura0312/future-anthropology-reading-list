# build-record — future-anthropology-reading-list

## 2026-10-16 論考（タブ03）と論文 PDF の図表: 図1 flow・図2 quadrant を figc で、表は md の markdown 表＋共通 CSS
- 採った: 図は figc 宣言（座標を書かない）→ verify 7検査 PASS の SVG を両媒体で共有し、キャプション・表番号・表の書式だけを媒体別 CSS（figures-page.css / figures-paper.css）で出し分ける。図1は水平7段が text_fit で落ちたため縦（size xs・360×880）。図2は quadrant に xs 幅が無く 680×432 のまま、ページ側で可読幅を抜けて 680px で表示（縮尺 1.0）。4象限は本文「優劣はない」に合わせ地色を揃えた。SVG 内の題・注は外し figcaption に一本化。alt は embed.py が inline 側にだけ <title>/<desc> を挿す（verify 済みファイルは触らない）。
- 棄却した: 図を figc 以外（手座標・挿絵）で描く／象限名の言い換え／1象限だけ accent／figc ソルバの改修（flow の赤い上罫・矢印、quadrant の点線軸は固定仕様。改修は D5 基盤の別決裁）。
- 破綻条件: design-quality-auditor 2周目で 75 未満（1周目 68・原因＝実効文字サイズ・図1の赤の多用・局所値）。2周目の実測は本体が PDF/ページを再生成して採点に出す（期日 2026-10-23）。414px で図2の象限名が 10px 未満なら文字版の併記へ切り替える。
- SCK: no matching rule
- 図解: 図的要素 2（flow・quadrant・ともに figc 型決定）＋表 → DGP pick 直接（2件とも no_candidate）／figc 経路。dgp へ渡さず。

委譲先: figc ×2 (sonnet), design-quality-auditor (opus) | 表・CSS・embed.py は inline
採点: 68/100 差し戻し（1周目・2周目は未採点）
接地: dsdb:なし（preset 未判定） / edd:pattern:なし（medium=report に65件あるが選択根拠に引用なし） / tokens:/Users/nishimura+/projects/research/miratuku-design-system/ds/tokens.css

## 2026-10-16 design gate
- 採点: 77/100 Good（4周目・design-quality-auditor・opus）。1周目68→2周目66→3周目73→4周目77
- 接地: dsdb:なし（preset 未判定） / edd:pattern:なし / tokens:~/projects/research/miratuku-design-system/ds/tokens.css
- 残: 論文版の明朝本文を canon 例外に登録するかは西村さん決裁待ち
